# Telnyx ED25519 Webhook Helpers
#
# This module provides higher-level webhook helpers that use ED25519
# signature verification instead of the standard HMAC-SHA256 used by
# the generated `webhooks.py` module.
#
# It also monkey-patches the generated `WebhooksResource.unwrap` and
# `AsyncWebhooksResource.unwrap` methods to use ED25519 verification
# by default, matching the behavior of the Go, TypeScript, PHP, and
# Java SDKs. The original HMAC-based methods are preserved as
# `_unwrap_hmac` on each class for users who need the old behavior.
#
# This file is in the `lib/` directory which is preserved across Stainless
# code generation runs. Do not move it to the generated code directories.
#
# Usage:
#
#   # Default behavior (ED25519, after importing telnyx):
#   client = Telnyx(api_key="...", public_key="...")
#   event = client.webhooks.unwrap(payload, headers=headers)
#
#   # Explicit ED25519 helper (same result):
#   from telnyx.lib.webhooks_ed25519 import unwrap_with_ed25519
#   event = unwrap_with_ed25519(client, payload, headers)
#
#   # Fallback to HMAC-SHA256 (old behavior):
#   event = client.webhooks._unwrap_hmac(payload, headers=headers)

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Mapping, cast

from .webhook_verification import (
    WebhookVerificationError,
    verify_webhook_signature,
)

if TYPE_CHECKING:
    from telnyx import Telnyx
    from telnyx.types.unwrap_webhook_event import UnwrapWebhookEvent

__all__ = [
    "WebhookVerificationError",
    "verify_ed25519",
    "unwrap_with_ed25519",
]


def verify_ed25519(
    client: Telnyx,
    payload: str | bytes,
    headers: Mapping[str, str],
    *,
    key: str | None = None,
) -> None:
    """Verify webhook signature using ED25519 without parsing the payload.

    This function verifies the ED25519 signature of a Telnyx webhook but
    does not parse the payload. Use this when you only need to verify
    authenticity and will handle parsing yourself.

    Args:
        client: The Telnyx client instance (used to get public_key if not provided)
        payload: The raw webhook payload as string or bytes
        headers: The webhook HTTP headers
        key: Optional public key override (base64-encoded ED25519).
             If not provided, uses client.public_key.

    Raises:
        WebhookVerificationError: If verification fails
        ValueError: If no public key is configured

    Example:
        from telnyx import Telnyx
        from telnyx.lib.webhooks_ed25519 import verify_ed25519

        client = Telnyx(
            api_key=os.environ["TELNYX_API_KEY"],
            public_key=os.environ["TELNYX_PUBLIC_KEY"]
        )

        verify_ed25519(client, request.body, request.headers)
    """
    public_key = key or client.public_key

    if not public_key:
        raise ValueError("No public key configured. Provide key parameter or configure client with public_key.")

    verify_webhook_signature(payload, headers, public_key)


def unwrap_with_ed25519(
    client: Telnyx,
    payload: str | bytes,
    headers: Mapping[str, str],
    *,
    key: str | None = None,
) -> UnwrapWebhookEvent:
    """Verify webhook signature using ED25519 and parse the payload.

    This function verifies the ED25519 signature of a Telnyx webhook and
    then parses the payload into an UnwrapWebhookEvent object. Use this
    as a drop-in replacement for client.webhooks.unwrap() when you need
    ED25519 verification instead of HMAC-SHA256.

    Args:
        client: The Telnyx client instance
        payload: The raw webhook payload as string or bytes
        headers: The webhook HTTP headers
        key: Optional public key override (base64-encoded ED25519).
             If not provided, uses client.public_key.

    Returns:
        UnwrapWebhookEvent: The parsed webhook event

    Raises:
        WebhookVerificationError: If signature verification fails
        ValueError: If no public key is configured

    Example:
        from telnyx import Telnyx
        from telnyx.lib.webhooks_ed25519 import unwrap_with_ed25519

        client = Telnyx(
            api_key=os.environ["TELNYX_API_KEY"],
            public_key=os.environ["TELNYX_PUBLIC_KEY"]
        )

        event = unwrap_with_ed25519(client, request.body, request.headers)
        print(f"Received event: {event.event_type}")
    """
    # Verify the signature first
    verify_ed25519(client, payload, headers, key=key)

    # Import here to avoid circular imports and keep this module lightweight
    from telnyx._models import construct_type
    from telnyx.types.unwrap_webhook_event import UnwrapWebhookEvent

    # Parse the payload
    if isinstance(payload, bytes):
        payload_str = payload.decode("utf-8")
    else:
        payload_str = payload

    parsed = json.loads(payload_str)

    # Construct the typed event using Telnyx's model infrastructure
    return construct_type(type_=UnwrapWebhookEvent, value=parsed)  # type: ignore[return-value]


# ---------------------------------------------------------------------------
# Monkey-patch: make ED25519 the default for WebhooksResource.unwrap()
# ---------------------------------------------------------------------------
#
# The generated `WebhooksResource` and `AsyncWebhooksResource` in
# `telnyx/resources/webhooks.py` use StandardWebhooks (HMAC-SHA256)
# for verification. We replace their `unwrap` methods with ED25519
# versions so that `client.webhooks.unwrap()` does the right thing
# by default, matching Go, TypeScript, PHP, and Java SDKs.
#
# The original HMAC-based methods are preserved as `_unwrap_hmac`
# on each class for anyone who needs the old behavior.

from telnyx._models import construct_type as _construct_type
from telnyx.resources.webhooks import (
    WebhooksResource as _WebhooksResource,
    AsyncWebhooksResource as _AsyncWebhooksResource,
)
from telnyx.types.unwrap_webhook_event import UnwrapWebhookEvent as _UnwrapWebhookEvent

# Preserve originals before patching
_WebhooksResource._unwrap_hmac = _WebhooksResource.unwrap  # type: ignore[attr-defined]
_AsyncWebhooksResource._unwrap_hmac = _AsyncWebhooksResource.unwrap  # type: ignore[attr-defined]


def _ed25519_unwrap(
    self: _WebhooksResource,
    payload: str,
    *,
    headers: Mapping[str, str],
    key: str | bytes | None = None,
) -> _UnwrapWebhookEvent:
    """Verify a Telnyx webhook using ED25519 signature verification.

    This is the patched version of ``WebhooksResource.unwrap`` that
    uses ED25519 instead of HMAC-SHA256, matching the behavior of
    the Go, TypeScript, PHP, and Java SDKs.

    To use the old HMAC-SHA256 verification, call
    ``client.webhooks._unwrap_hmac(payload, headers=headers)`` instead.
    """
    public_key = key or self._client.public_key

    if not public_key:
        raise ValueError(
            "Cannot verify a webhook without a key on either the client's public_key or passed in as an argument"
        )

    if isinstance(public_key, bytes):
        import base64

        public_key = base64.b64encode(public_key).decode("ascii")

    verify_webhook_signature(payload, headers, public_key)

    return cast(
        _UnwrapWebhookEvent,
        _construct_type(
            type_=_UnwrapWebhookEvent,
            value=json.loads(payload),
        ),
    )


async def _async_ed25519_unwrap(
    self: _AsyncWebhooksResource,
    payload: str,
    *,
    headers: Mapping[str, str],
    key: str | bytes | None = None,
) -> _UnwrapWebhookEvent:
    """Verify a Telnyx webhook using ED25519 signature verification (async).

    This is the patched version of ``AsyncWebhooksResource.unwrap`` that
    uses ED25519 instead of HMAC-SHA256, matching the behavior of
    the Go, TypeScript, PHP, and Java SDKs.

    To use the old HMAC-SHA256 verification, call
    ``client.webhooks._unwrap_hmac(payload, headers=headers)`` instead.
    """
    public_key = key or self._client.public_key

    if not public_key:
        raise ValueError(
            "Cannot verify a webhook without a key on either the client's public_key or passed in as an argument"
        )

    if isinstance(public_key, bytes):
        import base64

        public_key = base64.b64encode(public_key).decode("ascii")

    verify_webhook_signature(payload, headers, public_key)

    return cast(
        _UnwrapWebhookEvent,
        _construct_type(
            type_=_UnwrapWebhookEvent,
            value=json.loads(payload),
        ),
    )


# Apply the patches
_WebhooksResource.unwrap = _ed25519_unwrap  # type: ignore[assignment]
_AsyncWebhooksResource.unwrap = _async_ed25519_unwrap  # type: ignore[assignment]

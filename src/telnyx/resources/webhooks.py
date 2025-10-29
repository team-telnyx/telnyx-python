# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import json
import time
import base64
from typing import Mapping, cast

from .._models import construct_type
from .._resource import SyncAPIResource, AsyncAPIResource
from .._exceptions import TelnyxError
from ..types.unwrap_webhook_event import UnwrapWebhookEvent
from ..types.unsafe_unwrap_webhook_event import UnsafeUnwrapWebhookEvent

__all__ = ["WebhooksResource", "AsyncWebhooksResource", "TelnyxWebhookVerificationError"]


class TelnyxWebhookVerificationError(TelnyxError):
    """Raised when webhook signature verification fails."""
    pass


def _get_header_case_insensitive(headers: dict[str, str], key: str) -> str | None:
    """Get header value case-insensitively."""
    key_lower = key.lower()
    for header_key, header_value in headers.items():
        if header_key.lower() == key_lower:
            return header_value
    return None


def _verify_signature(payload: str, headers: dict[str, str], public_key: str | bytes) -> None:
    """
    Verify Telnyx webhook signature using ED25519 cryptography.

    Args:
        payload: The raw webhook payload as a string
        headers: The webhook headers
        public_key: The ED25519 public key (base64 string from Mission Control)

    Raises:
        TelnyxWebhookVerificationError: If verification fails
    """
    try:
        from nacl.signing import VerifyKey
        from nacl.exceptions import BadSignatureError
    except ImportError as exc:
        raise TelnyxError("You need to install `pynacl` to use webhook verification") from exc

    # Extract required headers (case-insensitive)
    signature_header = _get_header_case_insensitive(headers, 'telnyx-signature-ed25519')
    timestamp_header = _get_header_case_insensitive(headers, 'telnyx-timestamp')

    if not signature_header:
        raise TelnyxWebhookVerificationError("Missing header: Telnyx-Signature-Ed25519")

    if not timestamp_header:
        raise TelnyxWebhookVerificationError("Missing header: Telnyx-Timestamp")

    # Validate timestamp to prevent replay attacks (5 minute tolerance)
    try:
        webhook_time = int(timestamp_header)
        current_time = int(time.time())
        if abs(current_time - webhook_time) > 300:  # 5 minutes
            raise TelnyxWebhookVerificationError(f"Webhook timestamp too old or too new: {timestamp_header}")
    except ValueError as exc:
        raise TelnyxWebhookVerificationError(f"Invalid timestamp format: {timestamp_header}") from exc

    # Decode public key from base64 (Telnyx provides keys in base64 format)
    try:
        if isinstance(public_key, str):
            public_key_bytes = base64.b64decode(public_key)
        else:
            public_key_bytes = public_key

        if len(public_key_bytes) != 32:
            raise TelnyxWebhookVerificationError(
                f"Invalid public key: expected 32 bytes, got {len(public_key_bytes)} bytes"
            )

        verify_key = VerifyKey(public_key_bytes)
    except Exception as exc:
        raise TelnyxWebhookVerificationError(f"Invalid public key format: {exc}") from exc

    # Decode signature from base64 (Telnyx sends signatures in base64 format)
    try:
        signature_bytes = base64.b64decode(signature_header)

        if len(signature_bytes) != 64:
            raise TelnyxWebhookVerificationError(
                f"Invalid signature length: expected 64 bytes, got {len(signature_bytes)} bytes"
            )
    except Exception as exc:
        raise TelnyxWebhookVerificationError(f"Invalid signature format: {exc}") from exc

    # Create the signed payload: timestamp|payload
    signed_payload = f"{timestamp_header}|{payload}".encode('utf-8')

    # Verify the signature
    try:
        verify_key.verify(signed_payload, signature_bytes)
    except BadSignatureError as exc:
        raise TelnyxWebhookVerificationError(
            "Signature verification failed: signature does not match payload"
        ) from exc


class WebhooksResource(SyncAPIResource):
    def unsafe_unwrap(self, payload: str) -> UnsafeUnwrapWebhookEvent:
        return cast(
            UnsafeUnwrapWebhookEvent,
            construct_type(
                type_=UnsafeUnwrapWebhookEvent,
                value=json.loads(payload),
            ),
        )

    def unwrap(self, payload: str, *, headers: Mapping[str, str], key: str | bytes | None = None) -> UnwrapWebhookEvent:
        if key is None:
            key = self._client.public_key
            if key is None:
                raise ValueError(
                    "Cannot verify a webhook without a key on either the client's public_key or passed in as an argument"
                )

        if not isinstance(headers, dict):
            headers = dict(headers)

        _verify_signature(payload, headers, key)

        return cast(
            UnwrapWebhookEvent,
            construct_type(
                type_=UnwrapWebhookEvent,
                value=json.loads(payload),
            ),
        )


class AsyncWebhooksResource(AsyncAPIResource):
    def unsafe_unwrap(self, payload: str) -> UnsafeUnwrapWebhookEvent:
        return cast(
            UnsafeUnwrapWebhookEvent,
            construct_type(
                type_=UnsafeUnwrapWebhookEvent,
                value=json.loads(payload),
            ),
        )

    def unwrap(self, payload: str, *, headers: Mapping[str, str], key: str | bytes | None = None) -> UnwrapWebhookEvent:
        if key is None:
            key = self._client.public_key
            if key is None:
                raise ValueError(
                    "Cannot verify a webhook without a key on either the client's public_key or passed in as an argument"
                )

        if not isinstance(headers, dict):
            headers = dict(headers)

        _verify_signature(payload, headers, key)

        return cast(
            UnwrapWebhookEvent,
            construct_type(
                type_=UnwrapWebhookEvent,
                value=json.loads(payload),
            ),
        )

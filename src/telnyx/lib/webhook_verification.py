# Telnyx webhook verification using ED25519 signatures.
#
# This module provides ED25519 signature verification for Telnyx webhooks,
# matching the implementation pattern used in the Node SDK.
#
# The module is kept separate from generated code to avoid merge conflicts
# when Stainless updates webhook event types.
#
# Example usage:
#
#     from telnyx import Telnyx
#     from telnyx.lib import verify_signature, TelnyxWebhookVerificationError
#
#     client = Telnyx(
#         api_key=os.environ["TELNYX_API_KEY"],
#         public_key=os.environ["TELNYX_PUBLIC_KEY"],  # Base64 from Mission Control
#     )
#
#     # In your webhook handler:
#     try:
#         event = client.webhooks.unwrap(payload, headers=headers)
#     except TelnyxWebhookVerificationError as e:
#         return Response(status=401)

from __future__ import annotations

import time
import base64
from typing import Union

from .._exceptions import TelnyxError

__all__ = ["TelnyxWebhookVerificationError", "verify_signature"]

# Telnyx webhook signature headers (case-insensitive per HTTP spec)
SIGNATURE_HEADER = "telnyx-signature-ed25519"
TIMESTAMP_HEADER = "telnyx-timestamp"

# Tolerance for timestamp validation (5 minutes)
TIMESTAMP_TOLERANCE_SECONDS = 300


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


def verify_signature(payload: str, headers: dict[str, str], public_key: Union[str, bytes]) -> None:
    """
    Verify Telnyx webhook signature using ED25519 cryptography.

    This function verifies that a webhook payload was signed by Telnyx using
    ED25519 signatures. It checks the signature header and validates the
    timestamp to prevent replay attacks.

    Args:
        payload: The raw webhook payload as a string
        headers: The webhook headers (case-insensitive lookup)
        public_key: The ED25519 public key (base64 string from Mission Control)

    Raises:
        TelnyxWebhookVerificationError: If verification fails
        TelnyxError: If pynacl is not installed

    Example:
        >>> verify_signature(payload, headers, os.environ["TELNYX_PUBLIC_KEY"])
    """
    try:
        from nacl.signing import VerifyKey
        from nacl.exceptions import BadSignatureError
    except ImportError as exc:
        raise TelnyxError("You need to install `pynacl` to use webhook verification") from exc

    # Extract required headers (case-insensitive)
    signature_header = _get_header_case_insensitive(headers, SIGNATURE_HEADER)
    timestamp_header = _get_header_case_insensitive(headers, TIMESTAMP_HEADER)

    if not signature_header:
        raise TelnyxWebhookVerificationError(f"Missing header: {SIGNATURE_HEADER}")

    if not timestamp_header:
        raise TelnyxWebhookVerificationError(f"Missing header: {TIMESTAMP_HEADER}")

    # Validate timestamp to prevent replay attacks
    try:
        webhook_time = int(timestamp_header)
        current_time = int(time.time())
        if abs(current_time - webhook_time) > TIMESTAMP_TOLERANCE_SECONDS:
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
    signed_payload = f"{timestamp_header}|{payload}".encode("utf-8")

    # Verify the signature
    try:
        verify_key.verify(signed_payload, signature_bytes)
    except BadSignatureError as exc:
        raise TelnyxWebhookVerificationError(
            "Signature verification failed: signature does not match payload"
        ) from exc

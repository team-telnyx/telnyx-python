# Telnyx ED25519 Webhook Verification
#
# This module provides ED25519 signature verification for Telnyx webhooks,
# matching the implementation pattern used in the Go, Java, and Ruby SDKs.
#
# This file is in the `lib/` directory which is preserved across Stainless
# code generation runs. Do not move it to the generated code directories.
#
# Usage:
#
#   from telnyx.lib.webhook_verification import verify_webhook_signature, WebhookVerificationError
#
#   try:
#       verify_webhook_signature(payload, headers, public_key)
#   except WebhookVerificationError as e:
#       print(f"Verification failed: {e}")
#
# Or use the higher-level unwrap with ED25519:
#
#   from telnyx.lib.webhooks_ed25519 import unwrap_with_ed25519
#
#   event = unwrap_with_ed25519(client, payload, headers)

from __future__ import annotations

import time
import base64
from typing import Mapping

__all__ = [
    "WebhookVerificationError",
    "verify_webhook_signature",
    "SIGNATURE_HEADER",
    "TIMESTAMP_HEADER",
    "TIMESTAMP_TOLERANCE_SECONDS",
]

# Telnyx webhook signature headers (case-insensitive per HTTP spec)
SIGNATURE_HEADER = "telnyx-signature-ed25519"
TIMESTAMP_HEADER = "telnyx-timestamp"

# Tolerance for timestamp validation (5 minutes)
TIMESTAMP_TOLERANCE_SECONDS = 300


class WebhookVerificationError(Exception):
    """Error raised when webhook signature verification fails.

    This error is raised by the webhook verification module when:
    - No public key is configured
    - Required headers are missing (telnyx-signature-ed25519, telnyx-timestamp)
    - Timestamp is too old or too new (outside 5-minute tolerance)
    - Signature verification fails
    - Public key or signature format is invalid

    Example:
        try:
            verify_webhook_signature(payload, headers, public_key)
        except WebhookVerificationError as e:
            print(f"Webhook verification failed: {e}")
    """

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)


def _get_header(headers: Mapping[str, str], key: str) -> str | None:
    """Get header value case-insensitively.

    Args:
        headers: The headers mapping
        key: The header key to find

    Returns:
        The header value or None if not found
    """
    key_lower = key.lower()
    for header_key, header_value in headers.items():
        if header_key.lower() == key_lower:
            return header_value
    return None


def verify_webhook_signature(
    payload: str | bytes,
    headers: Mapping[str, str],
    public_key: str,
) -> None:
    """Verify the ED25519 signature of a Telnyx webhook.

    Telnyx webhooks are signed using ED25519 with the following format:
    - Header "Telnyx-Signature-Ed25519": Base64-encoded ED25519 signature (64 bytes)
    - Header "Telnyx-Timestamp": Unix timestamp in seconds
    - Signed payload: "{timestamp}|{payload}"

    Args:
        payload: The raw webhook body as string or bytes
        headers: The webhook HTTP headers
        public_key: Base64-encoded ED25519 public key from Telnyx Mission Control

    Raises:
        WebhookVerificationError: If verification fails for any reason

    Example:
        verify_webhook_signature(request.body, request.headers, os.environ["TELNYX_PUBLIC_KEY"])
    """
    # Lazy import to avoid making nacl a hard dependency
    try:
        from nacl.signing import VerifyKey  # type: ignore[import-not-found]
        from nacl.exceptions import BadSignatureError  # type: ignore[import-not-found]
    except ImportError as exc:
        raise WebhookVerificationError(
            "PyNaCl is required for ED25519 webhook verification. Install it with: pip install pynacl"
        ) from exc

    # Extract required headers (case-insensitive)
    signature_header = _get_header(headers, SIGNATURE_HEADER)
    timestamp_header = _get_header(headers, TIMESTAMP_HEADER)

    if not signature_header:
        raise WebhookVerificationError(f"Missing required header: {SIGNATURE_HEADER}")

    if not timestamp_header:
        raise WebhookVerificationError(f"Missing required header: {TIMESTAMP_HEADER}")

    # Validate timestamp to prevent replay attacks (5 minute tolerance)
    try:
        webhook_time = int(timestamp_header)
        current_time = int(time.time())
        time_diff = abs(current_time - webhook_time)

        if time_diff > TIMESTAMP_TOLERANCE_SECONDS:
            raise WebhookVerificationError(f"Webhook timestamp is too old or too new ({time_diff}s difference)")
    except ValueError as e:
        raise WebhookVerificationError(f"Invalid timestamp format: {timestamp_header}") from e

    # Decode public key from base64
    try:
        public_key_bytes = base64.b64decode(public_key)
        if len(public_key_bytes) != 32:
            raise WebhookVerificationError(f"Invalid public key: expected 32 bytes, got {len(public_key_bytes)} bytes")
    except Exception as e:
        if isinstance(e, WebhookVerificationError):
            raise
        raise WebhookVerificationError(f"Invalid public key format: {e}") from e

    # Decode signature from base64
    try:
        signature_bytes = base64.b64decode(signature_header)
        if len(signature_bytes) != 64:
            raise WebhookVerificationError(
                f"Invalid signature length: expected 64 bytes, got {len(signature_bytes)} bytes"
            )
    except Exception as e:
        if isinstance(e, WebhookVerificationError):
            raise
        raise WebhookVerificationError(f"Invalid signature format: {e}") from e

    # Convert payload to string if bytes
    if isinstance(payload, bytes):
        payload_str = payload.decode("utf-8")
    else:
        payload_str = payload

    # Build the signed payload: "{timestamp}|{payload}"
    signed_payload = f"{timestamp_header}|{payload_str}"

    # Verify the ED25519 signature using PyNaCl
    try:
        verify_key = VerifyKey(public_key_bytes)  # type: ignore[no-untyped-call]
        # PyNaCl's verify expects message + signature combined, or use verify_key.verify(signature, message)
        # Actually, we need to use the raw verify since we have separate signature and message
        verify_key.verify(signed_payload.encode("utf-8"), signature_bytes)  # type: ignore[no-untyped-call]
    except BadSignatureError as e:  # type: ignore[no-untyped-call]
        raise WebhookVerificationError("Signature verification failed: signature does not match payload") from e
    except Exception as e:
        raise WebhookVerificationError(f"Signature verification failed: {e}") from e

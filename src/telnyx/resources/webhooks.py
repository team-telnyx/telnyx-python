# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import json
from typing import Mapping, cast
from datetime import datetime, timezone

from .._models import construct_type
from .._resource import SyncAPIResource, AsyncAPIResource
from .._exceptions import TelnyxError
from ..types.unwrap_webhook_event import UnwrapWebhookEvent
from ..types.unsafe_unwrap_webhook_event import UnsafeUnwrapWebhookEvent

__all__ = ["WebhooksResource", "AsyncWebhooksResource", "TelnyxWebhook", "TelnyxWebhookVerificationError"]


class TelnyxWebhookVerificationError(TelnyxError):
    """Raised when webhook verification fails."""
    pass


class TelnyxWebhook:
    """
    Telnyx webhook verification following the standardwebhooks pattern.
    
    This class provides ED25519 signature verification for Telnyx webhooks
    using the same interface pattern as the standardwebhooks library.
    """
    
    def __init__(self, key: str | bytes):
        """
        Initialize the webhook verifier with a public key.
        
        Args:
            key: The public key for verification (hex string or bytes)
        """
        try:
            from nacl.signing import VerifyKey
        except ImportError as exc:
            raise TelnyxError("You need to install `pynacl` to verify Telnyx webhooks") from exc
        
        # Convert key to bytes if it's a string
        if isinstance(key, str):
            try:
                key = bytes.fromhex(key)  # Convert from hex string to bytes
            except ValueError as exc:
                raise TelnyxWebhookVerificationError(f"Invalid key format: {key!r}") from exc
        
        self._verify_key = VerifyKey(key)
    
    def verify(self, payload: str, headers: Mapping[str, str]) -> None:
        """
        Verify a webhook payload and headers.
        
        Args:
            payload: The webhook payload string
            headers: The webhook headers
            
        Raises:
            TelnyxWebhookVerificationError: If verification fails
        """
        try:
            from nacl.exceptions import BadSignatureError
        except ImportError as exc:
            raise TelnyxError("You need to install `pynacl` to verify Telnyx webhooks") from exc
        
        # Extract required headers (case-insensitive lookup)
        signature_header = headers.get("Telnyx-Signature-Ed25519") or headers.get("telnyx-signature-ed25519")
        timestamp_header = headers.get("Telnyx-Timestamp") or headers.get("telnyx-timestamp")
        user_agent = headers.get("User-Agent") or headers.get("user-agent", "")

        # Validate required headers
        if not signature_header:
            raise TelnyxWebhookVerificationError("Missing required header: Telnyx-Signature-Ed25519")
        
        if not timestamp_header:
            raise TelnyxWebhookVerificationError("Missing required header: Telnyx-Timestamp")

        # Verify User-Agent if present (optional security check)
        if user_agent and "telnyx-webhooks" not in user_agent.lower():
            raise TelnyxWebhookVerificationError(f"Unexpected User-Agent: {user_agent}")

        # Validate timestamp format and prevent replay attacks
        try:
            webhook_time = int(timestamp_header)
            current_time = int(datetime.now(timezone.utc).timestamp())
            
            # Allow 5 minutes tolerance
            if abs(current_time - webhook_time) > 300:
                raise TelnyxWebhookVerificationError(
                    f"Webhook timestamp too old or too new: {timestamp_header}"
                )
        except ValueError as exc:
            raise TelnyxWebhookVerificationError(
                f"Invalid timestamp format: {timestamp_header}"
            ) from exc

        # Decode the signature from hex
        try:
            signature = bytes.fromhex(signature_header)
        except ValueError as exc:
            raise TelnyxWebhookVerificationError(
                f"Invalid signature format: {signature_header}"
            ) from exc

        # Create the signed payload: timestamp + payload
        signed_payload = timestamp_header.encode('utf-8') + payload.encode('utf-8')

        # Verify the signature
        try:
            self._verify_key.verify(signed_payload, signature)
        except BadSignatureError as exc:
            raise TelnyxWebhookVerificationError("Invalid webhook signature") from exc


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

        # Use Telnyx-specific webhook verification following standardwebhooks pattern
        webhook = TelnyxWebhook(key)
        webhook.verify(payload, headers)

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

        # Use Telnyx-specific webhook verification following standardwebhooks pattern
        webhook = TelnyxWebhook(key)
        webhook.verify(payload, headers)

        return cast(
            UnwrapWebhookEvent,
            construct_type(
                type_=UnwrapWebhookEvent,
                value=json.loads(payload),
            ),
        )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import json
from typing import Mapping, cast

from .._models import construct_type
from .._resource import SyncAPIResource, AsyncAPIResource
from .._exceptions import TelnyxError
from ..types.unwrap_webhook_event import UnwrapWebhookEvent
from ..types.unsafe_unwrap_webhook_event import UnsafeUnwrapWebhookEvent

__all__ = ["WebhooksResource", "AsyncWebhooksResource"]


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
        import time
        import base64

        try:
            from nacl.signing import VerifyKey
            from nacl.exceptions import BadSignatureError
        except ImportError as exc:
            raise TelnyxError("You need to install `telnyx[webhooks]` to use this method") from exc

        if key is None:
            key = self._client.public_key
            if key is None:
                raise ValueError(
                    "Cannot verify a webhook without a key on either the client's public_key or passed in as an argument"
                )

        normalized_headers = {name.lower(): value for name, value in headers.items()}
        signature_header = normalized_headers.get("telnyx-signature-ed25519")
        timestamp_header = normalized_headers.get("telnyx-timestamp")
        if signature_header is None:
            raise ValueError("Missing required header: Telnyx-Signature-Ed25519")
        if timestamp_header is None:
            raise ValueError("Missing required header: Telnyx-Timestamp")

        try:
            timestamp = int(timestamp_header)
        except ValueError as exc:
            raise ValueError(f"Invalid timestamp format: {timestamp_header}") from exc
        if abs(time.time() - timestamp) > 300:
            raise ValueError("Webhook timestamp is too old or too new")

        try:
            public_key = key if isinstance(key, bytes) else base64.b64decode(key, validate=True)
            signature = base64.b64decode(signature_header, validate=True)
        except Exception as exc:
            raise ValueError(f"Invalid webhook key or signature encoding: {exc}") from exc
        if len(public_key) != 32:
            raise ValueError(f"Invalid public key: expected 32 bytes, got {len(public_key)} bytes")
        if len(signature) != 64:
            raise ValueError(f"Invalid signature: expected 64 bytes, got {len(signature)} bytes")

        try:
            VerifyKey(public_key).verify(f"{timestamp_header}|{payload}".encode("utf-8"), signature)
        except BadSignatureError as exc:
            raise ValueError("Signature verification failed: signature does not match payload") from exc

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
        import time
        import base64

        try:
            from nacl.signing import VerifyKey
            from nacl.exceptions import BadSignatureError
        except ImportError as exc:
            raise TelnyxError("You need to install `telnyx[webhooks]` to use this method") from exc

        if key is None:
            key = self._client.public_key
            if key is None:
                raise ValueError(
                    "Cannot verify a webhook without a key on either the client's public_key or passed in as an argument"
                )

        normalized_headers = {name.lower(): value for name, value in headers.items()}
        signature_header = normalized_headers.get("telnyx-signature-ed25519")
        timestamp_header = normalized_headers.get("telnyx-timestamp")
        if signature_header is None:
            raise ValueError("Missing required header: Telnyx-Signature-Ed25519")
        if timestamp_header is None:
            raise ValueError("Missing required header: Telnyx-Timestamp")

        try:
            timestamp = int(timestamp_header)
        except ValueError as exc:
            raise ValueError(f"Invalid timestamp format: {timestamp_header}") from exc
        if abs(time.time() - timestamp) > 300:
            raise ValueError("Webhook timestamp is too old or too new")

        try:
            public_key = key if isinstance(key, bytes) else base64.b64decode(key, validate=True)
            signature = base64.b64decode(signature_header, validate=True)
        except Exception as exc:
            raise ValueError(f"Invalid webhook key or signature encoding: {exc}") from exc
        if len(public_key) != 32:
            raise ValueError(f"Invalid public key: expected 32 bytes, got {len(public_key)} bytes")
        if len(signature) != 64:
            raise ValueError(f"Invalid signature: expected 64 bytes, got {len(signature)} bytes")

        try:
            VerifyKey(public_key).verify(f"{timestamp_header}|{payload}".encode("utf-8"), signature)
        except BadSignatureError as exc:
            raise ValueError("Signature verification failed: signature does not match payload") from exc

        return cast(
            UnwrapWebhookEvent,
            construct_type(
                type_=UnwrapWebhookEvent,
                value=json.loads(payload),
            ),
        )

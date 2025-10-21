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
        try:
            from standardwebhooks import Webhook
        except ImportError as exc:
            raise TelnyxError("You need to install `telnyx[webhooks]` to use this method") from exc

        if key is None:
            key = self._client.public_key
            if key is None:
                raise ValueError(
                    "Cannot verify a webhook without a key on either the client's public_key or passed in as an argument"
                )

        if not isinstance(headers, dict):
            headers = dict(headers)

        Webhook(key).verify(payload, headers)

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
        try:
            from standardwebhooks import Webhook
        except ImportError as exc:
            raise TelnyxError("You need to install `telnyx[webhooks]` to use this method") from exc

        if key is None:
            key = self._client.public_key
            if key is None:
                raise ValueError(
                    "Cannot verify a webhook without a key on either the client's public_key or passed in as an argument"
                )

        if not isinstance(headers, dict):
            headers = dict(headers)

        Webhook(key).verify(payload, headers)

        return cast(
            UnwrapWebhookEvent,
            construct_type(
                type_=UnwrapWebhookEvent,
                value=json.loads(payload),
            ),
        )

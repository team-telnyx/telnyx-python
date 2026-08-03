# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .email_webhook_event import EmailWebhookEvent as EmailWebhookEvent
from .webhook_list_params import WebhookListParams as WebhookListParams
from .webhook_create_params import WebhookCreateParams as WebhookCreateParams
from .webhook_update_params import WebhookUpdateParams as WebhookUpdateParams

if TYPE_CHECKING:
    from .email_webhook import EmailWebhook as EmailWebhook
    from .email_webhook_response import EmailWebhookResponse as EmailWebhookResponse
    from .offset_pagination_meta import OffsetPaginationMeta as OffsetPaginationMeta


def __getattr__(name: str) -> Any:
    if name == "EmailWebhook":
        from .email_webhook import EmailWebhook

        return EmailWebhook
    if name == "EmailWebhookResponse":
        from .email_webhook_response import EmailWebhookResponse

        return EmailWebhookResponse
    if name == "OffsetPaginationMeta":
        from .offset_pagination_meta import OffsetPaginationMeta

        return OffsetPaginationMeta
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

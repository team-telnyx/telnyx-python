# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from .email_webhook_event import EmailWebhookEvent

__all__ = ["WebhookUpdateParams"]


class WebhookUpdateParams(TypedDict, total=False):
    domain_id: Required[str]

    events: List[EmailWebhookEvent]

    url: str

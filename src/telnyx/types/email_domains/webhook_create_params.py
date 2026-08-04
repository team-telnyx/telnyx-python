# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from .email_webhook_event import EmailWebhookEvent

__all__ = ["WebhookCreateParams"]


class WebhookCreateParams(TypedDict, total=False):
    events: Required[List[EmailWebhookEvent]]
    """At least one event type is required."""

    url: Required[str]
    """HTTPS endpoint to deliver subscribed events to."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .email_webhook_event import EmailWebhookEvent

__all__ = ["EmailWebhook"]


class EmailWebhook(BaseModel):
    id: str

    created_at: datetime

    domain_id: str

    events: List[EmailWebhookEvent]
    """Allowlist of event types delivered to this webhook.

    At least one event is required — there is no default-to-all.
    """

    record_type: Literal["email_webhook"]

    updated_at: datetime

    url: str
    """HTTPS endpoint to deliver subscribed events to."""

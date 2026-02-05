# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .outbound_message import OutboundMessage

__all__ = ["DeliveryUpdateWebhookEvent", "Meta"]


class Meta(BaseModel):
    attempt: Optional[int] = None
    """Number of attempts to deliver the webhook event."""

    delivered_to: Optional[str] = None
    """The webhook URL the event was delivered to."""


class DeliveryUpdateWebhookEvent(BaseModel):
    data: Optional[OutboundMessage] = None

    meta: Optional[Meta] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .outbound_message_payload import OutboundMessagePayload

__all__ = ["DeliveryUpdateWebhookEvent", "Data", "Meta"]


class Data(BaseModel):
    id: Optional[str] = None
    """Identifies the type of resource."""

    event_type: Optional[Literal["message.sent", "message.finalized"]] = None
    """The type of event being delivered."""

    occurred_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    payload: Optional[OutboundMessagePayload] = None

    record_type: Optional[Literal["event"]] = None
    """Identifies the type of the resource."""


class Meta(BaseModel):
    attempt: Optional[int] = None
    """Number of attempts to deliver the webhook event."""

    delivered_to: Optional[str] = None
    """The webhook URL the event was delivered to."""


class DeliveryUpdateWebhookEvent(BaseModel):
    data: Optional[Data] = None

    meta: Optional[Meta] = None

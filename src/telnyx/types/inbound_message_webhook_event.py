# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.inbound_message_payload import InboundMessagePayload

__all__ = ["InboundMessageWebhookEvent", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """Identifies the type of resource."""

    event_type: Optional[Literal["message.received"]] = None
    """The type of event being delivered."""

    occurred_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    payload: Optional[InboundMessagePayload] = None

    record_type: Optional[Literal["event"]] = None
    """Identifies the type of the resource."""


class InboundMessageWebhookEvent(BaseModel):
    data: Optional[Data] = None

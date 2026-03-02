# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PortingEventWithoutWebhook"]


class PortingEventWithoutWebhook(BaseModel):
    id: Optional[str] = None
    """Uniquely identifies the event."""

    available_notification_methods: Optional[List[Literal["email", "webhook", "webhook_v1"]]] = None
    """Indicates the notification methods used."""

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    event_type: Optional[Literal["porting_order.loa_updated", "porting_order.sharing_token_expired"]] = None
    """Identifies the event type"""

    payload: None = None

    payload_status: Optional[Literal["created", "completed"]] = None
    """The status of the payload generation."""

    porting_order_id: Optional[str] = None
    """Identifies the porting order associated with the event."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was updated."""

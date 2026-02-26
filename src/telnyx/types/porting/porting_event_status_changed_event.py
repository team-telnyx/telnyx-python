# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.porting_order_status import PortingOrderStatus

__all__ = ["PortingEventStatusChangedEvent", "Payload"]


class Payload(BaseModel):
    """The webhook payload for the porting_order.status_changed event"""

    id: Optional[str] = None
    """Identifies the porting order that was moved."""

    customer_reference: Optional[str] = None
    """Identifies the customer reference associated with the porting order."""

    status: Optional[PortingOrderStatus] = None
    """Porting order status"""

    support_key: Optional[str] = None
    """Identifies the support key associated with the porting order."""

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the porting order was moved."""

    webhook_url: Optional[str] = None
    """The URL to send the webhook to."""


class PortingEventStatusChangedEvent(BaseModel):
    id: Optional[str] = None
    """Uniquely identifies the event."""

    available_notification_methods: Optional[List[Literal["email", "webhook", "webhook_v1"]]] = None
    """Indicates the notification methods used."""

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    event_type: Optional[
        Literal[
            "porting_order.deleted",
            "porting_order.loa_updated",
            "porting_order.messaging_changed",
            "porting_order.status_changed",
            "porting_order.sharing_token_expired",
            "porting_order.new_comment",
            "porting_order.split",
        ]
    ] = None
    """Identifies the event type"""

    payload: Optional[Payload] = None
    """The webhook payload for the porting_order.status_changed event"""

    payload_status: Optional[Literal["created", "completed"]] = None
    """The status of the payload generation."""

    porting_order_id: Optional[str] = None
    """Identifies the porting order associated with the event."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was updated."""

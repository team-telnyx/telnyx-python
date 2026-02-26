# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PortingEventDeletedPayload", "Payload"]


class Payload(BaseModel):
    id: Optional[str] = None
    """Identifies the porting order that was deleted."""

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    customer_reference: Optional[str] = None
    """Identifies the customer reference associated with the porting order."""

    deleted_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the porting order was deleted."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was updated."""


class PortingEventDeletedPayload(BaseModel):
    id: Optional[str] = None
    """Uniquely identifies the event."""

    available_notification_methods: Optional[List[Literal["email", "webhook", "webhook_v1"]]] = None
    """Indicates the notification methods used."""

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

    payload_status: Optional[Literal["created", "completed"]] = None
    """The status of the payload generation."""

    porting_order_id: Optional[str] = None
    """Identifies the porting order associated with the event."""

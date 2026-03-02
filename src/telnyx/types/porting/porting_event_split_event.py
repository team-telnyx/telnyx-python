# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PortingEventSplitEvent", "Payload", "PayloadFrom", "PayloadPortingPhoneNumber", "PayloadTo"]


class PayloadFrom(BaseModel):
    """The porting order that was split."""

    id: Optional[str] = None
    """Identifies the porting order that was split."""


class PayloadPortingPhoneNumber(BaseModel):
    id: Optional[str] = None
    """Identifies the porting phone number that was moved."""


class PayloadTo(BaseModel):
    """The new porting order that the phone numbers was moved to."""

    id: Optional[str] = None
    """Identifies the porting order that was split."""


class Payload(BaseModel):
    """The webhook payload for the porting_order.split event"""

    from_: Optional[PayloadFrom] = FieldInfo(alias="from", default=None)
    """The porting order that was split."""

    porting_phone_numbers: Optional[List[PayloadPortingPhoneNumber]] = None
    """The list of porting phone numbers that were moved to the new porting order."""

    to: Optional[PayloadTo] = None
    """The new porting order that the phone numbers was moved to."""


class PortingEventSplitEvent(BaseModel):
    id: Optional[str] = None
    """Uniquely identifies the event."""

    available_notification_methods: Optional[List[Literal["email", "webhook", "webhook_v1"]]] = None
    """Indicates the notification methods used."""

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    event_type: Optional[Literal["porting_order.split"]] = None
    """Identifies the event type"""

    payload: Optional[Payload] = None
    """The webhook payload for the porting_order.split event"""

    payload_status: Optional[Literal["created", "completed"]] = None
    """The status of the payload generation."""

    porting_order_id: Optional[str] = None
    """Identifies the porting order associated with the event."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was updated."""

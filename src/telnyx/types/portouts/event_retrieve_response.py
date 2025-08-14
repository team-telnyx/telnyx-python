# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "EventRetrieveResponse",
    "Data",
    "DataPayload",
    "DataPayloadWebhookPortoutStatusChangedPayload",
    "DataPayloadWebhookPortoutNewCommentPayload",
    "DataPayloadWebhookPortoutFocDateChangedPayload",
]


class DataPayloadWebhookPortoutStatusChangedPayload(BaseModel):
    id: Optional[str] = None
    """Identifies the port out that was moved."""

    attempted_pin: Optional[str] = None
    """The PIN that was attempted to be used to authorize the port out."""

    carrier_name: Optional[str] = None
    """Carrier the number will be ported out to"""

    phone_numbers: Optional[List[str]] = None
    """Phone numbers associated with this port-out order"""

    rejection_reason: Optional[str] = None
    """The reason why the order is being rejected by the user.

    If the order is authorized, this field can be left null
    """

    spid: Optional[str] = None
    """The new carrier SPID."""

    status: Optional[Literal["pending", "authorized", "ported", "rejected", "rejected-pending", "canceled"]] = None
    """The new status of the port out."""

    subscriber_name: Optional[str] = None
    """The name of the port-out's end user."""

    user_id: Optional[str] = None
    """Identifies the user that the port-out order belongs to."""


class DataPayloadWebhookPortoutNewCommentPayload(BaseModel):
    id: Optional[str] = None
    """Identifies the comment that was added to the port-out order."""

    comment: Optional[str] = None
    """The body of the comment."""

    portout_id: Optional[str] = None
    """Identifies the port-out order that the comment was added to."""

    user_id: Optional[str] = None
    """Identifies the user that added the comment."""


class DataPayloadWebhookPortoutFocDateChangedPayload(BaseModel):
    id: Optional[str] = None
    """Identifies the port-out order that have the FOC date changed."""

    foc_date: Optional[datetime] = None
    """ISO 8601 formatted date indicating the new FOC date."""

    user_id: Optional[str] = None
    """Identifies the organization that port-out order belongs to."""


DataPayload: TypeAlias = Union[
    DataPayloadWebhookPortoutStatusChangedPayload,
    DataPayloadWebhookPortoutNewCommentPayload,
    DataPayloadWebhookPortoutFocDateChangedPayload,
]


class Data(BaseModel):
    id: Optional[str] = None
    """Uniquely identifies the event."""

    available_notification_methods: Optional[List[Literal["email", "webhook"]]] = None
    """Indicates the notification methods used."""

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    event_type: Optional[Literal["portout.status_changed", "portout.foc_date_changed", "portout.new_comment"]] = None
    """Identifies the event type"""

    payload: Optional[DataPayload] = None
    """The webhook payload for the portout.status_changed event"""

    payload_status: Optional[Literal["created", "completed"]] = None
    """The status of the payload generation."""

    portout_id: Optional[str] = None
    """Identifies the port-out order associated with the event."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was updated."""


class EventRetrieveResponse(BaseModel):
    data: Optional[Data] = None

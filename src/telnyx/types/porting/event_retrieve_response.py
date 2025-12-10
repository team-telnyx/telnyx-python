# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.porting_order_status import PortingOrderStatus

__all__ = [
    "EventRetrieveResponse",
    "Data",
    "DataPortingEventDeletedPayload",
    "DataPortingEventDeletedPayloadPayload",
    "DataPortingEventMessagingChangedPayload",
    "DataPortingEventMessagingChangedPayloadPayload",
    "DataPortingEventMessagingChangedPayloadPayloadMessaging",
    "DataPortingEventStatusChangedEvent",
    "DataPortingEventStatusChangedEventPayload",
    "DataPortingEventNewCommentEvent",
    "DataPortingEventNewCommentEventPayload",
    "DataPortingEventNewCommentEventPayloadComment",
    "DataPortingEventSplitEvent",
    "DataPortingEventSplitEventPayload",
    "DataPortingEventSplitEventPayloadFrom",
    "DataPortingEventSplitEventPayloadPortingPhoneNumber",
    "DataPortingEventSplitEventPayloadTo",
    "DataPortingEventWithoutWebhook",
]


class DataPortingEventDeletedPayloadPayload(BaseModel):
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


class DataPortingEventDeletedPayload(BaseModel):
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

    payload: Optional[DataPortingEventDeletedPayloadPayload] = None

    payload_status: Optional[Literal["created", "completed"]] = None
    """The status of the payload generation."""

    porting_order_id: Optional[str] = None
    """Identifies the porting order associated with the event."""


class DataPortingEventMessagingChangedPayloadPayloadMessaging(BaseModel):
    """The messaging portability status of the porting order."""

    enable_messaging: Optional[bool] = None
    """
    Indicates whether Telnyx will port messaging capabilities from the losing
    carrier. If false, any messaging capabilities will stay with their current
    provider.
    """

    messaging_capable: Optional[bool] = None
    """Indicates whether the porting order is messaging capable."""

    messaging_port_completed: Optional[bool] = None
    """Indicates whether the messaging port is completed."""

    messaging_port_status: Optional[
        Literal["not_applicable", "pending", "activating", "exception", "canceled", "partial_port_complete", "ported"]
    ] = None
    """Indicates the messaging port status of the porting order."""


class DataPortingEventMessagingChangedPayloadPayload(BaseModel):
    """The webhook payload for the porting_order.messaging_changed event"""

    id: Optional[str] = None
    """Identifies the porting order that was moved."""

    customer_reference: Optional[str] = None
    """Identifies the customer reference associated with the porting order."""

    messaging: Optional[DataPortingEventMessagingChangedPayloadPayloadMessaging] = None
    """The messaging portability status of the porting order."""

    support_key: Optional[str] = None
    """Identifies the support key associated with the porting order."""


class DataPortingEventMessagingChangedPayload(BaseModel):
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

    payload: Optional[DataPortingEventMessagingChangedPayloadPayload] = None
    """The webhook payload for the porting_order.messaging_changed event"""

    payload_status: Optional[Literal["created", "completed"]] = None
    """The status of the payload generation."""

    porting_order_id: Optional[str] = None
    """Identifies the porting order associated with the event."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was updated."""


class DataPortingEventStatusChangedEventPayload(BaseModel):
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


class DataPortingEventStatusChangedEvent(BaseModel):
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

    payload: Optional[DataPortingEventStatusChangedEventPayload] = None
    """The webhook payload for the porting_order.status_changed event"""

    payload_status: Optional[Literal["created", "completed"]] = None
    """The status of the payload generation."""

    porting_order_id: Optional[str] = None
    """Identifies the porting order associated with the event."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was updated."""


class DataPortingEventNewCommentEventPayloadComment(BaseModel):
    """The comment that was added to the porting order."""

    id: Optional[str] = None
    """Identifies the comment."""

    body: Optional[str] = None
    """The body of the comment."""

    inserted_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the comment was created."""

    user_id: Optional[str] = None
    """Identifies the user that create the comment."""

    user_type: Optional[Literal["user", "admin", "system"]] = None
    """Identifies the type of the user that created the comment."""


class DataPortingEventNewCommentEventPayload(BaseModel):
    """The webhook payload for the porting_order.new_comment event"""

    comment: Optional[DataPortingEventNewCommentEventPayloadComment] = None
    """The comment that was added to the porting order."""

    porting_order_id: Optional[str] = None
    """Identifies the porting order that the comment was added to."""

    support_key: Optional[str] = None
    """Identifies the support key associated with the porting order."""


class DataPortingEventNewCommentEvent(BaseModel):
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

    payload: Optional[DataPortingEventNewCommentEventPayload] = None
    """The webhook payload for the porting_order.new_comment event"""

    payload_status: Optional[Literal["created", "completed"]] = None
    """The status of the payload generation."""

    porting_order_id: Optional[str] = None
    """Identifies the porting order associated with the event."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was updated."""


class DataPortingEventSplitEventPayloadFrom(BaseModel):
    """The porting order that was split."""

    id: Optional[str] = None
    """Identifies the porting order that was split."""


class DataPortingEventSplitEventPayloadPortingPhoneNumber(BaseModel):
    id: Optional[str] = None
    """Identifies the porting phone number that was moved."""


class DataPortingEventSplitEventPayloadTo(BaseModel):
    """The new porting order that the phone numbers was moved to."""

    id: Optional[str] = None
    """Identifies the porting order that was split."""


class DataPortingEventSplitEventPayload(BaseModel):
    """The webhook payload for the porting_order.split event"""

    from_: Optional[DataPortingEventSplitEventPayloadFrom] = FieldInfo(alias="from", default=None)
    """The porting order that was split."""

    porting_phone_numbers: Optional[List[DataPortingEventSplitEventPayloadPortingPhoneNumber]] = None
    """The list of porting phone numbers that were moved to the new porting order."""

    to: Optional[DataPortingEventSplitEventPayloadTo] = None
    """The new porting order that the phone numbers was moved to."""


class DataPortingEventSplitEvent(BaseModel):
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

    payload: Optional[DataPortingEventSplitEventPayload] = None
    """The webhook payload for the porting_order.split event"""

    payload_status: Optional[Literal["created", "completed"]] = None
    """The status of the payload generation."""

    porting_order_id: Optional[str] = None
    """Identifies the porting order associated with the event."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was updated."""


class DataPortingEventWithoutWebhook(BaseModel):
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

    payload: None = None

    payload_status: Optional[Literal["created", "completed"]] = None
    """The status of the payload generation."""

    porting_order_id: Optional[str] = None
    """Identifies the porting order associated with the event."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was updated."""


Data: TypeAlias = Union[
    DataPortingEventDeletedPayload,
    DataPortingEventMessagingChangedPayload,
    DataPortingEventStatusChangedEvent,
    DataPortingEventNewCommentEvent,
    DataPortingEventSplitEvent,
    DataPortingEventWithoutWebhook,
]


class EventRetrieveResponse(BaseModel):
    data: Optional[Data] = None

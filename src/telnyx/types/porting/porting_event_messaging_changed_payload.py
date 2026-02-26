# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PortingEventMessagingChangedPayload", "Payload", "PayloadMessaging"]


class PayloadMessaging(BaseModel):
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


class Payload(BaseModel):
    """The webhook payload for the porting_order.messaging_changed event"""

    id: Optional[str] = None
    """Identifies the porting order that was moved."""

    customer_reference: Optional[str] = None
    """Identifies the customer reference associated with the porting order."""

    messaging: Optional[PayloadMessaging] = None
    """The messaging portability status of the porting order."""

    support_key: Optional[str] = None
    """Identifies the support key associated with the porting order."""


class PortingEventMessagingChangedPayload(BaseModel):
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
    """The webhook payload for the porting_order.messaging_changed event"""

    payload_status: Optional[Literal["created", "completed"]] = None
    """The status of the payload generation."""

    porting_order_id: Optional[str] = None
    """Identifies the porting order associated with the event."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was updated."""

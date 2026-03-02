# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PortingEventNewCommentEvent", "Payload", "PayloadComment"]


class PayloadComment(BaseModel):
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


class Payload(BaseModel):
    """The webhook payload for the porting_order.new_comment event"""

    comment: Optional[PayloadComment] = None
    """The comment that was added to the porting order."""

    porting_order_id: Optional[str] = None
    """Identifies the porting order that the comment was added to."""

    support_key: Optional[str] = None
    """Identifies the support key associated with the porting order."""


class PortingEventNewCommentEvent(BaseModel):
    id: Optional[str] = None
    """Uniquely identifies the event."""

    available_notification_methods: Optional[List[Literal["email", "webhook", "webhook_v1"]]] = None
    """Indicates the notification methods used."""

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    event_type: Optional[Literal["porting_order.new_comment"]] = None
    """Identifies the event type"""

    payload: Optional[Payload] = None
    """The webhook payload for the porting_order.new_comment event"""

    payload_status: Optional[Literal["created", "completed"]] = None
    """The status of the payload generation."""

    porting_order_id: Optional[str] = None
    """Identifies the porting order associated with the event."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was updated."""

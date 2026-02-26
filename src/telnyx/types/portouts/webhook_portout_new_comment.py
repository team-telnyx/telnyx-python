# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["WebhookPortoutNewComment", "Payload"]


class Payload(BaseModel):
    """The webhook payload for the portout.new_comment event"""

    id: Optional[str] = None
    """Identifies the comment that was added to the port-out order."""

    comment: Optional[str] = None
    """The body of the comment."""

    portout_id: Optional[str] = None
    """Identifies the port-out order that the comment was added to."""

    user_id: Optional[str] = None
    """Identifies the user that added the comment."""


class WebhookPortoutNewComment(BaseModel):
    id: Optional[str] = None
    """Uniquely identifies the event."""

    available_notification_methods: Optional[List[Literal["email", "webhook"]]] = None
    """Indicates the notification methods used."""

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    event_type: Optional[Literal["portout.status_changed", "portout.foc_date_changed", "portout.new_comment"]] = None
    """Identifies the event type"""

    payload: Optional[Payload] = None
    """The webhook payload for the portout.new_comment event"""

    payload_status: Optional[Literal["created", "completed"]] = None
    """The status of the payload generation."""

    portout_id: Optional[str] = None
    """Identifies the port-out order associated with the event."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was updated."""

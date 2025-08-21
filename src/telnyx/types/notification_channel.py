# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["NotificationChannel"]


class NotificationChannel(BaseModel):
    id: Optional[str] = None
    """A UUID."""

    channel_destination: Optional[str] = None
    """The destination associated with the channel type."""

    channel_type_id: Optional[Literal["sms", "voice", "email", "webhook"]] = None
    """A Channel Type ID"""

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    notification_profile_id: Optional[str] = None
    """A UUID reference to the associated Notification Profile."""

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was updated."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["NotificationEventListResponse"]


class NotificationEventListResponse(BaseModel):
    """An object representing the available notifications."""

    id: Optional[str] = None
    """A UUID."""

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    enabled: Optional[bool] = None

    name: Optional[str] = None
    """A human readable name."""

    notification_category: Optional[str] = None

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was updated."""

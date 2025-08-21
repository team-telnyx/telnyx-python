# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .notification_channel import NotificationChannel

__all__ = ["NotificationChannelRetrieveResponse"]


class NotificationChannelRetrieveResponse(BaseModel):
    data: Optional[NotificationChannel] = None
    """A Notification Channel"""

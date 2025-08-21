# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .notification_profile import NotificationProfile

__all__ = ["NotificationProfileDeleteResponse"]


class NotificationProfileDeleteResponse(BaseModel):
    data: Optional[NotificationProfile] = None
    """A Collection of Notification Channels"""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["NotificationSetting", "Parameter"]


class Parameter(BaseModel):
    name: Optional[str] = None

    value: Optional[str] = None


class NotificationSetting(BaseModel):
    id: Optional[str] = None
    """A UUID."""

    associated_record_type: Optional[str] = None

    associated_record_type_value: Optional[str] = None

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    notification_channel_id: Optional[str] = None
    """A UUID reference to the associated Notification Channel."""

    notification_event_condition_id: Optional[str] = None
    """A UUID reference to the associated Notification Event Condition."""

    notification_profile_id: Optional[str] = None
    """A UUID reference to the associated Notification Profile."""

    parameters: Optional[List[Parameter]] = None

    status: Optional[
        Literal[
            "enabled",
            "enable-received",
            "enable-pending",
            "enable-submtited",
            "delete-received",
            "delete-pending",
            "delete-submitted",
            "deleted",
        ]
    ] = None
    """Most preferences apply immediately; however, other may needs to propagate."""

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was updated."""

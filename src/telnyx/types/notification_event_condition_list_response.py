# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .pagination_meta import PaginationMeta

__all__ = ["NotificationEventConditionListResponse", "Data", "DataParameter"]


class DataParameter(BaseModel):
    data_type: Optional[str] = None

    name: Optional[str] = None

    optional: Optional[bool] = None


class Data(BaseModel):
    id: Optional[str] = None
    """A UUID."""

    allow_multiple_channels: Optional[bool] = None
    """
    Dictates whether a notification channel id needs to be provided when creating a
    notficiation setting.
    """

    associated_record_type: Optional[Literal["account", "phone_number"]] = None

    asynchronous: Optional[bool] = None
    """Dictates whether a notification setting will take effect immediately."""

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    description: Optional[str] = None

    enabled: Optional[bool] = None

    name: Optional[str] = None

    notification_event_id: Optional[str] = None

    parameters: Optional[List[DataParameter]] = None

    supported_channels: Optional[List[str]] = None
    """Dictates the supported notification channel types that can be emitted."""

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was updated."""


class NotificationEventConditionListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMeta] = None

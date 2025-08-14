# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .pagination_meta import PaginationMeta

__all__ = ["NotificationEventListResponse", "Data"]


class Data(BaseModel):
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


class NotificationEventListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMeta] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .pagination_meta import PaginationMeta
from .notification_channel import NotificationChannel

__all__ = ["NotificationChannelListResponse"]


class NotificationChannelListResponse(BaseModel):
    data: Optional[List[NotificationChannel]] = None

    meta: Optional[PaginationMeta] = None

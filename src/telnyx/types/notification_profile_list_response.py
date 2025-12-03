# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .pagination_meta import PaginationMeta
from .notification_profile import NotificationProfile

__all__ = ["NotificationProfileListResponse"]


class NotificationProfileListResponse(BaseModel):
    data: Optional[List[NotificationProfile]] = None

    meta: Optional[PaginationMeta] = None

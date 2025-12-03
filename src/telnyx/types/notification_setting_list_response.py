# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .pagination_meta import PaginationMeta
from .notification_setting import NotificationSetting

__all__ = ["NotificationSettingListResponse"]


class NotificationSettingListResponse(BaseModel):
    data: Optional[List[NotificationSetting]] = None

    meta: Optional[PaginationMeta] = None

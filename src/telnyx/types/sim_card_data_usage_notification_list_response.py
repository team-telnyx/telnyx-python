# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .pagination_meta import PaginationMeta
from .sim_card_data_usage_notification import SimCardDataUsageNotification

__all__ = ["SimCardDataUsageNotificationListResponse"]


class SimCardDataUsageNotificationListResponse(BaseModel):
    data: Optional[List[SimCardDataUsageNotification]] = None

    meta: Optional[PaginationMeta] = None

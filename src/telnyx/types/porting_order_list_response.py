# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .porting_order import PortingOrder
from .pagination_meta import PaginationMeta

__all__ = ["PortingOrderListResponse"]


class PortingOrderListResponse(BaseModel):
    data: Optional[List[PortingOrder]] = None

    meta: Optional[PaginationMeta] = None

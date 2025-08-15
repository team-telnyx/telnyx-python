# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .pagination_meta import PaginationMeta
from .sub_number_order import SubNumberOrder

__all__ = ["SubNumberOrderListResponse"]


class SubNumberOrderListResponse(BaseModel):
    data: Optional[List[SubNumberOrder]] = None

    meta: Optional[PaginationMeta] = None

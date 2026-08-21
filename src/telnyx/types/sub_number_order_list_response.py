# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel
from .pagination_meta import PaginationMeta
from .numbers_sub_number_order import NumbersSubNumberOrder

__all__ = ["SubNumberOrderListResponse"]


class SubNumberOrderListResponse(BaseModel):
    data: Optional[List[NumbersSubNumberOrder]] = None

    meta: Optional[PaginationMeta] = None

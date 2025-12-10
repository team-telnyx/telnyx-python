# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .pagination_meta import PaginationMeta
from .number_block_order import NumberBlockOrder

__all__ = ["NumberBlockOrderListResponse"]


class NumberBlockOrderListResponse(BaseModel):
    data: Optional[List[NumberBlockOrder]] = None

    meta: Optional[PaginationMeta] = None

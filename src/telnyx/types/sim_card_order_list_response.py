# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .sim_card_order import SimCardOrder
from .pagination_meta import PaginationMeta

__all__ = ["SimCardOrderListResponse"]


class SimCardOrderListResponse(BaseModel):
    data: Optional[List[SimCardOrder]] = None

    meta: Optional[PaginationMeta] = None

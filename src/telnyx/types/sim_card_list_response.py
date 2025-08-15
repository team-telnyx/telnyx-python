# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .pagination_meta import PaginationMeta
from .shared.simple_sim_card import SimpleSimCard

__all__ = ["SimCardListResponse"]


class SimCardListResponse(BaseModel):
    data: Optional[List[SimpleSimCard]] = None

    meta: Optional[PaginationMeta] = None

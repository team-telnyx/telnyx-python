# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .sim_card_action import SimCardAction
from ..pagination_meta import PaginationMeta

__all__ = ["ActionListResponse"]


class ActionListResponse(BaseModel):
    data: Optional[List[SimCardAction]] = None

    meta: Optional[PaginationMeta] = None

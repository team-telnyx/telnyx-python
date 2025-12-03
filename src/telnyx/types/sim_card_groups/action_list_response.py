# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..pagination_meta import PaginationMeta
from .sim_card_group_action import SimCardGroupAction

__all__ = ["ActionListResponse"]


class ActionListResponse(BaseModel):
    data: Optional[List[SimCardGroupAction]] = None

    meta: Optional[PaginationMeta] = None

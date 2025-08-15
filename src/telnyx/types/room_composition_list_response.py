# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .pagination_meta import PaginationMeta
from .room_composition import RoomComposition

__all__ = ["RoomCompositionListResponse"]


class RoomCompositionListResponse(BaseModel):
    data: Optional[List[RoomComposition]] = None

    meta: Optional[PaginationMeta] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .room import Room
from .._models import BaseModel
from .pagination_meta import PaginationMeta

__all__ = ["RoomListResponse"]


class RoomListResponse(BaseModel):
    data: Optional[List[Room]] = None

    meta: Optional[PaginationMeta] = None

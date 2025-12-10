# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..room_session import RoomSession
from ..pagination_meta import PaginationMeta

__all__ = ["SessionList1Response"]


class SessionList1Response(BaseModel):
    data: Optional[List[RoomSession]] = None

    meta: Optional[PaginationMeta] = None

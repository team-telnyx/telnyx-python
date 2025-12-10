# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..pagination_meta import PaginationMeta
from ..shared.room_participant import RoomParticipant

__all__ = ["SessionRetrieveParticipantsResponse"]


class SessionRetrieveParticipantsResponse(BaseModel):
    data: Optional[List[RoomParticipant]] = None

    meta: Optional[PaginationMeta] = None

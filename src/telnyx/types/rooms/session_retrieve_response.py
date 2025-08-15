# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from ..room_session import RoomSession

__all__ = ["SessionRetrieveResponse"]


class SessionRetrieveResponse(BaseModel):
    data: Optional[RoomSession] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ..._models import BaseModel

if TYPE_CHECKING:
    from ..room_session import RoomSession

__all__ = ["SessionRetrieveResponse"]


class SessionRetrieveResponse(BaseModel):
    data: Optional[RoomSession] = None

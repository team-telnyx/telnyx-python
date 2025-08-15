# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .shared.room_participant import RoomParticipant

__all__ = ["RoomParticipantRetrieveResponse"]


class RoomParticipantRetrieveResponse(BaseModel):
    data: Optional[RoomParticipant] = None

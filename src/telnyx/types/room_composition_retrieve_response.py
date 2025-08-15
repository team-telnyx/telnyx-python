# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .room_composition import RoomComposition

__all__ = ["RoomCompositionRetrieveResponse"]


class RoomCompositionRetrieveResponse(BaseModel):
    data: Optional[RoomComposition] = None

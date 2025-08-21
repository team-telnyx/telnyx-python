# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .room_composition import RoomComposition

__all__ = ["RoomCompositionCreateResponse"]


class RoomCompositionCreateResponse(BaseModel):
    data: Optional[RoomComposition] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .room import Room
from .._models import BaseModel

__all__ = ["RoomUpdateResponse"]


class RoomUpdateResponse(BaseModel):
    data: Optional[Room] = None

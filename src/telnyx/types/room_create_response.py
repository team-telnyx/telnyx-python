# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .room import Room
from .._models import BaseModel

__all__ = ["RoomCreateResponse"]


class RoomCreateResponse(BaseModel):
    data: Optional[Room] = None

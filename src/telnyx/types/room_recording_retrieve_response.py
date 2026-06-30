# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .room_recording import RoomRecording

__all__ = ["RoomRecordingRetrieveResponse"]


class RoomRecordingRetrieveResponse(BaseModel):
    data: Optional[RoomRecording] = None

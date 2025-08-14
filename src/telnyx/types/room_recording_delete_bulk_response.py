# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["RoomRecordingDeleteBulkResponse", "Data"]


class Data(BaseModel):
    room_recordings: Optional[int] = None
    """Amount of room recordings affected"""


class RoomRecordingDeleteBulkResponse(BaseModel):
    data: Optional[Data] = None

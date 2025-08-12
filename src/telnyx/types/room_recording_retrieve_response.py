# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RoomRecordingRetrieveResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """A unique identifier for the room recording."""

    codec: Optional[str] = None
    """Shows the codec used for the room recording."""

    completed_at: Optional[datetime] = None
    """ISO 8601 timestamp when the room recording has completed."""

    created_at: Optional[datetime] = None
    """ISO 8601 timestamp when the room recording was created."""

    download_url: Optional[str] = None
    """Url to download the recording."""

    duration_secs: Optional[int] = None
    """Shows the room recording duration in seconds."""

    ended_at: Optional[datetime] = None
    """ISO 8601 timestamp when the room recording has ended."""

    participant_id: Optional[str] = None
    """Identify the room participant associated with the room recording."""

    record_type: Optional[str] = None

    room_id: Optional[str] = None
    """Identify the room associated with the room recording."""

    session_id: Optional[str] = None
    """Identify the room session associated with the room recording."""

    size_mb: Optional[float] = None
    """Shows the room recording size in MB."""

    started_at: Optional[datetime] = None
    """ISO 8601 timestamp when the room recording has stated."""

    status: Optional[Literal["completed", "processing"]] = None
    """Shows the room recording status."""

    type: Optional[Literal["audio", "video"]] = None
    """Shows the room recording type."""

    updated_at: Optional[datetime] = None
    """ISO 8601 timestamp when the room recording was updated."""


class RoomRecordingRetrieveResponse(BaseModel):
    data: Optional[Data] = None

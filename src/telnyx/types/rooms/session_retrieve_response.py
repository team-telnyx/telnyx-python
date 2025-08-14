# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["SessionRetrieveResponse", "Data", "DataParticipant"]


class DataParticipant(BaseModel):
    id: Optional[str] = None
    """A unique identifier for the room participant."""

    context: Optional[str] = None
    """Context provided to the given participant through the client SDK"""

    joined_at: Optional[datetime] = None
    """ISO 8601 timestamp when the participant joined the session."""

    left_at: Optional[datetime] = None
    """ISO 8601 timestamp when the participant left the session."""

    record_type: Optional[str] = None

    session_id: Optional[str] = None
    """Identify the room session that participant is part of."""

    updated_at: Optional[datetime] = None
    """ISO 8601 timestamp when the participant was updated."""


class Data(BaseModel):
    id: Optional[str] = None
    """A unique identifier for the room session."""

    active: Optional[bool] = None
    """Shows if the room session is active or not."""

    created_at: Optional[datetime] = None
    """ISO 8601 timestamp when the room session was created."""

    ended_at: Optional[datetime] = None
    """ISO 8601 timestamp when the room session has ended."""

    participants: Optional[List[DataParticipant]] = None

    record_type: Optional[str] = None

    room_id: Optional[str] = None
    """Identify the room hosting that room session."""

    updated_at: Optional[datetime] = None
    """ISO 8601 timestamp when the room session was updated."""


class SessionRetrieveResponse(BaseModel):
    data: Optional[Data] = None

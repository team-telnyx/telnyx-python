# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .shared.room_participant import RoomParticipant

__all__ = ["RoomSession"]


class RoomSession(BaseModel):
    id: Optional[str] = None
    """A unique identifier for the room session."""

    active: Optional[bool] = None
    """Shows if the room session is active or not."""

    created_at: Optional[datetime] = None
    """ISO 8601 timestamp when the room session was created."""

    ended_at: Optional[datetime] = None
    """ISO 8601 timestamp when the room session has ended."""

    participants: Optional[List[RoomParticipant]] = None

    record_type: Optional[str] = None

    room_id: Optional[str] = None
    """Identify the room hosting that room session."""

    updated_at: Optional[datetime] = None
    """ISO 8601 timestamp when the room session was updated."""

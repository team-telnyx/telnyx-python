# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .pagination_meta import PaginationMeta

__all__ = ["RoomParticipantListResponse", "Data"]


class Data(BaseModel):
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


class RoomParticipantListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMeta] = None

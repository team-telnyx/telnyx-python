# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["RoomUpdateResponse", "Data", "DataSession", "DataSessionParticipant"]


class DataSessionParticipant(BaseModel):
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


class DataSession(BaseModel):
    id: Optional[str] = None
    """A unique identifier for the room session."""

    active: Optional[bool] = None
    """Shows if the room session is active or not."""

    created_at: Optional[datetime] = None
    """ISO 8601 timestamp when the room session was created."""

    ended_at: Optional[datetime] = None
    """ISO 8601 timestamp when the room session has ended."""

    participants: Optional[List[DataSessionParticipant]] = None

    record_type: Optional[str] = None

    room_id: Optional[str] = None
    """Identify the room hosting that room session."""

    updated_at: Optional[datetime] = None
    """ISO 8601 timestamp when the room session was updated."""


class Data(BaseModel):
    id: Optional[str] = None
    """A unique identifier for the room."""

    active_session_id: Optional[str] = None
    """The identifier of the active room session if any."""

    created_at: Optional[datetime] = None
    """ISO 8601 timestamp when the room was created."""

    enable_recording: Optional[bool] = None
    """Enable or disable recording for that room."""

    max_participants: Optional[int] = None
    """Maximum participants allowed in the room."""

    record_type: Optional[str] = None

    sessions: Optional[List[DataSession]] = None

    unique_name: Optional[str] = None
    """The unique (within the Telnyx account scope) name of the room."""

    updated_at: Optional[datetime] = None
    """ISO 8601 timestamp when the room was updated."""

    webhook_event_failover_url: Optional[str] = None
    """
    The failover URL where webhooks related to this room will be sent if sending to
    the primary URL fails. Must include a scheme, such as 'https'.
    """

    webhook_event_url: Optional[str] = None
    """The URL where webhooks related to this room will be sent.

    Must include a scheme, such as 'https'.
    """

    webhook_timeout_secs: Optional[int] = None
    """Specifies how many seconds to wait before timing out a webhook."""


class RoomUpdateResponse(BaseModel):
    data: Optional[Data] = None

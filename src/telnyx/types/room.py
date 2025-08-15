# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .room_session import RoomSession

__all__ = ["Room"]


class Room(BaseModel):
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

    sessions: Optional[List[RoomSession]] = None

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

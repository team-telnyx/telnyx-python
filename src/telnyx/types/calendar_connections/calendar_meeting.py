# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CalendarMeeting", "Attendee", "Organizer"]


class Attendee(BaseModel):
    display_name: Optional[str] = None
    """Display name."""

    email: Optional[str] = None
    """Email address."""

    optional: Optional[bool] = None
    """Whether attendance is optional."""

    response_status: Optional[str] = None
    """Calendar RSVP status."""

    self: Optional[bool] = None
    """Whether this is the connected calendar user."""


class Organizer(BaseModel):
    display_name: Optional[str] = None
    """Display name."""

    email: Optional[str] = None
    """Email address."""

    self: Optional[bool] = None
    """Whether this is the connected calendar user."""


class CalendarMeeting(BaseModel):
    id: str
    """Tracked calendar meeting ID."""

    attendees: List[Attendee]
    """Calendar attendees; identity fields are cleared after the retention window."""

    bot_will_join: bool
    """Effective policy decision, not proof that the bot has joined."""

    bot_will_join_override: Optional[bool] = None
    """Explicit override; null follows the connection policy."""

    decision: Literal[
        "pending",
        "scheduled",
        "skipped_policy",
        "skipped_no_url",
        "skipped_duplicate",
        "skipped_unsupported",
        "cancelled",
    ]
    """Scheduling decision."""

    end_time: Optional[datetime] = None
    """Event end time."""

    is_external_organizer: Optional[bool] = None
    """Whether the connected calendar user is not the organizer."""

    organizer: Optional[Organizer] = None

    platform: Literal["zoom", "google_meet", "teams", "webex", "unknown"]
    """Detected meeting platform."""

    session_id: Optional[str] = None
    """Linked meeting session ID, or null until one exists."""

    start_time: datetime
    """Event start time."""

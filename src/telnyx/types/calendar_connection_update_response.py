# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .meeting_session_assistant import MeetingSessionAssistant
from .meeting_session_recording_destination import MeetingSessionRecordingDestination

__all__ = ["CalendarConnectionUpdateResponse", "Data"]


class Data(BaseModel):
    id: str
    """Calendar connection ID."""

    auto_join_policy: Literal["all_meetings", "external_organizer_excluded", "per_meeting"]
    """
    all_meetings joins eligible events; external_organizer_excluded requires the
    connected user to be the organizer; per_meeting requires an explicit opt-in.
    """

    bot_name: Optional[str] = None
    """Bot display name; null clears the override."""

    created_at: datetime
    """Creation time."""

    default_assistant: Optional[MeetingSessionAssistant] = None

    default_barge_in: Optional[bool] = None
    """Default manual speech interruption. Cannot be true with default_assistant."""

    default_recording: Optional[bool] = None
    """Google Meet and Teams recording intent.

    When null, recording is enabled only if a destination is set. True requires
    default_recording_export; false cannot be combined with a destination.
    """

    default_recording_export: Optional[MeetingSessionRecordingDestination] = None
    """Customer-owned Telnyx Storage destination for recording exports.

    Uses the authenticated organization and user; do not supply credentials, region,
    organization ID or object key.
    """

    default_summarize_on_end: Optional[bool] = None
    """Generate a summary when each future session transcript finalizes."""

    default_voice: Optional[str] = None
    """Manual-speech voice; must be null when default_assistant is set."""

    default_webhook_url: Optional[str] = None
    """HTTPS destination for future session webhooks.

    Null clears the default. A non-null update returns webhook_secret once; save it
    to verify signatures for sessions created with this default. Existing sessions
    retain their original signing secret.
    """

    platform: Literal["google_calendar", "microsoft_outlook"]
    """Calendar provider: Google Calendar or Microsoft Outlook."""

    platform_email: Optional[str] = None
    """Connected calendar email address."""

    status: Literal["connected", "disconnected", "error"]
    """Connection status."""

    status_detail: Optional[str] = None
    """Additional connection status detail."""

    updated_at: datetime
    """Last update time."""

    webhook_secret: Optional[str] = None
    """Returned only when PATCH supplies a non-null default_webhook_url.

    Not returned by list or retrieve. Save this secret to verify webhooks for future
    sessions.
    """


class CalendarConnectionUpdateResponse(BaseModel):
    data: Data

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .meeting_session_assistant import MeetingSessionAssistant
from .meeting_session_leave_policy import MeetingSessionLeavePolicy
from .meeting_session_recording_export import MeetingSessionRecordingExport

__all__ = ["MeetingSession", "Avatar", "Config", "ConfigDeepfakeDetection"]


class Avatar(BaseModel):
    """
    The assistant's avatar, captured from its `avatar_settings` when the session was created. For display only; later changes to the assistant do not update it.
    """

    avatar_id: str
    """Identifier of the avatar."""

    background_id: str
    """Identifier of the avatar's background."""

    model: str
    """Avatar rendering model, for example `foxtrot-1`."""

    provider: Literal["telnyx"]
    """Avatar provider identifier."""


class ConfigDeepfakeDetection(BaseModel):
    """Detection settings. Enabling audio or video detection is currently unsupported."""

    audio: bool

    video: bool


class Config(BaseModel):
    barge_in: bool
    """
    When enabled, a human participant `speech_on` event interrupts and stops the
    current bot audio; it does not bypass admission or initiate speech. Assistant
    sessions reject `barge_in: true`.
    """

    chat_on_enter: Optional[str] = None
    """The message posted to chat on join, or null when unset."""

    deepfake_detection: ConfigDeepfakeDetection
    """Detection settings. Enabling audio or video detection is currently unsupported."""

    speak_on_enter: Optional[str] = None
    """Text spoken on meeting entry, or null if not set."""

    summarize_on_end: bool
    """Whether a summary artifact is generated on session end."""

    voice: Optional[str] = None
    """Configured voice identifier, or null if not set."""

    leave_policy: Optional[MeetingSessionLeavePolicy] = None
    """Automatic departure settings for Google Meet and Teams.

    Omitted fields use the default behavior. Set at creation; cannot be changed
    later. Zoom ignores this policy.
    """

    recording: Optional[bool] = None
    """Recording intent set at creation for Google Meet and Teams.

    Distinct from the top-level recording field, which reports current activity.
    """

    recording_view: Optional[Literal["gallery_view", "speaker_view_no_sidebar"]] = None
    """Non-default recording layout. Omitted for the default speaker_view layout."""


class MeetingSession(BaseModel):
    """Represents a meeting session.

    Core serializer fields are required; platform-specific fields are optional. Nullable fields use null when absent. No actor, provider-bot, idempotency, routing, key, or internal fields are exposed.
    """

    id: str
    """Unique identifier for the meeting session."""

    account_id: str
    """Identifier of the owning account."""

    assistant: Optional[MeetingSessionAssistant] = None
    """Assistant configuration if an assistant is attached, otherwise null."""

    assistant_state: Optional[Literal["starting", "connected", "failed", "ended"]] = None
    """Current state of the assistant, or null if no assistant is attached."""

    assistant_state_changed_at: Optional[datetime] = None
    """Timestamp of the last assistant state change, or null."""

    avatar: Optional[Avatar] = None
    """
    The assistant's avatar, captured from its `avatar_settings` when the session was
    created. For display only; later changes to the assistant do not update it.
    """

    avatar_state: Optional[Literal["starting", "connected", "degraded", "disconnected"]] = None
    """Current state of the avatar, or null if the session has no avatar.

    `starting` until the avatar's video is playing, then `connected`; `degraded`
    when the session has fallen back to voice-only (the `avatar.degraded` event
    carries the reason); `disconnected` when the avatar has ended.
    """

    avatar_state_changed_at: Optional[datetime] = None
    """Timestamp of the last avatar state change, or null."""

    bot_name: str
    """Display name of the bot in the meeting."""

    config: Config

    created_at: datetime
    """Timestamp when the session was created."""

    ended_at: Optional[datetime] = None
    """Timestamp when the session ended, or null if ongoing."""

    failure_reason: Optional[str] = None
    """A machine-readable lifecycle reason, or null.

    Values include left_on_request, meeting_ended, everyone_left, no_one_joined,
    silence_timeout, max_duration_reached, admission_timeout, admission_denied,
    removed_from_meeting, recording_permission_denied, meeting_not_found,
    meeting_not_started, meeting_access_denied, meeting_full, cancelled,
    cancelled_calendar_disconnected, cancelled_calendar_event_deleted,
    cancelled_calendar_superseded, cancelled_policy, internal_error, and other.
    Treat this vocabulary as extensible.
    """

    join_at: Optional[datetime] = None
    """Scheduled join time, or null for immediate join."""

    joined_at: Optional[datetime] = None
    """
    Timestamp when the session first became `active`, or null if it never became
    active. This remains positive admission evidence after terminal transitions.
    """

    meeting_url: str
    """The meeting URL the bot joins."""

    metadata: Dict[str, object]
    """Arbitrary key-value metadata attached to the session."""

    platform: Literal["zoom", "google_meet", "teams", "webex", "unknown"]
    """Detected meeting platform."""

    provider: Literal["telnyx"]
    """Always telnyx."""

    recording: bool
    """Whether the session is being recorded."""

    status: Literal[
        "scheduled", "joining", "waiting_for_admission", "active", "leaving", "ended", "failed", "admission_denied"
    ]
    """Lifecycle status.

    `waiting_for_admission` means the bot reached the meeting lobby and may require
    host approval. `active` means the bot entered the meeting/media path. `ended`
    alone does not prove attendance; use non-null `joined_at` as positive evidence
    that the session became active. `admission_denied` is reserved for an explicit
    provider denial, while cancellation or another termination can end a
    never-admitted session as `ended`.
    """

    status_detail: Optional[str] = None
    """A machine-readable lifecycle reason, or null.

    Values include left_on_request, meeting_ended, everyone_left, no_one_joined,
    silence_timeout, max_duration_reached, admission_timeout, admission_denied,
    removed_from_meeting, recording_permission_denied, meeting_not_found,
    meeting_not_started, meeting_access_denied, meeting_full, cancelled,
    cancelled_calendar_disconnected, cancelled_calendar_event_deleted,
    cancelled_calendar_superseded, cancelled_policy, internal_error, and other.
    Treat this vocabulary as extensible.
    """

    updated_at: datetime
    """Timestamp of the last update to the session."""

    webhook_url: Optional[str] = None
    """Webhook endpoint for session lifecycle callbacks, or null if not configured."""

    recording_export: Optional[MeetingSessionRecordingExport] = None
    """Customer Storage recording reference.

    Pending is not downloadable; exported means upload was verified; failed is
    terminal. Download with ordinary Storage authorization. No presigned URL is
    returned.
    """

    remote_state_observed_at: Optional[datetime] = None
    """Optional observation time on session list items.

    Retrieve the individual session when current state is required.
    """

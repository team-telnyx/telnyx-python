# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MeetingSession", "Assistant", "Avatar", "Config"]


class Assistant(BaseModel):
    """Assistant configuration if an assistant is attached, otherwise null."""

    id: str
    """Identifier of the assistant."""

    audio_gate: Literal["none", "half_duplex"]
    """Audio gating strategy for the assistant call leg."""


class Avatar(BaseModel):
    """Avatar configuration if an avatar is attached, otherwise null."""

    avatar_id: str
    """Identifier of the avatar."""

    provider: Literal["anam"]
    """Avatar provider identifier."""


class Config(BaseModel):
    barge_in: bool
    """
    When enabled, a human participant `speech_on` event interrupts and stops the
    current bot audio; it does not bypass admission or initiate speech. Assistant
    sessions reject `barge_in: true`.
    """

    speak_on_enter: Optional[str] = None
    """Text spoken on meeting entry, or null if not set."""

    summarize_on_end: bool
    """Whether a summary artifact is generated on session end."""

    voice: Optional[str] = None
    """Configured voice identifier, or null if not set."""


class MeetingSession(BaseModel):
    """Represents a meeting session.

    All serializer fields are present and required; nullable fields use null when absent. No actor, provider-bot, idempotency, routing, key, or internal fields are exposed.
    """

    id: str
    """Unique identifier for the meeting session."""

    account_id: str
    """Identifier of the owning account."""

    assistant: Optional[Assistant] = None
    """Assistant configuration if an assistant is attached, otherwise null."""

    assistant_state: Optional[Literal["starting", "connected", "failed", "ended"]] = None
    """Current state of the assistant, or null if no assistant is attached."""

    assistant_state_changed_at: Optional[datetime] = None
    """Timestamp of the last assistant state change, or null."""

    avatar: Optional[Avatar] = None
    """Avatar configuration if an avatar is attached, otherwise null."""

    avatar_state: Optional[Literal["starting", "connected", "degraded", "disconnected"]] = None
    """Current state of the avatar connection, or null if no avatar is attached."""

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
    """Human-readable failure reason if the session failed, or null."""

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

    provider: str
    """Provider handling the meeting session."""

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
    """Additional human-readable detail about the status, or null."""

    updated_at: datetime
    """Timestamp of the last update to the session."""

    webhook_url: Optional[str] = None
    """Webhook endpoint for session lifecycle callbacks, or null if not configured."""

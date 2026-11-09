# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CalendarConnectionUpdateParams", "DefaultAssistant"]


class CalendarConnectionUpdateParams(TypedDict, total=False):
    auto_join_policy: Literal["all_meetings", "external_organizer_excluded", "per_meeting"]
    """
    all_meetings joins eligible events; external_organizer_excluded requires the
    connected user to be the organizer; per_meeting requires an explicit opt-in.
    """

    bot_name: Optional[str]
    """Bot display name; null clears the override."""

    default_assistant: Optional[DefaultAssistant]
    """Default assistant for future calendar-scheduled Google Meet and Teams sessions.

    The saved configuration must fit within 8 KiB. Use id, audio_gate,
    dynamic_variables, and leave_on_end; avatar is not accepted. audio_gate defaults
    to full_duplex.
    """

    default_barge_in: Optional[bool]
    """Default manual speech interruption. Cannot be true with default_assistant."""

    default_recording: Optional[bool]
    """Google Meet and Teams recording intent.

    When null, recording is enabled only if a destination is set. True requires
    default_recording_export; false cannot be combined with a destination.
    """

    default_recording_export: Optional["MeetingSessionRecordingDestinationParam"]
    """Customer-owned Telnyx Storage destination for recording exports.

    Uses the authenticated organization and user; do not supply credentials, region,
    organization ID or object key.
    """

    default_summarize_on_end: Optional[bool]
    """Generate a summary when each future session transcript finalizes."""

    default_voice: Optional[str]
    """Manual-speech voice; must be null when default_assistant is set."""

    default_webhook_url: Optional[str]
    """HTTPS destination for future session webhooks.

    Null clears the default. A non-null update returns webhook_secret once; save it
    to verify signatures for sessions created with this default. Existing sessions
    retain their original signing secret.
    """


class DefaultAssistant(TypedDict, total=False):
    """Default assistant for future calendar-scheduled Google Meet and Teams sessions.

    The saved configuration must fit within 8 KiB. Use id, audio_gate, dynamic_variables, and leave_on_end; avatar is not accepted. audio_gate defaults to full_duplex.
    """

    id: Required[str]
    """Identifier of the assistant to attach."""

    audio_gate: Literal["half_duplex", "full_duplex"]
    """
    Use full_duplex (default) to allow participants to interrupt, or half_duplex to
    pause listening while the assistant speaks. Full-duplex pricing depends on
    participant audio usage; see the Meeting pricing guide.
    """

    dynamic_variables: Dict[str, str]
    """
    Per-conversation values for the
    [dynamic variables](/docs/inference/ai-assistants/dynamic-variables) used in the
    Assistant's instructions, greeting, or tools. Delivered before the Assistant's
    first utterance, so they resolve for the opening line as well as the rest of the
    conversation. At most 63 entries; keys 1-128 characters; values must be strings.
    The map is budgeted in aggregate at 1,047,552 bytes (1023 KiB) rather than
    capped per value. `streaming_audio`, `ai_assistant_streaming_audio` and
    `meeting_session_id` are reserved and rejected with `400 invalid_request`.
    """

    leave_on_end: bool
    """Leave when the assistant conversation ends or fails.

    Defaults to false. Other leave-policy rules and explicit leave requests still
    apply.
    """


from .meeting_session_recording_destination_param import MeetingSessionRecordingDestinationParam

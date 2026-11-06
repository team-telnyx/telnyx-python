# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "MeetingSessionCreateParams",
    "Assistant",
    "CameraImage",
    "CameraImageMeetingSessionCameraImageBase64Source",
    "CameraImageMeetingSessionCameraImageURLSource",
]


class MeetingSessionCreateParams(TypedDict, total=False):
    meeting_url: Required[str]
    """The meeting URL the bot should join."""

    assistant: Assistant
    """Attach a Telnyx AI Assistant owned by the authenticated account.

    Supply its ID and optional conversation settings. Unknown fields are rejected.
    """

    barge_in: bool
    """
    When enabled, a human participant `speech_on` event interrupts and stops the
    current bot audio; it does not bypass admission or initiate speech. Assistant
    sessions reject `barge_in: true`.
    """

    bot_name: str
    """Display name for the bot in the meeting. Defaults to "Meeting Bot"."""

    camera_image: CameraImage
    """Not supported for Google Meet and Teams joins (422 unsupported_capability).

    Write-only static camera-tile image for this session, not an account or
    participant profile photo. Supply exactly one JPEG source. When effective, the
    image is used as the bot's static camera/video output; presentation varies by
    meeting platform and recording configuration and is not guaranteed in
    recordings. An attached assistant or avatar takes precedence, so this input is
    ignored and a URL source is not fetched.
    """

    chat_on_enter: str
    """
    A message the bot posts to the meeting's chat as soon as it becomes active —
    typically a recording disclosure. Delivered at most once. Independent of
    `speak_on_enter`: both may be set, and the chat message posts first because it
    does not wait for text-to-speech or avatar startup. Rejected with 422
    `unsupported_capability` on platforms without meeting chat. For Google Meet and
    Teams, text must be nonblank, at most 4096 UTF-8 bytes, with no control
    characters except tabs and line breaks. Counts toward the 1000-chat-request
    session limit.
    """

    idempotency_key: str
    """Use a unique key per intended join and reuse the same key and request on
    retries.

    Reusing a key with a different join configuration or meeting URL can return 409
    invalid_state. Always retry with the original request.
    """

    join_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Future ISO-8601 join timestamp including timezone.

    Google Meet and Teams accept dates at most three years ahead. Omit for an
    immediate join. Assistant sessions created through this endpoint must join
    immediately.
    """

    leave_policy: "MeetingSessionLeavePolicyParam"
    """Automatic departure settings for Google Meet and Teams.

    Omitted fields use the default behavior. Set at creation; cannot be changed
    later. Zoom ignores this policy.
    """

    metadata: Dict[str, object]
    """Arbitrary key-value metadata attached to the session.

    The serialized JSON representation must not exceed 16384 characters at runtime.
    """

    recording: bool
    """Google Meet and Teams only.

    Defaults to true when recording_export is supplied and false otherwise. True
    requires recording_export.bucket; false cannot be combined with
    recording_export. Fixed at creation, with no pause/resume action. Zoom rejects
    recording, recording_view, and recording_export with 422 unsupported_capability;
    omit these fields for Zoom.
    """

    recording_export: "MeetingSessionRecordingDestinationParam"
    """Customer-owned Telnyx Storage destination for recording exports.

    Uses the authenticated organization and user; do not supply credentials, region,
    organization ID or object key.
    """

    recording_view: Literal["speaker_view", "gallery_view", "speaker_view_no_sidebar"]
    """Recording layout for Google Meet and Teams.

    Defaults to speaker_view. Accepted at creation only; does not enable recording
    by itself.
    """

    speak_on_enter: str
    """Text the bot speaks after joining.

    Available for sessions without a digital avatar. With an AI Assistant, the
    greeting waits until the assistant is connected. Rejected with 400
    invalid_request when assistant.avatar is true.
    """

    summarize_on_end: bool
    """If true, generate a summary artifact when the session ends."""

    voice: str
    """
    Session-default voice identifier used for `speak_on_enter` and ordinary speak
    actions. A voice supplied on an individual speak action overrides this default
    for that utterance. With an assistant attached, its conversational voice remains
    configured on the assistant.
    """

    webhook_url: str
    """HTTPS endpoint to receive session lifecycle callbacks.

    Static validation requires HTTPS, rejects embedded credentials and blocked
    hosts, and enforces egress policy. Validation makes no network request to the
    endpoint.
    """


class Assistant(TypedDict, total=False):
    """Attach a Telnyx AI Assistant owned by the authenticated account.

    Supply its ID and optional conversation settings. Unknown fields are rejected.
    """

    id: Required[str]
    """Identifier of the assistant to attach."""

    audio_gate: Literal["half_duplex", "full_duplex"]
    """
    Use half_duplex (default) to pause listening while the assistant speaks, or
    full_duplex to allow participants to interrupt. Full-duplex pricing depends on
    participant audio usage; see the Meeting pricing guide.
    """

    avatar: bool
    """Beta.

    Show the avatar configured on the assistant (its `avatar_settings`; see
    [AI Assistant avatars](/docs/inference/ai-assistants/avatars)) as the bot's
    camera, lip-synced to the assistant's own speech. The request carries no avatar
    ID or key: the assistant is read at creation and the request is rejected with
    400 `invalid_request` if it has no Telnyx avatar configured. Available for
    Google Meet, Zoom, and Teams sessions. REST-only. Not echoed back on
    `assistant`; the session's top-level `avatar` and `avatar_state` fields report
    it instead. If the avatar fails, the session continues voice-only and
    `avatar_state` becomes `degraded`.
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


class CameraImageMeetingSessionCameraImageBase64Source(TypedDict, total=False):
    base64_data: Required[str]
    """Canonical plain RFC 4648 Base64 for a valid decoded JPEG.

    Data URIs, whitespace, and the URL-safe alphabet are rejected. The encoded value
    is limited to 1,835,008 characters and the decoded JPEG to 1,363,148 bytes. The
    JPEG is limited to 4,096 pixels per dimension, 4 megapixels, and 128 MB of
    decoder memory. The image bytes are not returned in the session response.
    """

    format: Required[Literal["jpeg"]]
    """Only JPEG images are accepted."""


class CameraImageMeetingSessionCameraImageURLSource(TypedDict, total=False):
    format: Required[Literal["jpeg"]]
    """Only JPEG images are accepted."""

    url: Required[str]
    """
    Public HTTPS JPEG URL with at most 2,048 characters and no credentials,
    fragment, surrounding whitespace, raw control characters, or explicit
    non-default port. Signed queries are allowed but must be treated as credentials.
    Fetching is limited to public network destinations, a five-second timeout, no
    redirects, a 2xx image/jpeg response with identity or no content encoding, and a
    1,363,148-byte limit enforced against both declared and streamed content. The
    service resolves the URL before bot creation and does not return the URL or
    image bytes in the session response.
    """


CameraImage: TypeAlias = Union[
    CameraImageMeetingSessionCameraImageBase64Source, CameraImageMeetingSessionCameraImageURLSource
]

from .meeting_session_leave_policy_param import MeetingSessionLeavePolicyParam
from .meeting_session_recording_destination_param import MeetingSessionRecordingDestinationParam

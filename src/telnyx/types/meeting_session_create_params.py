# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "MeetingSessionCreateParams",
    "Assistant",
    "Avatar",
    "CameraImage",
    "CameraImageMeetingSessionCameraImageBase64Source",
    "CameraImageMeetingSessionCameraImageURLSource",
]


class MeetingSessionCreateParams(TypedDict, total=False):
    meeting_url: Required[str]
    """The meeting URL the bot should join."""

    assistant: Assistant
    """Request options for attaching a voice assistant to the session.

    Routing fields (`call_control_connection_id`, `from`, and `loopback_sip_uri`)
    are used only to establish the assistant call leg and are omitted from response
    objects. `audio_gate` is returned with `id` in the assistant response object.
    """

    avatar: Avatar
    """Request options for attaching a bring-your-own-key avatar to the session."""

    barge_in: bool
    """
    When enabled, a human participant `speech_on` event interrupts and stops the
    current bot audio; it does not bypass admission or initiate speech. Assistant
    sessions reject `barge_in: true`.
    """

    bot_name: str
    """Display name for the bot in the meeting. Defaults to "Meeting Bot"."""

    camera_image: CameraImage
    """
    Write-only static camera-tile image for this session, not a native account or
    participant profile photo. Supply exactly one JPEG source. When effective, the
    image is used as the bot's static camera/video output; presentation varies by
    meeting platform and recording configuration and is not guaranteed in
    recordings. An effective Avatar or Assistant webpage output takes precedence, so
    this input is ignored and a URL source is not fetched.
    """

    idempotency_key: str
    """
    Client-supplied idempotency key to safely retry creation requests without
    duplicating sessions. Lookup is scoped to the authenticated account and compares
    the key only; the request payload is not fingerprinted or compared.
    """

    join_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """ISO-8601 timestamp in the future at which the bot should join.

    If omitted, the bot joins immediately.
    """

    metadata: Dict[str, object]
    """Arbitrary key-value metadata attached to the session.

    The serialized JSON representation must not exceed 16384 characters at runtime.
    """

    speak_on_enter: str
    """Text the bot speaks when it enters the meeting."""

    summarize_on_end: bool
    """If true, generate a summary artifact when the session ends."""

    voice: str
    """
    Session-default voice identifier used for `speak_on_enter` and ordinary speak
    actions. A voice supplied on an individual speak action overrides this default
    for that utterance.
    """

    webhook_url: str
    """HTTPS endpoint to receive session lifecycle callbacks.

    Static validation requires HTTPS, rejects embedded credentials and blocked
    hosts, and enforces egress policy. Validation makes no network request to the
    endpoint.
    """


_AssistantReservedKeywords = TypedDict(
    "_AssistantReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class Assistant(_AssistantReservedKeywords, total=False):
    """Request options for attaching a voice assistant to the session.

    Routing fields (`call_control_connection_id`, `from`, and `loopback_sip_uri`) are used only to establish the assistant call leg and are omitted from response objects. `audio_gate` is returned with `id` in the assistant response object.
    """

    id: Required[str]
    """Identifier of the assistant to attach."""

    call_control_connection_id: Required[str]
    """Call control connection used to bridge the assistant into the meeting audio."""

    loopback_sip_uri: Required[str]
    """SIP URI to which the assistant media loopback is established."""

    audio_gate: Literal["none", "half_duplex"]
    """Audio gating strategy for the assistant call leg."""


class Avatar(TypedDict, total=False):
    """Request options for attaching a bring-your-own-key avatar to the session."""

    api_key: Required[str]
    """Bring-your-own-key API key for the avatar provider.

    The key is never stored or returned by the API.
    """

    avatar_id: Required[str]
    """Identifier of the avatar to use."""

    provider: Required[Literal["anam"]]
    """Avatar provider identifier. Currently only "anam" is supported."""


class CameraImageMeetingSessionCameraImageBase64Source(TypedDict, total=False):
    base64_data: Required[str]
    """Canonical plain RFC 4648 Base64 for a valid decoded JPEG.

    Data URIs, whitespace, and the URL-safe alphabet are rejected. The encoded value
    is limited to 1,835,008 characters and the decoded JPEG to 1,363,148 bytes. The
    JPEG is limited to 4,096 pixels per dimension, 4 megapixels, and 128 MB of
    decoder memory. The image bytes are not persisted, returned, or logged.
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
    service resolves the URL before bot creation and does not persist, return, or
    log the URL or image bytes.
    """


CameraImage: TypeAlias = Union[
    CameraImageMeetingSessionCameraImageBase64Source, CameraImageMeetingSessionCameraImageURLSource
]

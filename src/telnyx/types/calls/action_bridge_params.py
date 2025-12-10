# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ActionBridgeParams"]


class ActionBridgeParams(TypedDict, total=False):
    body_call_control_id: Required[Annotated[str, PropertyInfo(alias="call_control_id")]]
    """
    The Call Control ID of the call you want to bridge with, can't be used together
    with queue parameter or video_room_id parameter.
    """

    client_state: str
    """Use this field to add state to every subsequent webhook.

    It must be a valid Base-64 encoded string.
    """

    command_id: str
    """Use this field to avoid duplicate commands.

    Telnyx will ignore any command with the same `command_id` for the same
    `call_control_id`.
    """

    mute_dtmf: Literal["none", "both", "self", "opposite"]
    """When enabled, DTMF tones are not passed to the call participant.

    The webhooks containing the DTMF information will be sent.
    """

    park_after_unbridge: str
    """Specifies behavior after the bridge ends (i.e.

    the opposite leg either hangs up or is transferred). If supplied with the value
    `self`, the current leg will be parked after unbridge. If not set, the default
    behavior is to hang up the leg.
    """

    play_ringtone: bool
    """
    Specifies whether to play a ringtone if the call you want to bridge with has not
    yet been answered.
    """

    queue: str
    """
    The name of the queue you want to bridge with, can't be used together with
    call_control_id parameter or video_room_id parameter. Bridging with a queue
    means bridging with the first call in the queue. The call will always be removed
    from the queue regardless of whether bridging succeeds. Returns an error when
    the queue is empty.
    """

    record: Literal["record-from-answer"]
    """Start recording automatically after an event. Disabled by default."""

    record_channels: Literal["single", "dual"]
    """
    Defines which channel should be recorded ('single' or 'dual') when `record` is
    specified.
    """

    record_custom_file_name: str
    """The custom recording file name to be used instead of the default `call_leg_id`.

    Telnyx will still add a Unix timestamp suffix.
    """

    record_format: Literal["wav", "mp3"]
    """
    Defines the format of the recording ('wav' or 'mp3') when `record` is specified.
    """

    record_max_length: int
    """
    Defines the maximum length for the recording in seconds when `record` is
    specified. The minimum value is 0. The maximum value is 43200. The default value
    is 0 (infinite).
    """

    record_timeout_secs: int
    """
    The number of seconds that Telnyx will wait for the recording to be stopped if
    silence is detected when `record` is specified. The timer only starts when the
    speech is detected. Please note that call transcription is used to detect
    silence and the related charge will be applied. The minimum value is 0. The
    default value is 0 (infinite).
    """

    record_track: Literal["both", "inbound", "outbound"]
    """The audio track to be recorded.

    Can be either `both`, `inbound` or `outbound`. If only single track is specified
    (`inbound`, `outbound`), `channels` configuration is ignored and it will be
    recorded as mono (single channel).
    """

    record_trim: Literal["trim-silence"]
    """
    When set to `trim-silence`, silence will be removed from the beginning and end
    of the recording.
    """

    ringtone: Literal[
        "at",
        "au",
        "be",
        "bg",
        "br",
        "ch",
        "cl",
        "cn",
        "cz",
        "de",
        "dk",
        "ee",
        "es",
        "fi",
        "fr",
        "gr",
        "hu",
        "il",
        "in",
        "it",
        "jp",
        "lt",
        "mx",
        "my",
        "nl",
        "no",
        "nz",
        "ph",
        "pl",
        "pt",
        "ru",
        "se",
        "sg",
        "th",
        "tw",
        "uk",
        "us-old",
        "us",
        "ve",
        "za",
    ]
    """Specifies which country ringtone to play when `play_ringtone` is set to `true`.

    If not set, the US ringtone will be played.
    """

    video_room_context: str
    """The additional parameter that will be passed to the video conference.

    It is a text field and the user can decide how to use it. For example, you can
    set the participant name or pass JSON text. It can be used only with
    video_room_id parameter.
    """

    video_room_id: str
    """
    The ID of the video room you want to bridge with, can't be used together with
    call_control_id parameter or queue parameter.
    """

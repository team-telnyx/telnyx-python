# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..sip_header_param import SipHeaderParam
from ..custom_sip_header_param import CustomSipHeaderParam
from ..sound_modifications_param import SoundModificationsParam

__all__ = ["ActionTransferParams", "AnsweringMachineDetectionConfig"]


class ActionTransferParams(TypedDict, total=False):
    to: Required[str]
    """The DID or SIP URI to dial out to."""

    answering_machine_detection: Literal["premium", "detect", "detect_beep", "detect_words", "greeting_end", "disabled"]
    """Enables Answering Machine Detection.

    When a call is answered, Telnyx runs real-time detection to determine if it was
    picked up by a human or a machine and sends an `call.machine.detection.ended`
    webhook with the analysis result. If 'greeting_end' or 'detect_words' is used
    and a 'machine' is detected, you will receive another
    'call.machine.greeting.ended' webhook when the answering machine greeting ends
    with a beep or silence. If `detect_beep` is used, you will only receive
    'call.machine.greeting.ended' if a beep is detected.
    """

    answering_machine_detection_config: AnsweringMachineDetectionConfig
    """
    Optional configuration parameters to modify 'answering_machine_detection'
    performance.
    """

    audio_url: str
    """
    The URL of a file to be played back when the transfer destination answers before
    bridging the call. The URL can point to either a WAV or MP3 file. media_name and
    audio_url cannot be used together in one request.
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

    custom_headers: Iterable[CustomSipHeaderParam]
    """Custom headers to be added to the SIP INVITE."""

    early_media: bool
    """If set to false, early media will not be passed to the originating leg."""

    from_: Annotated[str, PropertyInfo(alias="from")]
    """
    The `from` number to be used as the caller id presented to the destination (`to`
    number). The number should be in +E164 format. This attribute will default to
    the `to` number of the original call if omitted.
    """

    from_display_name: str
    """
    The `from_display_name` string to be used as the caller id name (SIP From
    Display Name) presented to the destination (`to` number). The string should have
    a maximum of 128 characters, containing only letters, numbers, spaces, and
    -\\__~!.+ special characters. If ommited, the display name will be the same as the
    number in the `from` field.
    """

    media_encryption: Literal["disabled", "SRTP", "DTLS"]
    """Defines whether media should be encrypted on the new call leg."""

    media_name: str
    """
    The media_name of a file to be played back when the transfer destination answers
    before bridging the call. The media_name must point to a file previously
    uploaded to api.telnyx.com/v2/media by the same user/organization. The file must
    either be a WAV or MP3 file.
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

    sip_auth_password: str
    """SIP Authentication password used for SIP challenges."""

    sip_auth_username: str
    """SIP Authentication username used for SIP challenges."""

    sip_headers: Iterable[SipHeaderParam]
    """SIP headers to be added to the SIP INVITE.

    Currently only User-to-User header is supported.
    """

    sip_transport_protocol: Literal["UDP", "TCP", "TLS"]
    """Defines SIP transport protocol to be used on the call."""

    sound_modifications: SoundModificationsParam
    """Use this field to modify sound effects, for example adjust the pitch."""

    target_leg_client_state: str
    """Use this field to add state to every subsequent webhook for the new leg.

    It must be a valid Base-64 encoded string.
    """

    time_limit_secs: int
    """Sets the maximum duration of a Call Control Leg in seconds.

    If the time limit is reached, the call will hangup and a `call.hangup` webhook
    with a `hangup_cause` of `time_limit` will be sent. For example, by setting a
    time limit of 120 seconds, a Call Leg will be automatically terminated two
    minutes after being answered. The default time limit is 14400 seconds or 4 hours
    and this is also the maximum allowed call length.
    """

    timeout_secs: int
    """
    The number of seconds that Telnyx will wait for the call to be answered by the
    destination to which it is being transferred. If the timeout is reached before
    an answer is received, the call will hangup and a `call.hangup` webhook with a
    `hangup_cause` of `timeout` will be sent. Minimum value is 5 seconds. Maximum
    value is 600 seconds.
    """

    webhook_url: str
    """
    Use this field to override the URL for which Telnyx will send subsequent
    webhooks to for this call.
    """

    webhook_url_method: Literal["POST", "GET"]
    """HTTP request type used for `webhook_url`."""


class AnsweringMachineDetectionConfig(TypedDict, total=False):
    after_greeting_silence_millis: int
    """
    Silence duration threshold after a greeting message or voice for it be
    considered human.
    """

    between_words_silence_millis: int
    """Maximum threshold for silence between words."""

    greeting_duration_millis: int
    """Maximum threshold of a human greeting.

    If greeting longer than this value, considered machine.
    """

    greeting_silence_duration_millis: int
    """If machine already detected, maximum threshold for silence between words.

    If exceeded, the greeting is considered ended.
    """

    greeting_total_analysis_time_millis: int
    """
    If machine already detected, maximum timeout threshold to determine the end of
    the machine greeting.
    """

    initial_silence_millis: int
    """If initial silence duration is greater than this value, consider it a machine."""

    maximum_number_of_words: int
    """If number of detected words is greater than this value, consder it a machine."""

    maximum_word_length_millis: int
    """If a single word lasts longer than this threshold, consider it a machine."""

    silence_threshold: int
    """Minimum noise threshold for any analysis."""

    total_analysis_time_millis: int
    """Maximum timeout threshold for overall detection."""

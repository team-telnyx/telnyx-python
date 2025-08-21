# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .stream_codec import StreamCodec
from .sip_header_param import SipHeaderParam
from .custom_sip_header_param import CustomSipHeaderParam
from .dialogflow_config_param import DialogflowConfigParam
from .sound_modifications_param import SoundModificationsParam
from .stream_bidirectional_mode import StreamBidirectionalMode
from .stream_bidirectional_codec import StreamBidirectionalCodec
from .stream_bidirectional_target_legs import StreamBidirectionalTargetLegs
from .calls.transcription_start_request_param import TranscriptionStartRequestParam

__all__ = ["CallDialParams", "AnsweringMachineDetectionConfig", "ConferenceConfig"]


class CallDialParams(TypedDict, total=False):
    connection_id: Required[str]
    """
    The ID of the Call Control App (formerly ID of the connection) to be used when
    dialing the destination.
    """

    from_: Required[Annotated[str, PropertyInfo(alias="from")]]
    """
    The `from` number to be used as the caller id presented to the destination (`to`
    number). The number should be in +E164 format.
    """

    to: Required[Union[str, List[str]]]
    """The DID or SIP URI to dial out to.

    Multiple DID or SIP URIs can be provided using an array of strings
    """

    answering_machine_detection: Literal["premium", "detect", "detect_beep", "detect_words", "greeting_end", "disabled"]
    """Enables Answering Machine Detection.

    Telnyx offers Premium and Standard detections. With Premium detection, when a
    call is answered, Telnyx runs real-time detection and sends a
    `call.machine.premium.detection.ended` webhook with one of the following
    results: `human_residence`, `human_business`, `machine`, `silence` or
    `fax_detected`. If we detect a beep, we also send a
    `call.machine.premium.greeting.ended` webhook with the result of
    `beep_detected`. If we detect a beep before
    `call.machine.premium.detection.ended` we only send
    `call.machine.premium.greeting.ended`, and if we detect a beep after
    `call.machine.premium.detection.ended`, we send both webhooks. With Standard
    detection, when a call is answered, Telnyx runs real-time detection to determine
    if it was picked up by a human or a machine and sends an
    `call.machine.detection.ended` webhook with the analysis result. If
    `greeting_end` or `detect_words` is used and a `machine` is detected, you will
    receive another `call.machine.greeting.ended` webhook when the answering machine
    greeting ends with a beep or silence. If `detect_beep` is used, you will only
    receive `call.machine.greeting.ended` if a beep is detected.
    """

    answering_machine_detection_config: AnsweringMachineDetectionConfig
    """
    Optional configuration parameters to modify 'answering_machine_detection'
    performance.
    """

    audio_url: str
    """The URL of a file to be played back to the callee when the call is answered.

    The URL can point to either a WAV or MP3 file. media_name and audio_url cannot
    be used together in one request.
    """

    billing_group_id: str
    """Use this field to set the Billing Group ID for the call.

    Must be a valid and existing Billing Group ID.
    """

    bridge_intent: bool
    """Indicates the intent to bridge this call with the call specified in link_to.

    When bridge_intent is true, link_to becomes required and the from number will be
    overwritten by the from number from the linked call.
    """

    bridge_on_answer: bool
    """Whether to automatically bridge answered call to the call specified in link_to.

    When bridge_on_answer is true, link_to becomes required.
    """

    client_state: str
    """Use this field to add state to every subsequent webhook.

    It must be a valid Base-64 encoded string.
    """

    command_id: str
    """Use this field to avoid duplicate commands.

    Telnyx will ignore others Dial commands with the same `command_id`.
    """

    conference_config: ConferenceConfig
    """Optional configuration parameters to dial new participant into a conference."""

    custom_headers: Iterable[CustomSipHeaderParam]
    """Custom headers to be added to the SIP INVITE."""

    dialogflow_config: DialogflowConfigParam

    enable_dialogflow: bool
    """Enables Dialogflow for the current call. The default value is false."""

    from_display_name: str
    """
    The `from_display_name` string to be used as the caller id name (SIP From
    Display Name) presented to the destination (`to` number). The string should have
    a maximum of 128 characters, containing only letters, numbers, spaces, and
    -\\__~!.+ special characters. If ommited, the display name will be the same as the
    number in the `from` field.
    """

    link_to: str
    """Use another call's control id for sharing the same call session id"""

    media_encryption: Literal["disabled", "SRTP", "DTLS"]
    """Defines whether media should be encrypted on the call."""

    media_name: str
    """
    The media_name of a file to be played back to the callee when the call is
    answered. The media_name must point to a file previously uploaded to
    api.telnyx.com/v2/media by the same user/organization. The file must either be a
    WAV or MP3 file.
    """

    preferred_codecs: str
    """
    The list of comma-separated codecs in a preferred order for the forked media to
    be received.
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

    send_silence_when_idle: bool
    """Generate silence RTP packets when no transmission available."""

    sip_auth_password: str
    """SIP Authentication password used for SIP challenges."""

    sip_auth_username: str
    """SIP Authentication username used for SIP challenges."""

    sip_headers: Iterable[SipHeaderParam]
    """SIP headers to be added to the SIP INVITE request.

    Currently only User-to-User header is supported.
    """

    sip_transport_protocol: Literal["UDP", "TCP", "TLS"]
    """Defines SIP transport protocol to be used on the call."""

    sound_modifications: SoundModificationsParam
    """Use this field to modify sound effects, for example adjust the pitch."""

    stream_bidirectional_codec: StreamBidirectionalCodec
    """Indicates codec for bidirectional streaming RTP payloads.

    Used only with stream_bidirectional_mode=rtp. Case sensitive.
    """

    stream_bidirectional_mode: StreamBidirectionalMode
    """Configures method of bidirectional streaming (mp3, rtp)."""

    stream_bidirectional_sampling_rate: Literal[8000, 16000, 48000]
    """Audio sampling rate."""

    stream_bidirectional_target_legs: StreamBidirectionalTargetLegs
    """Specifies which call legs should receive the bidirectional stream audio."""

    stream_codec: StreamCodec
    """Specifies the codec to be used for the streamed audio.

    When set to 'default' or when transcoding is not possible, the codec from the
    call will be used. Currently, transcoding is only supported between PCMU and
    PCMA codecs.
    """

    stream_establish_before_call_originate: bool
    """Establish websocket connection before dialing the destination.

    This is useful for cases where the websocket connection takes a long time to
    establish.
    """

    stream_track: Literal["inbound_track", "outbound_track", "both_tracks"]
    """Specifies which track should be streamed."""

    stream_url: str
    """The destination WebSocket address where the stream is going to be delivered."""

    supervise_call_control_id: str
    """The call leg which will be supervised by the new call."""

    supervisor_role: Literal["barge", "whisper", "monitor"]
    """The role of the supervisor call.

    'barge' means that supervisor call hears and is being heard by both ends of the
    call (caller & callee). 'whisper' means that only supervised_call_control_id
    hears supervisor but supervisor can hear everything. 'monitor' means that nobody
    can hear supervisor call, but supervisor can hear everything on the call.
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
    destination to which it is being called. If the timeout is reached before an
    answer is received, the call will hangup and a `call.hangup` webhook with a
    `hangup_cause` of `timeout` will be sent. Minimum value is 5 seconds. Maximum
    value is 600 seconds.
    """

    transcription: bool
    """Enable transcription upon call answer. The default value is false."""

    transcription_config: TranscriptionStartRequestParam

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


class ConferenceConfig(TypedDict, total=False):
    id: str
    """Conference ID to be joined"""

    beep_enabled: Literal["always", "never", "on_enter", "on_exit"]
    """
    Whether a beep sound should be played when the participant joins and/or leaves
    the conference. Can be used to override the conference-level setting.
    """

    conference_name: str
    """Conference name to be joined"""

    early_media: bool
    """Controls the moment when dialled call is joined into conference.

    If set to `true` user will be joined as soon as media is available (ringback).
    If `false` user will be joined when call is answered. Defaults to `true`
    """

    end_conference_on_exit: bool
    """
    Whether the conference should end and all remaining participants be hung up
    after the participant leaves the conference. Defaults to "false".
    """

    hold: bool
    """
    Whether the participant should be put on hold immediately after joining the
    conference. Defaults to "false".
    """

    hold_audio_url: str
    """
    The URL of a file to be played to the participant when they are put on hold
    after joining the conference. hold_media_name and hold_audio_url cannot be used
    together in one request. Takes effect only when "start_conference_on_create" is
    set to "false". This property takes effect only if "hold" is set to "true".
    """

    hold_media_name: str
    """
    The media_name of a file to be played to the participant when they are put on
    hold after joining the conference. The media_name must point to a file
    previously uploaded to api.telnyx.com/v2/media by the same user/organization.
    The file must either be a WAV or MP3 file. Takes effect only when
    "start_conference_on_create" is set to "false". This property takes effect only
    if "hold" is set to "true".
    """

    mute: bool
    """Whether the participant should be muted immediately after joining the
    conference.

    Defaults to "false".
    """

    soft_end_conference_on_exit: bool
    """Whether the conference should end after the participant leaves the conference.

    NOTE this doesn't hang up the other participants. Defaults to "false".
    """

    start_conference_on_create: bool
    """Whether the conference should be started on creation.

    If the conference isn't started all participants that join are automatically put
    on hold. Defaults to "true".
    """

    start_conference_on_enter: bool
    """
    Whether the conference should be started after the participant joins the
    conference. Defaults to "false".
    """

    supervisor_role: Literal["barge", "monitor", "none", "whisper"]
    """Sets the joining participant as a supervisor for the conference.

    A conference can have multiple supervisors. "barge" means the supervisor enters
    the conference as a normal participant. This is the same as "none". "monitor"
    means the supervisor is muted but can hear all participants. "whisper" means
    that only the specified "whisper_call_control_ids" can hear the supervisor.
    Defaults to "none".
    """

    whisper_call_control_ids: List[str]
    """Array of unique call_control_ids the joining supervisor can whisper to.

    If none provided, the supervisor will join the conference as a monitoring
    participant only.
    """

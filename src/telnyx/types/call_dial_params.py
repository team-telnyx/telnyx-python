# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .stream_codec import StreamCodec
from .sip_header_param import SipHeaderParam
from .custom_sip_header_param import CustomSipHeaderParam
from .dialogflow_config_param import DialogflowConfigParam
from .sound_modifications_param import SoundModificationsParam
from .stream_bidirectional_mode import StreamBidirectionalMode
from .stream_bidirectional_codec import StreamBidirectionalCodec
from .call_assistant_request_param import CallAssistantRequestParam
from .calls.aws_voice_settings_param import AwsVoiceSettingsParam
from .stream_bidirectional_target_legs import StreamBidirectionalTargetLegs
from .calls.telnyx_voice_settings_param import TelnyxVoiceSettingsParam
from .shared_params.rime_voice_settings import RimeVoiceSettings
from .shared_params.azure_voice_settings import AzureVoiceSettings
from .stream_bidirectional_sampling_rate import StreamBidirectionalSamplingRate
from .shared_params.minimax_voice_settings import MinimaxVoiceSettings
from .shared_params.resemble_voice_settings import ResembleVoiceSettings
from .calls.eleven_labs_voice_settings_param import ElevenLabsVoiceSettingsParam
from .calls.transcription_start_request_param import TranscriptionStartRequestParam

__all__ = [
    "CallDialParams",
    "AnsweringMachineDetectionConfig",
    "ConferenceConfig",
    "ConversationRelayConfig",
    "ConversationRelayConfigInterruptionSettings",
    "ConversationRelayConfigLanguage",
    "ConversationRelayConfigLanguageVoiceSettings",
    "ConversationRelayConfigLanguageVoiceSettingsInworldVoiceSettings",
    "ConversationRelayConfigLanguageVoiceSettingsXaiVoiceSettings",
    "ConversationRelayConfigVoiceSettings",
    "ConversationRelayConfigVoiceSettingsInworldVoiceSettings",
    "ConversationRelayConfigVoiceSettingsXaiVoiceSettings",
    "DeepfakeDetection",
    "WebhookRetriesPolicies",
]


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

    to: Required[Union[str, SequenceNotStr[str]]]
    """The DID or SIP URI to dial out to.

    Multiple DID or SIP URIs can be provided using an array of strings. For SIP URI
    destinations, append `;secure=true` or `;secure=srtp` to enable SRTP media
    encryption for that endpoint, or `;secure=dtls` to enable DTLS media encryption
    for that endpoint. If `media_encryption` is set to `SRTP` or `DTLS`, it takes
    precedence over any per-endpoint `secure` URI parameter. For a single string
    destination, you may append a comma followed by DTMF digits (e.g.
    `+18004247767,200`) to play those digits as DTMF once the called party answers —
    equivalent to setting `send_digits_on_answer` separately. If both are present,
    the explicit `send_digits_on_answer` parameter takes precedence. This shorthand
    is not supported when `to` is an array.
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
    performance. Only `total_analysis_time_millis` and `greeting_duration_millis`
    parameters are applicable when `premium` is selected as
    answering_machine_detection.
    """

    assistant: CallAssistantRequestParam
    """AI Assistant configuration.

    All fields except `id` are optional — the assistant's stored configuration will
    be used as fallback for any omitted fields.
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

    conversation_relay_config: ConversationRelayConfig
    """
    Starts a Conversation Relay session automatically when the answered/dialed call
    is answered. This embedded shape is supported on `answer` and `dial`. It uses
    public field names (`url`, `dtmf_detection`, `greeting`, `voice`, `language`,
    etc.) and maps them to the underlying Conversation Relay action. `client_state`,
    `tts_language`, and `transcription_language` inside this object are ignored; use
    the parent command's `client_state` and `command_id` fields instead.
    """

    custom_headers: Iterable[CustomSipHeaderParam]
    """Custom headers to be added to the SIP INVITE."""

    deepfake_detection: DeepfakeDetection
    """Enables deepfake detection on the call.

    When enabled, audio from the remote party is streamed to a detection service
    that analyzes whether the voice is AI-generated. Results are delivered via the
    `call.deepfake_detection.result` webhook.
    """

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
    """Defines whether media should be encrypted on the call.

    For SIP URI destinations, media encryption can also be requested per endpoint
    with the `secure` URI parameter: `;secure=true` or `;secure=srtp` enables SRTP,
    and `;secure=dtls` enables DTLS. This parameter, when set to `SRTP` or `DTLS`,
    takes precedence over the per-endpoint `secure` value.
    """

    media_name: str
    """
    The media_name of a file to be played back to the callee when the call is
    answered. The media_name must point to a file previously uploaded to
    api.telnyx.com/v2/media by the same user/organization. The file must either be a
    WAV or MP3 file.
    """

    park_after_unbridge: str
    """If supplied with the value `self`, the current leg will be parked after
    unbridge.

    If not set, the default behavior is to hang up the leg. When park_after_unbridge
    is set, link_to becomes required.
    """

    preferred_codecs: str
    """
    The list of comma-separated codecs in a preferred order for the forked media to
    be received.
    """

    prevent_double_bridge: bool
    """Prevents bridging and hangs up the call if the target is already bridged.

    Disabled by default.
    """

    privacy: Literal["id", "none"]
    """Indicates the privacy level to be used for the call.

    When set to `id`, caller ID information (name and number) will be hidden from
    the called party. When set to `none` or omitted, caller ID will be shown
    normally.
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

    send_digits_on_answer: str
    """DTMF digits to send automatically after the called party answers.

    Useful for reaching an extension behind an IVR (e.g. `"200"` to dial extension
    200 once the called party picks up). Allowed characters: `0-9`, `A-D`, `w` (0.5s
    pause), `W` (1s pause), `*`, `#`. Maximum 64 characters. When omitted, no
    automatic DTMF is sent. May also be supplied inline by appending `,<digits>` to
    `to` (e.g. `to=+18004247767,200`); if both forms are present, this explicit
    field takes precedence.
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

    sip_region: Literal["US", "Europe", "Canada", "Australia", "Middle East"]
    """Defines the SIP region to be used for the call."""

    sip_transport_protocol: Literal["UDP", "TCP", "TLS"]
    """Defines SIP transport protocol to be used on the call."""

    sound_modifications: SoundModificationsParam
    """Use this field to modify sound effects, for example adjust the pitch."""

    stream_auth_token: str
    """
    An authentication token to be sent as part of the WebSocket connection when
    using streaming. Maximum length is 4000 characters.
    """

    stream_bidirectional_codec: StreamBidirectionalCodec
    """Indicates codec for bidirectional streaming RTP payloads.

    Used only with stream_bidirectional_mode=rtp. Case sensitive.
    """

    stream_bidirectional_mode: StreamBidirectionalMode
    """Configures method of bidirectional streaming (mp3, rtp)."""

    stream_bidirectional_sampling_rate: StreamBidirectionalSamplingRate
    """Audio sampling rate."""

    stream_bidirectional_target_legs: StreamBidirectionalTargetLegs
    """Specifies which call legs should receive the bidirectional stream audio."""

    stream_codec: StreamCodec
    """Specifies the codec to be used for the streamed audio.

    When set to 'default' or when transcoding is not possible, the codec from the
    call will be used.
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

    webhook_retries_policies: Dict[str, WebhookRetriesPolicies]
    """A map of event types to retry policies.

    Each retry policy contains an array of `retries_ms` specifying the delays
    between retry attempts in milliseconds. Maximum 5 retries, total delay cannot
    exceed 60 seconds.
    """

    webhook_url: str
    """
    Use this field to override the URL for which Telnyx will send subsequent
    webhooks to for this call.
    """

    webhook_url_method: Literal["POST", "GET"]
    """HTTP request type used for `webhook_url`."""

    webhook_urls: Dict[str, str]
    """A map of event types to webhook URLs.

    When an event of the specified type occurs, the webhook URL associated with that
    event type will be called instead of the default webhook URL. Events not mapped
    here will use the default webhook URL.
    """

    webhook_urls_method: Literal["POST", "GET"]
    """HTTP request method to invoke `webhook_urls`."""


class AnsweringMachineDetectionConfig(TypedDict, total=False):
    """
    Optional configuration parameters to modify 'answering_machine_detection' performance. Only `total_analysis_time_millis` and `greeting_duration_millis` parameters are applicable when `premium` is selected as answering_machine_detection.
    """

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
    """Optional configuration parameters to dial new participant into a conference."""

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

    whisper_call_control_ids: SequenceNotStr[str]
    """Array of unique call_control_ids the joining supervisor can whisper to.

    If none provided, the supervisor will join the conference as a monitoring
    participant only.
    """


class ConversationRelayConfigInterruptionSettings(TypedDict, total=False):
    """Settings for handling caller interruptions during Conversation Relay speech."""

    enable: bool
    """Legacy boolean form.

    `true` is equivalent to `interruptible=any`; `false` is equivalent to
    `interruptible=none`.
    """

    interruptible: Literal["none", "any", "speech", "dtmf"]
    """Controls when caller input can interrupt assistant speech.

    `any` allows speech or DTMF interruptions; `none` disables interruptions;
    `speech` allows speech only; `dtmf` allows DTMF only.
    """

    interruptible_greeting: Literal["none", "any", "speech", "dtmf"]
    """Controls when caller input can interrupt assistant speech.

    `any` allows speech or DTMF interruptions; `none` disables interruptions;
    `speech` allows speech only; `dtmf` allows DTMF only.
    """

    welcome_greeting_interruptible: Literal["none", "any", "speech", "dtmf"]
    """Controls when caller input can interrupt assistant speech.

    `any` allows speech or DTMF interruptions; `none` disables interruptions;
    `speech` allows speech only; `dtmf` allows DTMF only.
    """


class ConversationRelayConfigLanguageVoiceSettingsInworldVoiceSettings(TypedDict, total=False):
    type: Required[Literal["inworld"]]
    """Voice settings provider type"""


class ConversationRelayConfigLanguageVoiceSettingsXaiVoiceSettings(TypedDict, total=False):
    type: Required[Literal["xai"]]
    """Voice settings provider type"""

    language: str
    """Language code, or `auto` to detect automatically."""


ConversationRelayConfigLanguageVoiceSettings: TypeAlias = Union[
    ElevenLabsVoiceSettingsParam,
    TelnyxVoiceSettingsParam,
    AwsVoiceSettingsParam,
    MinimaxVoiceSettings,
    AzureVoiceSettings,
    RimeVoiceSettings,
    ResembleVoiceSettings,
    ConversationRelayConfigLanguageVoiceSettingsInworldVoiceSettings,
    ConversationRelayConfigLanguageVoiceSettingsXaiVoiceSettings,
]


class ConversationRelayConfigLanguage(TypedDict, total=False):
    """Language-specific TTS and transcription settings for Conversation Relay."""

    language: Required[str]
    """BCP 47 language tag for this language configuration."""

    speech_model: str
    """Conversation Relay speech model.

    Prefer `transcription_engine_config.transcription_model` when configuring
    speech-to-text.
    """

    transcription_engine: Literal[
        "Google", "Telnyx", "Deepgram", "Azure", "xAI", "AssemblyAI", "Speechmatics", "Soniox", "A", "B"
    ]
    """Engine to use for speech recognition.

    Legacy values `A` - `Google`, `B` - `Telnyx` are supported for backward
    compatibility. When provided in a Conversation Relay language entry, Telnyx
    derives `transcription_provider` and `speech_model` for that language.
    """

    transcription_engine_config: Dict[str, object]
    """Engine-specific transcription settings for Conversation Relay.

    This accepts the same provider-specific options used by the Call Transcription
    Start command, such as `transcription_model`, without requiring the engine
    discriminator to be repeated inside this object.
    """

    transcription_provider: str
    """Conversation Relay transcription provider name.

    Prefer `transcription_engine` when configuring speech-to-text.
    """

    tts_provider: str
    """Text-to-speech provider for this language.

    If omitted and `voice` is provided, Telnyx derives the provider from the voice
    identifier.
    """

    voice: str
    """Voice identifier for this language."""

    voice_settings: ConversationRelayConfigLanguageVoiceSettings
    """The settings associated with the voice selected"""


class ConversationRelayConfigVoiceSettingsInworldVoiceSettings(TypedDict, total=False):
    type: Required[Literal["inworld"]]
    """Voice settings provider type"""


class ConversationRelayConfigVoiceSettingsXaiVoiceSettings(TypedDict, total=False):
    type: Required[Literal["xai"]]
    """Voice settings provider type"""

    language: str
    """Language code, or `auto` to detect automatically."""


ConversationRelayConfigVoiceSettings: TypeAlias = Union[
    ElevenLabsVoiceSettingsParam,
    TelnyxVoiceSettingsParam,
    AwsVoiceSettingsParam,
    MinimaxVoiceSettings,
    AzureVoiceSettings,
    RimeVoiceSettings,
    ResembleVoiceSettings,
    ConversationRelayConfigVoiceSettingsInworldVoiceSettings,
    ConversationRelayConfigVoiceSettingsXaiVoiceSettings,
]


class ConversationRelayConfig(TypedDict, total=False):
    """
    Starts a Conversation Relay session automatically when the answered/dialed call is answered. This embedded shape is supported on `answer` and `dial`. It uses public field names (`url`, `dtmf_detection`, `greeting`, `voice`, `language`, etc.) and maps them to the underlying Conversation Relay action. `client_state`, `tts_language`, and `transcription_language` inside this object are ignored; use the parent command's `client_state` and `command_id` fields instead.
    """

    url: Required[str]
    """WebSocket URL for your Conversation Relay server.

    Must start with `ws://` or `wss://`.
    """

    custom_parameters: Dict[str, object]
    """
    Custom key-value parameters forwarded to the relay session as assistant dynamic
    variables.
    """

    dtmf_detection: bool
    """Enable DTMF detection for the relay session."""

    greeting: str
    """Text played when the relay session starts."""

    interruptible: Literal["none", "any", "speech", "dtmf"]
    """Controls when caller input can interrupt assistant speech.

    `any` allows speech or DTMF interruptions; `none` disables interruptions;
    `speech` allows speech only; `dtmf` allows DTMF only.
    """

    interruptible_greeting: Literal["none", "any", "speech", "dtmf"]
    """Controls when caller input can interrupt assistant speech.

    `any` allows speech or DTMF interruptions; `none` disables interruptions;
    `speech` allows speech only; `dtmf` allows DTMF only.
    """

    interruption_settings: ConversationRelayConfigInterruptionSettings
    """Settings for handling caller interruptions during Conversation Relay speech."""

    language: str
    """Default language for both text-to-speech and speech recognition."""

    languages: Iterable[ConversationRelayConfigLanguage]
    """Per-language TTS and transcription settings."""

    provider: str
    """Structured voice provider.

    Must be supplied together with `structured_provider`.
    """

    structured_provider: Dict[str, object]
    """Provider-specific structured voice settings.

    Must be supplied together with `provider`; Telnyx sends the value as the nested
    provider configuration for Conversation Relay.
    """

    transcription_engine: Literal[
        "Google", "Telnyx", "Deepgram", "Azure", "xAI", "AssemblyAI", "Speechmatics", "Soniox", "A", "B"
    ]
    """Engine to use for speech recognition.

    Legacy values `A` - `Google`, `B` - `Telnyx` are supported for backward
    compatibility. For Conversation Relay, use this field with
    `transcription_engine_config`; the `transcription` object is not supported.
    """

    transcription_engine_config: Dict[str, object]
    """Engine-specific transcription settings for Conversation Relay.

    This accepts the same provider-specific options used by the Call Transcription
    Start command, such as `transcription_model`, without requiring the engine
    discriminator to be repeated inside this object.
    """

    tts_provider: str
    """Text-to-speech provider.

    If omitted, Telnyx derives it from `voice` or `provider`.
    """

    voice: str
    """The voice to be used by the voice assistant.

    Currently we support ElevenLabs, Telnyx and AWS voices.

    **Supported Providers:**

    - **AWS:** Use `AWS.Polly.<VoiceId>` (e.g., `AWS.Polly.Joanna`). For neural
      voices, which provide more realistic, human-like speech, append `-Neural` to
      the `VoiceId` (e.g., `AWS.Polly.Joanna-Neural`). Check the
      [available voices](https://docs.aws.amazon.com/polly/latest/dg/available-voices.html)
      for compatibility.
    - **Azure:** Use `Azure.<VoiceId>. (e.g. Azure.en-CA-ClaraNeural,
      Azure.en-CA-LiamNeural, Azure.en-US-BrianMultilingualNeural,
      Azure.en-US-Ava:DragonHDLatestNeural. For a complete list of voices, go to
      [Azure Voice Gallery](https://speech.microsoft.com/portal/voicegallery).)
    - **ElevenLabs:** Use `ElevenLabs.<ModelId>.<VoiceId>` (e.g.,
      `ElevenLabs.BaseModel.John`). The `ModelId` part is optional. To use
      ElevenLabs, you must provide your ElevenLabs API key as an integration secret
      under `"voice_settings": {"api_key_ref": "<secret_id>"}`. See
      [integration secrets documentation](https://developers.telnyx.com/api/secrets-manager/integration-secrets/create-integration-secret)
      for details. Check
      [available voices](https://elevenlabs.io/docs/api-reference/get-voices).
    - **Telnyx:** Use `Telnyx.<model_id>.<voice_id>`
    - **Inworld:** Use `Inworld.<ModelId>.<VoiceId>` (e.g., `Inworld.Mini.Loretta`,
      `Inworld.Max.Oliver`). Supported models: `Mini`, `Max`.
    - **xAI:** Use `xAI.<VoiceId>` (e.g., `xAI.eve`). Available voices: `eve`,
      `ara`, `rex`, `sal`, `leo`.
    """

    voice_settings: ConversationRelayConfigVoiceSettings
    """The settings associated with the voice selected"""


class DeepfakeDetection(TypedDict, total=False):
    """Enables deepfake detection on the call.

    When enabled, audio from the remote party is streamed to a detection service that analyzes whether the voice is AI-generated. Results are delivered via the `call.deepfake_detection.result` webhook.
    """

    enabled: Required[bool]
    """Whether deepfake detection is enabled."""

    rtp_timeout: int
    """Maximum time in seconds to wait for RTP audio before timing out.

    If no audio is received within this window, detection stops with an error.
    """

    timeout: int
    """Maximum time in seconds to wait for a detection result before timing out."""


class WebhookRetriesPolicies(TypedDict, total=False):
    retries_ms: Iterable[int]
    """Array of delays in milliseconds between retry attempts.

    Total sum cannot exceed 60000ms.
    """

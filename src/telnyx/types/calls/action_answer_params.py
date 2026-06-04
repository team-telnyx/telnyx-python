# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..stream_codec import StreamCodec
from ..sip_header_param import SipHeaderParam
from ..custom_sip_header_param import CustomSipHeaderParam
from .aws_voice_settings_param import AwsVoiceSettingsParam
from ..sound_modifications_param import SoundModificationsParam
from ..stream_bidirectional_mode import StreamBidirectionalMode
from ..stream_bidirectional_codec import StreamBidirectionalCodec
from .telnyx_voice_settings_param import TelnyxVoiceSettingsParam
from ..call_assistant_request_param import CallAssistantRequestParam
from .eleven_labs_voice_settings_param import ElevenLabsVoiceSettingsParam
from ..shared_params.xai_voice_settings import XaiVoiceSettings
from ..stream_bidirectional_target_legs import StreamBidirectionalTargetLegs
from .transcription_start_request_param import TranscriptionStartRequestParam
from ..shared_params.rime_voice_settings import RimeVoiceSettings
from ..shared_params.azure_voice_settings import AzureVoiceSettings
from ..shared_params.minimax_voice_settings import MinimaxVoiceSettings
from ..shared_params.resemble_voice_settings import ResembleVoiceSettings

__all__ = [
    "ActionAnswerParams",
    "ConversationRelayConfig",
    "ConversationRelayConfigInterruptionSettings",
    "ConversationRelayConfigLanguage",
    "ConversationRelayConfigLanguageVoiceSettings",
    "ConversationRelayConfigLanguageVoiceSettingsInworldVoiceSettings",
    "ConversationRelayConfigVoiceSettings",
    "ConversationRelayConfigVoiceSettingsInworldVoiceSettings",
    "DeepfakeDetection",
    "WebhookRetriesPolicies",
]


class ActionAnswerParams(TypedDict, total=False):
    assistant: CallAssistantRequestParam
    """AI Assistant configuration.

    All fields except `id` are optional — the assistant's stored configuration will
    be used as fallback for any omitted fields.
    """

    billing_group_id: str
    """Use this field to set the Billing Group ID for the call.

    Must be a valid and existing Billing Group ID.
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
    """Custom headers to be added to the SIP INVITE response."""

    deepfake_detection: DeepfakeDetection
    """Enables deepfake detection on the call.

    When enabled, audio from the remote party is streamed to a detection service
    that analyzes whether the voice is AI-generated. Results are delivered via the
    `call.deepfake_detection.result` webhook.
    """

    preferred_codecs: Literal["G722,PCMU,PCMA,G729,OPUS,VP8,H264"]
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

    sip_headers: Iterable[SipHeaderParam]
    """SIP headers to be added to the SIP INVITE response.

    Currently only User-to-User header is supported.
    """

    sound_modifications: SoundModificationsParam
    """Use this field to modify sound effects, for example adjust the pitch."""

    stream_bidirectional_codec: StreamBidirectionalCodec
    """Indicates codec for bidirectional streaming RTP payloads.

    Used only with stream_bidirectional_mode=rtp. Case sensitive.
    """

    stream_bidirectional_mode: StreamBidirectionalMode
    """Configures method of bidirectional streaming (mp3, rtp)."""

    stream_bidirectional_target_legs: StreamBidirectionalTargetLegs
    """Specifies which call legs should receive the bidirectional stream audio."""

    stream_codec: StreamCodec
    """Specifies the codec to be used for the streamed audio.

    When set to 'default' or when transcoding is not possible, the codec from the
    call will be used.
    """

    stream_track: Literal["inbound_track", "outbound_track", "both_tracks"]
    """Specifies which track should be streamed."""

    stream_url: str
    """The destination WebSocket address where the stream is going to be delivered."""

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
    event type will be called instead of `webhook_url`. Events not mapped here will
    use the default `webhook_url`.
    """

    webhook_urls_method: Literal["POST", "GET"]
    """HTTP request method to invoke `webhook_urls`."""


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


ConversationRelayConfigLanguageVoiceSettings: TypeAlias = Union[
    ElevenLabsVoiceSettingsParam,
    TelnyxVoiceSettingsParam,
    AwsVoiceSettingsParam,
    MinimaxVoiceSettings,
    AzureVoiceSettings,
    RimeVoiceSettings,
    ResembleVoiceSettings,
    ConversationRelayConfigLanguageVoiceSettingsInworldVoiceSettings,
    XaiVoiceSettings,
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


ConversationRelayConfigVoiceSettings: TypeAlias = Union[
    ElevenLabsVoiceSettingsParam,
    TelnyxVoiceSettingsParam,
    AwsVoiceSettingsParam,
    MinimaxVoiceSettings,
    AzureVoiceSettings,
    RimeVoiceSettings,
    ResembleVoiceSettings,
    ConversationRelayConfigVoiceSettingsInworldVoiceSettings,
    XaiVoiceSettings,
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

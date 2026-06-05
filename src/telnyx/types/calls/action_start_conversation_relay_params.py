# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .aws_voice_settings_param import AwsVoiceSettingsParam
from .telnyx_voice_settings_param import TelnyxVoiceSettingsParam
from .eleven_labs_voice_settings_param import ElevenLabsVoiceSettingsParam
from ..shared_params.rime_voice_settings import RimeVoiceSettings
from ..shared_params.azure_voice_settings import AzureVoiceSettings
from ..shared_params.minimax_voice_settings import MinimaxVoiceSettings
from ..shared_params.resemble_voice_settings import ResembleVoiceSettings

__all__ = [
    "ActionStartConversationRelayParams",
    "Assistant",
    "ConversationRelaySettings",
    "ConversationRelaySettingsLanguage",
    "ConversationRelaySettingsLanguageVoiceSettings",
    "ConversationRelaySettingsLanguageVoiceSettingsInworldVoiceSettings",
    "ConversationRelaySettingsLanguageVoiceSettingsXaiVoiceSettings",
    "InterruptionSettings",
    "Language",
    "LanguageVoiceSettings",
    "LanguageVoiceSettingsInworldVoiceSettings",
    "LanguageVoiceSettingsXaiVoiceSettings",
    "VoiceSettings",
    "VoiceSettingsInworldVoiceSettings",
    "VoiceSettingsXaiVoiceSettings",
]


class ActionStartConversationRelayParams(TypedDict, total=False):
    assistant: Assistant
    """Custom parameters for the Conversation Relay session.

    Pass key-value data as `assistant.dynamic_variables` to make it available to the
    relay session.
    """

    client_state: str
    """Use this field to add state to subsequent webhooks.

    It must be a valid Base-64 encoded string.
    """

    command_id: str
    """Use this field to avoid duplicate commands.

    Telnyx will ignore any command with the same `command_id` for the same
    `call_control_id`.
    """

    conversation_relay_dtmf_detection: bool
    """Enable DTMF detection for the relay session."""

    conversation_relay_settings: ConversationRelaySettings
    """Conversation Relay connection settings.

    This object can provide `url`, `dtmf_detection`, `interruptible`,
    `interruptible_greeting`, and `languages`. Top-level aliases override nested
    values when both are present.
    """

    conversation_relay_url: str
    """WebSocket URL for your Conversation Relay server.

    Must start with `ws://` or `wss://`.
    """

    custom_parameters: Dict[str, object]
    """
    Custom key-value parameters forwarded to the relay session as
    `assistant.dynamic_variables`. If `assistant.dynamic_variables` is also present,
    these values are merged in.
    """

    dtmf_detection: bool
    """Public alias for `conversation_relay_dtmf_detection`.

    If both are present, this value wins.
    """

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

    interruption_settings: InterruptionSettings
    """Settings for handling caller interruptions during Conversation Relay speech."""

    language: str
    """Default language for the relay session.

    This value is used for both text-to-speech and speech recognition.
    """

    languages: Iterable[Language]
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

    transcription: Dict[str, object]
    """Not supported for Conversation Relay start requests.

    Use `transcription_engine` and `transcription_engine_config` instead.
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

    url: str
    """Public alias for `conversation_relay_url`.

    Must start with `ws://` or `wss://`. If both are present, this value wins.
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

    voice_settings: VoiceSettings
    """The settings associated with the voice selected"""


class Assistant(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Custom parameters for the Conversation Relay session.

    Pass key-value data as `assistant.dynamic_variables` to make it available to the relay session.
    """

    dynamic_variables: Dict[str, str]
    """Custom key-value parameters forwarded to the Conversation Relay session."""


class ConversationRelaySettingsLanguageVoiceSettingsInworldVoiceSettings(TypedDict, total=False):
    type: Required[Literal["inworld"]]
    """Voice settings provider type"""


class ConversationRelaySettingsLanguageVoiceSettingsXaiVoiceSettings(TypedDict, total=False):
    type: Required[Literal["xai"]]
    """Voice settings provider type"""

    language: str
    """Language code, or `auto` to detect automatically."""


ConversationRelaySettingsLanguageVoiceSettings: TypeAlias = Union[
    ElevenLabsVoiceSettingsParam,
    TelnyxVoiceSettingsParam,
    AwsVoiceSettingsParam,
    MinimaxVoiceSettings,
    AzureVoiceSettings,
    RimeVoiceSettings,
    ResembleVoiceSettings,
    ConversationRelaySettingsLanguageVoiceSettingsInworldVoiceSettings,
    ConversationRelaySettingsLanguageVoiceSettingsXaiVoiceSettings,
]


class ConversationRelaySettingsLanguage(TypedDict, total=False):
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

    voice_settings: ConversationRelaySettingsLanguageVoiceSettings
    """The settings associated with the voice selected"""


class ConversationRelaySettings(TypedDict, total=False):
    """Conversation Relay connection settings.

    This object can provide `url`, `dtmf_detection`, `interruptible`, `interruptible_greeting`, and `languages`. Top-level aliases override nested values when both are present.
    """

    url: Required[str]
    """WebSocket URL for your Conversation Relay server.

    Must start with `ws://` or `wss://`.
    """

    dtmf_detection: bool
    """Whether to enable DTMF detection during the relay session."""

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

    languages: Iterable[ConversationRelaySettingsLanguage]
    """Language-specific TTS and transcription settings."""


class InterruptionSettings(TypedDict, total=False):
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


class LanguageVoiceSettingsInworldVoiceSettings(TypedDict, total=False):
    type: Required[Literal["inworld"]]
    """Voice settings provider type"""


class LanguageVoiceSettingsXaiVoiceSettings(TypedDict, total=False):
    type: Required[Literal["xai"]]
    """Voice settings provider type"""

    language: str
    """Language code, or `auto` to detect automatically."""


LanguageVoiceSettings: TypeAlias = Union[
    ElevenLabsVoiceSettingsParam,
    TelnyxVoiceSettingsParam,
    AwsVoiceSettingsParam,
    MinimaxVoiceSettings,
    AzureVoiceSettings,
    RimeVoiceSettings,
    ResembleVoiceSettings,
    LanguageVoiceSettingsInworldVoiceSettings,
    LanguageVoiceSettingsXaiVoiceSettings,
]


class Language(TypedDict, total=False):
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

    voice_settings: LanguageVoiceSettings
    """The settings associated with the voice selected"""


class VoiceSettingsInworldVoiceSettings(TypedDict, total=False):
    type: Required[Literal["inworld"]]
    """Voice settings provider type"""


class VoiceSettingsXaiVoiceSettings(TypedDict, total=False):
    type: Required[Literal["xai"]]
    """Voice settings provider type"""

    language: str
    """Language code, or `auto` to detect automatically."""


VoiceSettings: TypeAlias = Union[
    ElevenLabsVoiceSettingsParam,
    TelnyxVoiceSettingsParam,
    AwsVoiceSettingsParam,
    MinimaxVoiceSettings,
    AzureVoiceSettings,
    RimeVoiceSettings,
    ResembleVoiceSettings,
    VoiceSettingsInworldVoiceSettings,
    VoiceSettingsXaiVoiceSettings,
]

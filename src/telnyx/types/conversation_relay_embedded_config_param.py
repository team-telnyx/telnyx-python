# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .calls.aws_voice_settings_param import AwsVoiceSettingsParam
from .shared_params.xai_voice_settings import XaiVoiceSettings
from .calls.telnyx_voice_settings_param import TelnyxVoiceSettingsParam
from .conversation_relay_language_param import ConversationRelayLanguageParam
from .shared_params.rime_voice_settings import RimeVoiceSettings
from .shared_params.azure_voice_settings import AzureVoiceSettings
from .shared_params.inworld_voice_settings import InworldVoiceSettings
from .shared_params.minimax_voice_settings import MinimaxVoiceSettings
from .shared_params.resemble_voice_settings import ResembleVoiceSettings
from .calls.conversation_relay_interruptible import ConversationRelayInterruptible
from .calls.eleven_labs_voice_settings_param import ElevenLabsVoiceSettingsParam
from .conversation_relay_interruption_settings_param import ConversationRelayInterruptionSettingsParam

__all__ = ["ConversationRelayEmbeddedConfigParam", "VoiceSettings"]

VoiceSettings: TypeAlias = Union[
    ElevenLabsVoiceSettingsParam,
    TelnyxVoiceSettingsParam,
    AwsVoiceSettingsParam,
    MinimaxVoiceSettings,
    AzureVoiceSettings,
    RimeVoiceSettings,
    ResembleVoiceSettings,
    InworldVoiceSettings,
    XaiVoiceSettings,
]


class ConversationRelayEmbeddedConfigParam(TypedDict, total=False):
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

    interruptible: ConversationRelayInterruptible
    """Controls when caller input can interrupt assistant speech.

    `any` allows speech or DTMF interruptions; `none` disables interruptions;
    `speech` allows speech only; `dtmf` allows DTMF only.
    """

    interruptible_greeting: ConversationRelayInterruptible
    """Controls when caller input can interrupt assistant speech.

    `any` allows speech or DTMF interruptions; `none` disables interruptions;
    `speech` allows speech only; `dtmf` allows DTMF only.
    """

    interruption_settings: ConversationRelayInterruptionSettingsParam
    """Settings for handling caller interruptions during Conversation Relay speech."""

    language: str
    """Default language for both text-to-speech and speech recognition."""

    languages: Iterable[ConversationRelayLanguageParam]
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
      `Inworld.Max.Oliver`, `Inworld.TTS2.Loretta`). Supported models: `Mini`,
      `Max`, `TTS2`.
    - **Fish Audio:** Use `FishAudio.<ModelId>.<VoiceId>` (e.g.,
      `FishAudio.s2.1-pro.<reference_id>`). Supported models: `s2.1-pro`, `s2-pro`,
      `s1`. `VoiceId` is a Fish Voice-Library reference ID.
    - **xAI:** Use `xAI.<VoiceId>` (e.g., `xAI.eve`). Available voices: `eve`,
      `ara`, `rex`, `sal`, `leo`.
    """

    voice_settings: VoiceSettings
    """The settings associated with the voice selected"""

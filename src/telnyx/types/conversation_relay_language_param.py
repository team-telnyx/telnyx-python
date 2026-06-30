# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .calls.aws_voice_settings_param import AwsVoiceSettingsParam
from .shared_params.xai_voice_settings import XaiVoiceSettings
from .calls.telnyx_voice_settings_param import TelnyxVoiceSettingsParam
from .shared_params.rime_voice_settings import RimeVoiceSettings
from .shared_params.azure_voice_settings import AzureVoiceSettings
from .shared_params.inworld_voice_settings import InworldVoiceSettings
from .shared_params.minimax_voice_settings import MinimaxVoiceSettings
from .shared_params.resemble_voice_settings import ResembleVoiceSettings
from .calls.eleven_labs_voice_settings_param import ElevenLabsVoiceSettingsParam

__all__ = ["ConversationRelayLanguageParam", "VoiceSettings"]

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


class ConversationRelayLanguageParam(TypedDict, total=False):
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

    voice_settings: VoiceSettings
    """The settings associated with the voice selected"""

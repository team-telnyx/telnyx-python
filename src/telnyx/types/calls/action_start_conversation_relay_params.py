# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .aws_voice_settings_param import AwsVoiceSettingsParam
from .telnyx_voice_settings_param import TelnyxVoiceSettingsParam
from .eleven_labs_voice_settings_param import ElevenLabsVoiceSettingsParam
from ..shared_params.xai_voice_settings import XaiVoiceSettings
from ..shared_params.rime_voice_settings import RimeVoiceSettings
from ..shared_params.azure_voice_settings import AzureVoiceSettings
from ..shared_params.resemble_voice_settings import ResembleVoiceSettings

__all__ = [
    "ActionStartConversationRelayParams",
    "Assistant",
    "InterruptionSettings",
    "Language",
    "Participant",
    "Transcription",
    "VoiceSettings",
]


class ActionStartConversationRelayParams(TypedDict, total=False):
    conversation_relay_url: Required[str]
    """WebSocket URL for your Conversation Relay server.

    Must start with `ws://` or `wss://`.
    """

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

    greeting: str
    """Text played when the relay session starts."""

    interruption_settings: InterruptionSettings
    """Settings for handling caller interruptions during Conversation Relay speech."""

    language: str
    """Default language for the relay session.

    This value is used for both text-to-speech and speech recognition unless
    `tts_language` or `transcription_language` are provided.
    """

    languages: Iterable[Language]
    """Language-specific TTS and transcription settings.

    Use this when the relay session needs per-language provider, voice, or speech
    model configuration.
    """

    participants: Iterable[Participant]
    """Participants to add to the conversation."""

    send_message_history_updates: bool
    """When true, sends message history update webhooks."""

    transcription: Transcription
    """Speech-to-text settings for Conversation Relay."""

    transcription_language: str
    """Language to use for speech recognition.

    Overrides `language` for transcription when provided.
    """

    tts_language: str
    """Language to use for text-to-speech. Overrides `language` for TTS when provided."""

    user_response_timeout_ms: int
    """Time in milliseconds to wait for caller input before timing out."""

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


class Language(TypedDict, total=False):
    """Language-specific speech and transcription settings for Conversation Relay."""

    code: str
    """BCP 47 language code."""

    speech_model: str
    """Speech recognition model for this language."""

    transcription_provider: str
    """Speech-to-text provider for this language."""

    tts_provider: str
    """Text-to-speech provider for this language."""

    voice: str
    """Voice identifier for this language."""


class Participant(TypedDict, total=False):
    id: Required[str]
    """The call_control_id of the participant to add to the conversation."""

    role: Required[Literal["user"]]
    """The role of the participant in the conversation."""

    name: str
    """Display name for the participant."""

    on_hangup: Literal["continue_conversation", "end_conversation"]
    """Determines what happens to the conversation when this participant hangs up."""


class Transcription(TypedDict, total=False):
    """Speech-to-text settings for Conversation Relay."""

    language: str
    """Transcription language."""

    model: str
    """Transcription model to use."""

    provider: str
    """Transcription provider to use."""


VoiceSettings: TypeAlias = Union[
    ElevenLabsVoiceSettingsParam,
    TelnyxVoiceSettingsParam,
    AwsVoiceSettingsParam,
    AzureVoiceSettings,
    RimeVoiceSettings,
    ResembleVoiceSettings,
    XaiVoiceSettings,
]

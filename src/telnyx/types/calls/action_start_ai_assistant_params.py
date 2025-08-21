# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias, TypedDict

from .aws_voice_settings_param import AwsVoiceSettingsParam
from .transcription_config_param import TranscriptionConfigParam
from .interruption_settings_param import InterruptionSettingsParam
from .telnyx_voice_settings_param import TelnyxVoiceSettingsParam
from .eleven_labs_voice_settings_param import ElevenLabsVoiceSettingsParam

__all__ = ["ActionStartAIAssistantParams", "Assistant", "VoiceSettings"]


class ActionStartAIAssistantParams(TypedDict, total=False):
    assistant: Assistant
    """AI Assistant configuration"""

    client_state: str
    """Use this field to add state to every subsequent webhook.

    It must be a valid Base-64 encoded string.
    """

    command_id: str
    """Use this field to avoid duplicate commands.

    Telnyx will ignore any command with the same `command_id` for the same
    `call_control_id`.
    """

    greeting: str
    """
    Text that will be played when the assistant starts, if none then nothing will be
    played when the assistant starts. The greeting can be text for any voice or SSML
    for `AWS.Polly.<voice_id>` voices. There is a 3,000 character limit.
    """

    interruption_settings: InterruptionSettingsParam
    """Settings for handling user interruptions during assistant speech"""

    transcription: TranscriptionConfigParam
    """The settings associated with speech to text for the voice assistant.

    This is only relevant if the assistant uses a text-to-text language model. Any
    assistant using a model with native audio support (e.g.
    `fixie-ai/ultravox-v0_4`) will ignore this field.
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
    """

    voice_settings: VoiceSettings
    """The settings associated with the voice selected"""


class Assistant(TypedDict, total=False):
    id: str
    """The identifier of the AI assistant to use"""

    instructions: str
    """
    The system instructions that the voice assistant uses during the start assistant
    command. This will overwrite the instructions set in the assistant
    configuration.
    """

    openai_api_key_ref: str
    """Reference to the OpenAI API key. Required only when using OpenAI models"""


VoiceSettings: TypeAlias = Union[ElevenLabsVoiceSettingsParam, TelnyxVoiceSettingsParam, AwsVoiceSettingsParam]

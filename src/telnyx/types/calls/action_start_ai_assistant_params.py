# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import TypeAlias, TypedDict

from .tool_message_param import ToolMessageParam
from .user_message_param import UserMessageParam
from .system_message_param import SystemMessageParam
from .assistant_message_param import AssistantMessageParam
from .developer_message_param import DeveloperMessageParam
from .aws_voice_settings_param import AwsVoiceSettingsParam
from .transcription_config_param import TranscriptionConfigParam
from .interruption_settings_param import InterruptionSettingsParam
from .telnyx_voice_settings_param import TelnyxVoiceSettingsParam
from ..call_assistant_request_param import CallAssistantRequestParam
from .eleven_labs_voice_settings_param import ElevenLabsVoiceSettingsParam
from ..shared_params.xai_voice_settings import XaiVoiceSettings
from ..shared_params.rime_voice_settings import RimeVoiceSettings
from ..shared_params.azure_voice_settings import AzureVoiceSettings
from .ai_assistant_join_participant_param import AIAssistantJoinParticipantParam
from ..shared_params.resemble_voice_settings import ResembleVoiceSettings

__all__ = ["ActionStartAIAssistantParams", "MessageHistory", "VoiceSettings"]


class ActionStartAIAssistantParams(TypedDict, total=False):
    assistant: CallAssistantRequestParam
    """AI Assistant configuration.

    All fields except `id` are optional — the assistant's stored configuration will
    be used as fallback for any omitted fields.
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

    greeting: str
    """
    Text that will be played when the assistant starts, if none then nothing will be
    played when the assistant starts. The greeting can be text for any voice or SSML
    for `AWS.Polly.<voice_id>` voices. There is a 3,000 character limit.
    """

    interruption_settings: InterruptionSettingsParam
    """Settings for handling user interruptions during assistant speech"""

    message_history: Iterable[MessageHistory]
    """A list of messages to seed the conversation history before the assistant starts.

    Follows the same message format as the `ai_assistant_add_messages` command.
    """

    participants: Iterable[AIAssistantJoinParticipantParam]
    """A list of participants to add to the conversation when it starts."""

    send_message_history_updates: bool
    """
    When `true`, a webhook is sent each time the conversation message history is
    updated.
    """

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
    - **Inworld:** Use `Inworld.<ModelId>.<VoiceId>` (e.g., `Inworld.Mini.Loretta`,
      `Inworld.Max.Oliver`, `Inworld.TTS2.Loretta`). Supported models: `Mini`,
      `Max`, `TTS2`.
    - **xAI:** Use `xAI.<VoiceId>` (e.g., `xAI.eve`). Available voices: `eve`,
      `ara`, `rex`, `sal`, `leo`.
    """

    voice_settings: VoiceSettings
    """The settings associated with the voice selected"""


MessageHistory: TypeAlias = Union[
    UserMessageParam, AssistantMessageParam, ToolMessageParam, SystemMessageParam, DeveloperMessageParam
]

VoiceSettings: TypeAlias = Union[
    ElevenLabsVoiceSettingsParam,
    TelnyxVoiceSettingsParam,
    AwsVoiceSettingsParam,
    AzureVoiceSettings,
    RimeVoiceSettings,
    ResembleVoiceSettings,
    XaiVoiceSettings,
]

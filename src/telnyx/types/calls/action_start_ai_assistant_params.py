# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .aws_voice_settings_param import AwsVoiceSettingsParam
from .transcription_config_param import TranscriptionConfigParam
from .interruption_settings_param import InterruptionSettingsParam
from .telnyx_voice_settings_param import TelnyxVoiceSettingsParam
from ..call_assistant_request_param import CallAssistantRequestParam
from .eleven_labs_voice_settings_param import ElevenLabsVoiceSettingsParam
from ..shared_params.rime_voice_settings import RimeVoiceSettings
from ..shared_params.azure_voice_settings import AzureVoiceSettings
from ..shared_params.resemble_voice_settings import ResembleVoiceSettings

__all__ = [
    "ActionStartAIAssistantParams",
    "MessageHistory",
    "MessageHistoryUserMessage",
    "MessageHistoryAssistantMessage",
    "MessageHistoryAssistantMessageToolCall",
    "MessageHistoryAssistantMessageToolCallFunction",
    "MessageHistoryToolMessage",
    "MessageHistorySystemMessage",
    "MessageHistoryDeveloperMessage",
    "Participant",
    "VoiceSettings",
]


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

    participants: Iterable[Participant]
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
      `Inworld.Max.Oliver`). Supported models: `Mini`, `Max`.
    """

    voice_settings: VoiceSettings
    """The settings associated with the voice selected"""


class MessageHistoryUserMessage(TypedDict, total=False):
    """Messages sent by an end user"""

    content: Required[str]
    """The contents of the user message."""

    role: Required[Literal["user"]]
    """The role of the messages author, in this case `user`."""

    metadata: Dict[str, object]
    """Metadata to add to the message"""


class MessageHistoryAssistantMessageToolCallFunction(TypedDict, total=False):
    """The function that the model called."""

    name: Required[str]
    """The name of the function to call."""


class MessageHistoryAssistantMessageToolCall(TypedDict, total=False):
    """A call to a function tool created by the model."""

    id: Required[str]
    """The ID of the tool call."""

    function: Required[MessageHistoryAssistantMessageToolCallFunction]
    """The function that the model called."""

    type: Required[Literal["function"]]
    """The type of the tool. Currently, only `function` is supported."""


class MessageHistoryAssistantMessage(TypedDict, total=False):
    """Messages sent by the model in response to user messages."""

    role: Required[Literal["assistant"]]
    """The role of the messages author, in this case `assistant`."""

    content: str
    """The contents of the assistant message. Required unless `tool_calls`"""

    metadata: Dict[str, object]
    """Metadata to add to the message"""

    tool_calls: Iterable[MessageHistoryAssistantMessageToolCall]
    """The tool calls generated by the model, such as function calls."""


class MessageHistoryToolMessage(TypedDict, total=False):
    content: Required[str]
    """The contents of the tool message."""

    role: Required[Literal["tool"]]
    """The role of the messages author, in this case `tool`."""

    tool_call_id: Required[str]
    """Tool call that this message is responding to."""

    metadata: Dict[str, object]
    """Metadata to add to the message"""


class MessageHistorySystemMessage(TypedDict, total=False):
    """
    Developer-provided instructions that the model should follow, regardless of messages sent by the user.
    """

    content: Required[str]
    """The contents of the system message."""

    role: Required[Literal["system"]]
    """The role of the messages author, in this case `system`."""

    metadata: Dict[str, object]
    """Metadata to add to the message"""


class MessageHistoryDeveloperMessage(TypedDict, total=False):
    """
    Developer-provided instructions that the model should follow, regardless of messages sent by the user.
    """

    content: Required[str]
    """The contents of the developer message."""

    role: Required[Literal["developer"]]
    """The role of the messages author, in this case developer."""

    metadata: Dict[str, object]
    """Metadata to add to the message"""


MessageHistory: TypeAlias = Union[
    MessageHistoryUserMessage,
    MessageHistoryAssistantMessage,
    MessageHistoryToolMessage,
    MessageHistorySystemMessage,
    MessageHistoryDeveloperMessage,
]


class Participant(TypedDict, total=False):
    id: Required[str]
    """The call_control_id of the participant to add to the conversation."""

    role: Required[Literal["user"]]
    """The role of the participant in the conversation."""

    name: str
    """Display name for the participant."""

    on_hangup: Literal["continue_conversation", "end_conversation"]
    """Determines what happens to the conversation when this participant hangs up."""


VoiceSettings: TypeAlias = Union[
    ElevenLabsVoiceSettingsParam,
    TelnyxVoiceSettingsParam,
    AwsVoiceSettingsParam,
    AzureVoiceSettings,
    RimeVoiceSettings,
    ResembleVoiceSettings,
]

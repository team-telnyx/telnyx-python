# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import TypeAlias, TypedDict

from .tool_message_param import ToolMessageParam
from .user_message_param import UserMessageParam
from .system_message_param import SystemMessageParam
from .assistant_message_param import AssistantMessageParam
from .developer_message_param import DeveloperMessageParam
from .transcription_config_param import TranscriptionConfigParam
from .interruption_settings_param import InterruptionSettingsParam
from ..call_assistant_request_param import CallAssistantRequestParam
from .ai_assistant_join_participant_param import AIAssistantJoinParticipantParam

__all__ = ["ActionStartAIAssistantParams", "MessageHistory"]


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
    When `true`, a `call.ai_gather.message_history_updated` webhook carrying the
    full message history is sent each time the conversation message history is
    updated. The assistant's own `telephony_settings.send_message_history_updates`
    overrides this value when it is set.
    """

    transcription: TranscriptionConfigParam
    """The settings associated with speech to text for the voice assistant.

    This is only relevant if the assistant uses a text-to-text language model. Any
    assistant using a model with native audio support (e.g.
    `fixie-ai/ultravox-v0_4`) will ignore this field.
    """


MessageHistory: TypeAlias = Union[
    UserMessageParam, AssistantMessageParam, ToolMessageParam, SystemMessageParam, DeveloperMessageParam
]

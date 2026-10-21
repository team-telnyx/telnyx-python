# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Iterable, ForwardRef
from typing_extensions import TypeAlias, TypedDict

from ..call_assistant_request_param import CallAssistantRequestParam
from ..shared_params.xai_voice_settings import XaiVoiceSettings
from ..shared_params.azure_voice_settings import AzureVoiceSettings
from ..shared_params.inworld_voice_settings import InworldVoiceSettings
from ..shared_params.minimax_voice_settings import MinimaxVoiceSettings
from ..shared_params.resemble_voice_settings import ResembleVoiceSettings

__all__ = ["ActionStartAIAssistantParams", "MessageHistory", "VoiceSettings"]


class ActionStartAIAssistantParams(TypedDict, total=False):
    assistant: CallAssistantRequestParam
    """AI Assistant configuration and per-call overrides.

    All fields except `id` are optional. Omitted assistant fields use the stored
    configuration. Supplied `voice_settings` and `transcription` objects replace
    their stored objects rather than merging individual settings; include every
    setting you want to retain. `dynamic_variables` are merged, with request values
    taking precedence.
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

    interruption_settings: "InterruptionSettingsParam"
    """Settings for handling user interruptions during assistant speech"""

    message_history: Iterable[MessageHistory]
    """A list of messages to seed the conversation history before the assistant starts.

    Follows the same message format as the `ai_assistant_add_messages` command.
    """

    participants: Iterable["AIAssistantJoinParticipantParam"]
    """A list of participants to add to the conversation when it starts."""

    send_message_history_updates: bool
    """
    When `true`, a `call.ai_gather.message_history_updated` webhook carrying the
    full message history is sent each time the conversation message history is
    updated. The assistant's own `telephony_settings.send_message_history_updates`
    overrides this value when it is set.
    """

    transcription: "TranscriptionConfigParam"
    """The settings associated with speech to text for the voice assistant.

    This is only relevant if the assistant uses a text-to-text language model. Any
    assistant using a model with native audio support (e.g.
    `fixie-ai/ultravox-v0_4`) will ignore this field.
    """

    voice: str
    """
    The voice the assistant speaks with on this call, in place of the assistant's
    own voice. Use the same formats as the `voice` of the
    [speak](/api-reference/call-commands/speak-text) command. A community engine
    voice is `<EngineName>.<VoiceId>` (e.g., `acme.alpha`) and needs
    `voice_settings.api_key_ref`; see the
    [Community TTS engines guide](/docs/voice/tts/community-engines). Without
    `voice`, the assistant's own voice is used.
    """

    voice_settings: VoiceSettings
    """The settings of `voice`.

    A community engine voice requires `api_key_ref`; the other keys are the engine's
    own settings.
    """


if TYPE_CHECKING:
    MessageHistory: TypeAlias = Union[
        "UserMessageParam", "AssistantMessageParam", "ToolMessageParam", "SystemMessageParam", "DeveloperMessageParam"
    ]
else:
    MessageHistory = Union[
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).UserMessageParam"),
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).AssistantMessageParam"),
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).ToolMessageParam"),
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).SystemMessageParam"),
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).DeveloperMessageParam"),
    ]

if TYPE_CHECKING:
    VoiceSettings: TypeAlias = Union[
        "ElevenLabsVoiceSettingsParam",
        "TelnyxVoiceSettingsParam",
        "AwsVoiceSettingsParam",
        MinimaxVoiceSettings,
        AzureVoiceSettings,
        ResembleVoiceSettings,
        InworldVoiceSettings,
        XaiVoiceSettings,
        "SonioxVoiceSettingsParam",
        "CommunityVoiceSettingsParam",
    ]
else:
    VoiceSettings = Union[
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).ElevenLabsVoiceSettingsParam"),
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).TelnyxVoiceSettingsParam"),
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).AwsVoiceSettingsParam"),
        MinimaxVoiceSettings,
        AzureVoiceSettings,
        ResembleVoiceSettings,
        InworldVoiceSettings,
        XaiVoiceSettings,
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).SonioxVoiceSettingsParam"),
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).CommunityVoiceSettingsParam"),
    ]

from .tool_message_param import ToolMessageParam
from .user_message_param import UserMessageParam
from .system_message_param import SystemMessageParam
from .assistant_message_param import AssistantMessageParam
from .developer_message_param import DeveloperMessageParam
from .aws_voice_settings_param import AwsVoiceSettingsParam
from .transcription_config_param import TranscriptionConfigParam
from .interruption_settings_param import InterruptionSettingsParam
from .soniox_voice_settings_param import SonioxVoiceSettingsParam
from .telnyx_voice_settings_param import TelnyxVoiceSettingsParam
from .community_voice_settings_param import CommunityVoiceSettingsParam
from .eleven_labs_voice_settings_param import ElevenLabsVoiceSettingsParam
from .ai_assistant_join_participant_param import AIAssistantJoinParticipantParam

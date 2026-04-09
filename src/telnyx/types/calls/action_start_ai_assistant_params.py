# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..ai.hangup_tool_param import HangupToolParam
from ..ai.webhook_tool_param import WebhookToolParam
from ..ai.transfer_tool_param import TransferToolParam
from .aws_voice_settings_param import AwsVoiceSettingsParam
from .transcription_config_param import TranscriptionConfigParam
from .interruption_settings_param import InterruptionSettingsParam
from .telnyx_voice_settings_param import TelnyxVoiceSettingsParam
from .eleven_labs_voice_settings_param import ElevenLabsVoiceSettingsParam
from ..shared_params.rime_voice_settings import RimeVoiceSettings
from ..shared_params.azure_voice_settings import AzureVoiceSettings
from ..shared_params.resemble_voice_settings import ResembleVoiceSettings

__all__ = [
    "ActionStartAIAssistantParams",
    "Assistant",
    "AssistantTool",
    "AssistantToolBookAppointmentTool",
    "AssistantToolBookAppointmentToolBookAppointment",
    "AssistantToolCheckAvailabilityTool",
    "AssistantToolCheckAvailabilityToolCheckAvailability",
    "AssistantToolCallControlRetrievalTool",
    "AssistantToolCallControlRetrievalToolRetrieval",
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
    assistant: Assistant
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


class AssistantToolBookAppointmentToolBookAppointment(TypedDict, total=False):
    api_key_ref: Required[str]
    """Reference to an integration secret that contains your Cal.com API key.

    You would pass the `identifier` for an integration secret
    [/v2/integration_secrets](https://developers.telnyx.com/api/secrets-manager/integration-secrets/create-integration-secret)
    that refers to your Cal.com API key.
    """

    event_type_id: Required[int]
    """Event Type ID for which slots are being fetched.

    [cal.com](https://cal.com/docs/api-reference/v2/bookings/create-a-booking#body-event-type-id)
    """

    attendee_name: str
    """
    The name of the attendee
    [cal.com](https://cal.com/docs/api-reference/v2/bookings/create-a-booking#body-attendee-name).
    If not provided, the assistant will ask for the attendee's name.
    """

    attendee_timezone: str
    """
    The timezone of the attendee
    [cal.com](https://cal.com/docs/api-reference/v2/bookings/create-a-booking#body-attendee-timezone).
    If not provided, the assistant will ask for the attendee's timezone.
    """


class AssistantToolBookAppointmentTool(TypedDict, total=False):
    book_appointment: Required[AssistantToolBookAppointmentToolBookAppointment]

    type: Required[Literal["book_appointment"]]


class AssistantToolCheckAvailabilityToolCheckAvailability(TypedDict, total=False):
    api_key_ref: Required[str]
    """Reference to an integration secret that contains your Cal.com API key.

    You would pass the `identifier` for an integration secret
    [/v2/integration_secrets](https://developers.telnyx.com/api/secrets-manager/integration-secrets/create-integration-secret)
    that refers to your Cal.com API key.
    """

    event_type_id: Required[int]
    """Event Type ID for which slots are being fetched.

    [cal.com](https://cal.com/docs/api-reference/v2/slots/get-available-slots#parameter-event-type-id)
    """


class AssistantToolCheckAvailabilityTool(TypedDict, total=False):
    check_availability: Required[AssistantToolCheckAvailabilityToolCheckAvailability]

    type: Required[Literal["check_availability"]]


class AssistantToolCallControlRetrievalToolRetrieval(TypedDict, total=False):
    bucket_ids: Required[SequenceNotStr[str]]

    max_num_results: int
    """The maximum number of results to retrieve as context for the language model."""


class AssistantToolCallControlRetrievalTool(TypedDict, total=False):
    retrieval: Required[AssistantToolCallControlRetrievalToolRetrieval]

    type: Required[Literal["retrieval"]]


AssistantTool: TypeAlias = Union[
    AssistantToolBookAppointmentTool,
    AssistantToolCheckAvailabilityTool,
    WebhookToolParam,
    HangupToolParam,
    TransferToolParam,
    AssistantToolCallControlRetrievalTool,
]


class Assistant(TypedDict, total=False):
    """AI Assistant configuration.

    All fields except `id` are optional — the assistant's stored configuration will be used as fallback for any omitted fields.
    """

    id: Required[str]
    """The identifier of the AI assistant to use."""

    dynamic_variables: Dict[str, Union[str, float, bool]]
    """Map of dynamic variables and their default values.

    Dynamic variables can be referenced in instructions, greeting, and tool
    definitions using the `{{variable_name}}` syntax. Call-control-agent
    automatically merges in `telnyx_call_*` variables (telnyx_call_to,
    telnyx_call_from, telnyx_conversation_channel, telnyx_agent_target,
    telnyx_end_user_target, telnyx_call_caller_id_name) and custom header variables.
    """

    external_llm: object
    """External LLM configuration for bringing your own LLM endpoint."""

    fallback_config: object
    """Fallback LLM configuration used when the primary LLM provider is unavailable."""

    greeting: str
    """Initial greeting text spoken when the assistant starts.

    Can be plain text for any voice or SSML for `AWS.Polly.<voice_id>` voices. There
    is a 3,000 character limit.
    """

    instructions: str
    """System instructions for the voice assistant.

    Can be templated with
    [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables).
    This will overwrite the instructions set in the assistant configuration.
    """

    llm_api_key_ref: str
    """Integration secret identifier for the LLM provider API key.

    Use this field to reference an
    [integration secret](https://developers.telnyx.com/api/secrets-manager/integration-secrets/create-integration-secret)
    containing your LLM provider API key. Supports any LLM provider (OpenAI,
    Anthropic, etc.).
    """

    mcp_servers: Iterable[object]
    """
    MCP (Model Context Protocol) server configurations for extending the assistant's
    capabilities with external tools and data sources.
    """

    model: str
    """LLM model override for this call.

    If omitted, the assistant's configured model is used.
    """

    name: str
    """Assistant name override for this call."""

    observability_settings: object
    """
    Observability configuration for the assistant session, including Langfuse
    integration for tracing and monitoring.
    """

    openai_api_key_ref: str
    """Deprecated — use `llm_api_key_ref` instead.

    Integration secret identifier for the OpenAI API key. This field is maintained
    for backward compatibility; `llm_api_key_ref` is the canonical field name and
    supports all LLM providers.
    """

    tools: Iterable[AssistantTool]
    """
    Inline tool definitions available to the assistant (webhook, retrieval,
    transfer, hangup, etc.). Overrides the assistant's stored tools if provided.
    """


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

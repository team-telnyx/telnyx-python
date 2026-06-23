# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .flow_edge import FlowEdge
from .external_llm import ExternalLlm
from .node_position import NodePosition
from .observability import Observability
from .assistant_tool import AssistantTool
from .voice_settings import VoiceSettings
from .fallback_config import FallbackConfig
from .import_metadata import ImportMetadata
from .widget_settings import WidgetSettings
from .enabled_features import EnabledFeatures
from .insight_settings import InsightSettings
from .privacy_settings import PrivacySettings
from .messaging_settings import MessagingSettings
from .telephony_settings import TelephonySettings
from .assistant_mcp_server import AssistantMcpServer
from .assistant_integration import AssistantIntegration
from .transcription_settings import TranscriptionSettings
from .post_conversation_settings import PostConversationSettings
from .inference_embedding_interruption_settings import InferenceEmbeddingInterruptionSettings

__all__ = [
    "InferenceEmbedding",
    "ConversationFlow",
    "ConversationFlowNode",
    "ConversationFlowNodeFlowNode",
    "ConversationFlowNodeToolNode",
    "ConversationFlowNodeSpeakNode",
]


class ConversationFlowNodeFlowNode(BaseModel):
    """One step in a conversation flow, as returned by the API."""

    id: str
    """Caller-supplied unique identifier for this node within the flow."""

    instructions: str
    """Prompt that drives the LLM while this node is active. Required."""

    external_llm: Optional[ExternalLlm] = None
    """Override for `Assistant.external_llm` while this node is active.

    Use this to route a node's turns to a different external LLM (different `model`,
    `base_url`, credentials). Part of the LLM bundle — see `model` for cascade
    semantics. Mutually exclusive with `model` on the node (a single LLM identity
    per node).
    """

    instructions_mode: Optional[Literal["replace", "append"]] = None
    """How `instructions` combine with the assistant-level instructions.

    `replace` (default): the node's instructions are used alone. `append`: the
    node's instructions are concatenated after the assistant's instructions.
    """

    llm_api_key_ref: Optional[str] = None
    """Override for `Assistant.llm_api_key_ref` while this node is active.

    Part of the LLM bundle — see `model` for cascade semantics.
    """

    model: Optional[str] = None
    """Override for `Assistant.model` while this node is active.

    Part of the LLM bundle (`model` + `llm_api_key_ref` + `external_llm`): when any
    of the three is set on the node, all three are taken from the node and the
    assistant-level LLM identity is not consulted. When none of the three is set,
    the assistant's bundle cascades unchanged.
    """

    name: Optional[str] = None
    """Optional human-readable label, displayed in authoring UIs."""

    position: Optional[NodePosition] = None
    """Optional canvas coordinates used by authoring UIs to lay out the graph.

    Ignored by the runtime; round-trips so frontends can persist graph layout across
    reloads.
    """

    shared_tool_ids: Optional[List[str]] = None
    """IDs of shared (org-level) tools available at this node.

    Knowledge bases are attached the same way — via a shared retrieval tool. Tools
    not listed here are not callable while this node is active.
    """

    tools: Optional[List[List[AssistantTool]]] = None
    """Full tool definitions for this node, resolved from `shared_tool_ids`
    server-side.

    Populated on responses so clients can render the flow without a follow-up fetch
    per shared tool. Ignored on input — set `shared_tool_ids` to configure a node's
    tools.
    """

    tools_mode: Optional[Literal["replace", "append"]] = None
    """How `shared_tool_ids` combine with the assistant-level tool set.

    `replace` (default): only the node's tools are callable. `append`: the node's
    tools are added to the assistant's tools. Ignored when `shared_tool_ids` is
    null.
    """

    transcription: Optional[TranscriptionSettings] = None
    """Per-node transcription override (response form)."""

    type: Optional[Literal["prompt"]] = None
    """Node kind discriminator. `prompt` is an LLM-driven step."""

    voice_settings: Optional[VoiceSettings] = None
    """Per-node voice override (response form)."""


class ConversationFlowNodeToolNode(BaseModel):
    """A standalone tool step in a conversation flow, as returned by the API."""

    id: str
    """Caller-supplied unique identifier for this node within the flow."""

    shared_tool_id: str
    """ID of the single shared (org-level) tool this node executes.

    When the flow reaches this node the tool runs as a deliberate step (no LLM
    turn); its outgoing `tool_result` edges then route on the outcome. Arguments are
    filled from the conversation's dynamic variables by name — a dynamic variable
    whose name matches one of the tool's parameters supplies that argument.
    Cross-validated against the org's shared tools on write.
    """

    name: Optional[str] = None
    """Optional human-readable label, displayed in authoring UIs."""

    position: Optional[NodePosition] = None
    """Optional canvas coordinates used by authoring UIs to lay out the graph.

    Ignored by the runtime; round-trips so frontends can persist graph layout across
    reloads.
    """

    tool: Optional[List[AssistantTool]] = None
    """Full tool definition resolved from `shared_tool_id` server-side.

    Populated on responses so clients can render the node without a follow-up fetch.
    Ignored on input — set `shared_tool_id`.
    """

    type: Optional[Literal["tool"]] = None
    """Node kind discriminator. Always `tool` for a tool node."""


class ConversationFlowNodeSpeakNode(BaseModel):
    """A standalone scripted-message step in a flow, as returned by the API."""

    id: str
    """Caller-supplied unique identifier for this node within the flow."""

    message: str
    """Message delivered to the user verbatim when the flow reaches this node.

    No LLM turn — the text is spoken/sent exactly as written. `{{variable}}`
    placeholders are interpolated from the conversation's dynamic variables; an
    unresolved placeholder renders as an empty string. After delivering, the flow
    routes via the node's outgoing `llm` / `expression` edges (commonly a single
    unconditional edge).
    """

    name: Optional[str] = None
    """Optional human-readable label, displayed in authoring UIs."""

    position: Optional[NodePosition] = None
    """Optional canvas coordinates used by authoring UIs to lay out the graph.

    Ignored by the runtime; round-trips so frontends can persist graph layout across
    reloads.
    """

    type: Optional[Literal["speak"]] = None
    """Node kind discriminator. Always `speak` for a speak node."""


ConversationFlowNode: TypeAlias = Annotated[
    Union[ConversationFlowNodeFlowNode, ConversationFlowNodeToolNode, ConversationFlowNodeSpeakNode],
    PropertyInfo(discriminator="type"),
]


class ConversationFlow(BaseModel):
    """Conversation flow as returned by the API."""

    nodes: List[ConversationFlowNode]
    """All nodes in the flow."""

    start_node_id: str
    """ID of the node where the conversation begins."""

    edges: Optional[List[FlowEdge]] = None
    """Directed transitions between nodes."""


class InferenceEmbedding(BaseModel):
    id: str

    created_at: datetime

    instructions: str
    """System instructions for the assistant.

    These may be templated with
    [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)
    """

    model: str
    """ID of the model to use when `external_llm` is not set.

    You can use the
    [Get models API](https://developers.telnyx.com/api-reference/openai-chat/get-available-models-openai-compatible)
    to see available models. If `external_llm` is provided, the assistant uses
    `external_llm` instead of this field. If neither `model` nor `external_llm` is
    provided, Telnyx applies the default model.
    """

    name: str

    conversation_flow: Optional[ConversationFlow] = None
    """Conversation flow as returned by the API."""

    description: Optional[str] = None

    dynamic_variables: Optional[Dict[str, object]] = None
    """Map of dynamic variables and their values"""

    dynamic_variables_webhook_timeout_ms: Optional[int] = None
    """Timeout in milliseconds for the dynamic variables webhook.

    Must be between 1 and 10000 ms. If the webhook does not respond within this
    timeout, the call proceeds with default values. See the
    [dynamic variables guide](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables).
    """

    dynamic_variables_webhook_url: Optional[str] = None
    """
    If `dynamic_variables_webhook_url` is set, Telnyx sends a POST request to this
    URL at the start of the conversation to resolve dynamic variables. **Gotcha:**
    the webhook response must wrap variables under a top-level `dynamic_variables`
    object, e.g. `{"dynamic_variables": {"customer_name": "Jane"}}`. Returning a
    flat object will be ignored and variables will fall back to their defaults. See
    the
    [dynamic variables guide](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)
    for the full request/response format and timeout behavior.
    """

    enabled_features: Optional[List[EnabledFeatures]] = None

    external_llm: Optional[ExternalLlm] = None

    fallback_config: Optional[FallbackConfig] = None

    greeting: Optional[str] = None
    """Text that the assistant will use to start the conversation.

    This may be templated with
    [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables).
    Use an empty string to have the assistant wait for the user to speak first. Use
    the special value `<assistant-speaks-first-with-model-generated-message>` to
    have the assistant generate the greeting based on the system instructions.
    """

    import_metadata: Optional[ImportMetadata] = None

    insight_settings: Optional[InsightSettings] = None

    integrations: Optional[List[AssistantIntegration]] = None
    """Connected integrations attached to the assistant.

    The catalog of available integrations is at `/ai/integrations`; the user's
    connected integrations are at `/ai/integrations/connections`. Each item
    references a catalog integration by `integration_id`.
    """

    interruption_settings: Optional[InferenceEmbeddingInterruptionSettings] = None
    """
    Settings for interruptions and how the assistant decides the user has finished
    speaking. These timings are most relevant when using non turn-taking
    transcription models. For turn-taking models like `deepgram/flux`, end-of-turn
    behavior is controlled by the transcription end-of-turn settings under
    `transcription.settings` (`eot_threshold`, `eot_timeout_ms`,
    `eager_eot_threshold`).
    """

    llm_api_key_ref: Optional[str] = None
    """
    This is only needed when using third-party inference providers selected by
    `model`. The `identifier` for an integration secret
    [/v2/integration_secrets](https://developers.telnyx.com/api-reference/integration-secrets/create-a-secret)
    that refers to your LLM provider's API key. For bring-your-own endpoint
    authentication, use `external_llm.llm_api_key_ref` instead. Warning: Free plans
    are unlikely to work with this integration.
    """

    mcp_servers: Optional[List[AssistantMcpServer]] = None
    """MCP servers attached to the assistant.

    Create MCP servers with `/ai/mcp_servers`, then reference them by `id` here.
    """

    messaging_settings: Optional[MessagingSettings] = None

    observability_settings: Optional[Observability] = None

    post_conversation_settings: Optional[PostConversationSettings] = None
    """Configuration for post-conversation processing.

    When enabled, the assistant receives one additional LLM turn after the
    conversation ends, allowing it to execute tool calls such as logging to a CRM or
    sending a summary. The assistant can execute multiple parallel or sequential
    tools during this phase. Telephony-control tools (e.g. hangup, transfer) are
    unavailable post-conversation. Beta feature.
    """

    privacy_settings: Optional[PrivacySettings] = None

    related_mission_ids: Optional[List[str]] = None
    """IDs of missions related to this assistant."""

    tags: Optional[List[str]] = None
    """Tags associated with the assistant.

    Tags can also be managed with the assistant tag endpoints.
    """

    telephony_settings: Optional[TelephonySettings] = None

    tools: Optional[List[AssistantTool]] = None
    """Deprecated for new integrations.

    Inline tool definitions available to the assistant. Prefer `tool_ids` to attach
    shared tools created with the AI Tools endpoints.
    """

    transcription: Optional[TranscriptionSettings] = None

    version_created_at: Optional[datetime] = None
    """Timestamp when this assistant version was created."""

    version_id: Optional[str] = None
    """
    Identifier for the assistant version returned by version-aware assistant
    endpoints.
    """

    version_name: Optional[str] = None
    """Human-readable name for the assistant version."""

    voice_settings: Optional[VoiceSettings] = None

    widget_settings: Optional[WidgetSettings] = None
    """Configuration settings for the assistant's web widget."""

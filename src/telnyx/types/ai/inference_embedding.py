# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .observability import Observability
from .assistant_tool import AssistantTool
from .voice_settings import VoiceSettings
from .import_metadata import ImportMetadata
from .widget_settings import WidgetSettings
from .enabled_features import EnabledFeatures
from .insight_settings import InsightSettings
from .privacy_settings import PrivacySettings
from .messaging_settings import MessagingSettings
from .telephony_settings import TelephonySettings
from .transcription_settings import TranscriptionSettings

__all__ = [
    "InferenceEmbedding",
    "ConversationFlow",
    "ConversationFlowNode",
    "ConversationFlowNodeFlowNode",
    "ConversationFlowNodeFlowNodeExternalLlm",
    "ConversationFlowNodeFlowNodePosition",
    "ConversationFlowNodeToolNode",
    "ConversationFlowNodeToolNodePosition",
    "ConversationFlowNodeSpeakNode",
    "ConversationFlowNodeSpeakNodePosition",
    "ConversationFlowEdge",
    "ConversationFlowEdgeCondition",
    "ConversationFlowEdgeConditionLlmCondition",
    "ConversationFlowEdgeConditionExpressionCondition",
    "ConversationFlowEdgeConditionExpressionConditionExpression",
    "ConversationFlowEdgeConditionExpressionConditionExpressionDynamicVariableExpression",
    "ConversationFlowEdgeConditionExpressionConditionExpressionStringLiteralExpression",
    "ConversationFlowEdgeConditionExpressionConditionExpressionNumberLiteralExpression",
    "ConversationFlowEdgeConditionExpressionConditionExpressionBooleanLiteralExpression",
    "ConversationFlowEdgeConditionDefaultCondition",
    "ConversationFlowEdgeTarget",
    "ConversationFlowEdgeTargetNodeTarget",
    "ConversationFlowEdgeTargetAssistantTarget",
    "ConversationFlowEdgeTargetAssistantTargetPosition",
    "ExternalLlm",
    "FallbackConfig",
    "FallbackConfigExternalLlm",
    "Integration",
    "InterruptionSettings",
    "InterruptionSettingsStartSpeakingPlan",
    "InterruptionSettingsStartSpeakingPlanTranscriptionEndpointingPlan",
    "McpServer",
    "PostConversationSettings",
]


class ConversationFlowNodeFlowNodeExternalLlm(BaseModel):
    """Override for `Assistant.external_llm` while this node is active.

    Use this to route a node's turns to a different external LLM (different `model`, `base_url`, credentials). Part of the LLM bundle — see `model` for cascade semantics. Mutually exclusive with `model` on the node (a single LLM identity per node).
    """

    base_url: str
    """Base URL for the external LLM endpoint."""

    model: str
    """Model identifier to use with the external LLM endpoint."""

    authentication_method: Optional[Literal["token", "certificate"]] = None
    """Authentication method used when connecting to the external LLM endpoint."""

    certificate_ref: Optional[str] = None
    """
    Integration secret identifier for the client certificate used with certificate
    authentication.
    """

    forward_metadata: Optional[bool] = None
    """
    When `true`, Telnyx forwards the assistant's dynamic variables to the external
    LLM endpoint as a top-level `extra_metadata` object on the chat completion
    request body. Defaults to `false`. Example payload sent to the external
    endpoint:
    `{"extra_metadata": {"customer_name": "Jane", "account_id": "acct_789", "telnyx_agent_target": "+13125550100", "telnyx_end_user_target": "+13125550123"}}`.
    Distinct from OpenAI's native `metadata` field, which has its own size and type
    limits.
    """

    llm_api_key_ref: Optional[str] = None
    """Integration secret identifier for the external LLM API key."""

    token_retrieval_url: Optional[str] = None
    """
    URL used to retrieve an access token when certificate authentication is enabled.
    """


class ConversationFlowNodeFlowNodePosition(BaseModel):
    """Optional canvas coordinates used by authoring UIs to lay out the graph.

    Ignored by the runtime; round-trips so frontends can persist graph layout across reloads.
    """

    x: float
    """Horizontal coordinate in the authoring canvas."""

    y: float
    """Vertical coordinate in the authoring canvas."""


class ConversationFlowNodeFlowNode(BaseModel):
    """One step in a conversation flow, as returned by the API."""

    id: str
    """Caller-supplied unique identifier for this node within the flow."""

    instructions: str
    """Prompt that drives the LLM while this node is active. Required."""

    external_llm: Optional[ConversationFlowNodeFlowNodeExternalLlm] = None
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

    position: Optional[ConversationFlowNodeFlowNodePosition] = None
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


class ConversationFlowNodeToolNodePosition(BaseModel):
    """Optional canvas coordinates used by authoring UIs to lay out the graph.

    Ignored by the runtime; round-trips so frontends can persist graph layout across reloads.
    """

    x: float
    """Horizontal coordinate in the authoring canvas."""

    y: float
    """Vertical coordinate in the authoring canvas."""


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

    position: Optional[ConversationFlowNodeToolNodePosition] = None
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


class ConversationFlowNodeSpeakNodePosition(BaseModel):
    """Optional canvas coordinates used by authoring UIs to lay out the graph.

    Ignored by the runtime; round-trips so frontends can persist graph layout across reloads.
    """

    x: float
    """Horizontal coordinate in the authoring canvas."""

    y: float
    """Vertical coordinate in the authoring canvas."""


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

    position: Optional[ConversationFlowNodeSpeakNodePosition] = None
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


class ConversationFlowEdgeConditionLlmCondition(BaseModel):
    """Edge condition evaluated by the LLM from a natural-language prompt.

    The model is asked to judge the prompt against conversation context and
    returns true/false. Use this for fuzzy intents that aren't expressible as
    a deterministic expression (e.g. 'user wants to escalate to a human').
    """

    prompt: str
    """Natural-language criterion the LLM judges as true/false."""

    type: Literal["llm"]


class ConversationFlowEdgeConditionExpressionConditionExpressionDynamicVariableExpression(BaseModel):
    """Reference a dynamic variable by name.

    Resolved at runtime from the assistant's dynamic-variables context (see
    `Assistant.dynamic_variables` and the dynamic-variables webhook).
    """

    name: str
    """Variable name to look up in the runtime context."""

    type: Literal["variable"]


class ConversationFlowEdgeConditionExpressionConditionExpressionStringLiteralExpression(BaseModel):
    """Constant string value."""

    type: Literal["string_literal"]

    value: str
    """Literal string value."""


class ConversationFlowEdgeConditionExpressionConditionExpressionNumberLiteralExpression(BaseModel):
    """Constant numeric value (float; integers are accepted and stored as float)."""

    type: Literal["number_literal"]

    value: float
    """Literal numeric value."""


class ConversationFlowEdgeConditionExpressionConditionExpressionBooleanLiteralExpression(BaseModel):
    """Constant boolean value. Useful for unconditional ('always') edges."""

    type: Literal["bool_literal"]

    value: bool
    """Literal boolean value."""


ConversationFlowEdgeConditionExpressionConditionExpression: TypeAlias = Union[
    ConversationFlowEdgeConditionExpressionConditionExpressionDynamicVariableExpression,
    ConversationFlowEdgeConditionExpressionConditionExpressionStringLiteralExpression,
    ConversationFlowEdgeConditionExpressionConditionExpressionNumberLiteralExpression,
    ConversationFlowEdgeConditionExpressionConditionExpressionBooleanLiteralExpression,
    object,
]


class ConversationFlowEdgeConditionExpressionCondition(BaseModel):
    """Edge condition evaluated as a deterministic expression AST.

    The expression is computed against runtime dynamic variables and must
    evaluate to a boolean. Prefer this over `LLMCondition` when the rule is
    a clean function of known variables — it's cheaper and predictable.
    """

    expression: ConversationFlowEdgeConditionExpressionConditionExpression
    """A node in a deterministic expression AST.

    Exactly one variant is selected by the `type` discriminator. Terminal variants
    (`number_literal`, `string_literal`, `bool_literal`, `variable`) bottom out the
    recursion; `arithmetic`, `bool_op`, and `comparison` nest further
    sub-expressions.

    Extracted into a single named schema so the recursive union is defined once (was
    previously inlined at every operand site).
    """

    type: Literal["expression"]


class ConversationFlowEdgeConditionDefaultCondition(BaseModel):
    """Fallback edge condition: fires only when no other edge's condition is true.

    Evaluated after every conditioned (`llm` / `expression`) edge regardless
    of declaration order, so it routes the flow whenever none of the node's
    other outgoing edges match. Valid **only** on edges leaving a `tool` or
    `speak` node, where the deterministic step auto-advances and must always
    have somewhere to go. A tool/speak node with any outgoing edge is required
    to carry exactly one `default` edge so it never dead-ends; a tool/speak
    node with no outgoing edges is a valid terminal step. Carries no parameters.
    """

    type: Literal["default"]


ConversationFlowEdgeCondition: TypeAlias = Annotated[
    Union[
        ConversationFlowEdgeConditionLlmCondition,
        ConversationFlowEdgeConditionExpressionCondition,
        ConversationFlowEdgeConditionDefaultCondition,
    ],
    PropertyInfo(discriminator="type"),
]


class ConversationFlowEdgeTargetNodeTarget(BaseModel):
    """Edge target referencing another node within the same flow.

    The runtime transitions the active node to `node_id` and continues
    processing within the current assistant's flow.
    """

    node_id: str
    """ID of the node this edge transitions into."""

    type: Literal["node"]


class ConversationFlowEdgeTargetAssistantTargetPosition(BaseModel):
    """
    Optional canvas coordinates for rendering the target assistant as a node in authoring UIs. Pure presentation — the runtime ignores it; round-trips so frontends can persist graph layout across reloads. When multiple edges target the same assistant, each edge's `position` is independent (frontends typically use the first non-null one).
    """

    x: float
    """Horizontal coordinate in the authoring canvas."""

    y: float
    """Vertical coordinate in the authoring canvas."""


class ConversationFlowEdgeTargetAssistantTarget(BaseModel):
    """Edge target referencing a different assistant.

    When the edge fires, the conversation hands off to `assistant_id`: the
    active assistant on the conversation row is rewritten and the new
    assistant's flow starts at its own `start_node_id`. The current turn's
    LLM response is delivered to the user as-is; subsequent turns route
    to the new assistant.
    """

    assistant_id: str
    """ID of the assistant the conversation transitions to."""

    type: Literal["assistant"]

    position: Optional[ConversationFlowEdgeTargetAssistantTargetPosition] = None
    """
    Optional canvas coordinates for rendering the target assistant as a node in
    authoring UIs. Pure presentation — the runtime ignores it; round-trips so
    frontends can persist graph layout across reloads. When multiple edges target
    the same assistant, each edge's `position` is independent (frontends typically
    use the first non-null one).
    """

    voice_mode: Optional[Literal["unified", "distinct"]] = None
    """
    Voice behavior when handing off to the target assistant, mirroring the handoff
    tool's `voice_mode`. `unified` (default) keeps the current voice across the
    handoff; `distinct` lets the target assistant speak with its own configured
    voice. Only applies to assistant targets — node targets override voice via the
    node's own `voice_settings`.
    """


ConversationFlowEdgeTarget: TypeAlias = Annotated[
    Union[ConversationFlowEdgeTargetNodeTarget, ConversationFlowEdgeTargetAssistantTarget],
    PropertyInfo(discriminator="type"),
]


class ConversationFlowEdge(BaseModel):
    """Directed transition from one node to a target, gated by a condition.

    The target is either another node in the same flow (`NodeTarget`) or a
    different assistant (`AssistantTarget`). Multiple edges may share a
    `start_node_id`; the runtime evaluates them in the order they're
    declared and takes the first whose condition is true.
    """

    id: str
    """Caller-supplied unique identifier for this edge within the flow."""

    condition: ConversationFlowEdgeCondition
    """Condition that gates the transition.

    Discriminated by `type`: `llm`, `expression`.
    """

    start_node_id: str
    """ID of the node this edge transitions away from."""

    target: ConversationFlowEdgeTarget
    """Destination of the transition.

    Discriminated by `type`: `node` (jump to another node in this flow) or
    `assistant` (hand off to a different assistant).
    """


class ConversationFlow(BaseModel):
    """Conversation flow as returned by the API."""

    nodes: List[ConversationFlowNode]
    """All nodes in the flow."""

    start_node_id: str
    """ID of the node where the conversation begins."""

    edges: Optional[List[ConversationFlowEdge]] = None
    """Directed transitions between nodes."""


class ExternalLlm(BaseModel):
    base_url: str
    """Base URL for the external LLM endpoint."""

    model: str
    """Model identifier to use with the external LLM endpoint."""

    authentication_method: Optional[Literal["token", "certificate"]] = None
    """Authentication method used when connecting to the external LLM endpoint."""

    certificate_ref: Optional[str] = None
    """
    Integration secret identifier for the client certificate used with certificate
    authentication.
    """

    forward_metadata: Optional[bool] = None
    """
    When `true`, Telnyx forwards the assistant's dynamic variables to the external
    LLM endpoint as a top-level `extra_metadata` object on the chat completion
    request body. Defaults to `false`. Example payload sent to the external
    endpoint:
    `{"extra_metadata": {"customer_name": "Jane", "account_id": "acct_789", "telnyx_agent_target": "+13125550100", "telnyx_end_user_target": "+13125550123"}}`.
    Distinct from OpenAI's native `metadata` field, which has its own size and type
    limits.
    """

    llm_api_key_ref: Optional[str] = None
    """Integration secret identifier for the external LLM API key."""

    token_retrieval_url: Optional[str] = None
    """
    URL used to retrieve an access token when certificate authentication is enabled.
    """


class FallbackConfigExternalLlm(BaseModel):
    base_url: str
    """Base URL for the external LLM endpoint."""

    model: str
    """Model identifier to use with the external LLM endpoint."""

    authentication_method: Optional[Literal["token", "certificate"]] = None
    """Authentication method used when connecting to the external LLM endpoint."""

    certificate_ref: Optional[str] = None
    """
    Integration secret identifier for the client certificate used with certificate
    authentication.
    """

    forward_metadata: Optional[bool] = None
    """
    When `true`, Telnyx forwards the assistant's dynamic variables to the external
    LLM endpoint as a top-level `extra_metadata` object on the chat completion
    request body. Defaults to `false`. Example payload sent to the external
    endpoint:
    `{"extra_metadata": {"customer_name": "Jane", "account_id": "acct_789", "telnyx_agent_target": "+13125550100", "telnyx_end_user_target": "+13125550123"}}`.
    Distinct from OpenAI's native `metadata` field, which has its own size and type
    limits.
    """

    llm_api_key_ref: Optional[str] = None
    """Integration secret identifier for the external LLM API key."""

    token_retrieval_url: Optional[str] = None
    """
    URL used to retrieve an access token when certificate authentication is enabled.
    """


class FallbackConfig(BaseModel):
    external_llm: Optional[FallbackConfigExternalLlm] = None

    llm_api_key_ref: Optional[str] = None
    """Integration secret identifier for the fallback model API key."""

    model: Optional[str] = None
    """
    Fallback Telnyx-hosted model to use when the primary LLM provider is
    unavailable.
    """


class Integration(BaseModel):
    """Reference to a connected integration attached to an assistant.

    Discover available integrations with `/ai/integrations` and connected integrations with `/ai/integrations/connections`.
    """

    integration_id: str
    """Catalog integration ID to attach.

    This is the `id` from the integrations catalog at `/ai/integrations` (the same
    value also appears as `integration_id` on entries returned by
    `/ai/integrations/connections`). It is **not** the connection-level `id` from
    `/ai/integrations/connections`.
    """

    allowed_list: Optional[List[str]] = None
    """Optional per-assistant allowlist of integration tool names.

    When omitted or empty, all tools allowed by the connected integration are
    available to the assistant.
    """


class InterruptionSettingsStartSpeakingPlanTranscriptionEndpointingPlan(BaseModel):
    """Endpointing thresholds used to decide when the user has finished speaking.

    Applies to non turn-taking transcription models. For `deepgram/flux`, use `transcription.settings.eot_threshold` / `eot_timeout_ms` / `eager_eot_threshold`.
    """

    on_no_punctuation_seconds: Optional[float] = None
    """Seconds to wait after the transcript ends without punctuation."""

    on_number_seconds: Optional[float] = None
    """Seconds to wait after the transcript ends with a number."""

    on_punctuation_seconds: Optional[float] = None
    """Seconds to wait after the transcript ends with punctuation."""


class InterruptionSettingsStartSpeakingPlan(BaseModel):
    """Controls when the assistant starts speaking after the user stops.

    These thresholds primarily apply to non turn-taking transcription models. For turn-taking models like `deepgram/flux`, end-of-turn detection is driven by the transcription end-of-turn settings under `transcription.settings` instead.
    """

    transcription_endpointing_plan: Optional[InterruptionSettingsStartSpeakingPlanTranscriptionEndpointingPlan] = None
    """Endpointing thresholds used to decide when the user has finished speaking.

    Applies to non turn-taking transcription models. For `deepgram/flux`, use
    `transcription.settings.eot_threshold` / `eot_timeout_ms` /
    `eager_eot_threshold`.
    """

    wait_seconds: Optional[float] = None
    """Minimum seconds to wait before the assistant starts speaking."""


class InterruptionSettings(BaseModel):
    """
    Settings for interruptions and how the assistant decides the user has finished speaking. These timings are most relevant when using non turn-taking transcription models. For turn-taking models like `deepgram/flux`, end-of-turn behavior is controlled by the transcription end-of-turn settings under `transcription.settings` (`eot_threshold`, `eot_timeout_ms`, `eager_eot_threshold`).
    """

    disable_greeting_interruption: Optional[bool] = None
    """When true, disables user interruptions while the assistant greeting is playing."""

    enable: Optional[bool] = None
    """Whether users can interrupt the assistant while it is speaking."""

    start_speaking_plan: Optional[InterruptionSettingsStartSpeakingPlan] = None
    """Controls when the assistant starts speaking after the user stops.

    These thresholds primarily apply to non turn-taking transcription models. For
    turn-taking models like `deepgram/flux`, end-of-turn detection is driven by the
    transcription end-of-turn settings under `transcription.settings` instead.
    """


class McpServer(BaseModel):
    """Reference to an MCP server attached to an assistant.

    Create and manage MCP servers with the `/ai/mcp_servers` endpoints, then attach them to assistants by ID.
    """

    id: str
    """ID of the MCP server to attach.

    This must be the `id` of an MCP server returned by the `/ai/mcp_servers`
    endpoints.
    """

    allowed_tools: Optional[List[str]] = None
    """Optional per-assistant allowlist of MCP tool names.

    When omitted, the assistant uses the MCP server's configured `allowed_tools`.
    """


class PostConversationSettings(BaseModel):
    """Configuration for post-conversation processing.

    When enabled, the assistant receives one additional LLM turn after the conversation ends, allowing it to execute tool calls such as logging to a CRM or sending a summary. The assistant can execute multiple parallel or sequential tools during this phase. Telephony-control tools (e.g. hangup, transfer) are unavailable post-conversation. Beta feature.
    """

    enabled: Optional[bool] = None
    """Whether post-conversation processing is enabled.

    When true, the assistant will be invoked after the conversation ends to perform
    any final tool calls. Defaults to false.
    """


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

    integrations: Optional[List[Integration]] = None
    """Connected integrations attached to the assistant.

    The catalog of available integrations is at `/ai/integrations`; the user's
    connected integrations are at `/ai/integrations/connections`. Each item
    references a catalog integration by `integration_id`.
    """

    interruption_settings: Optional[InterruptionSettings] = None
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

    mcp_servers: Optional[List[McpServer]] = None
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

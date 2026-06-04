# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ...._types import SequenceNotStr
from ..enabled_features import EnabledFeatures
from ..assistant_tool_param import AssistantToolParam
from ..voice_settings_param import VoiceSettingsParam
from ..widget_settings_param import WidgetSettingsParam
from ..external_llm_req_param import ExternalLlmReqParam
from ..insight_settings_param import InsightSettingsParam
from ..privacy_settings_param import PrivacySettingsParam
from ..observability_req_param import ObservabilityReqParam
from ..messaging_settings_param import MessagingSettingsParam
from ..telephony_settings_param import TelephonySettingsParam
from ..fallback_config_req_param import FallbackConfigReqParam
from ..assistant_mcp_server_param import AssistantMcpServerParam
from ..assistant_integration_param import AssistantIntegrationParam
from ..transcription_settings_param import TranscriptionSettingsParam
from ..post_conversation_settings_req_param import PostConversationSettingsReqParam
from ..inference_embedding_interruption_settings_param import InferenceEmbeddingInterruptionSettingsParam

__all__ = [
    "VersionUpdateParams",
    "ConversationFlow",
    "ConversationFlowNode",
    "ConversationFlowNodeFlowNodeReq",
    "ConversationFlowNodeFlowNodeReqPosition",
    "ConversationFlowNodeToolNodeReq",
    "ConversationFlowNodeToolNodeReqPosition",
    "ConversationFlowEdge",
    "ConversationFlowEdgeCondition",
    "ConversationFlowEdgeConditionLlmCondition",
    "ConversationFlowEdgeConditionExpressionCondition",
    "ConversationFlowEdgeConditionExpressionConditionExpression",
    "ConversationFlowEdgeConditionExpressionConditionExpressionDynamicVariableExpression",
    "ConversationFlowEdgeConditionExpressionConditionExpressionStringLiteralExpression",
    "ConversationFlowEdgeConditionExpressionConditionExpressionNumberLiteralExpression",
    "ConversationFlowEdgeConditionExpressionConditionExpressionBooleanLiteralExpression",
    "ConversationFlowEdgeTarget",
    "ConversationFlowEdgeTargetNodeTarget",
    "ConversationFlowEdgeTargetAssistantTarget",
    "ConversationFlowEdgeTargetAssistantTargetPosition",
]


class VersionUpdateParams(TypedDict, total=False):
    assistant_id: Required[str]

    conversation_flow: ConversationFlow
    """Conversation flow as supplied by API clients (create / update).

    A directed graph of `FlowNodeReq` connected by `FlowEdge`s. Validation enforces
    unique node/edge IDs, that `start_node_id` references a real node, and that
    every edge's endpoints reference real nodes.
    """

    description: str

    dynamic_variables: Dict[str, object]
    """Map of dynamic variables and their default values"""

    dynamic_variables_webhook_timeout_ms: int
    """Timeout in milliseconds for the dynamic variables webhook.

    Must be between 1 and 10000 ms. If the webhook does not respond within this
    timeout, the call proceeds with default values. See the
    [dynamic variables guide](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables).
    """

    dynamic_variables_webhook_url: str
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

    enabled_features: List[EnabledFeatures]

    external_llm: ExternalLlmReqParam

    fallback_config: FallbackConfigReqParam

    greeting: str
    """Text that the assistant will use to start the conversation.

    This may be templated with
    [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables).
    Use an empty string to have the assistant wait for the user to speak first. Use
    the special value `<assistant-speaks-first-with-model-generated-message>` to
    have the assistant generate the greeting based on the system instructions.
    """

    insight_settings: InsightSettingsParam

    instructions: str
    """System instructions for the assistant.

    These may be templated with
    [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)
    """

    integrations: Iterable[AssistantIntegrationParam]
    """Connected integrations attached to the assistant.

    The catalog of available integrations is at `/ai/integrations`; the user's
    connected integrations are at `/ai/integrations/connections`. Each item
    references a catalog integration by `integration_id`.
    """

    interruption_settings: InferenceEmbeddingInterruptionSettingsParam
    """
    Settings for interruptions and how the assistant decides the user has finished
    speaking. These timings are most relevant when using non turn-taking
    transcription models. For turn-taking models like `deepgram/flux`, end-of-turn
    behavior is controlled by the transcription end-of-turn settings under
    `transcription.settings` (`eot_threshold`, `eot_timeout_ms`,
    `eager_eot_threshold`).
    """

    llm_api_key_ref: str
    """
    This is only needed when using third-party inference providers selected by
    `model`. The `identifier` for an integration secret
    [/v2/integration_secrets](https://developers.telnyx.com/api-reference/integration-secrets/create-a-secret)
    that refers to your LLM provider's API key. For bring-your-own endpoint
    authentication, use `external_llm.llm_api_key_ref` instead. Warning: Free plans
    are unlikely to work with this integration.
    """

    mcp_servers: Iterable[AssistantMcpServerParam]
    """MCP servers attached to the assistant.

    Create MCP servers with `/ai/mcp_servers`, then reference them by `id` here.
    """

    messaging_settings: MessagingSettingsParam

    model: str
    """ID of the model to use when `external_llm` is not set.

    You can use the
    [Get models API](https://developers.telnyx.com/api-reference/openai-chat/get-available-models-openai-compatible)
    to see available models. If `external_llm` is provided, the assistant uses
    `external_llm` instead of this field. If neither `model` nor `external_llm` is
    provided, Telnyx applies the default model.
    """

    name: str

    observability_settings: ObservabilityReqParam

    post_conversation_settings: PostConversationSettingsReqParam
    """Configuration for post-conversation processing.

    When enabled, the assistant receives one additional LLM turn after the
    conversation ends, allowing it to execute tool calls such as logging to a CRM or
    sending a summary. The assistant can execute multiple parallel or sequential
    tools during this phase. Telephony-control tools (e.g. hangup, transfer) are
    unavailable post-conversation. Beta feature.
    """

    privacy_settings: PrivacySettingsParam

    tags: SequenceNotStr[str]
    """Tags associated with the assistant.

    Tags can also be managed with the assistant tag endpoints.
    """

    telephony_settings: TelephonySettingsParam

    tool_ids: SequenceNotStr[str]
    """IDs of shared tools to attach to the assistant.

    New integrations should prefer `tool_ids` over inline `tools`.
    """

    tools: Iterable[AssistantToolParam]
    """Deprecated for new integrations.

    Inline tool definitions available to the assistant. Prefer `tool_ids` to attach
    shared tools created with the AI Tools endpoints.
    """

    transcription: TranscriptionSettingsParam

    version_name: str
    """Human-readable name for the assistant version."""

    voice_settings: VoiceSettingsParam

    widget_settings: WidgetSettingsParam
    """Configuration settings for the assistant's web widget."""


class ConversationFlowNodeFlowNodeReqPosition(TypedDict, total=False):
    """Optional canvas coordinates used by authoring UIs to lay out the graph.

    Ignored by the runtime; round-trips so frontends can persist graph layout across reloads.
    """

    x: Required[float]
    """Horizontal coordinate in the authoring canvas."""

    y: Required[float]
    """Vertical coordinate in the authoring canvas."""


class ConversationFlowNodeFlowNodeReq(TypedDict, total=False):
    """One step in a conversation flow, as supplied by API clients.

    Each node carries the prompt, tool scope, and optional overrides for
    model/voice/transcription. Unset overrides cascade from the assistant.
    """

    id: Required[str]
    """Caller-supplied unique identifier for this node within the flow."""

    instructions: Required[str]
    """Prompt that drives the LLM while this node is active. Required."""

    external_llm: ExternalLlmReqParam
    """Override for `Assistant.external_llm` while this node is active.

    Use this to route a node's turns to a different external LLM (different `model`,
    `base_url`, credentials). Part of the LLM bundle — see `model` for cascade
    semantics. Mutually exclusive with `model` on the node (a single LLM identity
    per node).
    """

    instructions_mode: Literal["replace", "append"]
    """How `instructions` combine with the assistant-level instructions.

    `replace` (default): the node's instructions are used alone. `append`: the
    node's instructions are concatenated after the assistant's instructions.
    """

    llm_api_key_ref: str
    """Override for `Assistant.llm_api_key_ref` while this node is active.

    Part of the LLM bundle — see `model` for cascade semantics.
    """

    model: str
    """Override for `Assistant.model` while this node is active.

    Part of the LLM bundle (`model` + `llm_api_key_ref` + `external_llm`): when any
    of the three is set on the node, all three are taken from the node and the
    assistant-level LLM identity is not consulted. When none of the three is set,
    the assistant's bundle cascades unchanged.
    """

    name: str
    """Optional human-readable label, displayed in authoring UIs."""

    position: ConversationFlowNodeFlowNodeReqPosition
    """Optional canvas coordinates used by authoring UIs to lay out the graph.

    Ignored by the runtime; round-trips so frontends can persist graph layout across
    reloads.
    """

    shared_tool_ids: SequenceNotStr[str]
    """IDs of shared (org-level) tools available at this node.

    Knowledge bases are attached the same way — via a shared retrieval tool. Tools
    not listed here are not callable while this node is active.
    """

    tools_mode: Literal["replace", "append"]
    """How `shared_tool_ids` combine with the assistant-level tool set.

    `replace` (default): only the node's tools are callable. `append`: the node's
    tools are added to the assistant's tools. Ignored when `shared_tool_ids` is
    null.
    """

    transcription: TranscriptionSettingsParam
    """Per-node transcription override (model/language/region).

    Unset fields cascade from the assistant-level transcription.
    """

    type: Literal["prompt"]
    """Node kind discriminator.

    `prompt` (default) is an LLM-driven step; `tool` is a standalone tool execution
    (see `ToolNodeReq`).
    """

    voice_settings: VoiceSettingsParam
    """Per-node voice override.

    Only fields set here override the assistant-level voice settings; unset fields
    cascade.
    """


class ConversationFlowNodeToolNodeReqPosition(TypedDict, total=False):
    """Optional canvas coordinates used by authoring UIs to lay out the graph.

    Ignored by the runtime; round-trips so frontends can persist graph layout across reloads.
    """

    x: Required[float]
    """Horizontal coordinate in the authoring canvas."""

    y: Required[float]
    """Vertical coordinate in the authoring canvas."""


class ConversationFlowNodeToolNodeReq(TypedDict, total=False):
    """A standalone tool step in a conversation flow, as supplied by clients.

    Unlike a prompt node, a tool node has no instructions or model — it
    isn't an LLM turn. Reaching it deterministically runs one shared tool
    (arguments filled from matching dynamic variables by name), then routes
    on the result via outgoing `tool_result` edges.
    """

    id: Required[str]
    """Caller-supplied unique identifier for this node within the flow."""

    shared_tool_id: Required[str]
    """ID of the single shared (org-level) tool this node executes.

    When the flow reaches this node the tool runs as a deliberate step (no LLM
    turn); its outgoing `tool_result` edges then route on the outcome. Arguments are
    filled from the conversation's dynamic variables by name — a dynamic variable
    whose name matches one of the tool's parameters supplies that argument.
    Cross-validated against the org's shared tools on write.
    """

    name: str
    """Optional human-readable label, displayed in authoring UIs."""

    position: ConversationFlowNodeToolNodeReqPosition
    """Optional canvas coordinates used by authoring UIs to lay out the graph.

    Ignored by the runtime; round-trips so frontends can persist graph layout across
    reloads.
    """

    type: Literal["tool"]
    """Node kind discriminator. Always `tool` for a tool node."""


ConversationFlowNode: TypeAlias = Union[ConversationFlowNodeFlowNodeReq, ConversationFlowNodeToolNodeReq]


class ConversationFlowEdgeConditionLlmCondition(TypedDict, total=False):
    """Edge condition evaluated by the LLM from a natural-language prompt.

    The model is asked to judge the prompt against conversation context and
    returns true/false. Use this for fuzzy intents that aren't expressible as
    a deterministic expression (e.g. 'user wants to escalate to a human').
    """

    prompt: Required[str]
    """Natural-language criterion the LLM judges as true/false."""

    type: Required[Literal["llm"]]


class ConversationFlowEdgeConditionExpressionConditionExpressionDynamicVariableExpression(TypedDict, total=False):
    """Reference a dynamic variable by name.

    Resolved at runtime from the assistant's dynamic-variables context (see
    `Assistant.dynamic_variables` and the dynamic-variables webhook).
    """

    name: Required[str]
    """Variable name to look up in the runtime context."""

    type: Required[Literal["variable"]]


class ConversationFlowEdgeConditionExpressionConditionExpressionStringLiteralExpression(TypedDict, total=False):
    """Constant string value."""

    type: Required[Literal["string_literal"]]

    value: Required[str]
    """Literal string value."""


class ConversationFlowEdgeConditionExpressionConditionExpressionNumberLiteralExpression(TypedDict, total=False):
    """Constant numeric value (float; integers are accepted and stored as float)."""

    type: Required[Literal["number_literal"]]

    value: Required[float]
    """Literal numeric value."""


class ConversationFlowEdgeConditionExpressionConditionExpressionBooleanLiteralExpression(TypedDict, total=False):
    """Constant boolean value. Useful for unconditional ('always') edges."""

    type: Required[Literal["bool_literal"]]

    value: Required[bool]
    """Literal boolean value."""


ConversationFlowEdgeConditionExpressionConditionExpression: TypeAlias = Union[
    ConversationFlowEdgeConditionExpressionConditionExpressionDynamicVariableExpression,
    ConversationFlowEdgeConditionExpressionConditionExpressionStringLiteralExpression,
    ConversationFlowEdgeConditionExpressionConditionExpressionNumberLiteralExpression,
    ConversationFlowEdgeConditionExpressionConditionExpressionBooleanLiteralExpression,
    object,
]


class ConversationFlowEdgeConditionExpressionCondition(TypedDict, total=False):
    """Edge condition evaluated as a deterministic expression AST.

    The expression is computed against runtime dynamic variables and must
    evaluate to a boolean. Prefer this over `LLMCondition` when the rule is
    a clean function of known variables — it's cheaper and predictable.
    """

    expression: Required[ConversationFlowEdgeConditionExpressionConditionExpression]
    """A node in a deterministic expression AST.

    Exactly one variant is selected by the `type` discriminator. Terminal variants
    (`number_literal`, `string_literal`, `bool_literal`, `variable`) bottom out the
    recursion; `arithmetic`, `bool_op`, and `comparison` nest further
    sub-expressions.

    Extracted into a single named schema so the recursive union is defined once (was
    previously inlined at every operand site).
    """

    type: Required[Literal["expression"]]


ConversationFlowEdgeCondition: TypeAlias = Union[
    ConversationFlowEdgeConditionLlmCondition, ConversationFlowEdgeConditionExpressionCondition
]


class ConversationFlowEdgeTargetNodeTarget(TypedDict, total=False):
    """Edge target referencing another node within the same flow.

    The runtime transitions the active node to `node_id` and continues
    processing within the current assistant's flow.
    """

    node_id: Required[str]
    """ID of the node this edge transitions into."""

    type: Required[Literal["node"]]


class ConversationFlowEdgeTargetAssistantTargetPosition(TypedDict, total=False):
    """
    Optional canvas coordinates for rendering the target assistant as a node in authoring UIs. Pure presentation — the runtime ignores it; round-trips so frontends can persist graph layout across reloads. When multiple edges target the same assistant, each edge's `position` is independent (frontends typically use the first non-null one).
    """

    x: Required[float]
    """Horizontal coordinate in the authoring canvas."""

    y: Required[float]
    """Vertical coordinate in the authoring canvas."""


class ConversationFlowEdgeTargetAssistantTarget(TypedDict, total=False):
    """Edge target referencing a different assistant.

    When the edge fires, the conversation hands off to `assistant_id`: the
    active assistant on the conversation row is rewritten and the new
    assistant's flow starts at its own `start_node_id`. The current turn's
    LLM response is delivered to the user as-is; subsequent turns route
    to the new assistant.
    """

    assistant_id: Required[str]
    """ID of the assistant the conversation transitions to."""

    type: Required[Literal["assistant"]]

    position: ConversationFlowEdgeTargetAssistantTargetPosition
    """
    Optional canvas coordinates for rendering the target assistant as a node in
    authoring UIs. Pure presentation — the runtime ignores it; round-trips so
    frontends can persist graph layout across reloads. When multiple edges target
    the same assistant, each edge's `position` is independent (frontends typically
    use the first non-null one).
    """

    voice_mode: Literal["unified", "distinct"]
    """
    Voice behavior when handing off to the target assistant, mirroring the handoff
    tool's `voice_mode`. `unified` (default) keeps the current voice across the
    handoff; `distinct` lets the target assistant speak with its own configured
    voice. Only applies to assistant targets — node targets override voice via the
    node's own `voice_settings`.
    """


ConversationFlowEdgeTarget: TypeAlias = Union[
    ConversationFlowEdgeTargetNodeTarget, ConversationFlowEdgeTargetAssistantTarget
]


class ConversationFlowEdge(TypedDict, total=False):
    """Directed transition from one node to a target, gated by a condition.

    The target is either another node in the same flow (`NodeTarget`) or a
    different assistant (`AssistantTarget`). Multiple edges may share a
    `start_node_id`; the runtime evaluates them in the order they're
    declared and takes the first whose condition is true.
    """

    id: Required[str]
    """Caller-supplied unique identifier for this edge within the flow."""

    condition: Required[ConversationFlowEdgeCondition]
    """Condition that gates the transition.

    Discriminated by `type`: `llm`, `expression`.
    """

    start_node_id: Required[str]
    """ID of the node this edge transitions away from."""

    target: Required[ConversationFlowEdgeTarget]
    """Destination of the transition.

    Discriminated by `type`: `node` (jump to another node in this flow) or
    `assistant` (hand off to a different assistant).
    """


class ConversationFlow(TypedDict, total=False):
    """Conversation flow as supplied by API clients (create / update).

    A directed graph of `FlowNodeReq` connected by `FlowEdge`s. Validation
    enforces unique node/edge IDs, that `start_node_id` references a real
    node, and that every edge's endpoints reference real nodes.
    """

    nodes: Required[Iterable[ConversationFlowNode]]
    """All nodes in the flow.

    Must contain `start_node_id`. Each node is a prompt node (`type: prompt`) or a
    tool node (`type: tool`).
    """

    start_node_id: Required[str]
    """ID of the node where the conversation begins."""

    edges: Iterable[ConversationFlowEdge]
    """Directed transitions between nodes. May be empty for a single-node flow."""

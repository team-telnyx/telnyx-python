# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from .flow_edge_param import FlowEdgeParam
from .node_position_param import NodePositionParam
from .voice_settings_param import VoiceSettingsParam
from .external_llm_req_param import ExternalLlmReqParam
from .transcription_settings_param import TranscriptionSettingsParam

__all__ = ["ConversationFlowReqParam", "Node", "NodeFlowNodeReq", "NodeToolNodeReq", "NodeSpeakNodeReq"]


class NodeFlowNodeReq(TypedDict, total=False):
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

    position: NodePositionParam
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


class NodeToolNodeReq(TypedDict, total=False):
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

    position: NodePositionParam
    """Optional canvas coordinates used by authoring UIs to lay out the graph.

    Ignored by the runtime; round-trips so frontends can persist graph layout across
    reloads.
    """

    type: Literal["tool"]
    """Node kind discriminator. Always `tool` for a tool node."""


class NodeSpeakNodeReq(TypedDict, total=False):
    """A standalone scripted-message step in a flow, as supplied by clients.

    Unlike a prompt node, a speak node has no instructions or model — it isn't
    an LLM turn. Reaching it delivers `message` to the user verbatim (with
    `{{variable}}` interpolation), then routes via outgoing `llm` /
    `expression` edges.
    """

    id: Required[str]
    """Caller-supplied unique identifier for this node within the flow."""

    message: Required[str]
    """Message delivered to the user verbatim when the flow reaches this node.

    No LLM turn — the text is spoken/sent exactly as written. `{{variable}}`
    placeholders are interpolated from the conversation's dynamic variables; an
    unresolved placeholder renders as an empty string. After delivering, the flow
    routes via the node's outgoing `llm` / `expression` edges (commonly a single
    unconditional edge).
    """

    name: str
    """Optional human-readable label, displayed in authoring UIs."""

    position: NodePositionParam
    """Optional canvas coordinates used by authoring UIs to lay out the graph.

    Ignored by the runtime; round-trips so frontends can persist graph layout across
    reloads.
    """

    type: Literal["speak"]
    """Node kind discriminator. Always `speak` for a speak node."""


Node: TypeAlias = Union[NodeFlowNodeReq, NodeToolNodeReq, NodeSpeakNodeReq]


class ConversationFlowReqParam(TypedDict, total=False):
    """Conversation flow as supplied by API clients (create / update).

    A directed graph of `FlowNodeReq` connected by `FlowEdge`s. Validation
    enforces unique node/edge IDs, that `start_node_id` references a real
    node, and that every edge's endpoints reference real nodes.
    """

    nodes: Required[Iterable[Node]]
    """All nodes in the flow.

    Must contain `start_node_id`. Each node is a prompt node (`type: prompt`) or a
    tool node (`type: tool`).
    """

    start_node_id: Required[str]
    """ID of the node where the conversation begins."""

    edges: Iterable[FlowEdgeParam]
    """Directed transitions between nodes. May be empty for a single-node flow."""

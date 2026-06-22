# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .node_position_param import NodePositionParam

__all__ = [
    "FlowEdgeParam",
    "Condition",
    "ConditionLlmCondition",
    "ConditionExpressionCondition",
    "ConditionDefaultCondition",
    "Target",
    "TargetNodeTarget",
    "TargetAssistantTarget",
]


class ConditionLlmCondition(TypedDict, total=False):
    """Edge condition evaluated by the LLM from a natural-language prompt.

    The model is asked to judge the prompt against conversation context and
    returns true/false. Use this for fuzzy intents that aren't expressible as
    a deterministic expression (e.g. 'user wants to escalate to a human').
    """

    prompt: Required[str]
    """Natural-language criterion the LLM judges as true/false."""

    type: Required[Literal["llm"]]


class ConditionExpressionCondition(TypedDict, total=False):
    """Edge condition evaluated as a deterministic expression AST.

    The expression is computed against runtime dynamic variables and must
    evaluate to a boolean. Prefer this over `LLMCondition` when the rule is
    a clean function of known variables — it's cheaper and predictable.
    """

    expression: Required[object]
    """Root of the expression AST; evaluates to a boolean.

    Typed as free-form JSON to avoid an uncompilable by-value self-reference; see
    the Expression schema for the variant structure.
    """

    type: Required[Literal["expression"]]


class ConditionDefaultCondition(TypedDict, total=False):
    """Fallback edge condition: fires only when no other edge's condition is true.

    Evaluated after every conditioned (`llm` / `expression`) edge regardless
    of declaration order, so it routes the flow whenever none of the node's
    other outgoing edges match. Valid **only** on edges leaving a `tool` or
    `speak` node, where the deterministic step auto-advances and must always
    have somewhere to go. A tool/speak node with any outgoing edge is required
    to carry exactly one `default` edge so it never dead-ends; a tool/speak
    node with no outgoing edges is a valid terminal step. Carries no parameters.
    """

    type: Required[Literal["default"]]


Condition: TypeAlias = Union[ConditionLlmCondition, ConditionExpressionCondition, ConditionDefaultCondition]


class TargetNodeTarget(TypedDict, total=False):
    """Edge target referencing another node within the same flow.

    The runtime transitions the active node to `node_id` and continues
    processing within the current assistant's flow.
    """

    node_id: Required[str]
    """ID of the node this edge transitions into."""

    type: Required[Literal["node"]]


class TargetAssistantTarget(TypedDict, total=False):
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

    position: NodePositionParam
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


Target: TypeAlias = Union[TargetNodeTarget, TargetAssistantTarget]


class FlowEdgeParam(TypedDict, total=False):
    """Directed transition from one node to a target, gated by a condition.

    The target is either another node in the same flow (`NodeTarget`) or a
    different assistant (`AssistantTarget`). Multiple edges may share a
    `start_node_id`; the runtime evaluates them in the order they're
    declared and takes the first whose condition is true.
    """

    id: Required[str]
    """Caller-supplied unique identifier for this edge within the flow."""

    condition: Required[Condition]
    """Condition that gates the transition.

    Discriminated by `type`: `llm`, `expression`.
    """

    start_node_id: Required[str]
    """ID of the node this edge transitions away from."""

    target: Required[Target]
    """Destination of the transition.

    Discriminated by `type`: `node` (jump to another node in this flow) or
    `assistant` (hand off to a different assistant).
    """

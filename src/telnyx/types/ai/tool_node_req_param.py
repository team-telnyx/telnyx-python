# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .node_position_param import NodePositionParam

__all__ = ["ToolNodeReqParam"]


class ToolNodeReqParam(TypedDict, total=False):
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

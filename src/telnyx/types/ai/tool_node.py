# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .node_position import NodePosition
from .assistant_tool import AssistantTool

__all__ = ["ToolNode"]


class ToolNode(BaseModel):
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

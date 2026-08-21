# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .flow_edge import FlowEdge
from .flow_node import FlowNode
from .tool_node import ToolNode
from .speak_node import SpeakNode

__all__ = ["ConversationFlow", "Node"]

Node: TypeAlias = Annotated[Union[FlowNode, ToolNode, SpeakNode], PropertyInfo(discriminator="type")]


class ConversationFlow(BaseModel):
    """Conversation flow as returned by the API."""

    nodes: List[Node]
    """All nodes in the flow."""

    start_node_id: str
    """ID of the node where the conversation begins."""

    edges: Optional[List[FlowEdge]] = None
    """Directed transitions between nodes."""

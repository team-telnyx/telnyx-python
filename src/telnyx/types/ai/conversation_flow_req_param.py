# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from .flow_edge_param import FlowEdgeParam
from .flow_node_req_param import FlowNodeReqParam
from .tool_node_req_param import ToolNodeReqParam
from .speak_node_req_param import SpeakNodeReqParam

__all__ = ["ConversationFlowReqParam", "Node"]

Node: TypeAlias = Union[FlowNodeReqParam, ToolNodeReqParam, SpeakNodeReqParam]


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

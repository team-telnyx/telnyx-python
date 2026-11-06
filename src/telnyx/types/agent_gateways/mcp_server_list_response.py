# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from ..._models import BaseModel
from .agent_gateway_mcp_server import AgentGatewayMcpServer

__all__ = ["McpServerListResponse"]


class McpServerListResponse(BaseModel):
    data: List[AgentGatewayMcpServer]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._models import BaseModel
from .agent_gateway_mcp_server import AgentGatewayMcpServer

__all__ = ["AgentGatewayMcpServerResponse"]


class AgentGatewayMcpServerResponse(BaseModel):
    data: AgentGatewayMcpServer

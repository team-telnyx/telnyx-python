# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._models import BaseModel
from .agent_gateway_tool_permissions import AgentGatewayToolPermissions

__all__ = ["AgentGatewayToolPermissionsResponse"]


class AgentGatewayToolPermissionsResponse(BaseModel):
    data: AgentGatewayToolPermissions

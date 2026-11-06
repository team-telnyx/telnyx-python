# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .tool_permission_create_params import ToolPermissionCreateParams as ToolPermissionCreateParams

if TYPE_CHECKING:
    from .agent_gateway_tool_permissions import AgentGatewayToolPermissions as AgentGatewayToolPermissions
    from .agent_gateway_tool_permissions_response import (
        AgentGatewayToolPermissionsResponse as AgentGatewayToolPermissionsResponse,
    )


def __getattr__(name: str) -> Any:
    if name == "AgentGatewayToolPermissions":
        from .agent_gateway_tool_permissions import AgentGatewayToolPermissions

        return AgentGatewayToolPermissions
    if name == "AgentGatewayToolPermissionsResponse":
        from .agent_gateway_tool_permissions_response import AgentGatewayToolPermissionsResponse

        return AgentGatewayToolPermissionsResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

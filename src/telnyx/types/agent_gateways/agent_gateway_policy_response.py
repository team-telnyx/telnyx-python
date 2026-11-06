# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._models import BaseModel
from .agent_gateway_policy import AgentGatewayPolicy

__all__ = ["AgentGatewayPolicyResponse"]


class AgentGatewayPolicyResponse(BaseModel):
    data: AgentGatewayPolicy
    """A named set of guardrails."""

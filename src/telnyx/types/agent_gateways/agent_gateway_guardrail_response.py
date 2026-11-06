# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._models import BaseModel
from .agent_gateway_guardrail import AgentGatewayGuardrail

__all__ = ["AgentGatewayGuardrailResponse"]


class AgentGatewayGuardrailResponse(BaseModel):
    data: AgentGatewayGuardrail

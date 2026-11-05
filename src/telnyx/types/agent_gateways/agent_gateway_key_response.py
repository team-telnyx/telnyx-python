# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._models import BaseModel
from .agent_gateway_key import AgentGatewayKey

__all__ = ["AgentGatewayKeyResponse"]


class AgentGatewayKeyResponse(BaseModel):
    data: AgentGatewayKey
    """A key on an instance, without its value."""

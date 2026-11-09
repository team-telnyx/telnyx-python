# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .._models import BaseModel
from .agent_gateway import AgentGateway

__all__ = ["AgentGatewayResponse"]


class AgentGatewayResponse(BaseModel):
    data: AgentGateway
    """An Agent Gateway instance on a WireGuard Interface."""

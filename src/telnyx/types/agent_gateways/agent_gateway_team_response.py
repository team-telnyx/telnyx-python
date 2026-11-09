# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._models import BaseModel
from .agent_gateway_team import AgentGatewayTeam

__all__ = ["AgentGatewayTeamResponse"]


class AgentGatewayTeamResponse(BaseModel):
    data: AgentGatewayTeam
    """
    A team on an instance: a model list, a budget, and rate limits that its keys
    share.
    """

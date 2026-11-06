# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel
from .agent_gateway_policy_step import AgentGatewayPolicyStep

__all__ = ["AgentGatewayPolicyPipeline"]


class AgentGatewayPolicyPipeline(BaseModel):
    """
    Ordered steps that run in place of the policy's guardrails running independently.
    """

    hook: Literal["before_request", "after_request"]
    """
    `before_request` runs the steps on the request, and `after_request` on the
    model's response.
    """

    steps: List[AgentGatewayPolicyStep]

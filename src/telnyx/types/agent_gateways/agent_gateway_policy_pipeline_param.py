# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AgentGatewayPolicyPipelineParam"]


class AgentGatewayPolicyPipelineParam(TypedDict, total=False):
    """
    Ordered steps that run in place of the policy's guardrails running independently.
    """

    hook: Required[Literal["before_request", "after_request"]]
    """
    `before_request` runs the steps on the request, and `after_request` on the
    model's response.
    """

    steps: Required[Iterable["AgentGatewayPolicyStepParam"]]


from .agent_gateway_policy_step_param import AgentGatewayPolicyStepParam

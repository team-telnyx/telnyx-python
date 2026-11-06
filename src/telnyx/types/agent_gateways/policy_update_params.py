# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["PolicyUpdateParams"]


class PolicyUpdateParams(TypedDict, total=False):
    instance_id: Required[str]

    base: Optional[str]
    """A policy this one builds on, by name.

    The policy starts with the base's guardrails.
    """

    description: Optional[str]
    """What the policy is for."""

    guardrails: "AgentGatewayPolicyGuardrailsParam"
    """
    The guardrails a policy adds to its base's, and the ones it removes from them,
    by name.
    """

    model: Optional[str]
    """A condition on the model, by name or regular expression.

    The policy's guardrails run only on requests for a matching model. `null`
    matches every model.
    """

    pipeline: Optional["AgentGatewayPolicyPipelineParam"]
    """
    Ordered steps that run in place of the policy's guardrails running
    independently.
    """


from .agent_gateway_policy_pipeline_param import AgentGatewayPolicyPipelineParam
from .agent_gateway_policy_guardrails_param import AgentGatewayPolicyGuardrailsParam

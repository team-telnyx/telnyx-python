# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from .agent_gateway_policy_pipeline import AgentGatewayPolicyPipeline
from .agent_gateway_policy_guardrails import AgentGatewayPolicyGuardrails

__all__ = ["AgentGatewayPolicy"]


class AgentGatewayPolicy(BaseModel):
    """A named set of guardrails."""

    base: Optional[str] = None
    """A policy this one builds on, by name.

    The policy starts with the base's guardrails.
    """

    created_at: Optional[datetime] = None
    """When the policy's current version was created. An update creates a new version."""

    description: Optional[str] = None
    """What the policy is for."""

    guardrails: AgentGatewayPolicyGuardrails
    """
    The guardrails a policy adds to its base's, and the ones it removes from them,
    by name.
    """

    model: Optional[str] = None
    """A condition on the model, by name or regular expression.

    The policy's guardrails run only on requests for a matching model. `null`
    matches every model.
    """

    name: str
    """A name, unique on the instance.

    A request names the policy in its `policies` field.
    """

    pipeline: Optional[AgentGatewayPolicyPipeline] = None
    """
    Ordered steps that run in place of the policy's guardrails running
    independently.
    """

    updated_at: Optional[datetime] = None
    """When the policy last changed."""

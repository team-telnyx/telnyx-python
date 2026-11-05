# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._models import BaseModel
from .agent_gateway_policy_attachment import AgentGatewayPolicyAttachment

__all__ = ["AgentGatewayPolicyAttachmentResponse"]


class AgentGatewayPolicyAttachmentResponse(BaseModel):
    data: AgentGatewayPolicyAttachment
    """Where an instance applies a policy."""

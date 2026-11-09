# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["AgentGatewayPolicyGuardrails"]


class AgentGatewayPolicyGuardrails(BaseModel):
    """
    The guardrails a policy adds to its base's, and the ones it removes from them, by name.
    """

    add: Optional[List[str]] = None
    """Guardrails the policy runs in addition to its base's."""

    remove: Optional[List[str]] = None
    """Guardrails from its base that the policy does not run."""

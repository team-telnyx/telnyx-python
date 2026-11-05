# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["AgentGatewayPolicyGuardrailsParam"]


class AgentGatewayPolicyGuardrailsParam(TypedDict, total=False):
    """
    The guardrails a policy adds to its base's, and the ones it removes from them, by name.
    """

    add: SequenceNotStr[str]
    """Guardrails the policy runs in addition to its base's."""

    remove: SequenceNotStr[str]
    """Guardrails from its base that the policy does not run."""

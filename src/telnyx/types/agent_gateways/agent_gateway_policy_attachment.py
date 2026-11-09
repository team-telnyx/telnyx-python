# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["AgentGatewayPolicyAttachment"]


class AgentGatewayPolicyAttachment(BaseModel):
    """Where an instance applies a policy."""

    id: str
    """The attachment's ID."""

    created_at: Optional[datetime] = None
    """When the attachment was created."""

    default: bool
    """`true` applies the policy only to the requests no other attachment matches."""

    models: List[str]
    """The models whose requests the policy applies to, by name.

    A name can use `*` as a wildcard. Empty applies the policy to every request.
    """

    policy: str
    """The policy to apply, by name."""

    priority: Optional[int] = None
    """An attachment with a priority applies before the others."""

    updated_at: Optional[datetime] = None
    """When the attachment last changed."""

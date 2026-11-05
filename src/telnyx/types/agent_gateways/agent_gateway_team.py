# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["AgentGatewayTeam"]


class AgentGatewayTeam(BaseModel):
    """
    A team on an instance: a model list, a budget, and rate limits that its keys share.
    """

    id: str
    """Identifies the team."""

    blocked: bool
    """Whether the instance refuses every key in the team."""

    budget_resets_at: Optional[datetime] = None
    """When the team's spend next resets."""

    budget_resets_every: Optional[str] = None
    """How often the team's spend resets, such as `30d`."""

    created_at: Optional[datetime] = None
    """When the team was created."""

    max_budget: Optional[float] = None
    """The most the team's keys may spend together, in USD, until the budget resets."""

    models: List[str]
    """The models the team's keys may use.

    Empty means every model the instance serves.
    """

    name: Optional[str] = None
    """A label for people. Names need not be unique."""

    requests_per_minute: Optional[int] = None
    """The most requests the team's keys may make per minute, together."""

    spend: float
    """What the team's keys have spent since the budget last reset, in USD."""

    tokens_per_minute: Optional[int] = None
    """The most tokens the team's keys may use per minute, together."""

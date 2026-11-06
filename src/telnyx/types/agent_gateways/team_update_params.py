# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["TeamUpdateParams"]


class TeamUpdateParams(TypedDict, total=False):
    instance_id: Required[str]

    blocked: bool
    """
    `true` makes the instance refuse every key in the team; `false` lets them
    through again.
    """

    budget_resets_every: Optional[str]
    """How often the spend resets."""

    max_budget: Optional[float]
    """The most the team's keys may spend together, in USD."""

    models: SequenceNotStr[str]
    """The models the team's keys may use. `[]` allows every model."""

    name: str
    """A label for people."""

    requests_per_minute: Optional[int]
    """The most requests the team's keys may make per minute, together."""

    tokens_per_minute: Optional[int]
    """The most tokens the team's keys may use per minute, together."""

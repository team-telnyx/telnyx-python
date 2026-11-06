# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["TeamCreateParams"]


class TeamCreateParams(TypedDict, total=False):
    name: Required[str]
    """A label for people."""

    budget_resets_every: Optional[str]
    """How often the spend resets: a number and a unit, `s`, `m`, `h`, or `d`."""

    max_budget: Optional[float]
    """The most the team's keys may spend together, in USD."""

    models: Optional[SequenceNotStr[str]]
    """The models the team's keys may use. Leave it out to allow every model."""

    requests_per_minute: Optional[int]
    """The most requests the team's keys may make per minute, together."""

    tokens_per_minute: Optional[int]
    """The most tokens the team's keys may use per minute, together."""

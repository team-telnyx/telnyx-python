# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["KeyCreateParams"]


class KeyCreateParams(TypedDict, total=False):
    budget_resets_every: Optional[str]
    """How often the spend resets: a number and a unit, `s`, `m`, `h`, or `d`."""

    expires_in: Optional[str]
    """
    How long until the key stops working: a number and a unit, `s`, `m`, `h`, or
    `d`.
    """

    max_budget: Optional[float]
    """The most the key may spend, in USD."""

    max_parallel_requests: Optional[int]
    """The most requests the key may have in flight at once."""

    models: Optional[SequenceNotStr[str]]
    """The models the key may use. Leave it out to allow every model."""

    name: Optional[str]
    """A label for people, unique on the instance."""

    requests_per_minute: Optional[int]
    """The most requests the key may make per minute."""

    team_id: Optional[str]
    """A team on the instance.

    The key shares the team's model list, budget, and rate limits.
    """

    tokens_per_minute: Optional[int]
    """The most tokens the key may use per minute."""

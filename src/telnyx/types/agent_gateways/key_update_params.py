# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["KeyUpdateParams"]


class KeyUpdateParams(TypedDict, total=False):
    instance_id: Required[str]

    blocked: bool
    """`true` makes the instance refuse the key; `false` lets it through again."""

    budget_resets_every: Optional[str]
    """How often the spend resets."""

    expires_in: Optional[str]
    """How long from now until the key stops working."""

    max_budget: Optional[float]
    """The most the key may spend, in USD."""

    max_parallel_requests: Optional[int]
    """The most requests the key may have in flight at once."""

    models: SequenceNotStr[str]
    """The models the key may use. `[]` allows every model."""

    name: str
    """A label for people."""

    requests_per_minute: Optional[int]
    """The most requests the key may make per minute."""

    team_id: Optional[str]
    """Move the key to this team, or `null` to leave its team."""

    tokens_per_minute: Optional[int]
    """The most tokens the key may use per minute."""

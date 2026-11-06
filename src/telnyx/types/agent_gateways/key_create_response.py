# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["KeyCreateResponse", "Data"]


class Data(BaseModel):
    """A key that was just issued: the only response that carries its value."""

    id: str
    """Identifies the key.

    It is a 64-character hash the instance stores in place of the key's value.
    """

    blocked: bool
    """Whether the instance refuses the key."""

    budget_resets_at: Optional[datetime] = None
    """When the key's spend next resets."""

    budget_resets_every: Optional[str] = None
    """How often the key's spend resets, such as `30d`."""

    created_at: Optional[datetime] = None
    """When the key was issued."""

    expires_at: Optional[datetime] = None
    """When the key stops working; `null` when it does not expire."""

    key: str
    """The key's value, sent as `Authorization: Bearer <key>` to the instance.

    Shown only in this response.
    """

    max_budget: Optional[float] = None
    """The most the key may spend, in USD, until its budget resets."""

    max_parallel_requests: Optional[int] = None
    """The most requests the key may have in flight at once."""

    models: List[str]
    """The models the key may use. Empty means every model the instance serves."""

    name: Optional[str] = None
    """A label for people; `null` when none was given."""

    requests_per_minute: Optional[int] = None
    """The most requests the key may make per minute."""

    spend: float
    """What the key has spent since its budget last reset, in USD."""

    team_id: Optional[str] = None
    """The team the key belongs to, if any."""

    tokens_per_minute: Optional[int] = None
    """The most tokens the key may use per minute."""


class KeyCreateResponse(BaseModel):
    data: Data
    """A key that was just issued: the only response that carries its value."""

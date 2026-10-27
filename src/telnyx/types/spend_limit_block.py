# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from datetime import date, datetime

from .._models import BaseModel

__all__ = ["SpendLimitBlock"]


class SpendLimitBlock(BaseModel):
    """The active block of the period. `null` when the period is not blocked."""

    blocked_until: date
    """
    Exclusive end of the block: it is lifted at 00:00 UTC on this date at the
    latest.
    """

    detected_at: datetime
    """When the block started."""

    limit_usd: str
    """The limit in USD that the spend went above, as a decimal string."""

    spend_usd: str
    """Spend in USD when the block started, as a decimal string."""

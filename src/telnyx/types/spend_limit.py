# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel
from .spend_limit_period import SpendLimitPeriod

__all__ = ["SpendLimit", "Block", "Limit", "Evaluation"]


class Block(BaseModel):
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


class Limit(BaseModel):
    """The limit set on the account for the product and period, whoever set it.

    `null` when none is set.
    """

    amount: Optional[str] = None
    """Limit in USD, as a decimal string. `null` when `unlimited` is true."""

    origin: Literal["self_service", "operator"]
    """
    `self_service` when a user of the account set it, `operator` when Telnyx support
    did.
    """

    unlimited: bool
    """True when the limit was set to explicitly no cap."""

    updated_at: datetime
    """When the limit was last set or changed."""


class Evaluation(BaseModel):
    """What a create, update or delete did to the period at once.

    Only present in write responses.
    """

    blocked_now: bool
    """The change blocked the product: the spend was already above the new limit."""

    evaluation_deferred: bool
    """The spend could not be checked now.

    The change is saved and applied within a few minutes.
    """

    released: bool
    """The change lifted a block of this period."""

    spend_usd: Optional[str] = None
    """Spend in USD used for the check, as a decimal string.

    `null` when the spend was not checked.
    """

    still_blocked_other_period: bool
    """
    The other period has an active block, so the product stays blocked whatever this
    period's result.
    """

    still_over_limit: bool
    """A block of this period remains because the spend is still above the new limit."""

    note: Optional[str] = None
    """Additional information about the result, when there is any."""


class SpendLimit(BaseModel):
    """The spend limit, spend and block state of one product and period."""

    block: Optional[Block] = None
    """The active block of the period. `null` when the period is not blocked."""

    blocked: bool
    """The product is blocked for this period.

    Always `false` in write responses; list the limits to read the block state.
    """

    effective_limit_usd: Optional[str] = None
    """The limit in USD that is enforced, as a decimal string. `null` means unlimited."""

    limit: Optional[Limit] = None
    """The limit set on the account for the product and period, whoever set it.

    `null` when none is set.
    """

    period: SpendLimitPeriod
    """`daily` is the current UTC day; `monthly` is the current UTC calendar month."""

    period_end: date
    """Exclusive end of the current period, a UTC date."""

    period_start: date
    """First UTC day of the current period."""

    product: str
    """Product the entry applies to."""

    product_name: str
    """Display name of the product."""

    record_type: str
    """Identifies the type of the resource."""

    spend_error: Optional[str] = None
    """Set when `spend_usd` is `null`."""

    spend_usd: Optional[str] = None
    """Spend in USD so far in the period, as a decimal string.

    It can lag actual usage by about a minute. `null` when it could not be read.
    """

    evaluation: Optional[Evaluation] = None
    """What a create, update or delete did to the period at once.

    Only present in write responses.
    """

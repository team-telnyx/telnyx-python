# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .spend_limit_period import SpendLimitPeriod

__all__ = ["SpendLimitCreateParams", "CreateSpendLimitWithAmount", "CreateSpendLimitUnlimited"]


class CreateSpendLimitWithAmount(TypedDict, total=False):
    amount: Required[float]
    """Limit in USD. `0` blocks at the first cent of spend."""

    product: Required[str]
    """Product to limit, as returned in `product` by the list operation."""

    period: SpendLimitPeriod
    """`daily` is the current UTC day; `monthly` is the current UTC calendar month."""

    reason: str
    """Why the limit is set or changed, kept for audit."""

    unlimited: Literal[False]
    """Optional; only `false` is allowed together with `amount`."""


class CreateSpendLimitUnlimited(TypedDict, total=False):
    product: Required[str]
    """Product to limit, as returned in `product` by the list operation."""

    unlimited: Required[Literal[True]]
    """`true`: explicitly no cap."""

    period: SpendLimitPeriod
    """`daily` is the current UTC day; `monthly` is the current UTC calendar month."""

    reason: str
    """Why the limit is set or changed, kept for audit."""


SpendLimitCreateParams: TypeAlias = Union[CreateSpendLimitWithAmount, CreateSpendLimitUnlimited]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["SpendLimitUpdateParams", "UpdateSpendLimitWithAmount", "UpdateSpendLimitUnlimited"]


class UpdateSpendLimitWithAmount(TypedDict, total=False):
    amount: Required[float]
    """Limit in USD. `0` blocks at the first cent of spend."""

    credential_id: str
    """
    Identifier of one API key as recorded on usage, never the key's secret,
    percent-encoded: the request is then about that key's limit. Absent means the
    total limit; present but blank is refused.
    """

    period: "SpendLimitPeriod"
    """Limit period. Defaults to `daily`; send it explicitly."""

    reason: str
    """Why the limit is set or changed, kept for audit."""

    unlimited: Literal[False]
    """Optional; only `false` is allowed together with `amount`."""


class UpdateSpendLimitUnlimited(TypedDict, total=False):
    unlimited: Required[Literal[True]]
    """`true`: explicitly no cap."""

    credential_id: str
    """
    Identifier of one API key as recorded on usage, never the key's secret,
    percent-encoded: the request is then about that key's limit. Absent means the
    total limit; present but blank is refused.
    """

    period: "SpendLimitPeriod"
    """Limit period. Defaults to `daily`; send it explicitly."""

    reason: str
    """Why the limit is set or changed, kept for audit."""


SpendLimitUpdateParams: TypeAlias = Union[UpdateSpendLimitWithAmount, UpdateSpendLimitUnlimited]

from .spend_limit_period import SpendLimitPeriod

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .spend_limit_period import SpendLimitPeriod

__all__ = ["SpendLimitDeleteParams"]


class SpendLimitDeleteParams(TypedDict, total=False):
    period: SpendLimitPeriod
    """Limit period. Defaults to `daily`; send it explicitly."""

    reason: str
    """Why the limit is removed, kept for audit. At most 500 characters."""

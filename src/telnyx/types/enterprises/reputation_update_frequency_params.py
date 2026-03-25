# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ReputationUpdateFrequencyParams"]


class ReputationUpdateFrequencyParams(TypedDict, total=False):
    check_frequency: Required[Literal["business_daily", "daily", "weekly", "biweekly", "monthly", "never"]]
    """New frequency for refreshing reputation data"""

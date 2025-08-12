# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SimCardDataUsageNotificationUpdateParams", "Threshold"]


class SimCardDataUsageNotificationUpdateParams(TypedDict, total=False):
    sim_card_id: str
    """The identification UUID of the related SIM card resource."""

    threshold: Threshold
    """Data usage threshold that will trigger the notification."""


class Threshold(TypedDict, total=False):
    amount: str

    unit: Literal["MB", "GB"]

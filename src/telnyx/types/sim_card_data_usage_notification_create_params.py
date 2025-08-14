# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SimCardDataUsageNotificationCreateParams", "Threshold"]


class SimCardDataUsageNotificationCreateParams(TypedDict, total=False):
    sim_card_id: Required[str]
    """The identification UUID of the related SIM card resource."""

    threshold: Required[Threshold]
    """Data usage threshold that will trigger the notification."""


class Threshold(TypedDict, total=False):
    amount: str

    unit: Literal["MB", "GB"]

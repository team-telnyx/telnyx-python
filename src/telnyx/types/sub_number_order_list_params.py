# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SubNumberOrderListParams", "Filter"]


class SubNumberOrderListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[status], filter[order_request_id], filter[country_code],
    filter[phone_number_type], filter[phone_numbers_count]
    """


class Filter(TypedDict, total=False):
    country_code: str
    """ISO alpha-2 country code."""

    order_request_id: str
    """ID of the number order the sub number order belongs to"""

    phone_number_type: str
    """Phone Number Type"""

    phone_numbers_count: int
    """Amount of numbers in the sub number order"""

    status: str
    """Filter sub number orders by status."""

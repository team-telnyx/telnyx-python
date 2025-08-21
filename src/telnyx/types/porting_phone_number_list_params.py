# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["PortingPhoneNumberListParams", "Filter", "Page"]


class PortingPhoneNumberListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[porting_order_status]
    """

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[size], page[number]
    """


class Filter(TypedDict, total=False):
    porting_order_status: Literal[
        "draft", "in-process", "submitted", "exception", "foc-date-confirmed", "cancel-pending", "ported", "cancelled"
    ]
    """Filter results by porting order status"""


class Page(TypedDict, total=False):
    number: int
    """The page number to load"""

    size: int
    """The size of the page"""

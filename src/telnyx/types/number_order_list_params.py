# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["NumberOrderListParams", "Filter", "FilterCreatedAt", "Page"]


class NumberOrderListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[status], filter[created_at], filter[phone_numbers_count],
    filter[customer_reference], filter[requirements_met]
    """

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[size], page[number]
    """


class FilterCreatedAt(TypedDict, total=False):
    gt: str
    """Filter number orders later than this value."""

    lt: str
    """Filter number orders earlier than this value."""


class Filter(TypedDict, total=False):
    created_at: FilterCreatedAt
    """Filter number orders by date range."""

    customer_reference: str
    """Filter number orders via the customer reference set."""

    phone_numbers_count: str
    """Filter number order with this amount of numbers"""

    requirements_met: bool
    """Filter number orders by requirements met."""

    status: str
    """Filter number orders by status."""


class Page(TypedDict, total=False):
    number: int
    """The page number to load"""

    size: int
    """The size of the page"""

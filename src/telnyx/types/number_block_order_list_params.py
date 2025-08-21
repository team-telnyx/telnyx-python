# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["NumberBlockOrderListParams", "Filter", "FilterCreatedAt", "Page"]


class NumberBlockOrderListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[status], filter[created_at],
    filter[phone_numbers.starting_number]
    """

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[size], page[number]
    """


class FilterCreatedAt(TypedDict, total=False):
    gt: str
    """Filter number block orders later than this value."""

    lt: str
    """Filter number block orders earlier than this value."""


class Filter(TypedDict, total=False):
    created_at: FilterCreatedAt
    """Filter number block orders by date range."""

    phone_numbers_starting_number: Annotated[str, PropertyInfo(alias="phone_numbers.starting_number")]
    """Filter number block orders having these phone numbers."""

    status: str
    """Filter number block orders by status."""


class Page(TypedDict, total=False):
    number: int
    """The page number to load"""

    size: int
    """The size of the page"""

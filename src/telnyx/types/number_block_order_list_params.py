# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["NumberBlockOrderListParams", "Filter", "FilterCreatedAt"]


class NumberBlockOrderListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[status], filter[created_at],
    filter[phone_numbers.starting_number]
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]


class FilterCreatedAt(TypedDict, total=False):
    """Filter number block orders by date range."""

    gt: str
    """Filter number block orders later than this value."""

    lt: str
    """Filter number block orders earlier than this value."""


class Filter(TypedDict, total=False):
    """Consolidated filter parameter (deepObject style).

    Originally: filter[status], filter[created_at], filter[phone_numbers.starting_number]
    """

    created_at: FilterCreatedAt
    """Filter number block orders by date range."""

    phone_numbers_starting_number: Annotated[str, PropertyInfo(alias="phone_numbers.starting_number")]
    """Filter number block orders having these phone numbers."""

    status: str
    """Filter number block orders by status."""

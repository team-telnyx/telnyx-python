# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["NumberOrderListParams", "Filter", "FilterCreatedAt"]


class NumberOrderListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[status], filter[created_at], filter[phone_numbers_count],
    filter[customer_reference], filter[requirements_met]
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]


class FilterCreatedAt(TypedDict, total=False):
    """Filter number orders by date range."""

    gt: str
    """Filter number orders later than this value."""

    lt: str
    """Filter number orders earlier than this value."""


class Filter(TypedDict, total=False):
    """Consolidated filter parameter (deepObject style).

    Originally: filter[status], filter[created_at], filter[phone_numbers_count], filter[customer_reference], filter[requirements_met]
    """

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

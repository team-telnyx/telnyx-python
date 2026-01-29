# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["NumberReservationListParams", "Filter", "FilterCreatedAt"]


class NumberReservationListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[status], filter[created_at],
    filter[phone_numbers.phone_number], filter[customer_reference]
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]


class FilterCreatedAt(TypedDict, total=False):
    """Filter number reservations by date range."""

    gt: str
    """Filter number reservations later than this value."""

    lt: str
    """Filter number reservations earlier than this value."""


class Filter(TypedDict, total=False):
    """Consolidated filter parameter (deepObject style).

    Originally: filter[status], filter[created_at], filter[phone_numbers.phone_number], filter[customer_reference]
    """

    created_at: FilterCreatedAt
    """Filter number reservations by date range."""

    customer_reference: str
    """Filter number reservations via the customer reference set."""

    phone_numbers_phone_number: Annotated[str, PropertyInfo(alias="phone_numbers.phone_number")]
    """Filter number reservations having these phone numbers."""

    status: str
    """Filter number reservations by status."""

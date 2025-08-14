# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PhoneNumberListParams", "Filter", "FilterCivicAddressID", "FilterLocationID", "FilterPhoneNumber", "Page"]


class PhoneNumberListParams(TypedDict, total=False):
    filter: Filter
    """Filter parameter for phone numbers (deepObject style).

    Supports filtering by phone_number, civic_address_id, and location_id with
    eq/contains operations.
    """

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[size], page[number]
    """


class FilterCivicAddressID(TypedDict, total=False):
    eq: str
    """The civic address ID to filter by"""


class FilterLocationID(TypedDict, total=False):
    eq: str
    """The location ID to filter by"""


class FilterPhoneNumber(TypedDict, total=False):
    contains: str
    """The phone number to filter by (partial match)"""

    eq: str
    """The phone number to filter by (exact match)"""


class Filter(TypedDict, total=False):
    civic_address_id: FilterCivicAddressID

    location_id: FilterLocationID

    phone_number: FilterPhoneNumber


class Page(TypedDict, total=False):
    number: int
    """The page number to load"""

    size: int
    """The size of the page"""

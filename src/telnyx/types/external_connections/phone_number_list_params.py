# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PhoneNumberListParams", "Filter", "FilterCivicAddressID", "FilterLocationID", "FilterPhoneNumber"]


class PhoneNumberListParams(TypedDict, total=False):
    filter: Filter
    """Filter parameter for phone numbers (deepObject style).

    Supports filtering by phone_number, civic_address_id, and location_id with
    eq/contains operations.
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]


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
    """Filter parameter for phone numbers (deepObject style).

    Supports filtering by phone_number, civic_address_id, and location_id with eq/contains operations.
    """

    civic_address_id: FilterCivicAddressID

    location_id: FilterLocationID

    phone_number: FilterPhoneNumber

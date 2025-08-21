# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = [
    "UploadListParams",
    "Filter",
    "FilterCivicAddressID",
    "FilterLocationID",
    "FilterPhoneNumber",
    "FilterStatus",
    "Page",
]


class UploadListParams(TypedDict, total=False):
    filter: Filter
    """Filter parameter for uploads (deepObject style).

    Supports filtering by status, civic_address_id, location_id, and phone_number
    with eq/contains operations.
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


class FilterStatus(TypedDict, total=False):
    eq: List[Literal["pending_upload", "pending", "in_progress", "success", "error"]]
    """The status of the upload to filter by"""


class Filter(TypedDict, total=False):
    civic_address_id: FilterCivicAddressID

    location_id: FilterLocationID

    phone_number: FilterPhoneNumber

    status: FilterStatus


class Page(TypedDict, total=False):
    number: int
    """The page number to load"""

    size: int
    """The size of the page"""

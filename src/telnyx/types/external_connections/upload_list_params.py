# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "UploadListParams",
    "Filter",
    "FilterCivicAddressID",
    "FilterLocationID",
    "FilterPhoneNumber",
    "FilterStatus",
]


class UploadListParams(TypedDict, total=False):
    filter: Filter
    """Filter parameter for uploads (deepObject style).

    Supports filtering by status, civic_address_id, location_id, and phone_number
    with eq/contains operations.
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


class FilterStatus(TypedDict, total=False):
    eq: List[Literal["pending_upload", "pending", "in_progress", "success", "error"]]
    """The status of the upload to filter by"""


class Filter(TypedDict, total=False):
    """Filter parameter for uploads (deepObject style).

    Supports filtering by status, civic_address_id, location_id, and phone_number with eq/contains operations.
    """

    civic_address_id: FilterCivicAddressID

    location_id: FilterLocationID

    phone_number: FilterPhoneNumber

    status: FilterStatus

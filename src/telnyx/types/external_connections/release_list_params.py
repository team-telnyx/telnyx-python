# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "ReleaseListParams",
    "Filter",
    "FilterCivicAddressID",
    "FilterLocationID",
    "FilterPhoneNumber",
    "FilterStatus",
]


class ReleaseListParams(TypedDict, total=False):
    filter: Filter
    """Filter parameter for releases (deepObject style).

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
    """Phone number filter operations.

    Use 'eq' for exact matches or 'contains' for partial matches.
    """

    contains: str
    """The partial phone number to filter by. Requires 3-15 digits."""

    eq: str
    """The phone number to filter by"""


class FilterStatus(TypedDict, total=False):
    eq: List[Literal["pending_upload", "pending", "in_progress", "complete", "failed", "expired", "unknown"]]
    """The status of the release to filter by"""


class Filter(TypedDict, total=False):
    """Filter parameter for releases (deepObject style).

    Supports filtering by status, civic_address_id, location_id, and phone_number with eq/contains operations.
    """

    civic_address_id: FilterCivicAddressID

    location_id: FilterLocationID

    phone_number: FilterPhoneNumber
    """Phone number filter operations.

    Use 'eq' for exact matches or 'contains' for partial matches.
    """

    status: FilterStatus

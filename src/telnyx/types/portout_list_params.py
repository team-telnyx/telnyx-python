# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PortoutListParams", "Filter", "FilterInsertedAt", "FilterPortedOutAt", "Page"]


class PortoutListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[carrier_name], filter[country_code], filter[country_code_in],
    filter[foc_date], filter[inserted_at], filter[phone_number], filter[pon],
    filter[ported_out_at], filter[spid], filter[status], filter[status_in],
    filter[support_key]
    """

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[number], page[size]
    """


class FilterInsertedAt(TypedDict, total=False):
    gte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter by inserted_at date greater than or equal."""

    lte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter by inserted_at date less than or equal."""


class FilterPortedOutAt(TypedDict, total=False):
    gte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter by ported_out_at date greater than or equal."""

    lte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter by ported_out_at date less than or equal."""


class Filter(TypedDict, total=False):
    carrier_name: str
    """Filter by new carrier name."""

    country_code: str
    """Filter by 2-letter country code"""

    country_code_in: List[str]
    """Filter by a list of 2-letter country codes"""

    foc_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter by foc_date. Matches all portouts with the same date"""

    inserted_at: FilterInsertedAt
    """Filter by inserted_at date range using nested operations"""

    phone_number: str
    """Filter by a phone number on the portout.

    Matches all portouts with the phone number
    """

    pon: str
    """Filter by Port Order Number (PON)."""

    ported_out_at: FilterPortedOutAt
    """Filter by ported_out_at date range using nested operations"""

    spid: str
    """Filter by new carrier spid."""

    status: Literal["pending", "authorized", "ported", "rejected", "rejected-pending", "canceled"]
    """Filter by portout status."""

    status_in: List[Literal["pending", "authorized", "ported", "rejected", "rejected-pending", "canceled"]]
    """Filter by a list of portout statuses"""

    support_key: str
    """Filter by the portout's support_key"""


class Page(TypedDict, total=False):
    number: int
    """The page number to load"""

    size: int
    """The size of the page"""

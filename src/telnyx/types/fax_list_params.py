# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FaxListParams", "Filter", "FilterCreatedAt", "FilterDirection", "FilterFrom", "FilterTo", "Page"]


class FaxListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[created_at][gte], filter[created_at][gt],
    filter[created_at][lte], filter[created_at][lt], filter[direction][eq],
    filter[from][eq], filter[to][eq]
    """

    page: Page
    """Consolidated pagination parameter (deepObject style).

    Originally: page[size], page[number]
    """


class FilterCreatedAt(TypedDict, total=False):
    gt: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """ISO 8601 date time for filtering faxes created after that date"""

    gte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """ISO 8601 date time for filtering faxes created after or on that date"""

    lt: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """ISO 8601 formatted date time for filtering faxes created before that date"""

    lte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """ISO 8601 formatted date time for filtering faxes created on or before that date"""


class FilterDirection(TypedDict, total=False):
    eq: str
    """The direction, inbound or outbound, for filtering faxes sent from this account"""


class FilterFrom(TypedDict, total=False):
    eq: str
    """The phone number, in E.164 format for filtering faxes sent from this number"""


class FilterTo(TypedDict, total=False):
    eq: str
    """The phone number, in E.164 format for filtering faxes sent to this number"""


_FilterReservedKeywords = TypedDict(
    "_FilterReservedKeywords",
    {
        "from": FilterFrom,
    },
    total=False,
)


class Filter(_FilterReservedKeywords, total=False):
    created_at: FilterCreatedAt
    """Date range filtering operations for fax creation timestamp"""

    direction: FilterDirection
    """Direction filtering operations"""

    to: FilterTo
    """To number filtering operations"""


class Page(TypedDict, total=False):
    number: int
    """Number of the page to be retrieved"""

    size: int
    """Number of fax resources for the single page returned"""

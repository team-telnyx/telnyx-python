# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ConnectionListParams", "Filter", "FilterCreatedAt", "FilterPhoneNumber", "FilterStatus", "Page"]


class ConnectionListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[phone_number][eq], filter[phone_number][in][],
    filter[status][eq], filter[status][in][], filter[created_at][lt],
    filter[created_at][gt]
    """

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[size], page[number]
    """

    sort: Literal["created_at", "connection_name", "active"]
    """Specifies the sort order for results.

    By default sorting direction is ascending. To have the results sorted in
    descending order add the <code> -</code> prefix.<br/><br/> That is: <ul>

      <li>
        <code>connection_name</code>: sorts the result by the
        <code>connection_name</code> field in ascending order.
      </li>

      <li>
        <code>-connection_name</code>: sorts the result by the
        <code>connection_name</code> field in descending order.
      </li>
    </ul> <br/> If not given, results are sorted by <code>created_at</code> in descending order.
    """


class FilterCreatedAt(TypedDict, total=False):
    gt: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filters records to those created after a specific date."""

    lt: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filters records to those created before a specific date."""


_FilterPhoneNumberReservedKeywords = TypedDict(
    "_FilterPhoneNumberReservedKeywords",
    {
        "in": List[str],
    },
    total=False,
)


class FilterPhoneNumber(_FilterPhoneNumberReservedKeywords, total=False):
    eq: str
    """Filters records to those with a specified number."""


_FilterStatusReservedKeywords = TypedDict(
    "_FilterStatusReservedKeywords",
    {
        "in": List[Literal["pending", "completed", "failed"]],
    },
    total=False,
)


class FilterStatus(_FilterStatusReservedKeywords, total=False):
    eq: Literal["pending", "completed", "failed"]
    """Filters records to those with a specific status."""


class Filter(TypedDict, total=False):
    created_at: FilterCreatedAt

    phone_number: FilterPhoneNumber

    status: FilterStatus


class Page(TypedDict, total=False):
    number: int
    """The page number to load"""

    size: int
    """The size of the page"""

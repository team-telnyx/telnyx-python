# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["CustomerServiceRecordListParams", "Filter", "FilterCreatedAt", "FilterPhoneNumber", "FilterStatus", "Sort"]


class CustomerServiceRecordListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[phone_number][eq], filter[phone_number][in][],
    filter[status][eq], filter[status][in][], filter[created_at][lt],
    filter[created_at][gt]
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]

    sort: Sort
    """Consolidated sort parameter (deepObject style). Originally: sort[value]"""


class FilterCreatedAt(TypedDict, total=False):
    gt: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filters records to those created after a specific date."""

    lt: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filters records to those created before a specific date."""


_FilterPhoneNumberReservedKeywords = TypedDict(
    "_FilterPhoneNumberReservedKeywords",
    {
        "in": SequenceNotStr[str],
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
    """Consolidated filter parameter (deepObject style).

    Originally: filter[phone_number][eq], filter[phone_number][in][], filter[status][eq], filter[status][in][], filter[created_at][lt], filter[created_at][gt]
    """

    created_at: FilterCreatedAt

    phone_number: FilterPhoneNumber

    status: FilterStatus


class Sort(TypedDict, total=False):
    """Consolidated sort parameter (deepObject style). Originally: sort[value]"""

    value: Literal["created_at", "-created_at"]
    """Specifies the sort order for results.

    If not given, results are sorted by created_at in descending order.
    """

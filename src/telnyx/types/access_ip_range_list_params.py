# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "AccessIPRangeListParams",
    "Filter",
    "FilterCidrBlock",
    "FilterCidrBlockCidrBlockPatternFilter",
    "FilterCreatedAt",
    "FilterCreatedAtDateRangeFilter",
    "Page",
]


class AccessIPRangeListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[cidr_block], filter[cidr_block][startswith],
    filter[cidr_block][endswith], filter[cidr_block][contains], filter[created_at].
    Supports complex bracket operations for dynamic filtering.
    """

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[number], page[size]
    """


class FilterCidrBlockCidrBlockPatternFilter(TypedDict, total=False):
    contains: str
    """Filter CIDR blocks containing the specified string"""

    endswith: str
    """Filter CIDR blocks ending with the specified string"""

    startswith: str
    """Filter CIDR blocks starting with the specified string"""


FilterCidrBlock: TypeAlias = Union[str, FilterCidrBlockCidrBlockPatternFilter]


class FilterCreatedAtDateRangeFilter(TypedDict, total=False):
    gt: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter for creation date-time greater than"""

    gte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter for creation date-time greater than or equal to"""

    lt: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter for creation date-time less than"""

    lte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter for creation date-time less than or equal to"""


FilterCreatedAt: TypeAlias = Union[Union[str, datetime], FilterCreatedAtDateRangeFilter]


class FilterTyped(TypedDict, total=False):
    cidr_block: FilterCidrBlock
    """Filter by exact CIDR block match"""

    created_at: Annotated[FilterCreatedAt, PropertyInfo(format="iso8601")]
    """Filter by exact creation date-time"""


Filter: TypeAlias = Union[FilterTyped, Dict[str, object]]


class Page(TypedDict, total=False):
    number: int

    size: int

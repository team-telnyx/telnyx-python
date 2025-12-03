# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["AccessIPAddressListParams", "Filter", "FilterCreatedAt", "FilterCreatedAtDateRangeFilter", "Page"]


class AccessIPAddressListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[ip_source], filter[ip_address], filter[created_at]. Supports
    complex bracket operations for dynamic filtering.
    """

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[number], page[size]
    """


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
    created_at: Annotated[FilterCreatedAt, PropertyInfo(format="iso8601")]
    """Filter by exact creation date-time"""

    ip_address: str
    """Filter by IP address"""

    ip_source: str
    """Filter by IP source"""


Filter: TypeAlias = Union[FilterTyped, Dict[str, object]]


class Page(TypedDict, total=False):
    number: int

    size: int

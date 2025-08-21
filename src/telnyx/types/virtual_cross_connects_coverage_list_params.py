# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "VirtualCrossConnectsCoverageListParams",
    "Filter",
    "Filters",
    "FiltersAvailableBandwidth",
    "FiltersAvailableBandwidthContains",
    "Page",
]


class VirtualCrossConnectsCoverageListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[cloud_provider], filter[cloud_provider_region],
    filter[location.region], filter[location.site], filter[location.pop],
    filter[location.code]
    """

    filters: Filters
    """Consolidated filters parameter (deepObject style).

    Originally: filters[available_bandwidth][contains]
    """

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[number], page[size]
    """


class Filter(TypedDict, total=False):
    cloud_provider: Literal["aws", "azure", "gce"]
    """The Virtual Private Cloud provider."""

    cloud_provider_region: str
    """The region of specific cloud provider."""

    location_code: Annotated[str, PropertyInfo(alias="location.code")]
    """The code of associated location to filter on."""

    location_pop: Annotated[str, PropertyInfo(alias="location.pop")]
    """The POP of associated location to filter on."""

    location_region: Annotated[str, PropertyInfo(alias="location.region")]
    """The region of associated location to filter on."""

    location_site: Annotated[str, PropertyInfo(alias="location.site")]
    """The site of associated location to filter on."""


class FiltersAvailableBandwidthContains(TypedDict, total=False):
    contains: int
    """Filter by available bandwidth containing the specified value"""


FiltersAvailableBandwidth: TypeAlias = Union[int, FiltersAvailableBandwidthContains]


class Filters(TypedDict, total=False):
    available_bandwidth: FiltersAvailableBandwidth
    """Filter by exact available bandwidth match"""


class Page(TypedDict, total=False):
    number: int
    """The page number to load"""

    size: int
    """The size of the page"""

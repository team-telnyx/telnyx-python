# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, ForwardRef
from typing_extensions import Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "NetworkCoverageListParams",
    "Filter",
    "Filters",
    "FiltersAvailableServices",
    "FiltersAvailableServicesContains",
]


class NetworkCoverageListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[location.region], filter[location.site],
    filter[location.pop], filter[location.code]
    """

    filters: Filters
    """Consolidated filters parameter (deepObject style).

    Originally: filters[available_services][contains]
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]


class Filter(TypedDict, total=False):
    """Consolidated filter parameter (deepObject style).

    Originally: filter[location.region], filter[location.site], filter[location.pop], filter[location.code]
    """

    location_code: Annotated[str, PropertyInfo(alias="location.code")]
    """The code of associated location to filter on."""

    location_pop: Annotated[str, PropertyInfo(alias="location.pop")]
    """The POP of associated location to filter on."""

    location_region: Annotated[str, PropertyInfo(alias="location.region")]
    """The region of associated location to filter on."""

    location_site: Annotated[str, PropertyInfo(alias="location.site")]
    """The site of associated location to filter on."""


class FiltersAvailableServicesContains(TypedDict, total=False):
    """Available service filtering operations"""

    contains: "AvailableService"
    """Filter by available services containing the specified service"""


if TYPE_CHECKING:
    FiltersAvailableServices: TypeAlias = Union["AvailableService", FiltersAvailableServicesContains]
else:
    FiltersAvailableServices = Union[
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).AvailableService"), FiltersAvailableServicesContains
    ]


class Filters(TypedDict, total=False):
    """Consolidated filters parameter (deepObject style).

    Originally: filters[available_services][contains]
    """

    available_services: FiltersAvailableServices
    """Filter by exact available service match"""


from .available_service import AvailableService

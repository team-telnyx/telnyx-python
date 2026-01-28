# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MobileNetworkOperatorListParams", "Filter", "FilterName"]


class MobileNetworkOperatorListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter for mobile network operators (deepObject style).

    Originally: filter[name][starts_with], filter[name][contains],
    filter[name][ends_with], filter[country_code], filter[mcc], filter[mnc],
    filter[tadig], filter[network_preferences_enabled]
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]


class FilterName(TypedDict, total=False):
    """Advanced name filtering operations"""

    contains: str
    """Filter by name containing match."""

    ends_with: str
    """Filter by name ending with."""

    starts_with: str
    """Filter by name starting with."""


class Filter(TypedDict, total=False):
    """Consolidated filter parameter for mobile network operators (deepObject style).

    Originally: filter[name][starts_with], filter[name][contains], filter[name][ends_with], filter[country_code], filter[mcc], filter[mnc], filter[tadig], filter[network_preferences_enabled]
    """

    country_code: str
    """Filter by exact country_code."""

    mcc: str
    """Filter by exact MCC."""

    mnc: str
    """Filter by exact MNC."""

    name: FilterName
    """Advanced name filtering operations"""

    network_preferences_enabled: bool
    """Filter by network_preferences_enabled."""

    tadig: str
    """Filter by exact TADIG."""

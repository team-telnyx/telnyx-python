# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["MobileNetworkOperatorListParams", "Filter", "FilterName", "Page"]


class MobileNetworkOperatorListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter for mobile network operators (deepObject style).

    Originally: filter[name][starts_with], filter[name][contains],
    filter[name][ends_with], filter[country_code], filter[mcc], filter[mnc],
    filter[tadig], filter[network_preferences_enabled]
    """

    page: Page
    """Consolidated pagination parameter (deepObject style).

    Originally: page[number], page[size]
    """


class FilterName(TypedDict, total=False):
    contains: str
    """Filter by name containing match."""

    ends_with: str
    """Filter by name ending with."""

    starts_with: str
    """Filter by name starting with."""


class Filter(TypedDict, total=False):
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


class Page(TypedDict, total=False):
    number: int
    """The page number to load."""

    size: int
    """The size of the page."""

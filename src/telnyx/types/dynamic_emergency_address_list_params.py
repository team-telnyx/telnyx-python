# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DynamicEmergencyAddressListParams", "Filter"]


class DynamicEmergencyAddressListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[status], filter[country_code]
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]


class Filter(TypedDict, total=False):
    """Consolidated filter parameter (deepObject style).

    Originally: filter[status], filter[country_code]
    """

    country_code: str
    """Filter by country code."""

    status: Literal["pending", "activated", "rejected"]
    """Filter by status."""

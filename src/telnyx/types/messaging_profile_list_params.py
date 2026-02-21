# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MessagingProfileListParams", "Filter"]


class MessagingProfileListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style). Originally: filter[name]"""

    filter_name_contains: Annotated[str, PropertyInfo(alias="filter[name][contains]")]
    """Filter profiles by name containing the given string."""

    filter_name_eq: Annotated[str, PropertyInfo(alias="filter[name][eq]")]
    """Filter profiles by exact name match."""

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]


class Filter(TypedDict, total=False):
    """Consolidated filter parameter (deepObject style). Originally: filter[name]"""

    name: str
    """Filter by name"""

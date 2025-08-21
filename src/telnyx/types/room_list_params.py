# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RoomListParams", "Filter", "FilterDateCreatedAt", "FilterDateUpdatedAt", "Page"]


class RoomListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[date_created_at][eq], filter[date_created_at][gte],
    filter[date_created_at][lte], filter[date_updated_at][eq],
    filter[date_updated_at][gte], filter[date_updated_at][lte], filter[unique_name]
    """

    include_sessions: bool
    """To decide if room sessions should be included in the response."""

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[size], page[number]
    """


class FilterDateCreatedAt(TypedDict, total=False):
    eq: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """ISO 8601 date for filtering rooms created on that date."""

    gte: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """ISO 8601 date for filtering rooms created on or after that date."""

    lte: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """ISO 8601 date for filtering rooms created on or before that date."""


class FilterDateUpdatedAt(TypedDict, total=False):
    eq: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """ISO 8601 date for filtering rooms updated on that date."""

    gte: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """ISO 8601 date for filtering rooms updated on or after that date."""

    lte: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """ISO 8601 date for filtering rooms updated on or before that date."""


class Filter(TypedDict, total=False):
    date_created_at: FilterDateCreatedAt

    date_updated_at: FilterDateUpdatedAt

    unique_name: str
    """Unique_name for filtering rooms."""


class Page(TypedDict, total=False):
    number: int
    """The page number to load."""

    size: int
    """The size of the page."""

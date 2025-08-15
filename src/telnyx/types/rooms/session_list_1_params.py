# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SessionList1Params", "Filter", "FilterDateCreatedAt", "FilterDateEndedAt", "FilterDateUpdatedAt", "Page"]


class SessionList1Params(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[date_created_at][eq], filter[date_created_at][gte],
    filter[date_created_at][lte], filter[date_updated_at][eq],
    filter[date_updated_at][gte], filter[date_updated_at][lte],
    filter[date_ended_at][eq], filter[date_ended_at][gte],
    filter[date_ended_at][lte], filter[active]
    """

    include_participants: bool
    """To decide if room participants should be included in the response."""

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[size], page[number]
    """


class FilterDateCreatedAt(TypedDict, total=False):
    eq: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """ISO 8601 date for filtering room sessions created on that date."""

    gte: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """ISO 8601 date for filtering room sessions created on or after that date."""

    lte: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """ISO 8601 date for filtering room sessions created on or before that date."""


class FilterDateEndedAt(TypedDict, total=False):
    eq: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """ISO 8601 date for filtering room sessions ended on that date."""

    gte: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """ISO 8601 date for filtering room sessions ended on or after that date."""

    lte: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """ISO 8601 date for filtering room sessions ended on or before that date."""


class FilterDateUpdatedAt(TypedDict, total=False):
    eq: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """ISO 8601 date for filtering room sessions updated on that date."""

    gte: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """ISO 8601 date for filtering room sessions updated on or after that date."""

    lte: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """ISO 8601 date for filtering room sessions updated on or before that date."""


class Filter(TypedDict, total=False):
    active: bool
    """Filter active or inactive room sessions."""

    date_created_at: FilterDateCreatedAt

    date_ended_at: FilterDateEndedAt

    date_updated_at: FilterDateUpdatedAt


class Page(TypedDict, total=False):
    number: int
    """The page number to load."""

    size: int
    """The size of the page."""

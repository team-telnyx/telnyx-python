# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "RoomParticipantListParams",
    "Filter",
    "FilterDateJoinedAt",
    "FilterDateLeftAt",
    "FilterDateUpdatedAt",
    "Page",
]


class RoomParticipantListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[date_joined_at][eq], filter[date_joined_at][gte],
    filter[date_joined_at][lte], filter[date_updated_at][eq],
    filter[date_updated_at][gte], filter[date_updated_at][lte],
    filter[date_left_at][eq], filter[date_left_at][gte], filter[date_left_at][lte],
    filter[context], filter[session_id]
    """

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[size], page[number]
    """


class FilterDateJoinedAt(TypedDict, total=False):
    eq: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """ISO 8601 date for filtering room participants that joined on that date."""

    gte: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """
    ISO 8601 date for filtering room participants that joined on or after that date.
    """

    lte: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """
    ISO 8601 date for filtering room participants that joined on or before that
    date.
    """


class FilterDateLeftAt(TypedDict, total=False):
    eq: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """ISO 8601 date for filtering room participants that left on that date."""

    gte: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """ISO 8601 date for filtering room participants that left on or after that date."""

    lte: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """ISO 8601 date for filtering room participants that left on or before that date."""


class FilterDateUpdatedAt(TypedDict, total=False):
    eq: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """ISO 8601 date for filtering room participants updated on that date."""

    gte: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """ISO 8601 date for filtering room participants updated on or after that date."""

    lte: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """ISO 8601 date for filtering room participants updated on or before that date."""


class Filter(TypedDict, total=False):
    context: str
    """Filter room participants based on the context."""

    date_joined_at: FilterDateJoinedAt

    date_left_at: FilterDateLeftAt

    date_updated_at: FilterDateUpdatedAt

    session_id: str
    """Session_id for filtering room participants."""


class Page(TypedDict, total=False):
    number: int
    """The page number to load."""

    size: int
    """The size of the page."""

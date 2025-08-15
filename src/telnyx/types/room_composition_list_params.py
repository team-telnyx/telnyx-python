# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RoomCompositionListParams", "Filter", "FilterDateCreatedAt", "Page"]


class RoomCompositionListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[date_created_at][eq], filter[date_created_at][gte],
    filter[date_created_at][lte], filter[session_id], filter[status]
    """

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[size], page[number]
    """


class FilterDateCreatedAt(TypedDict, total=False):
    eq: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """ISO 8601 date for filtering room compositions created on that date."""

    gte: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """ISO 8601 date for filtering room compositions created on or after that date."""

    lte: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """ISO 8601 date for filtering room compositions created on or before that date."""


class Filter(TypedDict, total=False):
    date_created_at: FilterDateCreatedAt

    session_id: str
    """The session_id for filtering room compositions."""

    status: Literal["completed", "processing", "enqueued"]
    """The status for filtering room compositions."""


class Page(TypedDict, total=False):
    number: int
    """The page number to load."""

    size: int
    """The size of the page."""

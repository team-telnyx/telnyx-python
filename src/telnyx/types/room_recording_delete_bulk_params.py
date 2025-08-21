# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RoomRecordingDeleteBulkParams", "Filter", "FilterDateEndedAt", "FilterDateStartedAt", "Page"]


class RoomRecordingDeleteBulkParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[date_ended_at][eq], filter[date_ended_at][gte],
    filter[date_ended_at][lte], filter[date_started_at][eq],
    filter[date_started_at][gte], filter[date_started_at][lte], filter[room_id],
    filter[participant_id], filter[session_id], filter[status], filter[type],
    filter[duration_secs]
    """

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[size], page[number]
    """


class FilterDateEndedAt(TypedDict, total=False):
    eq: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """ISO 8601 date for filtering room recordings ended on that date."""

    gte: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """ISO 8601 date for filtering room recordings ended on or after that date."""

    lte: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """ISO 8601 date for filtering room recordings ended on or before that date."""


class FilterDateStartedAt(TypedDict, total=False):
    eq: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """ISO 8601 date for filtering room recordings started on that date."""

    gte: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """ISO 8601 date for filtering room recordings started on or after that date."""

    lte: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """ISO 8601 date for filtering room recordings started on or before that date."""


class Filter(TypedDict, total=False):
    date_ended_at: FilterDateEndedAt

    date_started_at: FilterDateStartedAt

    duration_secs: int
    """duration_secs greater or equal for filtering room recordings."""

    participant_id: str
    """participant_id for filtering room recordings."""

    room_id: str
    """room_id for filtering room recordings."""

    session_id: str
    """session_id for filtering room recordings."""

    status: str
    """status for filtering room recordings."""

    type: str
    """type for filtering room recordings."""


class Page(TypedDict, total=False):
    number: int
    """The page number to load."""

    size: int
    """The size of the page."""

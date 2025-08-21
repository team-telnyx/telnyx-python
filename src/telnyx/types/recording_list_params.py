# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["RecordingListParams", "Filter", "FilterCreatedAt", "Page"]


class RecordingListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[conference_id], filter[created_at][gte],
    filter[created_at][lte], filter[call_leg_id], filter[call_session_id],
    filter[from], filter[to], filter[connection_id]
    """

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[size], page[number]
    """


class FilterCreatedAt(TypedDict, total=False):
    gte: str
    """Returns only recordings created later than or at given ISO 8601 datetime."""

    lte: str
    """Returns only recordings created earlier than or at given ISO 8601 datetime."""


_FilterReservedKeywords = TypedDict(
    "_FilterReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class Filter(_FilterReservedKeywords, total=False):
    call_leg_id: str
    """If present, recordings will be filtered to those with a matching call_leg_id."""

    call_session_id: str
    """
    If present, recordings will be filtered to those with a matching
    call_session_id.
    """

    conference_id: str
    """Returns only recordings associated with a given conference."""

    connection_id: str
    """
    If present, recordings will be filtered to those with a matching `connection_id`
    attribute (case-sensitive).
    """

    created_at: FilterCreatedAt

    to: str
    """
    If present, recordings will be filtered to those with a matching `to` attribute
    (case-sensitive).
    """


class Page(TypedDict, total=False):
    number: int
    """The page number to load."""

    size: int
    """The size of the page."""

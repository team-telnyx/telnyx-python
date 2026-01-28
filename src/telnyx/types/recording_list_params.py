# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RecordingListParams", "Filter", "FilterCreatedAt"]


class RecordingListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[conference_id], filter[created_at][gte],
    filter[created_at][lte], filter[call_leg_id], filter[call_session_id],
    filter[from], filter[to], filter[connection_id], filter[sip_call_id]
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]


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
    """Consolidated filter parameter (deepObject style).

    Originally: filter[conference_id], filter[created_at][gte], filter[created_at][lte], filter[call_leg_id], filter[call_session_id], filter[from], filter[to], filter[connection_id], filter[sip_call_id]
    """

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

    sip_call_id: str
    """
    If present, recordings will be filtered to those with a matching `sip_call_id`
    attribute. Matching is case-sensitive
    """

    to: str
    """
    If present, recordings will be filtered to those with a matching `to` attribute
    (case-sensitive).
    """

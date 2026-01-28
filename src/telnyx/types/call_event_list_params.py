# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CallEventListParams", "Filter", "FilterApplicationName", "FilterOccurredAt"]


class CallEventListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[application_name][contains],
    filter[outbound.outbound_voice_profile_id], filter[leg_id],
    filter[application_session_id], filter[connection_id], filter[product],
    filter[failed], filter[from], filter[to], filter[name], filter[type],
    filter[occurred_at][eq/gt/gte/lt/lte], filter[status]
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]


class FilterApplicationName(TypedDict, total=False):
    """Application name filters"""

    contains: str
    """
    If present, applications with <code>application_name</code> containing the given
    value will be returned. Matching is not case-sensitive. Requires at least three
    characters.
    """


class FilterOccurredAt(TypedDict, total=False):
    """Event occurred_at filters"""

    eq: str
    """Event occurred_at: equal"""

    gt: str
    """Event occurred_at: greater than"""

    gte: str
    """Event occurred_at: greater than or equal"""

    lt: str
    """Event occurred_at: lower than"""

    lte: str
    """Event occurred_at: lower than or equal"""


_FilterReservedKeywords = TypedDict(
    "_FilterReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class Filter(_FilterReservedKeywords, total=False):
    """Consolidated filter parameter (deepObject style).

    Originally: filter[application_name][contains], filter[outbound.outbound_voice_profile_id], filter[leg_id], filter[application_session_id], filter[connection_id], filter[product], filter[failed], filter[from], filter[to], filter[name], filter[type], filter[occurred_at][eq/gt/gte/lt/lte], filter[status]
    """

    application_name: FilterApplicationName
    """Application name filters"""

    application_session_id: str
    """The unique identifier of the call session.

    A session may include multiple call leg events.
    """

    connection_id: str
    """The unique identifier of the conection."""

    failed: bool
    """Delivery failed or not."""

    leg_id: str
    """The unique identifier of an individual call leg."""

    name: str
    """
    If present, conferences will be filtered to those with a matching `name`
    attribute. Matching is case-sensitive
    """

    occurred_at: FilterOccurredAt
    """Event occurred_at filters"""

    outbound_outbound_voice_profile_id: Annotated[str, PropertyInfo(alias="outbound.outbound_voice_profile_id")]
    """Identifies the associated outbound voice profile."""

    product: Literal["call_control", "fax", "texml"]
    """Filter by product."""

    status: Literal["init", "in_progress", "completed"]
    """If present, conferences will be filtered by status."""

    to: str
    """Filter by To number."""

    type: Literal["command", "webhook"]
    """Event type"""

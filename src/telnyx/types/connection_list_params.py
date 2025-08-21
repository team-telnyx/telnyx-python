# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ConnectionListParams", "Filter", "FilterConnectionName", "Page"]


class ConnectionListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[connection_name], filter[fqdn],
    filter[outbound_voice_profile_id], filter[outbound.outbound_voice_profile_id]
    """

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[size], page[number]
    """

    sort: Literal["created_at", "connection_name", "active"]
    """Specifies the sort order for results.

    By default sorting direction is ascending. To have the results sorted in
    descending order add the <code> -</code> prefix.<br/><br/> That is: <ul>

      <li>
        <code>connection_name</code>: sorts the result by the
        <code>connection_name</code> field in ascending order.
      </li>

      <li>
        <code>-connection_name</code>: sorts the result by the
        <code>connection_name</code> field in descending order.
      </li>
    </ul> <br/> If not given, results are sorted by <code>created_at</code> in descending order.
    """


class FilterConnectionName(TypedDict, total=False):
    contains: str
    """
    If present, connections with <code>connection_name</code> containing the given
    value will be returned. Matching is not case-sensitive. Requires at least three
    characters.
    """


class Filter(TypedDict, total=False):
    connection_name: FilterConnectionName
    """Filter by connection_name using nested operations"""

    fqdn: str
    """
    If present, connections with an `fqdn` that equals the given value will be
    returned. Matching is case-sensitive, and the full string must match.
    """

    outbound_voice_profile_id: str
    """Identifies the associated outbound voice profile."""


class Page(TypedDict, total=False):
    number: int
    """The page number to load"""

    size: int
    """The size of the page"""

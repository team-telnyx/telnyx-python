# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["FaxApplicationListParams", "Filter", "FilterApplicationName", "Page"]


class FaxApplicationListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[application_name][contains],
    filter[outbound_voice_profile_id]
    """

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[number], page[size]
    """

    sort: Literal["created_at", "application_name", "active"]
    """Specifies the sort order for results.

    By default sorting direction is ascending. To have the results sorted in
    descending order add the <code> -</code> prefix.<br/><br/> That is: <ul>

      <li>
        <code>application_name</code>: sorts the result by the
        <code>application_name</code> field in ascending order.
      </li>

      <li>
        <code>-application_name</code>: sorts the result by the
        <code>application_name</code> field in descending order.
      </li>
    </ul> <br/> If not given, results are sorted by <code>created_at</code> in descending order.
    """


class FilterApplicationName(TypedDict, total=False):
    contains: str
    """
    If present, applications with <code>application_name</code> containing the given
    value will be returned. Matching is not case-sensitive. Requires at least three
    characters.
    """


class Filter(TypedDict, total=False):
    application_name: FilterApplicationName
    """Application name filtering operations"""

    outbound_voice_profile_id: str
    """Identifies the associated outbound voice profile."""


class Page(TypedDict, total=False):
    number: int
    """The page number to load"""

    size: int
    """The size of the page"""

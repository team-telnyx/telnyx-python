# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FaxApplicationListParams", "Filter", "FilterApplicationName"]


class FaxApplicationListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[application_name][contains],
    filter[outbound_voice_profile_id]
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]

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
    """Application name filtering operations"""

    contains: str
    """
    If present, applications with <code>application_name</code> containing the given
    value will be returned. Matching is not case-sensitive. Requires at least three
    characters.
    """


class Filter(TypedDict, total=False):
    """Consolidated filter parameter (deepObject style).

    Originally: filter[application_name][contains], filter[outbound_voice_profile_id]
    """

    application_name: FilterApplicationName
    """Application name filtering operations"""

    outbound_voice_profile_id: str
    """Identifies the associated outbound voice profile."""

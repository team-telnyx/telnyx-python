# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TexmlApplicationListParams", "Filter"]


class TexmlApplicationListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[outbound_voice_profile_id], filter[friendly_name]
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]

    sort: Literal["created_at", "friendly_name", "active"]
    """Specifies the sort order for results.

    By default sorting direction is ascending. To have the results sorted in
    descending order add the <code> -</code> prefix.<br/><br/> That is: <ul>

      <li>
        <code>friendly_name</code>: sorts the result by the
        <code>friendly_name</code> field in ascending order.
      </li>

      <li>
        <code>-friendly_name</code>: sorts the result by the
        <code>friendly_name</code> field in descending order.
      </li>
    </ul> <br/> If not given, results are sorted by <code>created_at</code> in descending order.
    """


class Filter(TypedDict, total=False):
    """Consolidated filter parameter (deepObject style).

    Originally: filter[outbound_voice_profile_id], filter[friendly_name]
    """

    friendly_name: str
    """
    If present, applications with <code>friendly_name</code> containing the given
    value will be returned. Matching is not case-sensitive. Requires at least three
    characters.
    """

    outbound_voice_profile_id: str
    """Identifies the associated outbound voice profile."""

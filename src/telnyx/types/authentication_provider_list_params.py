# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AuthenticationProviderListParams", "Page"]


class AuthenticationProviderListParams(TypedDict, total=False):
    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[number], page[size]
    """

    sort: Literal[
        "name",
        "-name",
        "short_name",
        "-short_name",
        "active",
        "-active",
        "created_at",
        "-created_at",
        "updated_at",
        "-updated_at",
    ]
    """Specifies the sort order for results.

    By default sorting direction is ascending. To have the results sorted in
    descending order add the <code>-</code> prefix.<br/><br/> That is: <ul>

      <li>
        <code>name</code>: sorts the result by the
        <code>name</code> field in ascending order.
      </li>
      <li>
        <code>-name</code>: sorts the result by the
        <code>name</code> field in descending order.
      </li>
    </ul><br/>If not given, results are sorted by <code>created_at</code> in descending order.
    """


class Page(TypedDict, total=False):
    number: int
    """The page number to load"""

    size: int
    """The size of the page"""

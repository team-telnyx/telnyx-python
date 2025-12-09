# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AuthenticationProviderListParams"]


class AuthenticationProviderListParams(TypedDict, total=False):
    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]

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

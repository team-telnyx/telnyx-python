# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ManagedAccountListParams", "Filter", "FilterEmail", "FilterOrganizationName"]


class ManagedAccountListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[email][contains], filter[email][eq],
    filter[organization_name][contains], filter[organization_name][eq]
    """

    include_cancelled_accounts: bool
    """Specifies if cancelled accounts should be included in the results."""

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]

    sort: Literal["created_at", "email"]
    """Specifies the sort order for results.

    By default sorting direction is ascending. To have the results sorted in
    descending order add the <code> -</code> prefix.<br/><br/> That is: <ul>

      <li>
        <code>email</code>: sorts the result by the
        <code>email</code> field in ascending order.
      </li>

      <li>
        <code>-email</code>: sorts the result by the
        <code>email</code> field in descending order.
      </li>
    </ul> <br/> If not given, results are sorted by <code>created_at</code> in descending order.
    """


class FilterEmail(TypedDict, total=False):
    contains: str
    """If present, email containing the given value will be returned.

    Matching is not case-sensitive. Requires at least three characters.
    """

    eq: str
    """
    If present, only returns results with the <code>email</code> matching exactly
    the value given.
    """


class FilterOrganizationName(TypedDict, total=False):
    contains: str
    """
    If present, only returns results with the <code>organization_name</code>
    containing the given value. Matching is not case-sensitive. Requires at least
    three characters.
    """

    eq: str
    """
    If present, only returns results with the <code>organization_name</code>
    matching exactly the value given.
    """


class Filter(TypedDict, total=False):
    """Consolidated filter parameter (deepObject style).

    Originally: filter[email][contains], filter[email][eq], filter[organization_name][contains], filter[organization_name][eq]
    """

    email: FilterEmail

    organization_name: FilterOrganizationName

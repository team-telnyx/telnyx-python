# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["UserAddressListParams", "Filter", "FilterCustomerReference", "FilterStreetAddress"]


class UserAddressListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[customer_reference][eq],
    filter[customer_reference][contains], filter[street_address][contains]
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]

    sort: Literal["created_at", "first_name", "last_name", "business_name", "street_address"]
    """Specifies the sort order for results.

    By default sorting direction is ascending. To have the results sorted in
    descending order add the <code> -</code> prefix.<br/><br/> That is: <ul>

      <li>
        <code>street_address</code>: sorts the result by the
        <code>street_address</code> field in ascending order.
      </li>

      <li>
        <code>-street_address</code>: sorts the result by the
        <code>street_address</code> field in descending order.
      </li>
    </ul> <br/> If not given, results are sorted by <code>created_at</code> in descending order.
    """


class FilterCustomerReference(TypedDict, total=False):
    """Filter user addresses via the customer reference.

    Supports both exact matching (eq) and partial matching (contains). Matching is not case-sensitive.
    """

    contains: str
    """
    If present, user addresses with <code>customer_reference</code> containing the
    given value will be returned. Matching is not case-sensitive.
    """

    eq: str
    """Filter user addresses via exact customer reference match.

    Matching is not case-sensitive.
    """


class FilterStreetAddress(TypedDict, total=False):
    """Filter user addresses via street address.

    Supports partial matching (contains). Matching is not case-sensitive.
    """

    contains: str
    """
    If present, user addresses with <code>street_address</code> containing the given
    value will be returned. Matching is not case-sensitive. Requires at least three
    characters.
    """


class Filter(TypedDict, total=False):
    """Consolidated filter parameter (deepObject style).

    Originally: filter[customer_reference][eq], filter[customer_reference][contains], filter[street_address][contains]
    """

    customer_reference: FilterCustomerReference
    """Filter user addresses via the customer reference.

    Supports both exact matching (eq) and partial matching (contains). Matching is
    not case-sensitive.
    """

    street_address: FilterStreetAddress
    """Filter user addresses via street address.

    Supports partial matching (contains). Matching is not case-sensitive.
    """

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, TypeAlias, TypedDict

__all__ = [
    "AddressListParams",
    "Filter",
    "FilterAddressBook",
    "FilterCustomerReference",
    "FilterCustomerReferenceUnionMember1",
    "FilterStreetAddress",
    "Page",
]


class AddressListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[customer_reference][eq],
    filter[customer_reference][contains], filter[used_as_emergency],
    filter[street_address][contains], filter[address_book][eq]
    """

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[number], page[size]
    """

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


class FilterAddressBook(TypedDict, total=False):
    eq: str
    """
    If present, only returns results with the <code>address_book</code> flag equal
    to the given value.
    """


class FilterCustomerReferenceUnionMember1(TypedDict, total=False):
    contains: str
    """Partial match for customer_reference. Matching is not case-sensitive."""

    eq: str
    """Exact match for customer_reference."""


FilterCustomerReference: TypeAlias = Union[str, FilterCustomerReferenceUnionMember1]


class FilterStreetAddress(TypedDict, total=False):
    contains: str
    """
    If present, addresses with <code>street_address</code> containing the given
    value will be returned. Matching is not case-sensitive. Requires at least three
    characters.
    """


class Filter(TypedDict, total=False):
    address_book: FilterAddressBook

    customer_reference: FilterCustomerReference
    """
    If present, addresses with <code>customer_reference</code> containing the given
    value will be returned. Matching is not case-sensitive.
    """

    street_address: FilterStreetAddress

    used_as_emergency: str
    """
    If set as 'true', only addresses used as the emergency address for at least one
    active phone-number will be returned. When set to 'false', the opposite happens:
    only addresses not used as the emergency address from phone-numbers will be
    returned.
    """


class Page(TypedDict, total=False):
    number: int
    """The page number to load"""

    size: int
    """The size of the page"""

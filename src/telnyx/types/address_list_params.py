# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "AddressListParams",
    "Filter",
    "FilterAddressBook",
    "FilterCustomerReference",
    "FilterCustomerReferenceCustomerReferenceMatcher",
    "FilterStreetAddress",
]


class AddressListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[customer_reference][eq],
    filter[customer_reference][contains], filter[used_as_emergency],
    filter[street_address][contains], filter[address_book][eq]
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


class FilterAddressBook(TypedDict, total=False):
    eq: str
    """
    If present, only returns results with the <code>address_book</code> flag equal
    to the given value.
    """


class FilterCustomerReferenceCustomerReferenceMatcher(TypedDict, total=False):
    contains: str
    """Partial match for customer_reference. Matching is not case-sensitive."""

    eq: str
    """Exact match for customer_reference."""


FilterCustomerReference: TypeAlias = Union[str, FilterCustomerReferenceCustomerReferenceMatcher]


class FilterStreetAddress(TypedDict, total=False):
    contains: str
    """
    If present, addresses with <code>street_address</code> containing the given
    value will be returned. Matching is not case-sensitive. Requires at least three
    characters.
    """


class Filter(TypedDict, total=False):
    """Consolidated filter parameter (deepObject style).

    Originally: filter[customer_reference][eq], filter[customer_reference][contains], filter[used_as_emergency], filter[street_address][contains], filter[address_book][eq]
    """

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

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SimCardOrderListParams", "Filter", "FilterAddress", "FilterCost", "Page"]


class SimCardOrderListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter for SIM card orders (deepObject style).

    Originally: filter[created_at], filter[updated_at], filter[quantity],
    filter[cost.amount], filter[cost.currency], filter[address.id],
    filter[address.street_address], filter[address.extended_address],
    filter[address.locality], filter[address.administrative_area],
    filter[address.country_code], filter[address.postal_code]
    """

    page: Page
    """Consolidated pagination parameter (deepObject style).

    Originally: page[number], page[size]
    """


class FilterAddress(TypedDict, total=False):
    id: str
    """Uniquely identifies the address for the order."""

    administrative_area: str
    """Filter by state or province where the address is located."""

    country_code: str
    """
    Filter by the mobile operator two-character (ISO 3166-1 alpha-2) origin country
    code.
    """

    extended_address: str
    """
    Returns entries with matching name of the supplemental field for address
    information.
    """

    locality: str
    """Filter by the name of the city where the address is located."""

    postal_code: str
    """Filter by postal code for the address."""

    street_address: str
    """Returns entries with matching name of the street where the address is located."""


class FilterCost(TypedDict, total=False):
    amount: str
    """The total monetary amount of the order."""

    currency: str
    """Filter by ISO 4217 currency string."""


class Filter(TypedDict, total=False):
    address: FilterAddress

    cost: FilterCost

    created_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    Filter by ISO 8601 formatted date-time string matching resource creation
    date-time.
    """

    quantity: int
    """Filter orders by how many SIM cards were ordered."""

    updated_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    Filter by ISO 8601 formatted date-time string matching resource last update
    date-time.
    """


class Page(TypedDict, total=False):
    number: int
    """The page number to load."""

    size: int
    """The size of the page."""

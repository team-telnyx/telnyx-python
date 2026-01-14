# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SimCardOrderListParams", "Filter"]


class SimCardOrderListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter for SIM card orders (deepObject style).

    Originally: filter[created_at], filter[updated_at], filter[quantity],
    filter[cost.amount], filter[cost.currency], filter[address.id],
    filter[address.street_address], filter[address.extended_address],
    filter[address.locality], filter[address.administrative_area],
    filter[address.country_code], filter[address.postal_code]
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]


class Filter(TypedDict, total=False):
    """Consolidated filter parameter for SIM card orders (deepObject style).

    Originally: filter[created_at], filter[updated_at], filter[quantity], filter[cost.amount], filter[cost.currency], filter[address.id], filter[address.street_address], filter[address.extended_address], filter[address.locality], filter[address.administrative_area], filter[address.country_code], filter[address.postal_code]
    """

    address_administrative_area: Annotated[str, PropertyInfo(alias="address.administrative_area")]
    """Filter by state or province where the address is located."""

    address_country_code: Annotated[str, PropertyInfo(alias="address.country_code")]
    """
    Filter by the mobile operator two-character (ISO 3166-1 alpha-2) origin country
    code.
    """

    address_extended_address: Annotated[str, PropertyInfo(alias="address.extended_address")]
    """
    Returns entries with matching name of the supplemental field for address
    information.
    """

    address_id: Annotated[str, PropertyInfo(alias="address.id")]
    """Uniquely identifies the address for the order."""

    address_locality: Annotated[str, PropertyInfo(alias="address.locality")]
    """Filter by the name of the city where the address is located."""

    address_postal_code: Annotated[str, PropertyInfo(alias="address.postal_code")]
    """Filter by postal code for the address."""

    address_street_address: Annotated[str, PropertyInfo(alias="address.street_address")]
    """Returns entries with matching name of the street where the address is located."""

    cost_amount: Annotated[str, PropertyInfo(alias="cost.amount")]
    """The total monetary amount of the order."""

    cost_currency: Annotated[str, PropertyInfo(alias="cost.currency")]
    """Filter by ISO 4217 currency string."""

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

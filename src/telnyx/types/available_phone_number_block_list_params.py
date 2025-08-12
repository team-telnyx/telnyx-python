# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AvailablePhoneNumberBlockListParams", "Filter"]


class AvailablePhoneNumberBlockListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[locality], filter[country_code],
    filter[national_destination_code], filter[phone_number_type]
    """


class Filter(TypedDict, total=False):
    country_code: str
    """Filter phone numbers by country."""

    locality: str
    """Filter phone numbers by city."""

    national_destination_code: str
    """Filter by the national destination code of the number."""

    phone_number_type: Literal["local", "toll_free", "mobile", "national", "shared_cost"]
    """Filter phone numbers by number type."""

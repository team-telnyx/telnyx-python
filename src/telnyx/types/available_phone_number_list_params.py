# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["AvailablePhoneNumberListParams", "Filter", "FilterPhoneNumber"]


class AvailablePhoneNumberListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[phone_number], filter[locality], filter[administrative_area],
    filter[country_code], filter[national_destination_code], filter[rate_center],
    filter[phone_number_type], filter[features], filter[limit], filter[best_effort],
    filter[quickship], filter[reservable], filter[exclude_held_numbers]
    """


class FilterPhoneNumber(TypedDict, total=False):
    contains: str
    """
    Filter numbers containing a pattern (excludes NDC if used with
    `national_destination_code` filter).
    """

    ends_with: str
    """
    Filter numbers ending with a pattern (excludes NDC if used with
    `national_destination_code` filter).
    """

    starts_with: str
    """
    Filter numbers starting with a pattern (excludes NDC if used with
    `national_destination_code` filter).
    """


class Filter(TypedDict, total=False):
    administrative_area: str
    """Find numbers in a particular US state or CA province."""

    best_effort: bool
    """Filter to determine if best effort results should be included.

    Only available in USA/CANADA.
    """

    country_code: str
    """Filter phone numbers by country."""

    exclude_held_numbers: bool
    """
    Filter to exclude phone numbers that are currently on hold/reserved for your
    account.
    """

    features: List[Literal["sms", "mms", "voice", "fax", "emergency", "hd_voice", "international_sms", "local_calling"]]
    """Filter phone numbers with specific features."""

    limit: int
    """Limits the number of results."""

    locality: str
    """Filter phone numbers by city."""

    national_destination_code: str
    """Filter by the national destination code of the number."""

    phone_number: FilterPhoneNumber
    """Filter phone numbers by pattern matching."""

    phone_number_type: Literal["local", "toll_free", "mobile", "national", "shared_cost"]
    """Filter phone numbers by number type."""

    quickship: bool
    """
    Filter to exclude phone numbers that need additional time after to purchase to
    activate. Only applicable for +1 toll_free numbers.
    """

    rate_center: str
    """Filter phone numbers by rate center.

    This filter is only applicable to USA and Canada numbers.
    """

    reservable: bool
    """Filter to ensure only numbers that can be reserved are included in the results."""

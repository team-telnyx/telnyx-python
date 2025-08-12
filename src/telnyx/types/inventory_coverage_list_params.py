# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["InventoryCoverageListParams", "Filter"]


class InventoryCoverageListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[npa], filter[nxx], filter[administrative_area],
    filter[phone_number_type], filter[country_code], filter[count],
    filter[features], filter[groupBy]
    """


class Filter(TypedDict, total=False):
    administrative_area: str
    """Filter by administrative area"""

    count: bool
    """Include count in the result"""

    country_code: Literal[
        "AT",
        "AU",
        "BE",
        "BG",
        "CA",
        "CH",
        "CN",
        "CY",
        "CZ",
        "DE",
        "DK",
        "EE",
        "ES",
        "FI",
        "FR",
        "GB",
        "GR",
        "HU",
        "HR",
        "IE",
        "IT",
        "LT",
        "LU",
        "LV",
        "NL",
        "NZ",
        "MX",
        "NO",
        "PL",
        "PT",
        "RO",
        "SE",
        "SG",
        "SI",
        "SK",
        "US",
    ]
    """Filter by country. Defaults to US"""

    features: List[Literal["sms", "mms", "voice", "fax", "emergency"]]
    """Filter if the phone number should be used for voice, fax, mms, sms, emergency.

    Returns features in the response when used.
    """

    group_by: Annotated[Literal["locality", "npa", "national_destination_code"], PropertyInfo(alias="groupBy")]
    """Filter to group results"""

    npa: int
    """Filter by npa"""

    nxx: int
    """Filter by nxx"""

    phone_number_type: Literal["local", "toll_free", "national", "mobile", "landline", "shared_cost"]
    """Filter by phone number type"""

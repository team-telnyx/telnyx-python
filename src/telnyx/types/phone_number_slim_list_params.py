# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PhoneNumberSlimListParams", "Filter", "FilterNumberType", "FilterVoiceConnectionName", "Page"]


class PhoneNumberSlimListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[tag], filter[phone_number], filter[status],
    filter[country_iso_alpha2], filter[connection_id],
    filter[voice.connection_name], filter[voice.usage_payment_method],
    filter[billing_group_id], filter[emergency_address_id],
    filter[customer_reference], filter[number_type], filter[source]
    """

    include_connection: bool
    """Include the connection associated with the phone number."""

    include_tags: bool
    """Include the tags associated with the phone number."""

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[size], page[number]
    """

    sort: Literal["purchased_at", "phone_number", "connection_name", "usage_payment_method"]
    """Specifies the sort order for results.

    If not given, results are sorted by created_at in descending order.
    """


class FilterNumberType(TypedDict, total=False):
    eq: Literal["local", "national", "toll_free", "mobile", "shared_cost"]
    """Filter phone numbers by phone number type."""


class FilterVoiceConnectionName(TypedDict, total=False):
    contains: str
    """Filter contains connection name.

    Requires at least three characters and the include_connection param.
    """

    ends_with: str
    """Filter ends with connection name.

    Requires at least three characters and the include_connection param.
    """

    eq: str
    """Filter by connection name."""

    starts_with: str
    """Filter starts with connection name.

    Requires at least three characters and the include_connection param.
    """


class Filter(TypedDict, total=False):
    billing_group_id: str
    """Filter by the billing_group_id associated with phone numbers.

    To filter to only phone numbers that have no billing group associated them, set
    the value of this filter to the string 'null'.
    """

    connection_id: str
    """Filter by connection_id."""

    country_iso_alpha2: Union[str, List[str]]
    """Filter by phone number country ISO alpha-2 code.

    Can be a single value or an array of values.
    """

    customer_reference: str
    """Filter numbers via the customer_reference set."""

    emergency_address_id: str
    """Filter by the emergency_address_id associated with phone numbers.

    To filter only phone numbers that have no emergency address associated with
    them, set the value of this filter to the string 'null'.
    """

    number_type: FilterNumberType
    """Filter phone numbers by phone number type."""

    phone_number: str
    """Filter by phone number.

    Requires at least three digits. Non-numerical characters will result in no
    values being returned.
    """

    source: Literal["ported", "purchased"]
    """Filter phone numbers by their source.

    Use 'ported' for numbers ported from other carriers, or 'purchased' for numbers
    bought directly from Telnyx.
    """

    status: Literal[
        "purchase-pending",
        "purchase-failed",
        "port_pending",
        "active",
        "deleted",
        "port-failed",
        "emergency-only",
        "ported-out",
        "port-out-pending",
    ]
    """Filter by phone number status."""

    tag: str
    """Filter by phone number tags. (This requires the include_tags param)"""

    voice_connection_name: Annotated[FilterVoiceConnectionName, PropertyInfo(alias="voice.connection_name")]
    """
    Filter by voice connection name pattern matching (requires include_connection
    param).
    """

    voice_usage_payment_method: Annotated[
        Literal["pay-per-minute", "channel"], PropertyInfo(alias="voice.usage_payment_method")
    ]
    """Filter by usage_payment_method."""


class Page(TypedDict, total=False):
    number: int
    """The page number to load"""

    size: int
    """The size of the page"""

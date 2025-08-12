# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CsvDownloadCreateParams", "Filter", "FilterVoiceConnectionName"]


class CsvDownloadCreateParams(TypedDict, total=False):
    csv_format: Literal["V1", "V2"]
    """Which format to use when generating the CSV file.

    The default for backwards compatibility is 'V1'
    """

    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[has_bundle], filter[tag], filter[connection_id],
    filter[phone_number], filter[status], filter[voice.connection_name],
    filter[voice.usage_payment_method], filter[billing_group_id],
    filter[emergency_address_id], filter[customer_reference]
    """


class FilterVoiceConnectionName(TypedDict, total=False):
    contains: str
    """Filter contains connection name. Requires at least three characters."""

    ends_with: str
    """Filter ends with connection name. Requires at least three characters."""

    eq: str
    """Filter by connection name."""

    starts_with: str
    """Filter starts with connection name. Requires at least three characters."""


class Filter(TypedDict, total=False):
    billing_group_id: str
    """Filter by the billing_group_id associated with phone numbers.

    To filter to only phone numbers that have no billing group associated them, set
    the value of this filter to the string 'null'.
    """

    connection_id: str
    """Filter by connection_id."""

    customer_reference: str
    """Filter numbers via the customer_reference set."""

    emergency_address_id: str
    """Filter by the emergency_address_id associated with phone numbers.

    To filter only phone numbers that have no emergency address associated with
    them, set the value of this filter to the string 'null'.
    """

    has_bundle: str
    """Filter by phone number that have bundles."""

    phone_number: str
    """Filter by phone number.

    Requires at least three digits. Non-numerical characters will result in no
    values being returned.
    """

    status: Literal[
        "purchase-pending",
        "purchase-failed",
        "port-pending",
        "active",
        "deleted",
        "port-failed",
        "emergency-only",
        "ported-out",
        "port-out-pending",
    ]
    """Filter by phone number status."""

    tag: str
    """Filter by phone number tags."""

    voice_connection_name: Annotated[FilterVoiceConnectionName, PropertyInfo(alias="voice.connection_name")]
    """Filter by voice connection name pattern matching."""

    voice_usage_payment_method: Annotated[
        Literal["pay-per-minute", "channel"], PropertyInfo(alias="voice.usage_payment_method")
    ]
    """Filter by usage_payment_method."""

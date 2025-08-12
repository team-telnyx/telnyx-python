# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .update_voice_settings_param import UpdateVoiceSettingsParam

__all__ = ["JobUpdateBatchParams", "Filter", "FilterVoiceConnectionName"]


class JobUpdateBatchParams(TypedDict, total=False):
    phone_numbers: Required[List[str]]
    """Array of phone number ids and/or phone numbers in E164 format to update.

    This parameter is required if no filter parameters are provided. If you want to
    update specific numbers rather than all numbers matching a filter, you must use
    this parameter. Each item must be either a valid phone number ID or a phone
    number in E164 format (e.g., '+13127367254').
    """

    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[has_bundle], filter[tag], filter[connection_id],
    filter[phone_number], filter[status], filter[voice.connection_name],
    filter[voice.usage_payment_method], filter[billing_group_id],
    filter[emergency_address_id], filter[customer_reference]
    """

    billing_group_id: str
    """Identifies the billing group associated with the phone number."""

    connection_id: str
    """Identifies the connection associated with the phone number."""

    customer_reference: str
    """A customer reference string for customer look ups."""

    external_pin: str
    """
    If someone attempts to port your phone number away from Telnyx and your phone
    number has an external PIN set, we will attempt to verify that you provided the
    correct external PIN to the winning carrier. Note that not all carriers
    cooperate with this security mechanism.
    """

    hd_voice_enabled: bool
    """Indicates whether to enable or disable HD Voice on each phone number.

    HD Voice is a paid feature and may not be available for all phone numbers, more
    details about it can be found in the Telnyx support documentation.
    """

    tags: List[str]
    """A list of user-assigned tags to help organize phone numbers."""

    voice: UpdateVoiceSettingsParam


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

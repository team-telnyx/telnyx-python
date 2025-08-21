# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PhoneNumberDetailed"]


class PhoneNumberDetailed(BaseModel):
    id: Optional[str] = None
    """Identifies the resource."""

    billing_group_id: Optional[str] = None
    """Identifies the billing group associated with the phone number."""

    call_forwarding_enabled: Optional[bool] = None
    """
    Indicates if call forwarding will be enabled for this number if forwards_to and
    forwarding_type are filled in. Defaults to true for backwards compatibility with
    APIV1 use of numbers endpoints.
    """

    call_recording_enabled: Optional[bool] = None
    """Indicates whether call recording is enabled for this number."""

    caller_id_name_enabled: Optional[bool] = None
    """Indicates whether caller ID is enabled for this number."""

    cnam_listing_enabled: Optional[bool] = None
    """Indicates whether a CNAM listing is enabled for this number."""

    connection_id: Optional[str] = None
    """Identifies the connection associated with the phone number."""

    connection_name: Optional[str] = None
    """
    The user-assigned name of the connection to be associated with this phone
    number.
    """

    country_iso_alpha2: Optional[str] = None
    """The ISO 3166-1 alpha-2 country code of the phone number."""

    created_at: Optional[str] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    customer_reference: Optional[str] = None
    """A customer reference string for customer look ups."""

    emergency_address_id: Optional[str] = None
    """Identifies the emergency address associated with the phone number."""

    emergency_enabled: Optional[bool] = None
    """Indicates whether emergency services are enabled for this number."""

    emergency_status: Optional[
        Literal["active", "deprovisioning", "disabled", "provisioning", "provisioning-failed"]
    ] = None
    """
    Indicates the status of the provisioning of emergency services for the phone
    number. This field contains information about activity that may be ongoing for a
    number where it either is being provisioned or deprovisioned but is not yet
    enabled/disabled.
    """

    external_pin: Optional[str] = None
    """
    If someone attempts to port your phone number away from Telnyx and your phone
    number has an external PIN set, Telnyx will attempt to verify that you provided
    the correct external PIN to the winning carrier. Note that not all carriers
    cooperate with this security mechanism.
    """

    inbound_call_screening: Optional[Literal["disabled", "reject_calls", "flag_calls"]] = None
    """
    The inbound_call_screening setting is a phone number configuration option
    variable that allows users to configure their settings to block or flag
    fraudulent calls. It can be set to disabled, reject_calls, or flag_calls. This
    feature has an additional per-number monthly cost associated with it.
    """

    messaging_profile_id: Optional[str] = None
    """Identifies the messaging profile associated with the phone number."""

    messaging_profile_name: Optional[str] = None
    """The name of the messaging profile associated with the phone number."""

    phone_number: Optional[str] = None
    """The +E.164-formatted phone number associated with this record."""

    phone_number_type: Optional[
        Literal[
            "local", "toll_free", "mobile", "national", "shared_cost", "landline", "tollfree", "shortcode", "longcode"
        ]
    ] = None
    """
    The phone number's type. Note: For numbers purchased prior to July 2023 or when
    fetching a number's details immediately after a purchase completes, the legacy
    values `tollfree`, `shortcode` or `longcode` may be returned instead.
    """

    purchased_at: Optional[str] = None
    """ISO 8601 formatted date indicating when the resource was purchased."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    source_type: Optional[Literal["number_order", "port_request"]] = None
    """Indicates if the phone number was purchased or ported in.

    For some numbers this information may not be available.
    """

    status: Optional[
        Literal[
            "purchase-pending",
            "purchase-failed",
            "port-pending",
            "port-failed",
            "active",
            "deleted",
            "emergency-only",
            "ported-out",
            "port-out-pending",
            "requirement-info-pending",
            "requirement-info-under-review",
            "requirement-info-exception",
            "provision-pending",
        ]
    ] = None
    """The phone number's current status."""

    t38_fax_gateway_enabled: Optional[bool] = None
    """Indicates whether T38 Fax Gateway for inbound calls to this number."""

    tags: Optional[List[str]] = None
    """A list of user-assigned tags to help manage the phone number."""

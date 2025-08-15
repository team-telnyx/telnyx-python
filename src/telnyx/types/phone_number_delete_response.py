# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PhoneNumberDeleteResponse", "Data"]


class Data(BaseModel):
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

    created_at: Optional[str] = None
    """
    ISO 8601 formatted date indicating when the time it took to activate after the
    purchase.
    """

    customer_reference: Optional[str] = None
    """A customer reference string for customer look ups."""

    emergency_address_id: Optional[str] = None
    """Identifies the emergency address associated with the phone number."""

    emergency_enabled: Optional[bool] = None
    """Indicates whether emergency services are enabled for this number."""

    external_pin: Optional[str] = None
    """
    If someone attempts to port your phone number away from Telnyx and your phone
    number has an external PIN set, Telnyx will attempt to verify that you provided
    the correct external PIN to the winning carrier. Note that not all carriers
    cooperate with this security mechanism.
    """

    messaging_profile_id: Optional[str] = None
    """Identifies the messaging profile associated with the phone number."""

    messaging_profile_name: Optional[str] = None
    """The name of the messaging profile associated with the phone number."""

    phone_number: Optional[str] = None
    """The +E.164-formatted phone number associated with this record."""

    phone_number_type: Optional[Literal["local", "toll_free", "mobile", "national", "shared_cost", "landline"]] = None
    """The phone number's type."""

    purchased_at: Optional[str] = None
    """
    ISO 8601 formatted date indicating the time the request was made to purchase the
    number.
    """

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

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
        ]
    ] = None
    """The phone number's current status."""

    t38_fax_gateway_enabled: Optional[bool] = None
    """Indicates whether T38 Fax Gateway for inbound calls to this number."""

    tags: Optional[List[str]] = None
    """A list of user-assigned tags to help manage the phone number."""

    updated_at: Optional[str] = None
    """ISO 8601 formatted date indicating when the resource was updated."""


class PhoneNumberDeleteResponse(BaseModel):
    data: Optional[Data] = None

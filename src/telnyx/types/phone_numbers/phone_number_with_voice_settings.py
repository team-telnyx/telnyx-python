# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .cnam_listing import CnamListing
from .call_recording import CallRecording
from .media_features import MediaFeatures
from .call_forwarding import CallForwarding

__all__ = ["PhoneNumberWithVoiceSettings", "Emergency"]


class Emergency(BaseModel):
    emergency_address_id: Optional[str] = None
    """Identifies the address to be used with emergency services."""

    emergency_enabled: Optional[bool] = None
    """Allows you to enable or disable emergency services on the phone number.

    In order to enable emergency services, you must also set an
    emergency_address_id.
    """

    emergency_status: Optional[
        Literal["disabled", "active", "provisioning", "deprovisioning", "provisioning-failed"]
    ] = None
    """Represents the state of the number regarding emergency activation."""


class PhoneNumberWithVoiceSettings(BaseModel):
    id: Optional[str] = None
    """Identifies the type of resource."""

    call_forwarding: Optional[CallForwarding] = None
    """The call forwarding settings for a phone number."""

    call_recording: Optional[CallRecording] = None
    """The call recording settings for a phone number."""

    cnam_listing: Optional[CnamListing] = None
    """The CNAM listing settings for a phone number."""

    connection_id: Optional[str] = None
    """Identifies the connection associated with this phone number."""

    customer_reference: Optional[str] = None
    """A customer reference string for customer look ups."""

    emergency: Optional[Emergency] = None
    """The emergency services settings for a phone number."""

    inbound_call_screening: Optional[Literal["disabled", "reject_calls", "flag_calls"]] = None
    """
    The inbound_call_screening setting is a phone number configuration option
    variable that allows users to configure their settings to block or flag
    fraudulent calls. It can be set to disabled, reject_calls, or flag_calls. This
    feature has an additional per-number monthly cost associated with it.
    """

    media_features: Optional[MediaFeatures] = None
    """The media features settings for a phone number."""

    phone_number: Optional[str] = None
    """The phone number in +E164 format."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    tech_prefix_enabled: Optional[bool] = None
    """Controls whether a tech prefix is enabled for this phone number."""

    translated_number: Optional[str] = None
    """
    This field allows you to rewrite the destination number of an inbound call
    before the call is routed to you. The value of this field may be any
    alphanumeric value, and the value will replace the number originally dialed.
    """

    usage_payment_method: Optional[Literal["pay-per-minute", "channel"]] = None
    """
    Controls whether a number is billed per minute or uses your concurrent channels.
    """

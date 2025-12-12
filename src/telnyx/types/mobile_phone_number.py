# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MobilePhoneNumber", "CallForwarding", "CallRecording", "CnamListing", "Inbound", "Outbound"]


class CallForwarding(BaseModel):
    call_forwarding_enabled: Optional[bool] = None

    forwarding_type: Optional[Literal["always", "on-failure"]] = None

    forwards_to: Optional[str] = None


class CallRecording(BaseModel):
    inbound_call_recording_channels: Optional[Literal["single", "dual"]] = None

    inbound_call_recording_enabled: Optional[bool] = None

    inbound_call_recording_format: Optional[Literal["wav", "mp3"]] = None


class CnamListing(BaseModel):
    cnam_listing_details: Optional[str] = None

    cnam_listing_enabled: Optional[bool] = None


class Inbound(BaseModel):
    interception_app_id: Optional[str] = None
    """The ID of the app that will intercept inbound calls."""

    interception_app_name: Optional[str] = None
    """The name of the app that will intercept inbound calls."""


class Outbound(BaseModel):
    interception_app_id: Optional[str] = None
    """The ID of the app that will intercept outbound calls."""

    interception_app_name: Optional[str] = None
    """The name of the app that will intercept outbound calls."""


class MobilePhoneNumber(BaseModel):
    id: Optional[str] = None
    """Identifies the resource."""

    call_forwarding: Optional[CallForwarding] = None

    call_recording: Optional[CallRecording] = None

    caller_id_name_enabled: Optional[bool] = None
    """Indicates if caller ID name is enabled."""

    cnam_listing: Optional[CnamListing] = None

    connection_id: Optional[str] = None
    """The ID of the connection associated with this number."""

    connection_name: Optional[str] = None
    """The name of the connection."""

    connection_type: Optional[str] = None
    """The type of the connection."""

    country_iso_alpha2: Optional[str] = None
    """The ISO 3166-1 alpha-2 country code of the number."""

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    customer_reference: Optional[str] = None
    """A customer reference string."""

    inbound: Optional[Inbound] = None

    inbound_call_screening: Optional[Literal["disabled", "reject_calls", "flag_calls"]] = None
    """The inbound call screening setting."""

    mobile_voice_enabled: Optional[bool] = None
    """Indicates if mobile voice is enabled."""

    noise_suppression: Optional[Literal["inbound", "outbound", "both", "disabled"]] = None
    """The noise suppression setting."""

    outbound: Optional[Outbound] = None

    phone_number: Optional[str] = None
    """The +E.164-formatted phone number."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    sim_card_id: Optional[str] = None
    """The ID of the SIM card associated with this number."""

    status: Optional[str] = None
    """The status of the phone number."""

    tags: Optional[List[str]] = None
    """A list of tags associated with the number."""

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was last updated."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..numbers_error_73c9788e53 import NumbersError73c9788e53
from ..shared.phone_numbers_job_phone_number import PhoneNumbersJobPhoneNumber

__all__ = [
    "NumbersPhoneNumbersJob",
    "FailedOperation",
    "Parameters",
    "ParametersVoice",
    "ParametersVoiceCallForwarding",
    "ParametersVoiceCallRecording",
    "ParametersVoiceCnamListing",
    "ParametersVoiceMediaFeatures",
    "PendingOperation",
    "SuccessfulOperation",
]


class FailedOperation(BaseModel):
    id: Optional[str] = None
    """The phone number's ID"""

    errors: Optional[List[NumbersError73c9788e53]] = None

    phone_number: Optional[str] = None
    """The phone number in e164 format."""


class ParametersVoiceCallForwarding(BaseModel):
    call_forwarding_enabled: Optional[bool] = None
    """Saved call_forwarding_enabled setting."""

    forwarding_type: Optional[str] = None
    """Saved forwarding_type setting."""

    forwards_to: Optional[str] = None
    """Saved forwards_to setting."""


class ParametersVoiceCallRecording(BaseModel):
    inbound_call_recording_channels: Optional[str] = None
    """Saved inbound_call_recording_channels setting."""

    inbound_call_recording_enabled: Optional[bool] = None
    """Saved inbound_call_recording_enabled setting."""

    inbound_call_recording_format: Optional[str] = None
    """Saved inbound_call_recording_format setting."""

    record_continue_on_hold: Optional[bool] = None
    """Saved record_continue_on_hold setting."""


class ParametersVoiceCnamListing(BaseModel):
    cnam_listing_details: Optional[str] = None
    """Saved cnam_listing_details setting."""

    cnam_listing_enabled: Optional[bool] = None
    """Saved cnam_listing_enabled setting."""


class ParametersVoiceMediaFeatures(BaseModel):
    accept_any_rtp_packets_enabled: Optional[bool] = None
    """Saved accept_any_rtp_packets_enabled setting."""

    rtp_auto_adjust_enabled: Optional[bool] = None
    """Saved rtp_auto_adjust_enabled setting."""

    t38_fax_gateway_enabled: Optional[bool] = None
    """Saved t38_fax_gateway_enabled setting."""


class ParametersVoice(BaseModel):
    """
    Saved voice settings for an update_phone_numbers job, using the public field names and nesting. Only settings present at creation are returned.
    """

    call_forwarding: Optional[ParametersVoiceCallForwarding] = None

    call_recording: Optional[ParametersVoiceCallRecording] = None

    caller_id_name_enabled: Optional[bool] = None
    """Saved caller_id_name_enabled setting."""

    cnam_listing: Optional[ParametersVoiceCnamListing] = None

    inbound_call_screening: Optional[str] = None
    """Saved inbound_call_screening setting."""

    media_features: Optional[ParametersVoiceMediaFeatures] = None

    tech_prefix_enabled: Optional[bool] = None
    """Saved tech_prefix_enabled setting."""

    usage_payment_method: Optional[str] = None
    """Saved usage_payment_method setting."""


class Parameters(BaseModel):
    """
    Effective parameters saved when the job was created, not a snapshot of the original HTTP request or current phone-number settings. Update jobs include the saved update fields; emergency-settings jobs include the saved emergency fields; delete jobs include only targets. Absent fields are omitted, and saved false, null and empty values are preserved. Tags may be normalized to arrays; filter-created jobs contain resolved target identifiers rather than the original filters. Historical jobs with no saved arguments return an empty object.
    """

    add_tags: Optional[List[str]] = None
    """Saved add_tags for an update_phone_numbers job.

    Values reflect creation-time normalization.
    """

    billing_group_id: Optional[str] = None
    """Saved billing_group_id supplied for an update_phone_numbers job."""

    connection_id: Optional[str] = None
    """Saved connection_id supplied for an update_phone_numbers job."""

    customer_reference: Optional[str] = None
    """Saved customer_reference supplied for an update_phone_numbers job."""

    deletion_lock_enabled: Optional[bool] = None
    """Saved deletion_lock_enabled supplied for an update_phone_numbers job."""

    emergency_address_id: Optional[str] = None
    """Saved emergency address identifier for an update_emergency_settings job.

    An explicitly supplied null is preserved.
    """

    emergency_enabled: Optional[bool] = None
    """Saved emergency-services setting for an update_emergency_settings job."""

    external_pin: Optional[str] = None
    """Saved external_pin supplied for an update_phone_numbers job."""

    hd_voice_enabled: Optional[bool] = None
    """Saved hd_voice_enabled supplied for an update_phone_numbers job."""

    phone_numbers: Optional[List[Union[str, int]]] = None
    """Saved target phone numbers in E.164 format and/or identifiers.

    Jobs created using filters contain the resolved identifiers, not the original
    filter expression. Stored identifier types are preserved.
    """

    remove_tags: Optional[List[str]] = None
    """Saved remove_tags for an update_phone_numbers job.

    Values reflect creation-time normalization.
    """

    tags: Optional[List[str]] = None
    """Saved tags for an update_phone_numbers job.

    Values reflect creation-time normalization.
    """

    voice: Optional[ParametersVoice] = None
    """
    Saved voice settings for an update_phone_numbers job, using the public field
    names and nesting. Only settings present at creation are returned.
    """


class PendingOperation(BaseModel):
    """The phone numbers pending confirmation on update results.

    Entries in this list are transient, and will be moved to either successful_operations or failed_operations once the processing is done.
    """

    id: Optional[str] = None
    """The phone number's ID"""

    phone_number: Optional[str] = None
    """The phone number in e164 format."""


class SuccessfulOperation(BaseModel):
    """The phone numbers successfully updated."""

    id: Optional[str] = None
    """The phone number's ID"""

    phone_number: Optional[str] = None
    """The phone number in e164 format."""


class NumbersPhoneNumbersJob(BaseModel):
    id: Optional[str] = None
    """Identifies the resource."""

    created_at: Optional[str] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    etc: Optional[datetime] = None
    """
    ISO 8601 formatted date indicating when the estimated time of completion of the
    background job.
    """

    failed_operations: Optional[List[FailedOperation]] = None

    parameters: Optional[Parameters] = None
    """
    Effective parameters saved when the job was created, not a snapshot of the
    original HTTP request or current phone-number settings. Update jobs include the
    saved update fields; emergency-settings jobs include the saved emergency fields;
    delete jobs include only targets. Absent fields are omitted, and saved false,
    null and empty values are preserved. Tags may be normalized to arrays;
    filter-created jobs contain resolved target identifiers rather than the original
    filters. Historical jobs with no saved arguments return an empty object.
    """

    pending_operations: Optional[List[PendingOperation]] = None

    phone_numbers: Optional[List[PhoneNumbersJobPhoneNumber]] = None

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    status: Optional[Literal["pending", "in_progress", "completed", "failed", "expired"]] = None
    """Indicates the completion status of the background update."""

    successful_operations: Optional[List[SuccessfulOperation]] = None

    type: Optional[Literal["update_emergency_settings", "delete_phone_numbers", "update_phone_numbers"]] = None
    """Identifies the type of the background job."""

    updated_at: Optional[str] = None
    """ISO 8601 formatted date indicating when the resource was updated."""

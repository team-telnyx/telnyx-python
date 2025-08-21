# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .cnam_listing_param import CnamListingParam
from .call_recording_param import CallRecordingParam
from .media_features_param import MediaFeaturesParam
from .call_forwarding_param import CallForwardingParam

__all__ = ["UpdateVoiceSettingsParam"]


class UpdateVoiceSettingsParam(TypedDict, total=False):
    call_forwarding: CallForwardingParam
    """The call forwarding settings for a phone number."""

    call_recording: CallRecordingParam
    """The call recording settings for a phone number."""

    caller_id_name_enabled: bool
    """Controls whether the caller ID name is enabled for this phone number."""

    cnam_listing: CnamListingParam
    """The CNAM listing settings for a phone number."""

    inbound_call_screening: Literal["disabled", "reject_calls", "flag_calls"]
    """
    The inbound_call_screening setting is a phone number configuration option
    variable that allows users to configure their settings to block or flag
    fraudulent calls. It can be set to disabled, reject_calls, or flag_calls. This
    feature has an additional per-number monthly cost associated with it.
    """

    media_features: MediaFeaturesParam
    """The media features settings for a phone number."""

    tech_prefix_enabled: bool
    """Controls whether a tech prefix is enabled for this phone number."""

    translated_number: str
    """
    This field allows you to rewrite the destination number of an inbound call
    before the call is routed to you. The value of this field may be any
    alphanumeric value, and the value will replace the number originally dialed.
    """

    usage_payment_method: Literal["pay-per-minute", "channel"]
    """
    Controls whether a number is billed per minute or uses your concurrent channels.
    """

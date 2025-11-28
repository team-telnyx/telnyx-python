# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["MobilePhoneNumberUpdateParams", "CallForwarding", "CallRecording", "CnamListing", "Inbound", "Outbound"]


class MobilePhoneNumberUpdateParams(TypedDict, total=False):
    call_forwarding: CallForwarding

    call_recording: CallRecording

    caller_id_name_enabled: bool

    cnam_listing: CnamListing

    connection_id: Optional[str]

    customer_reference: Optional[str]

    inbound: Inbound

    inbound_call_screening: Literal["disabled", "reject_calls", "flag_calls"]

    noise_suppression: bool

    outbound: Outbound

    tags: SequenceNotStr[str]


class CallForwarding(TypedDict, total=False):
    call_forwarding_enabled: bool

    forwarding_type: Optional[Literal["always", "on-failure"]]

    forwards_to: Optional[str]


class CallRecording(TypedDict, total=False):
    inbound_call_recording_channels: Literal["single", "dual"]

    inbound_call_recording_enabled: bool

    inbound_call_recording_format: Literal["wav", "mp3"]


class CnamListing(TypedDict, total=False):
    cnam_listing_details: Optional[str]

    cnam_listing_enabled: bool


class Inbound(TypedDict, total=False):
    interception_app_id: Optional[str]
    """
    The ID of the CallControl or TeXML Application that will intercept inbound
    calls.
    """


class Outbound(TypedDict, total=False):
    interception_app_id: Optional[str]
    """
    The ID of the CallControl or TeXML Application that will intercept outbound
    calls.
    """

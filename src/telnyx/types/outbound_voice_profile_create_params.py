# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

from .service_plan import ServicePlan
from .traffic_type import TrafficType
from .usage_payment_method import UsagePaymentMethod
from .outbound_call_recording_param import OutboundCallRecordingParam

__all__ = ["OutboundVoiceProfileCreateParams"]


class OutboundVoiceProfileCreateParams(TypedDict, total=False):
    name: Required[str]
    """A user-supplied name to help with organization."""

    billing_group_id: Optional[str]
    """The ID of the billing group associated with the outbound proflile.

    Defaults to null (for no group assigned).
    """

    call_recording: OutboundCallRecordingParam

    concurrent_call_limit: Optional[int]
    """Must be no more than your global concurrent call limit. Null means no limit."""

    daily_spend_limit: str
    """
    The maximum amount of usage charges, in USD, you want Telnyx to allow on this
    outbound voice profile in a day before disallowing new calls.
    """

    daily_spend_limit_enabled: bool
    """
    Specifies whether to enforce the daily_spend_limit on this outbound voice
    profile.
    """

    enabled: bool
    """Specifies whether the outbound voice profile can be used.

    Disabled profiles will result in outbound calls being blocked for the associated
    Connections.
    """

    max_destination_rate: float
    """
    Maximum rate (price per minute) for a Destination to be allowed when making
    outbound calls.
    """

    service_plan: ServicePlan
    """Indicates the coverage of the termination regions."""

    tags: List[str]

    traffic_type: TrafficType
    """Specifies the type of traffic allowed in this profile."""

    usage_payment_method: UsagePaymentMethod
    """Setting for how costs for outbound profile are calculated."""

    whitelisted_destinations: List[str]
    """
    The list of destinations you want to be able to call using this outbound voice
    profile formatted in alpha2.
    """

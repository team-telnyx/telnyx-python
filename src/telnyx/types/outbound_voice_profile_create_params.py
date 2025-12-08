# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
from .service_plan import ServicePlan
from .traffic_type import TrafficType
from .usage_payment_method import UsagePaymentMethod
from .outbound_call_recording_param import OutboundCallRecordingParam

__all__ = ["OutboundVoiceProfileCreateParams", "CallingWindow"]


class OutboundVoiceProfileCreateParams(TypedDict, total=False):
    name: Required[str]
    """A user-supplied name to help with organization."""

    billing_group_id: Optional[str]
    """The ID of the billing group associated with the outbound proflile.

    Defaults to null (for no group assigned).
    """

    call_recording: OutboundCallRecordingParam

    calling_window: CallingWindow
    """
    (BETA) Specifies the time window and call limits for calls made using this
    outbound voice profile. Note that all times are UTC in 24-hour clock time.
    """

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

    tags: SequenceNotStr[str]

    traffic_type: TrafficType
    """Specifies the type of traffic allowed in this profile."""

    usage_payment_method: UsagePaymentMethod
    """Setting for how costs for outbound profile are calculated."""

    whitelisted_destinations: SequenceNotStr[str]
    """
    The list of destinations you want to be able to call using this outbound voice
    profile formatted in alpha2.
    """


class CallingWindow(TypedDict, total=False):
    """
    (BETA) Specifies the time window and call limits for calls made using this outbound voice profile. Note that all times are UTC in 24-hour clock time.
    """

    calls_per_cld: int
    """
    (BETA) The maximum number of calls that can be initiated to a single called
    party (CLD) within the calling window. A null value means no limit.
    """

    end_time: str
    """
    (BETA) The UTC time of day (in HH:MM format, 24-hour clock) when calls are no
    longer allowed to start.
    """

    start_time: str
    """
    (BETA) The UTC time of day (in HH:MM format, 24-hour clock) when calls are
    allowed to start.
    """

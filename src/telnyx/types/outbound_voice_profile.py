# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .service_plan import ServicePlan
from .traffic_type import TrafficType
from .usage_payment_method import UsagePaymentMethod
from .outbound_call_recording import OutboundCallRecording

__all__ = ["OutboundVoiceProfile"]


class OutboundVoiceProfile(BaseModel):
    name: str
    """A user-supplied name to help with organization."""

    id: Optional[str] = None
    """Identifies the resource."""

    billing_group_id: Optional[str] = None
    """The ID of the billing group associated with the outbound proflile.

    Defaults to null (for no group assigned).
    """

    call_recording: Optional[OutboundCallRecording] = None

    concurrent_call_limit: Optional[int] = None
    """Must be no more than your global concurrent call limit. Null means no limit."""

    connections_count: Optional[int] = None
    """Amount of connections associated with this outbound voice profile."""

    created_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was created."""

    daily_spend_limit: Optional[str] = None
    """
    The maximum amount of usage charges, in USD, you want Telnyx to allow on this
    outbound voice profile in a day before disallowing new calls.
    """

    daily_spend_limit_enabled: Optional[bool] = None
    """
    Specifies whether to enforce the daily_spend_limit on this outbound voice
    profile.
    """

    enabled: Optional[bool] = None
    """Specifies whether the outbound voice profile can be used.

    Disabled profiles will result in outbound calls being blocked for the associated
    Connections.
    """

    max_destination_rate: Optional[float] = None
    """
    Maximum rate (price per minute) for a Destination to be allowed when making
    outbound calls.
    """

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    service_plan: Optional[ServicePlan] = None
    """Indicates the coverage of the termination regions."""

    tags: Optional[List[str]] = None

    traffic_type: Optional[TrafficType] = None
    """Specifies the type of traffic allowed in this profile."""

    updated_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was updated."""

    usage_payment_method: Optional[UsagePaymentMethod] = None
    """Setting for how costs for outbound profile are calculated."""

    whitelisted_destinations: Optional[List[str]] = None
    """
    The list of destinations you want to be able to call using this outbound voice
    profile formatted in alpha2.
    """

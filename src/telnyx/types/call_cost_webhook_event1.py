# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CallCostWebhookEvent", "Data", "DataPayload", "DataPayloadCostPart"]


class DataPayloadCostPart(BaseModel):
    billed_duration_secs: Optional[int] = None
    """The billed duration in seconds for this part of the call."""

    call_part: Optional[str] = None
    """The product component this cost applies to.

    Values are determined by the billing system (e.g. sip-trunking, call-control,
    call-recording). Not a fixed set — new values may appear as products evolve.
    """

    cost: Optional[str] = None
    """The cost for this part of the call."""

    currency: Optional[str] = None
    """The currency of the cost."""

    rate: Optional[str] = None
    """The per-minute rate applied."""


class DataPayload(BaseModel):
    billed_duration_secs: Optional[int] = None
    """The longest billed duration across all cost parts, in seconds."""

    billing_group_id: Optional[str] = None
    """Identifies the billing group associated with the call."""

    call_control_id: Optional[str] = None
    """Call ID used to issue commands via Call Control API."""

    call_leg_id: Optional[str] = None
    """ID that is unique to the call and can be used to correlate webhook events."""

    call_session_id: Optional[str] = None
    """
    ID that is unique to the call session and can be used to correlate webhook
    events. Call session is a group of related call legs that logically belong to
    the same phone call, e.g. an inbound and outbound leg of a transferred call.
    """

    client_state: Optional[str] = None
    """State received from a command. Base64-encoded."""

    connection_id: Optional[str] = None
    """Call Control App ID (formerly Telnyx connection ID) used in the call."""

    cost_parts: Optional[List[DataPayloadCostPart]] = None
    """Breakdown of costs by call part."""

    occurred_at: Optional[datetime] = None
    """ISO 8601 datetime of when the event occurred."""

    status: Optional[Literal["success", "error"]] = None
    """The status of the cost calculation (`success` or `error`)."""

    total_cost: Optional[str] = None
    """The total cost of the call."""


class Data(BaseModel):
    id: Optional[str] = None
    """Unique identifier of the event."""

    event_type: Optional[Literal["call.cost"]] = None
    """The type of event being delivered."""

    occurred_at: Optional[datetime] = None
    """ISO 8601 datetime of when the event occurred."""

    payload: Optional[DataPayload] = None

    record_type: Optional[Literal["event"]] = None
    """Identifies the type of the resource."""


class CallCostWebhookEvent(BaseModel):
    data: Optional[Data] = None

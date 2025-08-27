# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .sip_header import SipHeader
from .custom_sip_header import CustomSipHeader

__all__ = [
    "CallHangupWebhookEvent",
    "Data",
    "DataPayload",
    "DataPayloadCallQualityStats",
    "DataPayloadCallQualityStatsInbound",
    "DataPayloadCallQualityStatsOutbound",
]


class DataPayloadCallQualityStatsInbound(BaseModel):
    jitter_max_variance: Optional[str] = None
    """Maximum jitter variance for inbound audio."""

    jitter_packet_count: Optional[str] = None
    """Number of packets used for jitter calculation on inbound audio."""

    mos: Optional[str] = None
    """Mean Opinion Score (MOS) for inbound audio quality."""

    packet_count: Optional[str] = None
    """Total number of inbound audio packets."""

    skip_packet_count: Optional[str] = None
    """Number of skipped inbound packets (packet loss)."""


class DataPayloadCallQualityStatsOutbound(BaseModel):
    packet_count: Optional[str] = None
    """Total number of outbound audio packets."""

    skip_packet_count: Optional[str] = None
    """Number of skipped outbound packets (packet loss)."""


class DataPayloadCallQualityStats(BaseModel):
    inbound: Optional[DataPayloadCallQualityStatsInbound] = None
    """Inbound call quality statistics."""

    outbound: Optional[DataPayloadCallQualityStatsOutbound] = None
    """Outbound call quality statistics."""


class DataPayload(BaseModel):
    call_control_id: Optional[str] = None
    """Call ID used to issue commands via Call Control API."""

    call_leg_id: Optional[str] = None
    """ID that is unique to the call and can be used to correlate webhook events."""

    call_quality_stats: Optional[DataPayloadCallQualityStats] = None
    """Call quality statistics aggregated from the CHANNEL_HANGUP_COMPLETE event.

    Only includes metrics that are available (filters out nil values). Returns nil
    if no metrics are available.
    """

    call_session_id: Optional[str] = None
    """
    ID that is unique to the call session and can be used to correlate webhook
    events. Call session is a group of related call legs that logically belong to
    the same phone call, e.g. an inbound and outbound leg of a transferred call.
    """

    client_state: Optional[str] = None
    """State received from a command."""

    connection_id: Optional[str] = None
    """Call Control App ID (formerly Telnyx connection ID) used in the call."""

    custom_headers: Optional[List[CustomSipHeader]] = None
    """Custom headers set on answer command"""

    from_: Optional[str] = FieldInfo(alias="from", default=None)
    """Number or SIP URI placing the call."""

    hangup_cause: Optional[
        Literal[
            "call_rejected",
            "normal_clearing",
            "originator_cancel",
            "timeout",
            "time_limit",
            "user_busy",
            "not_found",
            "unspecified",
        ]
    ] = None
    """
    The reason the call was ended (`call_rejected`, `normal_clearing`,
    `originator_cancel`, `timeout`, `time_limit`, `user_busy`, `not_found` or
    `unspecified`).
    """

    hangup_source: Optional[Literal["caller", "callee", "unknown"]] = None
    """The party who ended the call (`callee`, `caller`, `unknown`)."""

    sip_hangup_cause: Optional[str] = None
    """The reason the call was ended (SIP response code).

    If the SIP response is unavailable (in inbound calls for example) this is set to
    `unspecified`.
    """

    sip_headers: Optional[List[SipHeader]] = None
    """User-to-User and Diversion headers from sip invite."""

    start_time: Optional[datetime] = None
    """ISO 8601 datetime of when the call started."""

    state: Optional[Literal["hangup"]] = None
    """State received from a command."""

    tags: Optional[List[str]] = None
    """Array of tags associated to number."""

    to: Optional[str] = None
    """Destination number or SIP URI of the call."""


class Data(BaseModel):
    id: Optional[str] = None
    """Identifies the type of resource."""

    event_type: Optional[Literal["call.hangup"]] = None
    """The type of event being delivered."""

    occurred_at: Optional[datetime] = None
    """ISO 8601 datetime of when the event occurred."""

    payload: Optional[DataPayload] = None

    record_type: Optional[Literal["event"]] = None
    """Identifies the type of the resource."""


class CallHangupWebhookEvent(BaseModel):
    data: Optional[Data] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .sip_header import SipHeader
from .custom_sip_header import CustomSipHeader

__all__ = ["CallInitiatedWebhookEvent", "Data", "DataPayload"]


class DataPayload(BaseModel):
    call_control_id: Optional[str] = None
    """Call ID used to issue commands via Call Control API."""

    call_leg_id: Optional[str] = None
    """ID that is unique to the call and can be used to correlate webhook events."""

    call_screening_result: Optional[str] = None
    """Call screening result."""

    call_session_id: Optional[str] = None
    """
    ID that is unique to the call session and can be used to correlate webhook
    events. Call session is a group of related call legs that logically belong to
    the same phone call, e.g. an inbound and outbound leg of a transferred call.
    """

    caller_id_name: Optional[str] = None
    """Caller id."""

    client_state: Optional[str] = None
    """State received from a command."""

    connection_codecs: Optional[str] = None
    """The list of comma-separated codecs enabled for the connection."""

    connection_id: Optional[str] = None
    """Call Control App ID (formerly Telnyx connection ID) used in the call."""

    custom_headers: Optional[List[CustomSipHeader]] = None
    """Custom headers from sip invite"""

    direction: Optional[Literal["incoming", "outgoing"]] = None
    """Whether the call is `incoming` or `outgoing`."""

    from_: Optional[str] = FieldInfo(alias="from", default=None)
    """Number or SIP URI placing the call."""

    offered_codecs: Optional[str] = None
    """The list of comma-separated codecs offered by caller."""

    shaken_stir_attestation: Optional[str] = None
    """SHAKEN/STIR attestation level."""

    shaken_stir_validated: Optional[bool] = None
    """Whether attestation was successfully validated or not."""

    sip_headers: Optional[List[SipHeader]] = None
    """User-to-User and Diversion headers from sip invite."""

    start_time: Optional[datetime] = None
    """ISO 8601 datetime of when the call started."""

    state: Optional[Literal["parked", "bridging"]] = None
    """State received from a command."""

    tags: Optional[List[str]] = None
    """Array of tags associated to number."""

    to: Optional[str] = None
    """Destination number or SIP URI of the call."""


class Data(BaseModel):
    id: Optional[str] = None
    """Identifies the type of resource."""

    event_type: Optional[Literal["call.initiated"]] = None
    """The type of event being delivered."""

    occurred_at: Optional[datetime] = None
    """ISO 8601 datetime of when the event occurred."""

    payload: Optional[DataPayload] = None

    record_type: Optional[Literal["event"]] = None
    """Identifies the type of the resource."""


class CallInitiatedWebhookEvent(BaseModel):
    data: Optional[Data] = None

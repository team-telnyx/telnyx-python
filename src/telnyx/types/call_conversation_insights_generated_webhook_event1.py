# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CallConversationInsightsGeneratedWebhookEvent", "Data", "DataPayload", "DataPayloadResult"]


class DataPayloadResult(BaseModel):
    insight_id: Optional[str] = None
    """ID that is unique to the insight result being generated for the call."""

    result: Union[str, object, None] = None
    """The result of the insight."""


class DataPayload(BaseModel):
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

    calling_party_type: Optional[Literal["pstn", "sip"]] = None
    """The type of calling party connection."""

    client_state: Optional[str] = None
    """State received from a command."""

    connection_id: Optional[str] = None
    """Call Control App ID (formerly Telnyx connection ID) used in the call."""

    insight_group_id: Optional[str] = None
    """ID that is unique to the insight group being generated for the call."""

    results: Optional[List[DataPayloadResult]] = None
    """Array of insight results being generated for the call."""


class Data(BaseModel):
    id: Optional[str] = None
    """Identifies the type of resource."""

    event_type: Optional[Literal["call.conversation_insights.generated"]] = None
    """The type of event being delivered."""

    occurred_at: Optional[datetime] = None
    """ISO 8601 datetime of when the event occurred."""

    payload: Optional[DataPayload] = None

    record_type: Optional[Literal["event"]] = None
    """Identifies the type of the resource."""


class CallConversationInsightsGeneratedWebhookEvent(BaseModel):
    data: Optional[Data] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CallAIGatherMessageHistoryUpdatedWebhookEvent", "Data", "DataPayload", "DataPayloadMessageHistory"]


class DataPayloadMessageHistory(BaseModel):
    content: Optional[str] = None
    """The content of the message"""

    role: Optional[Literal["assistant", "user"]] = None
    """The role of the message sender"""


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

    client_state: Optional[str] = None
    """State received from a command."""

    connection_id: Optional[str] = None
    """Telnyx connection ID used in the call."""

    from_: Optional[str] = FieldInfo(alias="from", default=None)
    """Number or SIP URI placing the call."""

    message_history: Optional[List[DataPayloadMessageHistory]] = None
    """The history of the messages exchanged during the AI gather"""

    to: Optional[str] = None
    """Destination number or SIP URI of the call."""


class Data(BaseModel):
    id: Optional[str] = None
    """Identifies the type of resource."""

    event_type: Optional[Literal["call.ai_gather.message_history_updated"]] = None
    """The type of event being delivered."""

    occurred_at: Optional[datetime] = None
    """ISO 8601 datetime of when the event occurred."""

    payload: Optional[DataPayload] = None

    record_type: Optional[Literal["event"]] = None
    """Identifies the type of the resource."""


class CallAIGatherMessageHistoryUpdatedWebhookEvent(BaseModel):
    data: Optional[Data] = None

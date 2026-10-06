# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CallConversationCreatedWebhookEvent", "Data", "DataPayload"]


class DataPayload(BaseModel):
    call_control_id: Optional[str] = None
    """Call ID used to issue commands via Call Control API."""

    call_leg_id: Optional[str] = None
    """ID that is unique to the call leg."""

    call_session_id: Optional[str] = None
    """ID that is unique to the call session (group of related call legs)."""

    calling_party_type: Optional[Literal["pstn", "sip"]] = None
    """The type of calling party connection."""

    client_state: Optional[str] = None
    """Base64-encoded state received from a command."""

    connection_id: Optional[str] = None
    """Call Control App ID (formerly Telnyx connection ID) used in the call."""

    conversation_id: Optional[str] = None
    """Unique identifier of the conversation created for this call."""

    from_: Optional[str] = FieldInfo(alias="from", default=None)
    """The caller's number or identifier."""

    to: Optional[str] = None
    """The callee's number or SIP address."""


class Data(BaseModel):
    """A conversation has been created for the call.

    Use the conversation ID to correlate subsequent conversation events.
    """

    id: Optional[str] = None
    """Unique identifier for the event."""

    created_at: Optional[datetime] = None
    """Timestamp when the event was created in the system."""

    event_type: Optional[Literal["call.conversation.created"]] = None
    """The type of event being delivered."""

    occurred_at: Optional[datetime] = None
    """ISO 8601 datetime of when the event occurred."""

    payload: Optional[DataPayload] = None

    record_type: Optional[Literal["event"]] = None
    """Identifies the type of the resource."""


class CallConversationCreatedWebhookEvent(BaseModel):
    data: Optional[Data] = None
    """A conversation has been created for the call.

    Use the conversation ID to correlate subsequent conversation events.
    """

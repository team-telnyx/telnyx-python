# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CallConversationStartFailedWebhookEvent", "Data", "DataPayload"]


class DataPayload(BaseModel):
    assistant_id: Optional[str] = None
    """Identifier of the AI assistant that failed to start."""

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

    from_: Optional[str] = FieldInfo(alias="from", default=None)
    """The caller's number or identifier."""

    reason: Optional[Literal["invalid_request", "service_error"]] = None
    """Why the conversation could not be started.

    `invalid_request`: the assistant request was rejected, for example because the
    assistant ID does not exist. `service_error`: the assistant could not be started
    because of an error on the Telnyx side.
    """

    to: Optional[str] = None
    """The callee's number or SIP address."""


class Data(BaseModel):
    """
    The AI assistant requested for the call could not be started, so no conversation was created. No `call.conversation.created` or `call.conversation.ended` is sent for this attempt.
    """

    id: Optional[str] = None
    """Unique identifier for the event."""

    created_at: Optional[datetime] = None
    """Timestamp when the event was created in the system."""

    event_type: Optional[Literal["call.conversation.start_failed"]] = None
    """The type of event being delivered."""

    occurred_at: Optional[datetime] = None
    """ISO 8601 datetime of when the event occurred."""

    payload: Optional[DataPayload] = None

    record_type: Optional[Literal["event"]] = None
    """Identifies the type of the resource."""


class CallConversationStartFailedWebhookEvent(BaseModel):
    data: Optional[Data] = None
    """
    The AI assistant requested for the call could not be started, so no conversation
    was created. No `call.conversation.created` or `call.conversation.ended` is sent
    for this attempt.
    """

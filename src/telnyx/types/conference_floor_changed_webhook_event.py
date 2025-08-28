# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ConferenceFloorChangedWebhookEvent", "Payload"]


class Payload(BaseModel):
    call_control_id: Optional[str] = None
    """Call Control ID of the new speaker."""

    call_leg_id: Optional[str] = None
    """Call Leg ID of the new speaker."""

    call_session_id: Optional[str] = None
    """Call Session ID of the new speaker."""

    client_state: Optional[str] = None
    """State received from a command."""

    conference_id: Optional[str] = None
    """Conference ID that had a speaker change event."""

    connection_id: Optional[str] = None
    """Call Control App ID (formerly Telnyx connection ID) used in the call."""

    occurred_at: Optional[datetime] = None
    """ISO 8601 datetime of when the event occurred."""


class ConferenceFloorChangedWebhookEvent(BaseModel):
    id: Optional[str] = None
    """Identifies the type of resource."""

    event_type: Optional[Literal["conference.floor.changed"]] = None
    """The type of event being delivered."""

    payload: Optional[Payload] = None

    record_type: Optional[Literal["event"]] = None
    """Identifies the type of the resource."""

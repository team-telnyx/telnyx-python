# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ConferenceSpeakStarted", "Payload"]


class Payload(BaseModel):
    conference_id: Optional[str] = None
    """ID of the conference the text was spoken in."""

    connection_id: Optional[str] = None
    """Call Control App ID (formerly Telnyx connection ID) used in the call."""

    creator_call_session_id: Optional[str] = None
    """ID that is unique to the call session that started the conference."""

    occurred_at: Optional[datetime] = None
    """ISO 8601 datetime of when the event occurred."""


class ConferenceSpeakStarted(BaseModel):
    id: Optional[str] = None
    """Identifies the type of resource."""

    event_type: Optional[Literal["conference.speak.started"]] = None
    """The type of event being delivered."""

    payload: Optional[Payload] = None

    record_type: Optional[Literal["event"]] = None
    """Identifies the type of the resource."""

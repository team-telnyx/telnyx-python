# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ConferenceSpeakEndedWebhookEvent", "Data", "DataPayload"]


class DataPayload(BaseModel):
    conference_id: Optional[str] = None
    """ID of the conference the text was spoken in."""

    connection_id: Optional[str] = None
    """Call Control App ID (formerly Telnyx connection ID) used in the call."""

    creator_call_session_id: Optional[str] = None
    """ID that is unique to the call session that started the conference."""

    occurred_at: Optional[datetime] = None
    """ISO 8601 datetime of when the event occurred."""


class Data(BaseModel):
    id: Optional[str] = None
    """Identifies the type of resource."""

    event_type: Optional[Literal["conference.speak.ended"]] = None
    """The type of event being delivered."""

    payload: Optional[DataPayload] = None

    record_type: Optional[Literal["event"]] = None
    """Identifies the type of the resource."""


class ConferenceSpeakEndedWebhookEvent(BaseModel):
    data: Optional[Data] = None

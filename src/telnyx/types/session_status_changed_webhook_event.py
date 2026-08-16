# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SessionStatusChangedWebhookEvent", "Data"]


class Data(BaseModel):
    """Status transition details."""

    recording: bool
    """Whether the session is recording at this lifecycle edge."""

    session_id: str
    """The meeting session this event belongs to."""

    status: str
    """The new session status."""

    status_detail: Optional[str] = None
    """
    Additional detail about the status (for example `timeout_exceeded_everyone_left`
    or `cancelled`), or null.
    """


class SessionStatusChangedWebhookEvent(BaseModel):
    id: str
    """Unique event id; deduplicate deliveries on it."""

    data: Data
    """Status transition details."""

    event: Literal["session.status_changed"]
    """Event type."""

    occurred_at: datetime
    """When the event occurred."""

    version: str
    """Envelope version."""

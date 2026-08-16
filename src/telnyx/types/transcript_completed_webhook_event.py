# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TranscriptCompletedWebhookEvent", "Data"]


class Data(BaseModel):
    """Finalized transcript details."""

    ended_at: Optional[datetime] = None
    """Session end time, or null when unavailable."""

    last_seq: Optional[int] = None
    """Last transcript segment sequence number, or null for an empty transcript."""

    segment_count: int
    """Number of transcript segments observed during finalization."""

    session_id: str
    """The meeting session this event belongs to."""


class TranscriptCompletedWebhookEvent(BaseModel):
    id: str
    """Unique event id; deduplicate deliveries on it."""

    data: Data
    """Finalized transcript details."""

    event: Literal["transcript.completed"]
    """Event type."""

    occurred_at: datetime
    """When the event occurred."""

    version: str
    """Envelope version."""

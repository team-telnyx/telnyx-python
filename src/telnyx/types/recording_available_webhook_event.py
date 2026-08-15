# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RecordingAvailableWebhookEvent", "Data"]


class Data(BaseModel):
    """Available recording types."""

    recording_types: List[str]
    """Available recording types."""

    session_id: str
    """The meeting session this event belongs to."""


class RecordingAvailableWebhookEvent(BaseModel):
    id: str
    """Unique event id; deduplicate deliveries on it."""

    data: Data
    """Available recording types."""

    event: Literal["recording.available"]
    """Event type."""

    occurred_at: datetime
    """When the event occurred."""

    version: str
    """Envelope version."""

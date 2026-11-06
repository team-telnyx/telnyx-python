# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RecordingExportedWebhookEvent", "Data"]


class Data(BaseModel):
    bucket: str

    bytes: int

    key: str

    region: str

    session_id: str

    sha256: str

    type: Literal["video"]


class RecordingExportedWebhookEvent(BaseModel):
    id: str
    """Unique event id; deduplicate deliveries on it."""

    data: Data

    event: Literal["recording.exported"]
    """Event type."""

    occurred_at: datetime
    """When the event occurred."""

    version: str
    """Envelope version."""

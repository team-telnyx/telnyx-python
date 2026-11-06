# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RecordingExportFailedWebhookEvent", "Data"]


class Data(BaseModel):
    bucket: str

    key: str

    reason: Literal[
        "invalid_target",
        "invalid_media",
        "source_changed",
        "source_unavailable",
        "too_large",
        "storage_unavailable",
        "object_conflict",
        "verification_failed",
        "worker_lost",
        "internal_error",
    ]

    region: str

    session_id: str

    type: Literal["video"]


class RecordingExportFailedWebhookEvent(BaseModel):
    id: str
    """Unique event id; deduplicate deliveries on it."""

    data: Data

    event: Literal["recording.export_failed"]
    """Event type."""

    occurred_at: datetime
    """When the event occurred."""

    version: str
    """Envelope version."""

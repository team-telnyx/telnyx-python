# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ArtifactFailedWebhookEvent", "Data"]


class Data(BaseModel):
    """Failed artifact reference and reason."""

    artifact_id: str
    """Id of the failed artifact."""

    session_id: str
    """The meeting session this event belongs to."""

    type: Literal["summary", "action_items"]
    """Type of the failed artifact."""


class ArtifactFailedWebhookEvent(BaseModel):
    id: str
    """Unique event id; deduplicate deliveries on it."""

    data: Data
    """Failed artifact reference and reason."""

    event: Literal["artifact.failed"]
    """Event type."""

    occurred_at: datetime
    """When the event occurred."""

    version: str
    """Envelope version."""

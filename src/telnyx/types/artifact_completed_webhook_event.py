# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ArtifactCompletedWebhookEvent", "Data", "DataContent", "DataModelProvenance"]


class DataContent(BaseModel):
    """Generated artifact content."""

    text: str
    """Generated artifact text."""


class DataModelProvenance(BaseModel):
    """Model that generated the artifact."""

    model: str

    provider: str


class Data(BaseModel):
    """Completed artifact, including its generated content."""

    artifact_id: str
    """Id of the completed artifact."""

    content: DataContent
    """Generated artifact content."""

    api_model_provenance: DataModelProvenance = FieldInfo(alias="model_provenance")
    """Model that generated the artifact."""

    session_id: str
    """The meeting session this event belongs to."""

    type: Literal["summary", "action_items"]
    """Type of the completed artifact."""


class ArtifactCompletedWebhookEvent(BaseModel):
    id: str
    """Unique event id; deduplicate deliveries on it."""

    data: Data
    """Completed artifact, including its generated content."""

    event: Literal["artifact.completed"]
    """Event type."""

    occurred_at: datetime
    """When the event occurred."""

    version: str
    """Envelope version."""

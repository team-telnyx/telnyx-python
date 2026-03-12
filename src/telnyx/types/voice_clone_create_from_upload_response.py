# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VoiceCloneCreateFromUploadResponse", "Data"]


class Data(BaseModel):
    """A voice clone object."""

    id: Optional[str] = None
    """Unique identifier for the voice clone."""

    created_at: Optional[datetime] = None
    """Timestamp when the voice clone was created."""

    gender: Optional[Literal["male", "female", "neutral"]] = None
    """Gender of the voice clone."""

    label: Optional[str] = None
    """Voice style description.

    If not explicitly set on upload, falls back to the source design's prompt text.
    """

    language: Optional[str] = None
    """ISO 639-1 language code of the voice clone."""

    name: Optional[str] = None
    """Name of the voice clone."""

    record_type: Optional[Literal["voice_clone"]] = None
    """Identifies the resource type."""

    source_voice_design_id: Optional[str] = None
    """UUID of the source voice design. `null` for upload-based clones."""

    source_voice_design_version: Optional[int] = None
    """Version of the source voice design used. `null` for upload-based clones."""

    updated_at: Optional[datetime] = None
    """Timestamp when the voice clone was last updated."""


class VoiceCloneCreateFromUploadResponse(BaseModel):
    """Response envelope for a single voice clone."""

    data: Optional[Data] = None
    """A voice clone object."""

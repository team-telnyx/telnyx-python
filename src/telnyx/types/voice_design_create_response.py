# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VoiceDesignCreateResponse", "Data"]


class Data(BaseModel):
    """A voice design object with full version detail."""

    id: Optional[str] = None
    """Unique identifier for the voice design."""

    created_at: Optional[datetime] = None
    """Timestamp when the voice design was first created."""

    name: Optional[str] = None
    """Name of the voice design."""

    prompt: Optional[str] = None
    """Natural language prompt used to define the voice style for this version."""

    record_type: Optional[Literal["voice_design"]] = None
    """Identifies the resource type."""

    text: Optional[str] = None
    """Sample text used to synthesize this version."""

    updated_at: Optional[datetime] = None
    """Timestamp when the voice design was last updated."""

    version: Optional[int] = None
    """Version number of this voice design."""

    version_created_at: Optional[datetime] = None
    """Timestamp when this specific version was created."""

    voice_sample_size: Optional[int] = None
    """Size of the voice sample audio in bytes."""


class VoiceDesignCreateResponse(BaseModel):
    """Response envelope for a single voice design with full version detail."""

    data: Optional[Data] = None
    """A voice design object with full version detail."""

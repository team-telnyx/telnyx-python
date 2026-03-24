# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VoiceDesignRenameResponse", "Data"]


class Data(BaseModel):
    """A summarized voice design object (without version-specific fields)."""

    id: Optional[str] = None
    """Unique identifier for the voice design."""

    created_at: Optional[datetime] = None
    """Timestamp when the voice design was first created."""

    name: Optional[str] = None
    """Name of the voice design."""

    provider: Optional[Literal["telnyx", "minimax"]] = None
    """Voice synthesis provider used for this design."""

    provider_supported_models: Optional[List[str]] = None
    """List of TTS model identifiers supported by this design's provider."""

    record_type: Optional[Literal["voice_design"]] = None
    """Identifies the resource type."""

    updated_at: Optional[datetime] = None
    """Timestamp when the voice design was last updated."""


class VoiceDesignRenameResponse(BaseModel):
    """
    Response envelope for a voice design after a rename operation (no version-specific fields).
    """

    data: Optional[Data] = None
    """A summarized voice design object (without version-specific fields)."""

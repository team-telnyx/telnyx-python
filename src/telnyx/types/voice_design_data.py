# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VoiceDesignData"]


class VoiceDesignData(BaseModel):
    """A voice design object with full version detail."""

    id: Optional[str] = None
    """Unique identifier for the voice design."""

    created_at: Optional[datetime] = None
    """Timestamp when the voice design was first created."""

    name: Optional[str] = None
    """Name of the voice design."""

    prompt: Optional[str] = None
    """Natural language prompt used to define the voice style for this version."""

    provider: Optional[Literal["telnyx", "minimax"]] = None
    """Voice synthesis provider used for this design."""

    provider_supported_models: Optional[List[str]] = None
    """List of TTS model identifiers supported by this design's provider (e.g.

    `Qwen3TTS`, `speech-02-turbo`).
    """

    provider_voice_id: Optional[str] = None
    """Provider-specific voice identifier.

    For Telnyx designs this is the design version ID; for Minimax it is the
    Minimax-assigned voice ID.
    """

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

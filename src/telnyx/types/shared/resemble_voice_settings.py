# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ResembleVoiceSettings"]


class ResembleVoiceSettings(BaseModel):
    type: Literal["resemble"]
    """Voice settings provider type"""

    format: Optional[Literal["wav", "mp3"]] = None
    """Output audio format."""

    precision: Optional[Literal["PCM_16", "PCM_24", "PCM_32", "MULAW"]] = None
    """Audio precision format."""

    sample_rate: Optional[Literal["8000", "16000", "22050", "32000", "44100", "48000"]] = None
    """Audio sample rate in Hz."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ResembleVoiceSettings"]


class ResembleVoiceSettings(TypedDict, total=False):
    type: Required[Literal["resemble"]]
    """Voice settings provider type"""

    format: Literal["wav", "mp3"]
    """Output audio format."""

    precision: Literal["PCM_16", "PCM_24", "PCM_32", "MULAW"]
    """Audio precision format."""

    sample_rate: Literal["8000", "16000", "22050", "32000", "44100", "48000"]
    """Audio sample rate in Hz."""

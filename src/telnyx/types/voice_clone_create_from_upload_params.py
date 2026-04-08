# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import FileTypes

__all__ = ["VoiceCloneCreateFromUploadParams"]


class VoiceCloneCreateFromUploadParams(TypedDict, total=False):
    audio_file: Required[FileTypes]
    """Audio file to clone the voice from.

    Supported formats: WAV, MP3, FLAC, OGG, M4A. For best quality, provide 5–10
    seconds of clear, uninterrupted speech. Maximum size: 5MB for Telnyx, 20MB for
    Minimax.
    """

    language: Required[str]
    """ISO 639-1 language code (e.g. `en`, `fr`) or `auto` for automatic detection."""

    name: Required[str]
    """Name for the voice clone."""

    gender: Literal["male", "female", "neutral"]
    """Gender of the voice clone."""

    label: str
    """Optional custom label describing the voice style.

    If omitted, falls back to the source design's prompt text.
    """

    provider: Literal["telnyx", "minimax", "Telnyx", "Minimax"]
    """Voice synthesis provider. Case-insensitive. Defaults to `telnyx`."""

    ref_text: str
    """Optional transcript of the audio file. Providing this improves clone quality."""

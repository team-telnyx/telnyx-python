# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import FileTypes

__all__ = ["VoiceCloneCreateFromUploadParams", "TelnyxQwen3TtsClone", "TelnyxUltraClone", "MinimaxClone"]


class TelnyxQwen3TtsClone(TypedDict, total=False):
    audio_file: Required[FileTypes]
    """Audio file to clone the voice from.

    Supported formats: WAV, MP3, FLAC, OGG, M4A. For best quality, provide 5–10
    seconds of clear, uninterrupted speech. Maximum size: 5MB.
    """

    gender: Required[Literal["male", "female", "neutral"]]
    """Gender of the voice clone."""

    language: Required[str]
    """ISO 639-1 language code from the Qwen language set."""

    name: Required[str]
    """Name for the voice clone."""

    provider: Required[Literal["telnyx", "Telnyx"]]
    """Voice synthesis provider. Must be `telnyx`."""

    label: str
    """Optional custom label describing the voice style."""

    model_id: Optional[Literal["Qwen3TTS"]]
    """TTS model identifier. Nullable/omittable — defaults to Qwen3TTS."""

    ref_text: str
    """Optional transcript of the audio file. Providing this improves clone quality."""


class TelnyxUltraClone(TypedDict, total=False):
    audio_file: Required[FileTypes]
    """Audio file to clone the voice from.

    Supported formats: WAV, MP3, FLAC, OGG, M4A. For best quality, provide 5–10
    seconds of clear, uninterrupted speech. Maximum size: 5MB.
    """

    gender: Required[Literal["male", "female", "neutral"]]
    """Gender of the voice clone."""

    language: Required[str]
    """ISO 639-1 language code from the Ultra language set (40 languages)."""

    model_id: Required[Literal["Ultra"]]
    """TTS model identifier. Must be `Ultra`."""

    name: Required[str]
    """Name for the voice clone."""

    provider: Required[Literal["telnyx", "Telnyx"]]
    """Voice synthesis provider. Must be `telnyx`."""

    label: str
    """Optional custom label describing the voice style."""

    ref_text: str
    """Optional transcript of the audio file. Providing this improves clone quality."""


class MinimaxClone(TypedDict, total=False):
    audio_file: Required[FileTypes]
    """Audio file to clone the voice from.

    Supported formats: WAV, MP3, FLAC, OGG, M4A. For best quality, provide 5–10
    seconds of clear, uninterrupted speech. Maximum size: 20MB.
    """

    gender: Required[Literal["male", "female", "neutral"]]
    """Gender of the voice clone."""

    language: Required[str]
    """ISO 639-1 language code from the Minimax language set."""

    name: Required[str]
    """Name for the voice clone."""

    provider: Required[Literal["minimax", "Minimax"]]
    """Voice synthesis provider. Must be `minimax`."""

    label: str
    """Optional custom label describing the voice style."""

    model_id: Optional[Literal["speech-2.8-turbo"]]
    """TTS model identifier. Nullable — defaults to speech-2.8-turbo."""

    ref_text: str
    """Optional transcript of the audio file. Providing this improves clone quality."""


VoiceCloneCreateFromUploadParams: TypeAlias = Union[TelnyxQwen3TtsClone, TelnyxUltraClone, MinimaxClone]

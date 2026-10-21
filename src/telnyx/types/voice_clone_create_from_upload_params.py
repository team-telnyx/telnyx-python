# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import FileTypes

__all__ = [
    "VoiceCloneCreateFromUploadParams",
    "VoiceCloneUploadRequest",
    "VoiceCloneUploadRequestTelnyxQwen3TtsClone",
    "VoiceCloneUploadRequestTelnyxUltraClone",
    "VoiceCloneUploadRequestTelnyxBayanClone",
    "VoiceCloneUploadRequestMinimaxClone",
]


class VoiceCloneCreateFromUploadParams(TypedDict, total=False):
    voice_clone_upload_request: Required[VoiceCloneUploadRequest]
    """Multipart form data for creating a voice clone from a direct audio upload.

    Maximum file size: 20MB.
    """


class VoiceCloneUploadRequestTelnyxQwen3TtsClone(TypedDict, total=False):
    """Upload-based voice clone using the Telnyx Qwen3TTS model (default)."""

    audio_file: Required[FileTypes]
    """Audio file to clone the voice from.

    Supported formats: WAV, MP3, FLAC, OGG, M4A. For best quality, provide 5–10
    seconds of clear, uninterrupted speech. Maximum size: 20MB.
    """

    gender: Required[Literal["male", "female", "neutral"]]
    """Gender of the voice clone."""

    language: Required[str]
    """ISO 639-1 language code from the Qwen language set."""

    name: Required[str]
    """Name for the voice clone."""

    provider: Required[Literal["telnyx", "minimax"]]
    """Voice synthesis provider. Must be `telnyx`."""

    label: str
    """Optional custom label describing the voice style."""

    model_id: Optional[Literal["Qwen3TTS"]]
    """TTS model identifier. Nullable/omittable — defaults to Qwen3TTS."""

    ref_text: str
    """Optional transcript of the audio file. Providing this improves clone quality."""


class VoiceCloneUploadRequestTelnyxUltraClone(TypedDict, total=False):
    """Upload-based voice clone using the Telnyx Ultra model."""

    audio_file: Required[FileTypes]
    """Audio file to clone the voice from.

    Supported formats: WAV, MP3, FLAC, OGG, M4A. For best quality, provide up to 60
    seconds of clear, uninterrupted speech. Maximum size: 20MB.
    """

    gender: Required[Literal["male", "female", "neutral"]]
    """Gender of the voice clone."""

    language: Required[str]
    """ISO 639-1 language code from the Ultra language set (42 languages)."""

    model_id: Required[Literal["Ultra"]]
    """TTS model identifier. Must be `Ultra`."""

    name: Required[str]
    """Name for the voice clone."""

    provider: Required[Literal["telnyx", "minimax"]]
    """Voice synthesis provider. Must be `telnyx`."""

    label: str
    """Optional custom label describing the voice style."""

    ref_text: str
    """Optional transcript of the audio file. Providing this improves clone quality."""


class VoiceCloneUploadRequestTelnyxBayanClone(TypedDict, total=False):
    """Upload-based voice clone using the Telnyx Bayan model (Arabic and English).

    The clone is `active` on creation. Use it as voice `Telnyx.Bayan.<clone_id>`.
    """

    audio_file: Required[FileTypes]
    """Audio file to clone the voice from.

    Supported formats: WAV, MP3, FLAC, OGG, M4A. Converted to 24 kHz mono WAV and
    trimmed to the first 10 seconds. For best quality, provide about 10 seconds of
    clean, single-speaker speech. Maximum size: 20MB.
    """

    gender: Required[Literal["male", "female", "neutral"]]
    """Gender of the voice clone."""

    model_id: Required[Literal["Bayan"]]
    """TTS model identifier. Must be `Bayan`."""

    name: Required[str]
    """Name for the voice clone."""

    ref_text: Required[str]
    """Exact transcript of the reference audio.

    Required for Bayan: a missing, empty, or whitespace-only value returns `422`
    with `source.pointer` `/ref_text`. An inaccurate transcript can make synthesis
    with the clone truncated or garbled. Record a known script of about 10 seconds
    and pass it verbatim.
    """

    label: str
    """Optional custom label describing the voice style."""

    language: Literal["ar", "en"]
    """Language of the reference audio: `ar` (Arabic) or `en` (English).

    Defaults to `ar`. Other values return `422`.
    """

    provider: Literal["telnyx", "Telnyx"]
    """Voice synthesis provider. Defaults to `telnyx`."""


class VoiceCloneUploadRequestMinimaxClone(TypedDict, total=False):
    """Upload-based voice clone using the Minimax provider."""

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

    provider: Required[Literal["telnyx", "minimax"]]
    """Voice synthesis provider. Must be `minimax`."""

    label: str
    """Optional custom label describing the voice style."""

    model_id: Optional[Literal["speech-2.8-turbo"]]
    """TTS model identifier. Nullable — defaults to speech-2.8-turbo."""

    ref_text: str
    """Optional transcript of the audio file. Providing this improves clone quality."""


VoiceCloneUploadRequest: TypeAlias = Union[
    VoiceCloneUploadRequestTelnyxQwen3TtsClone,
    VoiceCloneUploadRequestTelnyxUltraClone,
    VoiceCloneUploadRequestTelnyxBayanClone,
    VoiceCloneUploadRequestMinimaxClone,
]

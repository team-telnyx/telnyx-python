# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TextToSpeechGenerateSpeechParams"]


class TextToSpeechGenerateSpeechParams(TypedDict, total=False):
    audio_format: Literal["pcm", "wav", "mp3"]
    """Audio output format override.

    Supported for Telnyx models. `pcm` and `wav` are available for
    `Natural`/`NaturalHD` models. The `Ultra` model outputs PCM at 24kHz s16le or
    MP3 at 128kbps 24kHz.
    """

    disable_cache: bool
    """When `true`, bypass the audio cache and generate fresh audio."""

    model_id: str
    """Model identifier for the chosen provider.

    Examples: `Natural`, `NaturalHD`, `Ultra` (Telnyx); `Polly.Generative` (AWS).
    """

    provider: Literal["aws", "telnyx", "azure", "elevenlabs", "minimax", "murfai", "rime", "resemble", "xai"]
    """TTS provider.

    Defaults to `telnyx` if not specified. Ignored when `voice` is provided.
    """

    socket_id: str
    """Client-provided socket identifier for tracking.

    If not provided, one is generated server-side.
    """

    voice: str
    """
    Voice identifier in the format `provider.model_id.voice_id` or
    `provider.voice_id` (e.g. `telnyx.NaturalHD.Telnyx_Alloy`,
    `Telnyx.Ultra.<voice_id>`, or `azure.en-US-AvaMultilingualNeural`). When
    provided, the `provider`, `model_id`, and `voice_id` are extracted
    automatically. Takes precedence over individual `provider`/`model_id`/`voice_id`
    parameters.
    """

    voice_id: str
    """Voice identifier for the chosen provider."""

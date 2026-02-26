# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TextToSpeechGenerateSpeechParams"]


class TextToSpeechGenerateSpeechParams(TypedDict, total=False):
    text: Required[str]
    """The text to convert to speech"""

    voice: Required[str]
    """The voice ID in the format Provider.ModelId.VoiceId.

    Examples:

    - AWS.Polly.Joanna-Neural
    - Azure.en-US-AvaMultilingualNeural
    - ElevenLabs.eleven_multilingual_v2.Rachel
    - Telnyx.KokoroTTS.af

    Use the `GET /text-to-speech/voices` endpoint to get a complete list of
    available voices.
    """

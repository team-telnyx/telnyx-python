# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TranscriptionConfigParam"]


class TranscriptionConfigParam(TypedDict, total=False):
    model: str
    """The speech to text model to be used by the voice assistant.

    - `distil-whisper/distil-large-v2` is lower latency but English-only.
    - `openai/whisper-large-v3-turbo` is multi-lingual with automatic language
      detection but slightly higher latency.
    - `google` is a multi-lingual option, please describe the language in the
      `language` field.
    """

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TranscriptionConfigParam"]


class TranscriptionConfigParam(TypedDict, total=False):
    """The settings associated with speech to text for the voice assistant.

    This is only relevant if the assistant uses a text-to-text language model. Any assistant using a model with native audio support (e.g. `fixie-ai/ultravox-v0_4`) will ignore this field.
    """

    model: str
    """The speech to text model to be used by the voice assistant.

    - `distil-whisper/distil-large-v2` is lower latency but English-only.
    - `openai/whisper-large-v3-turbo` is multi-lingual with automatic language
      detection but slightly higher latency.
    - `google` is a multi-lingual option, please describe the language in the
      `language` field.
    """

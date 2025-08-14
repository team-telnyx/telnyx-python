# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["TranscriptionSettings"]


class TranscriptionSettings(BaseModel):
    language: Optional[str] = None
    """The language of the audio to be transcribed.

    This is only applicable for `openai/whisper-large-v3-turbo` model. If not set,
    of if set to `auto`, the model will automatically detect the language. For the
    full list of supported languages, see the
    [whisper tokenizer](https://github.com/openai/whisper/blob/main/whisper/tokenizer.py).
    """

    model: Optional[str] = None
    """The speech to text model to be used by the voice assistant.

    - `distil-whisper/distil-large-v2` is lower latency but English-only.
    - `openai/whisper-large-v3-turbo` is multi-lingual with automatic language
      detection but slightly higher latency.
    """

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["AudioTranscribeParams"]


class AudioTranscribeParams(TypedDict, total=False):
    model: Required[
        Literal[
            "distil-whisper/distil-large-v2",
            "openai/whisper-large-v3-turbo",
            "deepgram/nova-2",
            "deepgram/nova-2-medical",
            "deepgram/nova-3",
            "deepgram/nova-3-medical",
        ]
    ]
    """ID of the model to use.

    `distil-whisper/distil-large-v2` is lower latency but English-only.
    `openai/whisper-large-v3-turbo` is multi-lingual but slightly higher latency.
    The `deepgram/*` models only accept mp3/wav files: `deepgram/nova-3` covers ~49
    languages plus `multi` and `deepgram/nova-2` covers ~33, while the `-medical`
    variants are tuned for clinical vocabulary and accept English only (`en` and its
    regional variants, e.g. `en-US`, `en-GB`).
    """

    file: FileTypes
    """
    The audio file object to transcribe, in one of these formats: flac, mp3, mp4,
    mpeg, mpga, m4a, ogg, wav, or webm. File uploads are limited to 100 MB. Cannot
    be used together with `file_url`. Note: the `deepgram/*` models only support mp3
    and wav formats.
    """

    file_url: str
    """
    Link to audio file in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a,
    ogg, wav, or webm. Support for hosted files is limited to 100MB. Cannot be used
    together with `file`. Note: the `deepgram/*` models only support mp3 and wav
    formats.
    """

    language: str
    """The language of the audio to be transcribed.

    `deepgram/nova-3` supports ~49 languages plus `multi`, and `deepgram/nova-2`
    supports ~33 plus `multi`; the `-medical` variants are English only (`en` and
    its regional variants, e.g. `en-US`, `en-GB`). Deepgram models validate on the
    base language and forward the full tag, so regional variants such as `de-CH` and
    `pt-BR` are accepted where the base language is supported; an unsupported
    language returns a 400. For `openai/whisper-large-v3-turbo`, supports multiple
    languages. `distil-whisper/distil-large-v2` does not support language parameter.
    """

    model_config: Dict[str, object]
    """Additional model-specific configuration parameters.

    Only allowed with the `deepgram/*` models. Can include Deepgram-specific options
    such as `smart_format`, `punctuate`, `diarize`, `utterance`, `numerals`, and
    `language`. If `language` is provided both as a top-level parameter and in
    `model_config`, the top-level parameter takes precedence.
    """

    response_format: Literal["json", "verbose_json"]
    """The format of the transcript output.

    Use `verbose_json` to take advantage of timestamps.
    """

    timestamp_granularities: Annotated[Literal["segment"], PropertyInfo(alias="timestamp_granularities[]")]
    """The timestamp granularities to populate for this transcription.

    `response_format` must be set verbose_json to use timestamp granularities.
    Currently `segment` is supported.
    """

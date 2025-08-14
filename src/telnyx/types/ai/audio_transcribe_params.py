# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["AudioTranscribeParams"]


class AudioTranscribeParams(TypedDict, total=False):
    model: Required[Literal["distil-whisper/distil-large-v2", "openai/whisper-large-v3-turbo"]]
    """ID of the model to use.

    `distil-whisper/distil-large-v2` is lower latency but English-only.
    `openai/whisper-large-v3-turbo` is multi-lingual but slightly higher latency.
    """

    file: FileTypes
    """
    The audio file object to transcribe, in one of these formats: flac, mp3, mp4,
    mpeg, mpga, m4a, ogg, wav, or webm. File uploads are limited to 100 MB. Cannot
    be used together with `file_url`
    """

    file_url: str
    """
    Link to audio file in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a,
    ogg, wav, or webm. Support for hosted files is limited to 100MB. Cannot be used
    together with `file`
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

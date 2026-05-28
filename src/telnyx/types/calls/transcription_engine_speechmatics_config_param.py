# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TranscriptionEngineSpeechmaticsConfigParam"]


class TranscriptionEngineSpeechmaticsConfigParam(TypedDict, total=False):
    interim_results: bool
    """Whether to send also interim results.

    If set to false, only final results will be sent.
    """

    language: Literal[
        "en",
        "ba",
        "eu",
        "gl",
        "ga",
        "mt",
        "mn",
        "sw",
        "ug",
        "cy",
        "ar_en",
        "cmn_en",
        "en_ms",
        "en_ta",
        "tl",
        "es-bilingual-en",
        "cmn_en_ms_ta",
    ]
    """Language to use for speech recognition"""

    transcription_engine: Literal["Speechmatics"]
    """Engine identifier for Speechmatics transcription service"""

    transcription_model: Literal["speechmatics/standard"]
    """The model to use for transcription."""

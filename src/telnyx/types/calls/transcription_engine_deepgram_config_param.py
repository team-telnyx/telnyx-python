# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TranscriptionEngineDeepgramConfigParam"]


class TranscriptionEngineDeepgramConfigParam(TypedDict, total=False):
    transcription_engine: Required[Literal["Deepgram"]]
    """Engine identifier for Deepgram transcription service"""

    transcription_model: Required[Literal["deepgram/nova-2", "deepgram/nova-3"]]
    """The model to use for transcription."""

    language: Literal[
        "bg",
        "ca",
        "zh",
        "zh-CN",
        "zh-Hans",
        "zh-TW",
        "zh-Hant",
        "zh-HK",
        "cs",
        "da",
        "da-DK",
        "nl",
        "en",
        "en-US",
        "en-AU",
        "en-GB",
        "en-NZ",
        "en-IN",
        "et",
        "fi",
        "nl-BE",
        "fr",
        "fr-CA",
        "de",
        "de-CH",
        "el",
        "hi",
        "hu",
        "id",
        "it",
        "ja",
        "ko",
        "ko-KR",
        "lv",
        "lt",
        "ms",
        "no",
        "pl",
        "pt",
        "pt-BR",
        "pt-PT",
        "ro",
        "ru",
        "sk",
        "es",
        "es-419",
        "sv",
        "sv-SE",
        "th",
        "th-TH",
        "tr",
        "uk",
        "vi",
        "auto_detect",
    ]
    """Language to use for speech recognition.

    Available languages depend on the selected model.
    """

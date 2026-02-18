# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["DeepgramNova3ConfigParam"]


class DeepgramNova3ConfigParam(TypedDict, total=False):
    transcription_engine: Required[Literal["Deepgram"]]

    transcription_model: Required[Literal["deepgram/nova-3"]]

    keywords_boosting: Dict[str, float]
    """
    Keywords and their respective intensifiers (boosting values) to improve
    transcription accuracy for specific words or phrases. The intensifier should be
    a numeric value. Example: `{"snuffleupagus": 5, "systrom": 2, "krieger": 1}`.
    """

    language: Literal[
        "en-US",
        "en-AU",
        "en-GB",
        "en-IN",
        "en-NZ",
        "de",
        "nl",
        "sv-SE",
        "da-DK",
        "es",
        "es-419",
        "fr",
        "fr-CA",
        "pt-BR",
        "pt-PT",
        "auto_detect",
    ]
    """Language to use for speech recognition with nova-3 model"""

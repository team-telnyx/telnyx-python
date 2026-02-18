# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MinimaxVoiceSettings"]


class MinimaxVoiceSettings(TypedDict, total=False):
    type: Required[Literal["minimax"]]
    """Voice settings provider type"""

    language_boost: Optional[
        Literal[
            "auto",
            "Chinese",
            "Chinese,Yue",
            "English",
            "Arabic",
            "Russian",
            "Spanish",
            "French",
            "Portuguese",
            "German",
            "Turkish",
            "Dutch",
            "Ukrainian",
            "Vietnamese",
            "Indonesian",
            "Japanese",
            "Italian",
            "Korean",
            "Thai",
            "Polish",
            "Romanian",
            "Greek",
            "Czech",
            "Finnish",
            "Hindi",
            "Bulgarian",
            "Danish",
            "Hebrew",
            "Malay",
            "Persian",
            "Slovak",
            "Swedish",
            "Croatian",
            "Filipino",
            "Hungarian",
            "Norwegian",
            "Slovenian",
            "Catalan",
            "Nynorsk",
            "Tamil",
            "Afrikaans",
        ]
    ]
    """
    Enhances recognition for specific languages and dialects during MiniMax TTS
    synthesis. Default is null (no boost). Set to 'auto' for automatic language
    detection.
    """

    pitch: int
    """Voice pitch adjustment. Default is 0."""

    speed: float
    """Speech speed multiplier. Default is 1.0."""

    vol: float
    """Speech volume multiplier. Default is 1.0."""

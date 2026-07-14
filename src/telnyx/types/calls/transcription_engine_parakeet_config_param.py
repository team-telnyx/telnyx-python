# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TranscriptionEngineParakeetConfigParam"]


class TranscriptionEngineParakeetConfigParam(TypedDict, total=False):
    interim_results: bool
    """Whether to send also interim results.

    If set to false, only final results will be sent.
    """

    transcription_engine: Literal["Parakeet"]
    """Engine identifier for Parakeet transcription service"""

    transcription_model: Literal["nvidia/parakeet-v3"]
    """The model to use for transcription."""

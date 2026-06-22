# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TranscriptionEngineAssemblyaiConfigParam"]


class TranscriptionEngineAssemblyaiConfigParam(TypedDict, total=False):
    interim_results: bool
    """Whether to send also interim results.

    If set to false, only final results will be sent.
    """

    transcription_engine: Literal["AssemblyAI"]
    """Engine identifier for AssemblyAI transcription service"""

    transcription_model: Literal["assemblyai/universal-streaming"]
    """The model to use for transcription."""

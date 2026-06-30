# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .texml_recording_transcription import TexmlRecordingTranscription as TexmlRecordingTranscription


def __getattr__(name: str) -> Any:
    if name == "TexmlRecordingTranscription":
        from .texml_recording_transcription import TexmlRecordingTranscription

        return TexmlRecordingTranscription
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

"""
Custom utilities for the Telnyx SDK.

This package provides additional functionality that extends the core SDK,
including WebSocket support for real-time streaming APIs.
"""

from telnyx.lib.speech_to_text_ws import (
    SttWord,
    SttEvent,
    SpeechToTextWS,
    AsyncSpeechToTextWS,
    SpeechToTextWSError,
    SpeechToTextStreamParams,
)

__all__ = [
    "SpeechToTextStreamParams",
    "SttEvent",
    "SttWord",
    "SpeechToTextWS",
    "AsyncSpeechToTextWS",
    "SpeechToTextWSError",
]

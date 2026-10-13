# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ConversationRelayTranscriptionEngineConfigParam"]


class ConversationRelayTranscriptionEngineConfigParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Engine-specific transcription settings for Conversation Relay.

    This accepts the same provider-specific options used by the Call Transcription Start command, such as `transcription_model`, without requiring the engine discriminator to be repeated inside this object. With Deepgram Flux (`deepgram/flux`), `interim_results`, `eot_threshold` and `eager_eot_threshold` control the interim prompts and the `eagerEndOfTurn` and `turnResumed` frames sent to your WebSocket server.
    """

    eager_eot_threshold: float
    """
    Deepgram Flux: confidence at which an `eagerEndOfTurn` frame is sent before the
    final prompt, followed by `turnResumed` if the caller keeps talking. When
    omitted, these frames are not sent.
    """

    eot_threshold: float
    """Deepgram Flux: confidence required to end the caller's turn."""

    interim_results: bool
    """Deepgram Flux: send interim transcripts as `prompt` frames with `last: false`."""

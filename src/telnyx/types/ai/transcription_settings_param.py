# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .transcription_settings_config_param import TranscriptionSettingsConfigParam

__all__ = ["TranscriptionSettingsParam"]


class TranscriptionSettingsParam(TypedDict, total=False):
    language: str
    """The language of the audio to be transcribed.

    If not set, of if set to `auto`, the model will automatically detect the
    language.
    """

    model: Literal[
        "deepgram/flux",
        "deepgram/nova-3",
        "deepgram/nova-2",
        "azure/fast",
        "distil-whisper/distil-large-v2",
        "openai/whisper-large-v3-turbo",
    ]
    """The speech to text model to be used by the voice assistant.

    All the deepgram models are run on-premise.

    - `deepgram/flux` is optimized for turn-taking but is English-only.
    - `deepgram/nova-3` is multi-lingual with automatic language detection but
      slightly higher latency.
    """

    region: str
    """
    Region on third party cloud providers (currently Azure) if using one of their
    models
    """

    settings: TranscriptionSettingsConfigParam

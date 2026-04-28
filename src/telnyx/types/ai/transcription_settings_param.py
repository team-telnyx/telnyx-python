# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .transcription_settings_config_param import TranscriptionSettingsConfigParam

__all__ = ["TranscriptionSettingsParam"]


class TranscriptionSettingsParam(TypedDict, total=False):
    api_key_ref: str
    """Integration secret identifier for the transcription provider API key.

    Currently used for Azure transcription regions that require a customer-provided
    API key.
    """

    language: str
    """The language of the audio to be transcribed.

    If not set, or if set to `auto`, the model will automatically detect the
    language.
    """

    model: Literal[
        "deepgram/flux",
        "deepgram/nova-3",
        "deepgram/nova-2",
        "azure/fast",
        "assemblyai/universal-streaming",
        "xai/grok-stt",
        "distil-whisper/distil-large-v2",
        "openai/whisper-large-v3-turbo",
    ]
    """The speech to text model to be used by the voice assistant.

    All Deepgram models are run on-premise.

    - `deepgram/flux` is optimized for turn-taking but is English-only.
    - `deepgram/nova-3` is multilingual with automatic language detection.
    - `deepgram/nova-2` is Deepgram's previous-generation multilingual model.
    - `azure/fast` is a multilingual Azure transcription model.
    - `assemblyai/universal-streaming` is a multilingual streaming model with
      configurable turn detection.
    - `xai/grok-stt` is a multilingual Grok STT model.
    """

    region: str
    """
    Region on third party cloud providers (currently Azure) if using one of their
    models. Some regions require `api_key_ref`.
    """

    settings: TranscriptionSettingsConfigParam

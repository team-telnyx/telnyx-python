# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TranscriptionFallbackModelParam"]


class TranscriptionFallbackModelParam(TypedDict, total=False):
    """
    A streaming speech-to-text model that takes over transcription when the model in use fails.
    """

    model: Required[
        Literal[
            "deepgram/flux",
            "deepgram/nova-3",
            "deepgram/nova-2",
            "assemblyai/universal-3-6-pro",
            "assemblyai/universal-3-5-pro",
            "assemblyai/universal-streaming",
            "xai/grok-stt",
            "soniox/stt-rt-v4",
            "soniox/stt-rt-v5",
            "humain/realtime",
            "reson8/turns",
        ]
    ]
    """The fallback model.

    It must be a streaming model other than `transcription.model` and the other
    fallbacks: `deepgram/flux`, `deepgram/nova-3`, `deepgram/nova-2`,
    `assemblyai/universal-3-6-pro` (or its legacy aliases
    `assemblyai/universal-3-5-pro` and `assemblyai/universal-streaming`),
    `xai/grok-stt`, `soniox/stt-rt-v4`, `soniox/stt-rt-v5`, `humain/realtime`, or
    `reson8/turns`.
    """

    language: Optional[str]
    """The language the fallback transcribes.

    Omit it or set it to `null` to use the language of `transcription.model`. The
    request is rejected when the fallback model doesn't support the language it
    would run.
    """

    settings: Optional["TranscriptionSettingsConfigParam"]
    """
    Settings for the fallback, with the same fields and limits as
    `transcription.settings`. Fields that don't apply to this model's provider are
    dropped, and the provider's defaults fill in the rest. Omit it or set it to
    `null` to use the settings of `transcription.model` where they apply to this
    model.
    """


from .transcription_settings_config_param import TranscriptionSettingsConfigParam

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TelnyxVoiceSettingsParam"]


class TelnyxVoiceSettingsParam(TypedDict, total=False):
    type: Required[Literal["telnyx"]]
    """Voice settings provider type"""

    voice_speed: float
    """The voice speed to be used for the voice.

    Telnyx `Ultra` voices accept values from 0.6 to 1.5; values outside that range
    are rejected by the synthesis engine. `Qwen3TTS` and `KokoroTTS` accept the
    field but do not apply it. Default value is 1.0. Not supported for
    `Telnyx.Bayan.*` or `Telnyx.Sukhan.*` voices.
    """

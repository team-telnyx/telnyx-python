# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TelnyxVoiceSettingsParam"]


class TelnyxVoiceSettingsParam(TypedDict, total=False):
    type: Required[Literal["telnyx"]]
    """Voice settings provider type"""

    voice_speed: float
    """The voice speed to be used for the voice.

    The voice speed must be between 0.1 and 2.0. Default value is 1.0.
    """

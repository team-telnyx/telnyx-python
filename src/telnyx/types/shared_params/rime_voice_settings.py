# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RimeVoiceSettings"]


class RimeVoiceSettings(TypedDict, total=False):
    type: Required[Literal["rime"]]
    """Voice settings provider type"""

    voice_speed: float
    """Speech speed multiplier. Default is 1.0."""

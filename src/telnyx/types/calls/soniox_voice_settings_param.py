# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SonioxVoiceSettingsParam"]


class SonioxVoiceSettingsParam(TypedDict, total=False):
    type: Required[Literal["soniox"]]
    """Voice settings provider type"""

    reduce_silence: bool
    """Shortens the pauses between words."""

    speed: float
    """Speaking rate. 1.0 is normal speed."""

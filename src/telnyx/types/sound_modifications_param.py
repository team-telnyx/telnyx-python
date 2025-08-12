# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SoundModificationsParam"]


class SoundModificationsParam(TypedDict, total=False):
    octaves: float
    """Adjust the pitch in octaves, values should be between -1 and 1, default 0"""

    pitch: float
    """Set the pitch directly, value should be > 0, default 1 (lower = lower tone)"""

    semitone: float
    """Adjust the pitch in semitones, values should be between -14 and 14, default 0"""

    track: str
    """The track to which the sound modifications will be applied.

    Accepted values are `inbound` or `outbound`
    """

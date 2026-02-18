# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MinimaxVoiceSettings"]


class MinimaxVoiceSettings(TypedDict, total=False):
    type: Required[Literal["minimax"]]
    """Voice settings provider type"""

    pitch: int
    """Voice pitch adjustment. Default is 0."""

    speed: float
    """Speech speed multiplier. Default is 1.0."""

    vol: float
    """Speech volume multiplier. Default is 1.0."""

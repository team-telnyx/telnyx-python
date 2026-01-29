# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AudioVisualizerConfigParam"]


class AudioVisualizerConfigParam(TypedDict, total=False):
    color: Literal["verdant", "twilight", "bloom", "mystic", "flare", "glacier"]
    """The color theme for the audio visualizer."""

    preset: str
    """The preset style for the audio visualizer."""

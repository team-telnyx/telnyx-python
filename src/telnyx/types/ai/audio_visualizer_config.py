# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AudioVisualizerConfig"]


class AudioVisualizerConfig(BaseModel):
    color: Optional[Literal["verdant", "twilight", "bloom", "mystic", "flare", "glacier"]] = None
    """The color theme for the audio visualizer."""

    preset: Optional[str] = None
    """The preset style for the audio visualizer."""

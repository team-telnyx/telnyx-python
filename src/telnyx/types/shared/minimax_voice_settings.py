# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MinimaxVoiceSettings"]


class MinimaxVoiceSettings(BaseModel):
    type: Literal["minimax"]
    """Voice settings provider type"""

    pitch: Optional[int] = None
    """Voice pitch adjustment. Default is 0."""

    speed: Optional[float] = None
    """Speech speed multiplier. Default is 1.0."""

    vol: Optional[float] = None
    """Speech volume multiplier. Default is 1.0."""

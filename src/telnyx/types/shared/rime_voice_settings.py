# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RimeVoiceSettings"]


class RimeVoiceSettings(BaseModel):
    type: Literal["rime"]
    """Voice settings provider type"""

    voice_speed: Optional[float] = None
    """Speech speed multiplier. Default is 1.0."""

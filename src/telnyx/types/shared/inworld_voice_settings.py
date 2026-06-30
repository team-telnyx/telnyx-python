# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["InworldVoiceSettings"]


class InworldVoiceSettings(BaseModel):
    type: Literal["inworld"]
    """Voice settings provider type"""

    delivery_mode: Optional[Literal["STABLE", "BALANCED", "CREATIVE"]] = None
    """
    Controls the expressiveness and consistency of the Inworld `TTS2` model's speech
    synthesis. `STABLE` favors consistent, predictable output, `CREATIVE` allows
    more expressive variation, and `BALANCED` sits in between. Optional and only
    supported by `TTS2`; when omitted, the provider default applies.
    """

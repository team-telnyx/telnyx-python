# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .voice_clone_data import VoiceCloneData

__all__ = ["VoiceCloneCreateResponse"]


class VoiceCloneCreateResponse(BaseModel):
    """Response envelope for a single voice clone."""

    data: Optional[VoiceCloneData] = None
    """A voice clone object."""

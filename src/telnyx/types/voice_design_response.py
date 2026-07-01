# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .voice_design_data import VoiceDesignData

__all__ = ["VoiceDesignResponse"]


class VoiceDesignResponse(BaseModel):
    """Response envelope for a single voice design with full version detail."""

    data: Optional[VoiceDesignData] = None
    """A voice design object with full version detail."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .voice_design_summary_data import VoiceDesignSummaryData

__all__ = ["VoiceDesignRenameResponse"]


class VoiceDesignRenameResponse(BaseModel):
    """
    Response envelope for a voice design after a rename operation (no version-specific fields).
    """

    data: Optional[VoiceDesignSummaryData] = None
    """A summarized voice design object (without version-specific fields)."""

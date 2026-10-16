# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ..._models import BaseModel

__all__ = ["VisionToolParams"]


class VisionToolParams(BaseModel):
    max_frame_age_secs: Optional[int] = None
    """
    Frames received longer ago than this many seconds are not shown to the
    assistant, so it never describes a frozen or disconnected camera as live.
    """

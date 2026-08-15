# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["MeetingSessionRetrieveTranscriptResponse", "Data", "Meta"]


class Data(BaseModel):
    confidence: Optional[float] = None

    occurred_at: datetime

    relative_ts: Optional[float] = None

    seq: int

    speaker_label: Optional[str] = None

    text: str


class Meta(BaseModel):
    next_after: Optional[int] = None
    """
    Cursor to pass as `after` on the next request, or null when the response
    contains no segments.
    """


class MeetingSessionRetrieveTranscriptResponse(BaseModel):
    data: List[Data]

    meta: Meta

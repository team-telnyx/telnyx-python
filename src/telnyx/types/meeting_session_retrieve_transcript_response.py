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
    """Monotonic transcript append cursor.

    This is separate from the event-history cursor and does not establish
    conversational turn order.
    """

    speaker_label: Optional[str] = None
    """Recorded participant or bot label, or null when unavailable.

    Labels are attribution, not verified identity. Segments from concurrent speakers
    can finalize in a different order from the conversation.
    """

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

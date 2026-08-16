# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from .._models import BaseModel
from .meeting_session import MeetingSession

__all__ = ["MeetingSessionListResponse"]


class MeetingSessionListResponse(BaseModel):
    data: List[MeetingSession]

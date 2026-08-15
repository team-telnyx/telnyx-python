# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from datetime import datetime

from .._models import BaseModel

__all__ = ["MeetingSessionRetrieveEventsResponse", "Data"]


class Data(BaseModel):
    occurred_at: datetime

    payload: Dict[str, object]

    seq: int

    type: str


class MeetingSessionRetrieveEventsResponse(BaseModel):
    data: List[Data]

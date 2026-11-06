# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._models import BaseModel
from .calendar_meeting import CalendarMeeting

__all__ = ["MeetingUpdateResponse"]


class MeetingUpdateResponse(BaseModel):
    data: CalendarMeeting

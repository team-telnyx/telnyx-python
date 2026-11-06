# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .meeting_list_params import MeetingListParams as MeetingListParams
from .meeting_update_params import MeetingUpdateParams as MeetingUpdateParams

if TYPE_CHECKING:
    from .calendar_meeting import CalendarMeeting as CalendarMeeting
    from .meeting_list_response import MeetingListResponse as MeetingListResponse
    from .meeting_update_response import MeetingUpdateResponse as MeetingUpdateResponse


def __getattr__(name: str) -> Any:
    if name == "CalendarMeeting":
        from .calendar_meeting import CalendarMeeting

        return CalendarMeeting
    if name == "MeetingUpdateResponse":
        from .meeting_update_response import MeetingUpdateResponse

        return MeetingUpdateResponse
    if name == "MeetingListResponse":
        from .meeting_list_response import MeetingListResponse

        return MeetingListResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

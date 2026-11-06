# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .calendar import (
    CalendarResource,
    AsyncCalendarResource,
    CalendarResourceWithRawResponse,
    AsyncCalendarResourceWithRawResponse,
    CalendarResourceWithStreamingResponse,
    AsyncCalendarResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["MeetingBotResource", "AsyncMeetingBotResource"]


class MeetingBotResource(SyncAPIResource):
    @cached_property
    def calendar(self) -> CalendarResource:
        """Connect calendars and manage automatic meeting joins."""
        return CalendarResource(self._client)

    @cached_property
    def with_raw_response(self) -> MeetingBotResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return MeetingBotResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MeetingBotResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return MeetingBotResourceWithStreamingResponse(self)


class AsyncMeetingBotResource(AsyncAPIResource):
    @cached_property
    def calendar(self) -> AsyncCalendarResource:
        """Connect calendars and manage automatic meeting joins."""
        return AsyncCalendarResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMeetingBotResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMeetingBotResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMeetingBotResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncMeetingBotResourceWithStreamingResponse(self)


class MeetingBotResourceWithRawResponse:
    def __init__(self, meeting_bot: MeetingBotResource) -> None:
        self._meeting_bot = meeting_bot

    @cached_property
    def calendar(self) -> CalendarResourceWithRawResponse:
        """Connect calendars and manage automatic meeting joins."""
        return CalendarResourceWithRawResponse(self._meeting_bot.calendar)


class AsyncMeetingBotResourceWithRawResponse:
    def __init__(self, meeting_bot: AsyncMeetingBotResource) -> None:
        self._meeting_bot = meeting_bot

    @cached_property
    def calendar(self) -> AsyncCalendarResourceWithRawResponse:
        """Connect calendars and manage automatic meeting joins."""
        return AsyncCalendarResourceWithRawResponse(self._meeting_bot.calendar)


class MeetingBotResourceWithStreamingResponse:
    def __init__(self, meeting_bot: MeetingBotResource) -> None:
        self._meeting_bot = meeting_bot

    @cached_property
    def calendar(self) -> CalendarResourceWithStreamingResponse:
        """Connect calendars and manage automatic meeting joins."""
        return CalendarResourceWithStreamingResponse(self._meeting_bot.calendar)


class AsyncMeetingBotResourceWithStreamingResponse:
    def __init__(self, meeting_bot: AsyncMeetingBotResource) -> None:
        self._meeting_bot = meeting_bot

    @cached_property
    def calendar(self) -> AsyncCalendarResourceWithStreamingResponse:
        """Connect calendars and manage automatic meeting joins."""
        return AsyncCalendarResourceWithStreamingResponse(self._meeting_bot.calendar)

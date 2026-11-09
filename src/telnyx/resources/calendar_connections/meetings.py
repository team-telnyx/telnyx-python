# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.calendar_connections import meeting_list_params, meeting_update_params
from ...types.calendar_connections.meeting_list_response import MeetingListResponse
from ...types.calendar_connections.meeting_update_response import MeetingUpdateResponse

__all__ = ["MeetingsResource", "AsyncMeetingsResource"]


class MeetingsResource(SyncAPIResource):
    """Connect calendars and manage automatic meeting joins."""

    @cached_property
    def with_raw_response(self) -> MeetingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return MeetingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MeetingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return MeetingsResourceWithStreamingResponse(self)

    def update(
        self,
        meeting_id: str,
        *,
        id: str,
        bot_will_join: Optional[bool],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingUpdateResponse:
        """
        Set an individual meeting override: true opts in, false opts out, null follows
        the connection policy. A supported meeting link is required. Changes re-evaluate
        the meeting immediately; poll the linked session for its final lifecycle
        outcome.

        Args:
          bot_will_join: True opts in, false opts out, null follows connection policy. A supported
              meeting URL is still required.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not meeting_id:
            raise ValueError(f"Expected a non-empty value for `meeting_id` but received {meeting_id!r}")
        return self._patch(
            path_template("/calendar_connections/{id}/meetings/{meeting_id}", id=id, meeting_id=meeting_id),
            body=maybe_transform({"bot_will_join": bot_will_join}, meeting_update_params.MeetingUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeetingUpdateResponse,
        )

    def list(
        self,
        id: str,
        *,
        from_: Union[str, datetime] | Omit = omit,
        to: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingListResponse:
        """List tracked meetings in a window.

        Defaults from now through seven days from
        now. from must not exceed to and the window must not exceed 31 days.
        bot_will_join is the effective policy decision; check session_id and the linked
        session status for actual attendance.

        Args:
          from_: Window start; defaults to now.

          to: Window end; defaults to seven days from now.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/calendar_connections/{id}/meetings", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                    },
                    meeting_list_params.MeetingListParams,
                ),
            ),
            cast_to=MeetingListResponse,
        )


class AsyncMeetingsResource(AsyncAPIResource):
    """Connect calendars and manage automatic meeting joins."""

    @cached_property
    def with_raw_response(self) -> AsyncMeetingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMeetingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMeetingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncMeetingsResourceWithStreamingResponse(self)

    async def update(
        self,
        meeting_id: str,
        *,
        id: str,
        bot_will_join: Optional[bool],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingUpdateResponse:
        """
        Set an individual meeting override: true opts in, false opts out, null follows
        the connection policy. A supported meeting link is required. Changes re-evaluate
        the meeting immediately; poll the linked session for its final lifecycle
        outcome.

        Args:
          bot_will_join: True opts in, false opts out, null follows connection policy. A supported
              meeting URL is still required.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not meeting_id:
            raise ValueError(f"Expected a non-empty value for `meeting_id` but received {meeting_id!r}")
        return await self._patch(
            path_template("/calendar_connections/{id}/meetings/{meeting_id}", id=id, meeting_id=meeting_id),
            body=await async_maybe_transform(
                {"bot_will_join": bot_will_join}, meeting_update_params.MeetingUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeetingUpdateResponse,
        )

    async def list(
        self,
        id: str,
        *,
        from_: Union[str, datetime] | Omit = omit,
        to: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingListResponse:
        """List tracked meetings in a window.

        Defaults from now through seven days from
        now. from must not exceed to and the window must not exceed 31 days.
        bot_will_join is the effective policy decision; check session_id and the linked
        session status for actual attendance.

        Args:
          from_: Window start; defaults to now.

          to: Window end; defaults to seven days from now.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/calendar_connections/{id}/meetings", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                    },
                    meeting_list_params.MeetingListParams,
                ),
            ),
            cast_to=MeetingListResponse,
        )


class MeetingsResourceWithRawResponse:
    def __init__(self, meetings: MeetingsResource) -> None:
        self._meetings = meetings

        self.update = to_raw_response_wrapper(
            meetings.update,
        )
        self.list = to_raw_response_wrapper(
            meetings.list,
        )


class AsyncMeetingsResourceWithRawResponse:
    def __init__(self, meetings: AsyncMeetingsResource) -> None:
        self._meetings = meetings

        self.update = async_to_raw_response_wrapper(
            meetings.update,
        )
        self.list = async_to_raw_response_wrapper(
            meetings.list,
        )


class MeetingsResourceWithStreamingResponse:
    def __init__(self, meetings: MeetingsResource) -> None:
        self._meetings = meetings

        self.update = to_streamed_response_wrapper(
            meetings.update,
        )
        self.list = to_streamed_response_wrapper(
            meetings.list,
        )


class AsyncMeetingsResourceWithStreamingResponse:
    def __init__(self, meetings: AsyncMeetingsResource) -> None:
        self._meetings = meetings

        self.update = async_to_streamed_response_wrapper(
            meetings.update,
        )
        self.list = async_to_streamed_response_wrapper(
            meetings.list,
        )

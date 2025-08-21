# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import call_event_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.call_event_list_response import CallEventListResponse

__all__ = ["CallEventsResource", "AsyncCallEventsResource"]


class CallEventsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CallEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return CallEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CallEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return CallEventsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        filter: call_event_list_params.Filter | NotGiven = NOT_GIVEN,
        page: call_event_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallEventListResponse:
        """Filters call events by given filter parameters.

        Events are ordered by
        `occurred_at`. If filter for `leg_id` or `application_session_id` is not
        present, it only filters events from the last 24 hours.

        **Note**: Only one `filter[occurred_at]` can be passed.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[application_name][contains], filter[outbound.outbound_voice_profile_id],
              filter[leg_id], filter[application_session_id], filter[connection_id],
              filter[product], filter[failed], filter[from], filter[to], filter[name],
              filter[type], filter[occurred_at][eq/gt/gte/lt/lte], filter[status]

          page: Consolidated page parameter (deepObject style). Originally: page[after],
              page[before], page[limit], page[size], page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/call_events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                    },
                    call_event_list_params.CallEventListParams,
                ),
            ),
            cast_to=CallEventListResponse,
        )


class AsyncCallEventsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCallEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCallEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCallEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncCallEventsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        filter: call_event_list_params.Filter | NotGiven = NOT_GIVEN,
        page: call_event_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallEventListResponse:
        """Filters call events by given filter parameters.

        Events are ordered by
        `occurred_at`. If filter for `leg_id` or `application_session_id` is not
        present, it only filters events from the last 24 hours.

        **Note**: Only one `filter[occurred_at]` can be passed.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[application_name][contains], filter[outbound.outbound_voice_profile_id],
              filter[leg_id], filter[application_session_id], filter[connection_id],
              filter[product], filter[failed], filter[from], filter[to], filter[name],
              filter[type], filter[occurred_at][eq/gt/gte/lt/lte], filter[status]

          page: Consolidated page parameter (deepObject style). Originally: page[after],
              page[before], page[limit], page[size], page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/call_events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                    },
                    call_event_list_params.CallEventListParams,
                ),
            ),
            cast_to=CallEventListResponse,
        )


class CallEventsResourceWithRawResponse:
    def __init__(self, call_events: CallEventsResource) -> None:
        self._call_events = call_events

        self.list = to_raw_response_wrapper(
            call_events.list,
        )


class AsyncCallEventsResourceWithRawResponse:
    def __init__(self, call_events: AsyncCallEventsResource) -> None:
        self._call_events = call_events

        self.list = async_to_raw_response_wrapper(
            call_events.list,
        )


class CallEventsResourceWithStreamingResponse:
    def __init__(self, call_events: CallEventsResource) -> None:
        self._call_events = call_events

        self.list = to_streamed_response_wrapper(
            call_events.list,
        )


class AsyncCallEventsResourceWithStreamingResponse:
    def __init__(self, call_events: AsyncCallEventsResource) -> None:
        self._call_events = call_events

        self.list = async_to_streamed_response_wrapper(
            call_events.list,
        )

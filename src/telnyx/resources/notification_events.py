# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import notification_event_list_params
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
from ..types.notification_event_list_response import NotificationEventListResponse

__all__ = ["NotificationEventsResource", "AsyncNotificationEventsResource"]


class NotificationEventsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NotificationEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return NotificationEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NotificationEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return NotificationEventsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        page: notification_event_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NotificationEventListResponse:
        """
        Returns a list of your notifications events.

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/notification_events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"page": page}, notification_event_list_params.NotificationEventListParams),
            ),
            cast_to=NotificationEventListResponse,
        )


class AsyncNotificationEventsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNotificationEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNotificationEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNotificationEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncNotificationEventsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        page: notification_event_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NotificationEventListResponse:
        """
        Returns a list of your notifications events.

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/notification_events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"page": page}, notification_event_list_params.NotificationEventListParams
                ),
            ),
            cast_to=NotificationEventListResponse,
        )


class NotificationEventsResourceWithRawResponse:
    def __init__(self, notification_events: NotificationEventsResource) -> None:
        self._notification_events = notification_events

        self.list = to_raw_response_wrapper(
            notification_events.list,
        )


class AsyncNotificationEventsResourceWithRawResponse:
    def __init__(self, notification_events: AsyncNotificationEventsResource) -> None:
        self._notification_events = notification_events

        self.list = async_to_raw_response_wrapper(
            notification_events.list,
        )


class NotificationEventsResourceWithStreamingResponse:
    def __init__(self, notification_events: NotificationEventsResource) -> None:
        self._notification_events = notification_events

        self.list = to_streamed_response_wrapper(
            notification_events.list,
        )


class AsyncNotificationEventsResourceWithStreamingResponse:
    def __init__(self, notification_events: AsyncNotificationEventsResource) -> None:
        self._notification_events = notification_events

        self.list = async_to_streamed_response_wrapper(
            notification_events.list,
        )

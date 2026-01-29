# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import notification_event_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from .._base_client import AsyncPaginator, make_request_options
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
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[NotificationEventListResponse]:
        """
        Returns a list of your notifications events.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/notification_events",
            page=SyncDefaultFlatPagination[NotificationEventListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    notification_event_list_params.NotificationEventListParams,
                ),
            ),
            model=NotificationEventListResponse,
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

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[NotificationEventListResponse, AsyncDefaultFlatPagination[NotificationEventListResponse]]:
        """
        Returns a list of your notifications events.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/notification_events",
            page=AsyncDefaultFlatPagination[NotificationEventListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    notification_event_list_params.NotificationEventListParams,
                ),
            ),
            model=NotificationEventListResponse,
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

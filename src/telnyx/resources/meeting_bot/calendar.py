# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.meeting_bot import calendar_retrieve_oauth_callback_params

__all__ = ["CalendarResource", "AsyncCalendarResource"]


class CalendarResource(SyncAPIResource):
    """Connect calendars and manage automatic meeting joins."""

    @cached_property
    def with_raw_response(self) -> CalendarResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return CalendarResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CalendarResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return CalendarResourceWithStreamingResponse(self)

    def retrieve_oauth_callback(
        self,
        *,
        code: str | Omit = omit,
        error: str | Omit = omit,
        state: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """Browser redirect after calendar consent.

        Use the returned oauth_url rather than
        constructing this request. Verified state identifies the connecting user.
        Returns HTML for success, cancellation, or failure; no JSON error envelope or
        bearer token is used.

        Args:
          code: Authorization code supplied by the calendar provider.

          error: Authorization error supplied by the calendar provider, such as access_denied.

          state: Unmodified signed state from the authorization URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/html", **(extra_headers or {})}
        return self._get(
            "/meeting_bot/calendar/oauth_callback",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "code": code,
                        "error": error,
                        "state": state,
                    },
                    calendar_retrieve_oauth_callback_params.CalendarRetrieveOAuthCallbackParams,
                ),
            ),
            cast_to=str,
        )


class AsyncCalendarResource(AsyncAPIResource):
    """Connect calendars and manage automatic meeting joins."""

    @cached_property
    def with_raw_response(self) -> AsyncCalendarResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCalendarResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCalendarResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncCalendarResourceWithStreamingResponse(self)

    async def retrieve_oauth_callback(
        self,
        *,
        code: str | Omit = omit,
        error: str | Omit = omit,
        state: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """Browser redirect after calendar consent.

        Use the returned oauth_url rather than
        constructing this request. Verified state identifies the connecting user.
        Returns HTML for success, cancellation, or failure; no JSON error envelope or
        bearer token is used.

        Args:
          code: Authorization code supplied by the calendar provider.

          error: Authorization error supplied by the calendar provider, such as access_denied.

          state: Unmodified signed state from the authorization URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/html", **(extra_headers or {})}
        return await self._get(
            "/meeting_bot/calendar/oauth_callback",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "code": code,
                        "error": error,
                        "state": state,
                    },
                    calendar_retrieve_oauth_callback_params.CalendarRetrieveOAuthCallbackParams,
                ),
            ),
            cast_to=str,
        )


class CalendarResourceWithRawResponse:
    def __init__(self, calendar: CalendarResource) -> None:
        self._calendar = calendar

        self.retrieve_oauth_callback = to_raw_response_wrapper(
            calendar.retrieve_oauth_callback,
        )


class AsyncCalendarResourceWithRawResponse:
    def __init__(self, calendar: AsyncCalendarResource) -> None:
        self._calendar = calendar

        self.retrieve_oauth_callback = async_to_raw_response_wrapper(
            calendar.retrieve_oauth_callback,
        )


class CalendarResourceWithStreamingResponse:
    def __init__(self, calendar: CalendarResource) -> None:
        self._calendar = calendar

        self.retrieve_oauth_callback = to_streamed_response_wrapper(
            calendar.retrieve_oauth_callback,
        )


class AsyncCalendarResourceWithStreamingResponse:
    def __init__(self, calendar: AsyncCalendarResource) -> None:
        self._calendar = calendar

        self.retrieve_oauth_callback = async_to_streamed_response_wrapper(
            calendar.retrieve_oauth_callback,
        )

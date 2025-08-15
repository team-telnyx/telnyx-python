# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ...types.external_connections import log_message_list_params
from ...types.external_connections.log_message_list_response import LogMessageListResponse
from ...types.external_connections.log_message_dismiss_response import LogMessageDismissResponse
from ...types.external_connections.log_message_retrieve_response import LogMessageRetrieveResponse

__all__ = ["LogMessagesResource", "AsyncLogMessagesResource"]


class LogMessagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LogMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return LogMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LogMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return LogMessagesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LogMessageRetrieveResponse:
        """
        Retrieve a log message for an external connection associated with your account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/external_connections/log_messages/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogMessageRetrieveResponse,
        )

    def list(
        self,
        *,
        filter: log_message_list_params.Filter | NotGiven = NOT_GIVEN,
        page: log_message_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LogMessageListResponse:
        """
        Retrieve a list of log messages for all external connections associated with
        your account.

        Args:
          filter: Filter parameter for log messages (deepObject style). Supports filtering by
              external_connection_id and telephone_number with eq/contains operations.

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/external_connections/log_messages",
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
                    log_message_list_params.LogMessageListParams,
                ),
            ),
            cast_to=LogMessageListResponse,
        )

    def dismiss(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LogMessageDismissResponse:
        """
        Dismiss a log message for an external connection associated with your account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/external_connections/log_messages/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogMessageDismissResponse,
        )


class AsyncLogMessagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLogMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLogMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLogMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncLogMessagesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LogMessageRetrieveResponse:
        """
        Retrieve a log message for an external connection associated with your account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/external_connections/log_messages/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogMessageRetrieveResponse,
        )

    async def list(
        self,
        *,
        filter: log_message_list_params.Filter | NotGiven = NOT_GIVEN,
        page: log_message_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LogMessageListResponse:
        """
        Retrieve a list of log messages for all external connections associated with
        your account.

        Args:
          filter: Filter parameter for log messages (deepObject style). Supports filtering by
              external_connection_id and telephone_number with eq/contains operations.

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/external_connections/log_messages",
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
                    log_message_list_params.LogMessageListParams,
                ),
            ),
            cast_to=LogMessageListResponse,
        )

    async def dismiss(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LogMessageDismissResponse:
        """
        Dismiss a log message for an external connection associated with your account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/external_connections/log_messages/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogMessageDismissResponse,
        )


class LogMessagesResourceWithRawResponse:
    def __init__(self, log_messages: LogMessagesResource) -> None:
        self._log_messages = log_messages

        self.retrieve = to_raw_response_wrapper(
            log_messages.retrieve,
        )
        self.list = to_raw_response_wrapper(
            log_messages.list,
        )
        self.dismiss = to_raw_response_wrapper(
            log_messages.dismiss,
        )


class AsyncLogMessagesResourceWithRawResponse:
    def __init__(self, log_messages: AsyncLogMessagesResource) -> None:
        self._log_messages = log_messages

        self.retrieve = async_to_raw_response_wrapper(
            log_messages.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            log_messages.list,
        )
        self.dismiss = async_to_raw_response_wrapper(
            log_messages.dismiss,
        )


class LogMessagesResourceWithStreamingResponse:
    def __init__(self, log_messages: LogMessagesResource) -> None:
        self._log_messages = log_messages

        self.retrieve = to_streamed_response_wrapper(
            log_messages.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            log_messages.list,
        )
        self.dismiss = to_streamed_response_wrapper(
            log_messages.dismiss,
        )


class AsyncLogMessagesResourceWithStreamingResponse:
    def __init__(self, log_messages: AsyncLogMessagesResource) -> None:
        self._log_messages = log_messages

        self.retrieve = async_to_streamed_response_wrapper(
            log_messages.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            log_messages.list,
        )
        self.dismiss = async_to_streamed_response_wrapper(
            log_messages.dismiss,
        )

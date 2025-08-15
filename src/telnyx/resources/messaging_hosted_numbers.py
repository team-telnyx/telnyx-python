# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.messaging_hosted_number_delete_response import MessagingHostedNumberDeleteResponse

__all__ = ["MessagingHostedNumbersResource", "AsyncMessagingHostedNumbersResource"]


class MessagingHostedNumbersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MessagingHostedNumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return MessagingHostedNumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagingHostedNumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return MessagingHostedNumbersResourceWithStreamingResponse(self)

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessagingHostedNumberDeleteResponse:
        """
        Delete a messaging hosted number

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/messaging_hosted_numbers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingHostedNumberDeleteResponse,
        )


class AsyncMessagingHostedNumbersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMessagingHostedNumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagingHostedNumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagingHostedNumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncMessagingHostedNumbersResourceWithStreamingResponse(self)

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessagingHostedNumberDeleteResponse:
        """
        Delete a messaging hosted number

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/messaging_hosted_numbers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingHostedNumberDeleteResponse,
        )


class MessagingHostedNumbersResourceWithRawResponse:
    def __init__(self, messaging_hosted_numbers: MessagingHostedNumbersResource) -> None:
        self._messaging_hosted_numbers = messaging_hosted_numbers

        self.delete = to_raw_response_wrapper(
            messaging_hosted_numbers.delete,
        )


class AsyncMessagingHostedNumbersResourceWithRawResponse:
    def __init__(self, messaging_hosted_numbers: AsyncMessagingHostedNumbersResource) -> None:
        self._messaging_hosted_numbers = messaging_hosted_numbers

        self.delete = async_to_raw_response_wrapper(
            messaging_hosted_numbers.delete,
        )


class MessagingHostedNumbersResourceWithStreamingResponse:
    def __init__(self, messaging_hosted_numbers: MessagingHostedNumbersResource) -> None:
        self._messaging_hosted_numbers = messaging_hosted_numbers

        self.delete = to_streamed_response_wrapper(
            messaging_hosted_numbers.delete,
        )


class AsyncMessagingHostedNumbersResourceWithStreamingResponse:
    def __init__(self, messaging_hosted_numbers: AsyncMessagingHostedNumbersResource) -> None:
        self._messaging_hosted_numbers = messaging_hosted_numbers

        self.delete = async_to_streamed_response_wrapper(
            messaging_hosted_numbers.delete,
        )

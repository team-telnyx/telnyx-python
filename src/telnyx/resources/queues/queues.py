# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .calls import (
    CallsResource,
    AsyncCallsResource,
    CallsResourceWithRawResponse,
    AsyncCallsResourceWithRawResponse,
    CallsResourceWithStreamingResponse,
    AsyncCallsResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.queue_retrieve_response import QueueRetrieveResponse

__all__ = ["QueuesResource", "AsyncQueuesResource"]


class QueuesResource(SyncAPIResource):
    @cached_property
    def calls(self) -> CallsResource:
        return CallsResource(self._client)

    @cached_property
    def with_raw_response(self) -> QueuesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return QueuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QueuesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return QueuesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        queue_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueueRetrieveResponse:
        """
        Retrieve an existing call queue

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_name:
            raise ValueError(f"Expected a non-empty value for `queue_name` but received {queue_name!r}")
        return self._get(
            f"/queues/{queue_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueueRetrieveResponse,
        )


class AsyncQueuesResource(AsyncAPIResource):
    @cached_property
    def calls(self) -> AsyncCallsResource:
        return AsyncCallsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncQueuesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQueuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQueuesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncQueuesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        queue_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueueRetrieveResponse:
        """
        Retrieve an existing call queue

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_name:
            raise ValueError(f"Expected a non-empty value for `queue_name` but received {queue_name!r}")
        return await self._get(
            f"/queues/{queue_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueueRetrieveResponse,
        )


class QueuesResourceWithRawResponse:
    def __init__(self, queues: QueuesResource) -> None:
        self._queues = queues

        self.retrieve = to_raw_response_wrapper(
            queues.retrieve,
        )

    @cached_property
    def calls(self) -> CallsResourceWithRawResponse:
        return CallsResourceWithRawResponse(self._queues.calls)


class AsyncQueuesResourceWithRawResponse:
    def __init__(self, queues: AsyncQueuesResource) -> None:
        self._queues = queues

        self.retrieve = async_to_raw_response_wrapper(
            queues.retrieve,
        )

    @cached_property
    def calls(self) -> AsyncCallsResourceWithRawResponse:
        return AsyncCallsResourceWithRawResponse(self._queues.calls)


class QueuesResourceWithStreamingResponse:
    def __init__(self, queues: QueuesResource) -> None:
        self._queues = queues

        self.retrieve = to_streamed_response_wrapper(
            queues.retrieve,
        )

    @cached_property
    def calls(self) -> CallsResourceWithStreamingResponse:
        return CallsResourceWithStreamingResponse(self._queues.calls)


class AsyncQueuesResourceWithStreamingResponse:
    def __init__(self, queues: AsyncQueuesResource) -> None:
        self._queues = queues

        self.retrieve = async_to_streamed_response_wrapper(
            queues.retrieve,
        )

    @cached_property
    def calls(self) -> AsyncCallsResourceWithStreamingResponse:
        return AsyncCallsResourceWithStreamingResponse(self._queues.calls)

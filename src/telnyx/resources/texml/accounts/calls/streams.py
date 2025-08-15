# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.texml.accounts.calls import stream_streaming_sid_json_params
from .....types.texml.accounts.calls.stream_streaming_sid_json_response import StreamStreamingSidJsonResponse

__all__ = ["StreamsResource", "AsyncStreamsResource"]


class StreamsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StreamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return StreamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StreamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return StreamsResourceWithStreamingResponse(self)

    def streaming_sid_json(
        self,
        streaming_sid: str,
        *,
        account_sid: str,
        call_sid: str,
        status: Literal["stopped"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StreamStreamingSidJsonResponse:
        """
        Updates streaming resource for particular call.

        Args:
          status: The status of the Stream you wish to update.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        if not call_sid:
            raise ValueError(f"Expected a non-empty value for `call_sid` but received {call_sid!r}")
        if not streaming_sid:
            raise ValueError(f"Expected a non-empty value for `streaming_sid` but received {streaming_sid!r}")
        return self._post(
            f"/texml/Accounts/{account_sid}/Calls/{call_sid}/Streams/{streaming_sid}.json",
            body=maybe_transform({"status": status}, stream_streaming_sid_json_params.StreamStreamingSidJsonParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StreamStreamingSidJsonResponse,
        )


class AsyncStreamsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStreamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStreamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStreamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncStreamsResourceWithStreamingResponse(self)

    async def streaming_sid_json(
        self,
        streaming_sid: str,
        *,
        account_sid: str,
        call_sid: str,
        status: Literal["stopped"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StreamStreamingSidJsonResponse:
        """
        Updates streaming resource for particular call.

        Args:
          status: The status of the Stream you wish to update.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        if not call_sid:
            raise ValueError(f"Expected a non-empty value for `call_sid` but received {call_sid!r}")
        if not streaming_sid:
            raise ValueError(f"Expected a non-empty value for `streaming_sid` but received {streaming_sid!r}")
        return await self._post(
            f"/texml/Accounts/{account_sid}/Calls/{call_sid}/Streams/{streaming_sid}.json",
            body=await async_maybe_transform(
                {"status": status}, stream_streaming_sid_json_params.StreamStreamingSidJsonParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StreamStreamingSidJsonResponse,
        )


class StreamsResourceWithRawResponse:
    def __init__(self, streams: StreamsResource) -> None:
        self._streams = streams

        self.streaming_sid_json = to_raw_response_wrapper(
            streams.streaming_sid_json,
        )


class AsyncStreamsResourceWithRawResponse:
    def __init__(self, streams: AsyncStreamsResource) -> None:
        self._streams = streams

        self.streaming_sid_json = async_to_raw_response_wrapper(
            streams.streaming_sid_json,
        )


class StreamsResourceWithStreamingResponse:
    def __init__(self, streams: StreamsResource) -> None:
        self._streams = streams

        self.streaming_sid_json = to_streamed_response_wrapper(
            streams.streaming_sid_json,
        )


class AsyncStreamsResourceWithStreamingResponse:
    def __init__(self, streams: AsyncStreamsResource) -> None:
        self._streams = streams

        self.streaming_sid_json = async_to_streamed_response_wrapper(
            streams.streaming_sid_json,
        )

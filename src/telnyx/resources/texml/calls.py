# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

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
from ...types.texml import call_update_params
from ..._base_client import make_request_options
from ...types.texml.call_update_response import CallUpdateResponse

__all__ = ["CallsResource", "AsyncCallsResource"]


class CallsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CallsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return CallsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CallsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/telnyx-python#with_streaming_response
        """
        return CallsResourceWithStreamingResponse(self)

    def update(
        self,
        call_sid: str,
        *,
        fallback_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        fallback_url: str | NotGiven = NOT_GIVEN,
        method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        status_callback: str | NotGiven = NOT_GIVEN,
        status_callback_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        texml: str | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallUpdateResponse:
        """Update TeXML call.

        Please note that the keys present in the payload MUST BE
        formatted in CamelCase as specified in the example.

        Args:
          fallback_method: HTTP request type used for `FallbackUrl`.

          fallback_url: A failover URL for which Telnyx will retrieve the TeXML call instructions if the
              Url is not responding.

          method: HTTP request type used for `Url`.

          status: The value to set the call status to. Setting the status to completed ends the
              call.

          status_callback: URL destination for Telnyx to send status callback events to for the call.

          status_callback_method: HTTP request type used for `StatusCallback`.

          texml: TeXML to replace the current one with.

          url: The URL where TeXML will make a request to retrieve a new set of TeXML
              instructions to continue the call flow.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_sid:
            raise ValueError(f"Expected a non-empty value for `call_sid` but received {call_sid!r}")
        return self._post(
            f"/texml/calls/{call_sid}/update",
            body=maybe_transform(
                {
                    "fallback_method": fallback_method,
                    "fallback_url": fallback_url,
                    "method": method,
                    "status": status,
                    "status_callback": status_callback,
                    "status_callback_method": status_callback_method,
                    "texml": texml,
                    "url": url,
                },
                call_update_params.CallUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallUpdateResponse,
        )


class AsyncCallsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCallsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCallsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCallsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/telnyx-python#with_streaming_response
        """
        return AsyncCallsResourceWithStreamingResponse(self)

    async def update(
        self,
        call_sid: str,
        *,
        fallback_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        fallback_url: str | NotGiven = NOT_GIVEN,
        method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        status_callback: str | NotGiven = NOT_GIVEN,
        status_callback_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        texml: str | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallUpdateResponse:
        """Update TeXML call.

        Please note that the keys present in the payload MUST BE
        formatted in CamelCase as specified in the example.

        Args:
          fallback_method: HTTP request type used for `FallbackUrl`.

          fallback_url: A failover URL for which Telnyx will retrieve the TeXML call instructions if the
              Url is not responding.

          method: HTTP request type used for `Url`.

          status: The value to set the call status to. Setting the status to completed ends the
              call.

          status_callback: URL destination for Telnyx to send status callback events to for the call.

          status_callback_method: HTTP request type used for `StatusCallback`.

          texml: TeXML to replace the current one with.

          url: The URL where TeXML will make a request to retrieve a new set of TeXML
              instructions to continue the call flow.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_sid:
            raise ValueError(f"Expected a non-empty value for `call_sid` but received {call_sid!r}")
        return await self._post(
            f"/texml/calls/{call_sid}/update",
            body=await async_maybe_transform(
                {
                    "fallback_method": fallback_method,
                    "fallback_url": fallback_url,
                    "method": method,
                    "status": status,
                    "status_callback": status_callback,
                    "status_callback_method": status_callback_method,
                    "texml": texml,
                    "url": url,
                },
                call_update_params.CallUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallUpdateResponse,
        )


class CallsResourceWithRawResponse:
    def __init__(self, calls: CallsResource) -> None:
        self._calls = calls

        self.update = to_raw_response_wrapper(
            calls.update,
        )


class AsyncCallsResourceWithRawResponse:
    def __init__(self, calls: AsyncCallsResource) -> None:
        self._calls = calls

        self.update = async_to_raw_response_wrapper(
            calls.update,
        )


class CallsResourceWithStreamingResponse:
    def __init__(self, calls: CallsResource) -> None:
        self._calls = calls

        self.update = to_streamed_response_wrapper(
            calls.update,
        )


class AsyncCallsResourceWithStreamingResponse:
    def __init__(self, calls: AsyncCallsResource) -> None:
        self._calls = calls

        self.update = async_to_streamed_response_wrapper(
            calls.update,
        )

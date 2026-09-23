# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

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
from ...types.texml import call_create_params
from ..._base_client import make_request_options
from ...types.texml.call_create_response import CallCreateResponse

__all__ = ["CallsResource", "AsyncCallsResource"]


class CallsResource(SyncAPIResource):
    """TeXML REST Commands"""

    @cached_property
    def with_raw_response(self) -> CallsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return CallsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CallsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return CallsResourceWithStreamingResponse(self)

    def create(
        self,
        connection_id: str,
        *,
        from_: str,
        to: str,
        method: Literal["GET", "POST"] | Omit = omit,
        texml: str | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallCreateResponse:
        """
        Initiate an outbound TeXML call using a TeXML application connection ID, not an
        account SID. Request parameter names are case-sensitive. From and To are
        required; Texml supplies inline instructions and Url overrides the application
        XML request URL. When neither is supplied, the application configuration
        supplies the instructions. The response is a flat call object without a data
        wrapper.

        Args:
          from_: The E.164-formatted phone number or SIP URI to present as the caller.

          to: The E.164-formatted phone number or SIP URI to call.

          method: HTTP method used to retrieve TeXML instructions from Url.

          texml: Inline TeXML instructions to execute when the call is answered.

          url: The URL from which to retrieve TeXML instructions. Overrides the TeXML
              application XML request URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._post(
            path_template("/texml/calls/{connection_id}", connection_id=connection_id),
            body=maybe_transform(
                {
                    "from_": from_,
                    "to": to,
                    "method": method,
                    "texml": texml,
                    "url": url,
                },
                call_create_params.CallCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallCreateResponse,
        )


class AsyncCallsResource(AsyncAPIResource):
    """TeXML REST Commands"""

    @cached_property
    def with_raw_response(self) -> AsyncCallsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCallsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCallsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncCallsResourceWithStreamingResponse(self)

    async def create(
        self,
        connection_id: str,
        *,
        from_: str,
        to: str,
        method: Literal["GET", "POST"] | Omit = omit,
        texml: str | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallCreateResponse:
        """
        Initiate an outbound TeXML call using a TeXML application connection ID, not an
        account SID. Request parameter names are case-sensitive. From and To are
        required; Texml supplies inline instructions and Url overrides the application
        XML request URL. When neither is supplied, the application configuration
        supplies the instructions. The response is a flat call object without a data
        wrapper.

        Args:
          from_: The E.164-formatted phone number or SIP URI to present as the caller.

          to: The E.164-formatted phone number or SIP URI to call.

          method: HTTP method used to retrieve TeXML instructions from Url.

          texml: Inline TeXML instructions to execute when the call is answered.

          url: The URL from which to retrieve TeXML instructions. Overrides the TeXML
              application XML request URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._post(
            path_template("/texml/calls/{connection_id}", connection_id=connection_id),
            body=await async_maybe_transform(
                {
                    "from_": from_,
                    "to": to,
                    "method": method,
                    "texml": texml,
                    "url": url,
                },
                call_create_params.CallCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallCreateResponse,
        )


class CallsResourceWithRawResponse:
    def __init__(self, calls: CallsResource) -> None:
        self._calls = calls

        self.create = to_raw_response_wrapper(
            calls.create,
        )


class AsyncCallsResourceWithRawResponse:
    def __init__(self, calls: AsyncCallsResource) -> None:
        self._calls = calls

        self.create = async_to_raw_response_wrapper(
            calls.create,
        )


class CallsResourceWithStreamingResponse:
    def __init__(self, calls: CallsResource) -> None:
        self._calls = calls

        self.create = to_streamed_response_wrapper(
            calls.create,
        )


class AsyncCallsResourceWithStreamingResponse:
    def __init__(self, calls: AsyncCallsResource) -> None:
        self._calls = calls

        self.create = async_to_streamed_response_wrapper(
            calls.create,
        )

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
from ..types.global_ip_protocol_list_response import GlobalIPProtocolListResponse

__all__ = ["GlobalIPProtocolsResource", "AsyncGlobalIPProtocolsResource"]


class GlobalIPProtocolsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GlobalIPProtocolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return GlobalIPProtocolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GlobalIPProtocolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return GlobalIPProtocolsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalIPProtocolListResponse:
        """List all Global IP Protocols"""
        return self._get(
            "/global_ip_protocols",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalIPProtocolListResponse,
        )


class AsyncGlobalIPProtocolsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGlobalIPProtocolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGlobalIPProtocolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGlobalIPProtocolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncGlobalIPProtocolsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalIPProtocolListResponse:
        """List all Global IP Protocols"""
        return await self._get(
            "/global_ip_protocols",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalIPProtocolListResponse,
        )


class GlobalIPProtocolsResourceWithRawResponse:
    def __init__(self, global_ip_protocols: GlobalIPProtocolsResource) -> None:
        self._global_ip_protocols = global_ip_protocols

        self.list = to_raw_response_wrapper(
            global_ip_protocols.list,
        )


class AsyncGlobalIPProtocolsResourceWithRawResponse:
    def __init__(self, global_ip_protocols: AsyncGlobalIPProtocolsResource) -> None:
        self._global_ip_protocols = global_ip_protocols

        self.list = async_to_raw_response_wrapper(
            global_ip_protocols.list,
        )


class GlobalIPProtocolsResourceWithStreamingResponse:
    def __init__(self, global_ip_protocols: GlobalIPProtocolsResource) -> None:
        self._global_ip_protocols = global_ip_protocols

        self.list = to_streamed_response_wrapper(
            global_ip_protocols.list,
        )


class AsyncGlobalIPProtocolsResourceWithStreamingResponse:
    def __init__(self, global_ip_protocols: AsyncGlobalIPProtocolsResource) -> None:
        self._global_ip_protocols = global_ip_protocols

        self.list = async_to_streamed_response_wrapper(
            global_ip_protocols.list,
        )

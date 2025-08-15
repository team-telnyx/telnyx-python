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
from ..types.global_ip_allowed_port_list_response import GlobalIPAllowedPortListResponse

__all__ = ["GlobalIPAllowedPortsResource", "AsyncGlobalIPAllowedPortsResource"]


class GlobalIPAllowedPortsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GlobalIPAllowedPortsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return GlobalIPAllowedPortsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GlobalIPAllowedPortsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return GlobalIPAllowedPortsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalIPAllowedPortListResponse:
        """List all Global IP Allowed Ports"""
        return self._get(
            "/global_ip_allowed_ports",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalIPAllowedPortListResponse,
        )


class AsyncGlobalIPAllowedPortsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGlobalIPAllowedPortsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGlobalIPAllowedPortsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGlobalIPAllowedPortsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncGlobalIPAllowedPortsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalIPAllowedPortListResponse:
        """List all Global IP Allowed Ports"""
        return await self._get(
            "/global_ip_allowed_ports",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalIPAllowedPortListResponse,
        )


class GlobalIPAllowedPortsResourceWithRawResponse:
    def __init__(self, global_ip_allowed_ports: GlobalIPAllowedPortsResource) -> None:
        self._global_ip_allowed_ports = global_ip_allowed_ports

        self.list = to_raw_response_wrapper(
            global_ip_allowed_ports.list,
        )


class AsyncGlobalIPAllowedPortsResourceWithRawResponse:
    def __init__(self, global_ip_allowed_ports: AsyncGlobalIPAllowedPortsResource) -> None:
        self._global_ip_allowed_ports = global_ip_allowed_ports

        self.list = async_to_raw_response_wrapper(
            global_ip_allowed_ports.list,
        )


class GlobalIPAllowedPortsResourceWithStreamingResponse:
    def __init__(self, global_ip_allowed_ports: GlobalIPAllowedPortsResource) -> None:
        self._global_ip_allowed_ports = global_ip_allowed_ports

        self.list = to_streamed_response_wrapper(
            global_ip_allowed_ports.list,
        )


class AsyncGlobalIPAllowedPortsResourceWithStreamingResponse:
    def __init__(self, global_ip_allowed_ports: AsyncGlobalIPAllowedPortsResource) -> None:
        self._global_ip_allowed_ports = global_ip_allowed_ports

        self.list = async_to_streamed_response_wrapper(
            global_ip_allowed_ports.list,
        )

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
from ..types.global_ip_health_check_type_list_response import GlobalIPHealthCheckTypeListResponse

__all__ = ["GlobalIPHealthCheckTypesResource", "AsyncGlobalIPHealthCheckTypesResource"]


class GlobalIPHealthCheckTypesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GlobalIPHealthCheckTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return GlobalIPHealthCheckTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GlobalIPHealthCheckTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return GlobalIPHealthCheckTypesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalIPHealthCheckTypeListResponse:
        """List all Global IP Health check types."""
        return self._get(
            "/global_ip_health_check_types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalIPHealthCheckTypeListResponse,
        )


class AsyncGlobalIPHealthCheckTypesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGlobalIPHealthCheckTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGlobalIPHealthCheckTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGlobalIPHealthCheckTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncGlobalIPHealthCheckTypesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalIPHealthCheckTypeListResponse:
        """List all Global IP Health check types."""
        return await self._get(
            "/global_ip_health_check_types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalIPHealthCheckTypeListResponse,
        )


class GlobalIPHealthCheckTypesResourceWithRawResponse:
    def __init__(self, global_ip_health_check_types: GlobalIPHealthCheckTypesResource) -> None:
        self._global_ip_health_check_types = global_ip_health_check_types

        self.list = to_raw_response_wrapper(
            global_ip_health_check_types.list,
        )


class AsyncGlobalIPHealthCheckTypesResourceWithRawResponse:
    def __init__(self, global_ip_health_check_types: AsyncGlobalIPHealthCheckTypesResource) -> None:
        self._global_ip_health_check_types = global_ip_health_check_types

        self.list = async_to_raw_response_wrapper(
            global_ip_health_check_types.list,
        )


class GlobalIPHealthCheckTypesResourceWithStreamingResponse:
    def __init__(self, global_ip_health_check_types: GlobalIPHealthCheckTypesResource) -> None:
        self._global_ip_health_check_types = global_ip_health_check_types

        self.list = to_streamed_response_wrapper(
            global_ip_health_check_types.list,
        )


class AsyncGlobalIPHealthCheckTypesResourceWithStreamingResponse:
    def __init__(self, global_ip_health_check_types: AsyncGlobalIPHealthCheckTypesResource) -> None:
        self._global_ip_health_check_types = global_ip_health_check_types

        self.list = async_to_streamed_response_wrapper(
            global_ip_health_check_types.list,
        )

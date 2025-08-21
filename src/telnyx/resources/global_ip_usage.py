# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import global_ip_usage_retrieve_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.global_ip_usage_retrieve_response import GlobalIPUsageRetrieveResponse

__all__ = ["GlobalIPUsageResource", "AsyncGlobalIPUsageResource"]


class GlobalIPUsageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GlobalIPUsageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return GlobalIPUsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GlobalIPUsageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return GlobalIPUsageResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        filter: global_ip_usage_retrieve_params.Filter | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalIPUsageRetrieveResponse:
        """
        Global IP Usage Metrics

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[global_ip_id][in]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/global_ip_usage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"filter": filter}, global_ip_usage_retrieve_params.GlobalIPUsageRetrieveParams),
            ),
            cast_to=GlobalIPUsageRetrieveResponse,
        )


class AsyncGlobalIPUsageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGlobalIPUsageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGlobalIPUsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGlobalIPUsageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncGlobalIPUsageResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        filter: global_ip_usage_retrieve_params.Filter | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalIPUsageRetrieveResponse:
        """
        Global IP Usage Metrics

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[global_ip_id][in]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/global_ip_usage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"filter": filter}, global_ip_usage_retrieve_params.GlobalIPUsageRetrieveParams
                ),
            ),
            cast_to=GlobalIPUsageRetrieveResponse,
        )


class GlobalIPUsageResourceWithRawResponse:
    def __init__(self, global_ip_usage: GlobalIPUsageResource) -> None:
        self._global_ip_usage = global_ip_usage

        self.retrieve = to_raw_response_wrapper(
            global_ip_usage.retrieve,
        )


class AsyncGlobalIPUsageResourceWithRawResponse:
    def __init__(self, global_ip_usage: AsyncGlobalIPUsageResource) -> None:
        self._global_ip_usage = global_ip_usage

        self.retrieve = async_to_raw_response_wrapper(
            global_ip_usage.retrieve,
        )


class GlobalIPUsageResourceWithStreamingResponse:
    def __init__(self, global_ip_usage: GlobalIPUsageResource) -> None:
        self._global_ip_usage = global_ip_usage

        self.retrieve = to_streamed_response_wrapper(
            global_ip_usage.retrieve,
        )


class AsyncGlobalIPUsageResourceWithStreamingResponse:
    def __init__(self, global_ip_usage: AsyncGlobalIPUsageResource) -> None:
        self._global_ip_usage = global_ip_usage

        self.retrieve = async_to_streamed_response_wrapper(
            global_ip_usage.retrieve,
        )

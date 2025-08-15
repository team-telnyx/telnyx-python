# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import global_ip_assignments_usage_retrieve_params
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
from ..types.global_ip_assignments_usage_retrieve_response import GlobalIPAssignmentsUsageRetrieveResponse

__all__ = ["GlobalIPAssignmentsUsageResource", "AsyncGlobalIPAssignmentsUsageResource"]


class GlobalIPAssignmentsUsageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GlobalIPAssignmentsUsageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return GlobalIPAssignmentsUsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GlobalIPAssignmentsUsageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return GlobalIPAssignmentsUsageResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        filter: global_ip_assignments_usage_retrieve_params.Filter | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalIPAssignmentsUsageRetrieveResponse:
        """
        Global IP Assignment Usage Metrics

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[global_ip_assignment_id][in], filter[global_ip_id][in]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/global_ip_assignments_usage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"filter": filter},
                    global_ip_assignments_usage_retrieve_params.GlobalIPAssignmentsUsageRetrieveParams,
                ),
            ),
            cast_to=GlobalIPAssignmentsUsageRetrieveResponse,
        )


class AsyncGlobalIPAssignmentsUsageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGlobalIPAssignmentsUsageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGlobalIPAssignmentsUsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGlobalIPAssignmentsUsageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncGlobalIPAssignmentsUsageResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        filter: global_ip_assignments_usage_retrieve_params.Filter | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalIPAssignmentsUsageRetrieveResponse:
        """
        Global IP Assignment Usage Metrics

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[global_ip_assignment_id][in], filter[global_ip_id][in]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/global_ip_assignments_usage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"filter": filter},
                    global_ip_assignments_usage_retrieve_params.GlobalIPAssignmentsUsageRetrieveParams,
                ),
            ),
            cast_to=GlobalIPAssignmentsUsageRetrieveResponse,
        )


class GlobalIPAssignmentsUsageResourceWithRawResponse:
    def __init__(self, global_ip_assignments_usage: GlobalIPAssignmentsUsageResource) -> None:
        self._global_ip_assignments_usage = global_ip_assignments_usage

        self.retrieve = to_raw_response_wrapper(
            global_ip_assignments_usage.retrieve,
        )


class AsyncGlobalIPAssignmentsUsageResourceWithRawResponse:
    def __init__(self, global_ip_assignments_usage: AsyncGlobalIPAssignmentsUsageResource) -> None:
        self._global_ip_assignments_usage = global_ip_assignments_usage

        self.retrieve = async_to_raw_response_wrapper(
            global_ip_assignments_usage.retrieve,
        )


class GlobalIPAssignmentsUsageResourceWithStreamingResponse:
    def __init__(self, global_ip_assignments_usage: GlobalIPAssignmentsUsageResource) -> None:
        self._global_ip_assignments_usage = global_ip_assignments_usage

        self.retrieve = to_streamed_response_wrapper(
            global_ip_assignments_usage.retrieve,
        )


class AsyncGlobalIPAssignmentsUsageResourceWithStreamingResponse:
    def __init__(self, global_ip_assignments_usage: AsyncGlobalIPAssignmentsUsageResource) -> None:
        self._global_ip_assignments_usage = global_ip_assignments_usage

        self.retrieve = async_to_streamed_response_wrapper(
            global_ip_assignments_usage.retrieve,
        )

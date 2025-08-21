# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import virtual_cross_connects_coverage_list_params
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
from ..types.virtual_cross_connects_coverage_list_response import VirtualCrossConnectsCoverageListResponse

__all__ = ["VirtualCrossConnectsCoverageResource", "AsyncVirtualCrossConnectsCoverageResource"]


class VirtualCrossConnectsCoverageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VirtualCrossConnectsCoverageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return VirtualCrossConnectsCoverageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VirtualCrossConnectsCoverageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return VirtualCrossConnectsCoverageResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        filter: virtual_cross_connects_coverage_list_params.Filter | NotGiven = NOT_GIVEN,
        filters: virtual_cross_connects_coverage_list_params.Filters | NotGiven = NOT_GIVEN,
        page: virtual_cross_connects_coverage_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VirtualCrossConnectsCoverageListResponse:
        """
        List Virtual Cross Connects Cloud Coverage.<br /><br />This endpoint shows which
        cloud regions are available for the `location_code` your Virtual Cross Connect
        will be provisioned in.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[cloud_provider], filter[cloud_provider_region], filter[location.region],
              filter[location.site], filter[location.pop], filter[location.code]

          filters:
              Consolidated filters parameter (deepObject style). Originally:
              filters[available_bandwidth][contains]

          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/virtual_cross_connects_coverage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "filters": filters,
                        "page": page,
                    },
                    virtual_cross_connects_coverage_list_params.VirtualCrossConnectsCoverageListParams,
                ),
            ),
            cast_to=VirtualCrossConnectsCoverageListResponse,
        )


class AsyncVirtualCrossConnectsCoverageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVirtualCrossConnectsCoverageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVirtualCrossConnectsCoverageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVirtualCrossConnectsCoverageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncVirtualCrossConnectsCoverageResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        filter: virtual_cross_connects_coverage_list_params.Filter | NotGiven = NOT_GIVEN,
        filters: virtual_cross_connects_coverage_list_params.Filters | NotGiven = NOT_GIVEN,
        page: virtual_cross_connects_coverage_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VirtualCrossConnectsCoverageListResponse:
        """
        List Virtual Cross Connects Cloud Coverage.<br /><br />This endpoint shows which
        cloud regions are available for the `location_code` your Virtual Cross Connect
        will be provisioned in.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[cloud_provider], filter[cloud_provider_region], filter[location.region],
              filter[location.site], filter[location.pop], filter[location.code]

          filters:
              Consolidated filters parameter (deepObject style). Originally:
              filters[available_bandwidth][contains]

          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/virtual_cross_connects_coverage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "filters": filters,
                        "page": page,
                    },
                    virtual_cross_connects_coverage_list_params.VirtualCrossConnectsCoverageListParams,
                ),
            ),
            cast_to=VirtualCrossConnectsCoverageListResponse,
        )


class VirtualCrossConnectsCoverageResourceWithRawResponse:
    def __init__(self, virtual_cross_connects_coverage: VirtualCrossConnectsCoverageResource) -> None:
        self._virtual_cross_connects_coverage = virtual_cross_connects_coverage

        self.list = to_raw_response_wrapper(
            virtual_cross_connects_coverage.list,
        )


class AsyncVirtualCrossConnectsCoverageResourceWithRawResponse:
    def __init__(self, virtual_cross_connects_coverage: AsyncVirtualCrossConnectsCoverageResource) -> None:
        self._virtual_cross_connects_coverage = virtual_cross_connects_coverage

        self.list = async_to_raw_response_wrapper(
            virtual_cross_connects_coverage.list,
        )


class VirtualCrossConnectsCoverageResourceWithStreamingResponse:
    def __init__(self, virtual_cross_connects_coverage: VirtualCrossConnectsCoverageResource) -> None:
        self._virtual_cross_connects_coverage = virtual_cross_connects_coverage

        self.list = to_streamed_response_wrapper(
            virtual_cross_connects_coverage.list,
        )


class AsyncVirtualCrossConnectsCoverageResourceWithStreamingResponse:
    def __init__(self, virtual_cross_connects_coverage: AsyncVirtualCrossConnectsCoverageResource) -> None:
        self._virtual_cross_connects_coverage = virtual_cross_connects_coverage

        self.list = async_to_streamed_response_wrapper(
            virtual_cross_connects_coverage.list,
        )

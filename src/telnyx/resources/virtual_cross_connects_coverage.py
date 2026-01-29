# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import virtual_cross_connects_coverage_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from .._base_client import AsyncPaginator, make_request_options
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
        filter: virtual_cross_connects_coverage_list_params.Filter | Omit = omit,
        filters: virtual_cross_connects_coverage_list_params.Filters | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[VirtualCrossConnectsCoverageListResponse]:
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/virtual_cross_connects_coverage",
            page=SyncDefaultFlatPagination[VirtualCrossConnectsCoverageListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "filters": filters,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    virtual_cross_connects_coverage_list_params.VirtualCrossConnectsCoverageListParams,
                ),
            ),
            model=VirtualCrossConnectsCoverageListResponse,
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

    def list(
        self,
        *,
        filter: virtual_cross_connects_coverage_list_params.Filter | Omit = omit,
        filters: virtual_cross_connects_coverage_list_params.Filters | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[
        VirtualCrossConnectsCoverageListResponse, AsyncDefaultFlatPagination[VirtualCrossConnectsCoverageListResponse]
    ]:
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/virtual_cross_connects_coverage",
            page=AsyncDefaultFlatPagination[VirtualCrossConnectsCoverageListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "filters": filters,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    virtual_cross_connects_coverage_list_params.VirtualCrossConnectsCoverageListParams,
                ),
            ),
            model=VirtualCrossConnectsCoverageListResponse,
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

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import network_coverage_list_params
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
from ..types.network_coverage_list_response import NetworkCoverageListResponse

__all__ = ["NetworkCoverageResource", "AsyncNetworkCoverageResource"]


class NetworkCoverageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NetworkCoverageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return NetworkCoverageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NetworkCoverageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return NetworkCoverageResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        filter: network_coverage_list_params.Filter | Omit = omit,
        filters: network_coverage_list_params.Filters | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[NetworkCoverageListResponse]:
        """
        List all locations and the interfaces that region supports

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[location.region], filter[location.site], filter[location.pop],
              filter[location.code]

          filters:
              Consolidated filters parameter (deepObject style). Originally:
              filters[available_services][contains]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/network_coverage",
            page=SyncDefaultFlatPagination[NetworkCoverageListResponse],
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
                    network_coverage_list_params.NetworkCoverageListParams,
                ),
            ),
            model=NetworkCoverageListResponse,
        )


class AsyncNetworkCoverageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNetworkCoverageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNetworkCoverageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNetworkCoverageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncNetworkCoverageResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        filter: network_coverage_list_params.Filter | Omit = omit,
        filters: network_coverage_list_params.Filters | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[NetworkCoverageListResponse, AsyncDefaultFlatPagination[NetworkCoverageListResponse]]:
        """
        List all locations and the interfaces that region supports

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[location.region], filter[location.site], filter[location.pop],
              filter[location.code]

          filters:
              Consolidated filters parameter (deepObject style). Originally:
              filters[available_services][contains]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/network_coverage",
            page=AsyncDefaultFlatPagination[NetworkCoverageListResponse],
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
                    network_coverage_list_params.NetworkCoverageListParams,
                ),
            ),
            model=NetworkCoverageListResponse,
        )


class NetworkCoverageResourceWithRawResponse:
    def __init__(self, network_coverage: NetworkCoverageResource) -> None:
        self._network_coverage = network_coverage

        self.list = to_raw_response_wrapper(
            network_coverage.list,
        )


class AsyncNetworkCoverageResourceWithRawResponse:
    def __init__(self, network_coverage: AsyncNetworkCoverageResource) -> None:
        self._network_coverage = network_coverage

        self.list = async_to_raw_response_wrapper(
            network_coverage.list,
        )


class NetworkCoverageResourceWithStreamingResponse:
    def __init__(self, network_coverage: NetworkCoverageResource) -> None:
        self._network_coverage = network_coverage

        self.list = to_streamed_response_wrapper(
            network_coverage.list,
        )


class AsyncNetworkCoverageResourceWithStreamingResponse:
    def __init__(self, network_coverage: AsyncNetworkCoverageResource) -> None:
        self._network_coverage = network_coverage

        self.list = async_to_streamed_response_wrapper(
            network_coverage.list,
        )

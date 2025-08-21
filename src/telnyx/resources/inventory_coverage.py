# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import inventory_coverage_list_params
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
from ..types.inventory_coverage_list_response import InventoryCoverageListResponse

__all__ = ["InventoryCoverageResource", "AsyncInventoryCoverageResource"]


class InventoryCoverageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InventoryCoverageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return InventoryCoverageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InventoryCoverageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return InventoryCoverageResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        filter: inventory_coverage_list_params.Filter | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InventoryCoverageListResponse:
        """Creates an inventory coverage request.

        If locality, npa or
        national_destination_code is used in groupBy, and no region or locality filters
        are used, the whole paginated set is returned.

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[npa],
              filter[nxx], filter[administrative_area], filter[phone_number_type],
              filter[country_code], filter[count], filter[features], filter[groupBy]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/inventory_coverage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"filter": filter}, inventory_coverage_list_params.InventoryCoverageListParams),
            ),
            cast_to=InventoryCoverageListResponse,
        )


class AsyncInventoryCoverageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInventoryCoverageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInventoryCoverageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInventoryCoverageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncInventoryCoverageResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        filter: inventory_coverage_list_params.Filter | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InventoryCoverageListResponse:
        """Creates an inventory coverage request.

        If locality, npa or
        national_destination_code is used in groupBy, and no region or locality filters
        are used, the whole paginated set is returned.

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[npa],
              filter[nxx], filter[administrative_area], filter[phone_number_type],
              filter[country_code], filter[count], filter[features], filter[groupBy]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/inventory_coverage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"filter": filter}, inventory_coverage_list_params.InventoryCoverageListParams
                ),
            ),
            cast_to=InventoryCoverageListResponse,
        )


class InventoryCoverageResourceWithRawResponse:
    def __init__(self, inventory_coverage: InventoryCoverageResource) -> None:
        self._inventory_coverage = inventory_coverage

        self.list = to_raw_response_wrapper(
            inventory_coverage.list,
        )


class AsyncInventoryCoverageResourceWithRawResponse:
    def __init__(self, inventory_coverage: AsyncInventoryCoverageResource) -> None:
        self._inventory_coverage = inventory_coverage

        self.list = async_to_raw_response_wrapper(
            inventory_coverage.list,
        )


class InventoryCoverageResourceWithStreamingResponse:
    def __init__(self, inventory_coverage: InventoryCoverageResource) -> None:
        self._inventory_coverage = inventory_coverage

        self.list = to_streamed_response_wrapper(
            inventory_coverage.list,
        )


class AsyncInventoryCoverageResourceWithStreamingResponse:
    def __init__(self, inventory_coverage: AsyncInventoryCoverageResource) -> None:
        self._inventory_coverage = inventory_coverage

        self.list = async_to_streamed_response_wrapper(
            inventory_coverage.list,
        )

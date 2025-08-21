# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import wireless_retrieve_regions_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .detail_records_reports import (
    DetailRecordsReportsResource,
    AsyncDetailRecordsReportsResource,
    DetailRecordsReportsResourceWithRawResponse,
    AsyncDetailRecordsReportsResourceWithRawResponse,
    DetailRecordsReportsResourceWithStreamingResponse,
    AsyncDetailRecordsReportsResourceWithStreamingResponse,
)
from ...types.wireless_retrieve_regions_response import WirelessRetrieveRegionsResponse

__all__ = ["WirelessResource", "AsyncWirelessResource"]


class WirelessResource(SyncAPIResource):
    @cached_property
    def detail_records_reports(self) -> DetailRecordsReportsResource:
        return DetailRecordsReportsResource(self._client)

    @cached_property
    def with_raw_response(self) -> WirelessResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return WirelessResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WirelessResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return WirelessResourceWithStreamingResponse(self)

    def retrieve_regions(
        self,
        *,
        product: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WirelessRetrieveRegionsResponse:
        """
        Retrieve all wireless regions for the given product.

        Args:
          product: The product for which to list regions (e.g., 'public_ips',
              'private_wireless_gateways').

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/wireless/regions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"product": product}, wireless_retrieve_regions_params.WirelessRetrieveRegionsParams
                ),
            ),
            cast_to=WirelessRetrieveRegionsResponse,
        )


class AsyncWirelessResource(AsyncAPIResource):
    @cached_property
    def detail_records_reports(self) -> AsyncDetailRecordsReportsResource:
        return AsyncDetailRecordsReportsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWirelessResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWirelessResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWirelessResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncWirelessResourceWithStreamingResponse(self)

    async def retrieve_regions(
        self,
        *,
        product: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WirelessRetrieveRegionsResponse:
        """
        Retrieve all wireless regions for the given product.

        Args:
          product: The product for which to list regions (e.g., 'public_ips',
              'private_wireless_gateways').

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/wireless/regions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"product": product}, wireless_retrieve_regions_params.WirelessRetrieveRegionsParams
                ),
            ),
            cast_to=WirelessRetrieveRegionsResponse,
        )


class WirelessResourceWithRawResponse:
    def __init__(self, wireless: WirelessResource) -> None:
        self._wireless = wireless

        self.retrieve_regions = to_raw_response_wrapper(
            wireless.retrieve_regions,
        )

    @cached_property
    def detail_records_reports(self) -> DetailRecordsReportsResourceWithRawResponse:
        return DetailRecordsReportsResourceWithRawResponse(self._wireless.detail_records_reports)


class AsyncWirelessResourceWithRawResponse:
    def __init__(self, wireless: AsyncWirelessResource) -> None:
        self._wireless = wireless

        self.retrieve_regions = async_to_raw_response_wrapper(
            wireless.retrieve_regions,
        )

    @cached_property
    def detail_records_reports(self) -> AsyncDetailRecordsReportsResourceWithRawResponse:
        return AsyncDetailRecordsReportsResourceWithRawResponse(self._wireless.detail_records_reports)


class WirelessResourceWithStreamingResponse:
    def __init__(self, wireless: WirelessResource) -> None:
        self._wireless = wireless

        self.retrieve_regions = to_streamed_response_wrapper(
            wireless.retrieve_regions,
        )

    @cached_property
    def detail_records_reports(self) -> DetailRecordsReportsResourceWithStreamingResponse:
        return DetailRecordsReportsResourceWithStreamingResponse(self._wireless.detail_records_reports)


class AsyncWirelessResourceWithStreamingResponse:
    def __init__(self, wireless: AsyncWirelessResource) -> None:
        self._wireless = wireless

        self.retrieve_regions = async_to_streamed_response_wrapper(
            wireless.retrieve_regions,
        )

    @cached_property
    def detail_records_reports(self) -> AsyncDetailRecordsReportsResourceWithStreamingResponse:
        return AsyncDetailRecordsReportsResourceWithStreamingResponse(self._wireless.detail_records_reports)

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
from ..types.region_list_response import RegionListResponse

__all__ = ["RegionsResource", "AsyncRegionsResource"]


class RegionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RegionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return RegionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RegionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return RegionsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RegionListResponse:
        """List all regions and the interfaces that region supports"""
        return self._get(
            "/regions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegionListResponse,
        )


class AsyncRegionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRegionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRegionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRegionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncRegionsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RegionListResponse:
        """List all regions and the interfaces that region supports"""
        return await self._get(
            "/regions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegionListResponse,
        )


class RegionsResourceWithRawResponse:
    def __init__(self, regions: RegionsResource) -> None:
        self._regions = regions

        self.list = to_raw_response_wrapper(
            regions.list,
        )


class AsyncRegionsResourceWithRawResponse:
    def __init__(self, regions: AsyncRegionsResource) -> None:
        self._regions = regions

        self.list = async_to_raw_response_wrapper(
            regions.list,
        )


class RegionsResourceWithStreamingResponse:
    def __init__(self, regions: RegionsResource) -> None:
        self._regions = regions

        self.list = to_streamed_response_wrapper(
            regions.list,
        )


class AsyncRegionsResourceWithStreamingResponse:
    def __init__(self, regions: AsyncRegionsResource) -> None:
        self._regions = regions

        self.list = async_to_streamed_response_wrapper(
            regions.list,
        )

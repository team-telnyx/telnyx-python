# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.campaign_builder.brand_qualify_by_usecase_response import BrandQualifyByUsecaseResponse

__all__ = ["BrandResource", "AsyncBrandResource"]


class BrandResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BrandResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return BrandResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrandResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return BrandResourceWithStreamingResponse(self)

    def qualify_by_usecase(
        self,
        usecase: str,
        *,
        brand_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrandQualifyByUsecaseResponse:
        """
        This endpoint allows you to see whether or not the supplied brand is suitable
        for your desired campaign use case.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        if not usecase:
            raise ValueError(f"Expected a non-empty value for `usecase` but received {usecase!r}")
        return self._get(
            f"/campaignBuilder/brand/{brand_id}/usecase/{usecase}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandQualifyByUsecaseResponse,
        )


class AsyncBrandResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBrandResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBrandResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBrandResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncBrandResourceWithStreamingResponse(self)

    async def qualify_by_usecase(
        self,
        usecase: str,
        *,
        brand_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrandQualifyByUsecaseResponse:
        """
        This endpoint allows you to see whether or not the supplied brand is suitable
        for your desired campaign use case.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        if not usecase:
            raise ValueError(f"Expected a non-empty value for `usecase` but received {usecase!r}")
        return await self._get(
            f"/campaignBuilder/brand/{brand_id}/usecase/{usecase}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandQualifyByUsecaseResponse,
        )


class BrandResourceWithRawResponse:
    def __init__(self, brand: BrandResource) -> None:
        self._brand = brand

        self.qualify_by_usecase = to_raw_response_wrapper(
            brand.qualify_by_usecase,
        )


class AsyncBrandResourceWithRawResponse:
    def __init__(self, brand: AsyncBrandResource) -> None:
        self._brand = brand

        self.qualify_by_usecase = async_to_raw_response_wrapper(
            brand.qualify_by_usecase,
        )


class BrandResourceWithStreamingResponse:
    def __init__(self, brand: BrandResource) -> None:
        self._brand = brand

        self.qualify_by_usecase = to_streamed_response_wrapper(
            brand.qualify_by_usecase,
        )


class AsyncBrandResourceWithStreamingResponse:
    def __init__(self, brand: AsyncBrandResource) -> None:
        self._brand = brand

        self.qualify_by_usecase = async_to_streamed_response_wrapper(
            brand.qualify_by_usecase,
        )

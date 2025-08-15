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
from ..types.country_coverage_retrieve_response import CountryCoverageRetrieveResponse
from ..types.country_coverage_retrieve_country_response import CountryCoverageRetrieveCountryResponse

__all__ = ["CountryCoverageResource", "AsyncCountryCoverageResource"]


class CountryCoverageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CountryCoverageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return CountryCoverageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CountryCoverageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return CountryCoverageResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CountryCoverageRetrieveResponse:
        """Get country coverage"""
        return self._get(
            "/country_coverage",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CountryCoverageRetrieveResponse,
        )

    def retrieve_country(
        self,
        country_code: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CountryCoverageRetrieveCountryResponse:
        """
        Get coverage for a specific country

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not country_code:
            raise ValueError(f"Expected a non-empty value for `country_code` but received {country_code!r}")
        return self._get(
            f"/country_coverage/countries/{country_code}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CountryCoverageRetrieveCountryResponse,
        )


class AsyncCountryCoverageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCountryCoverageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCountryCoverageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCountryCoverageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncCountryCoverageResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CountryCoverageRetrieveResponse:
        """Get country coverage"""
        return await self._get(
            "/country_coverage",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CountryCoverageRetrieveResponse,
        )

    async def retrieve_country(
        self,
        country_code: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CountryCoverageRetrieveCountryResponse:
        """
        Get coverage for a specific country

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not country_code:
            raise ValueError(f"Expected a non-empty value for `country_code` but received {country_code!r}")
        return await self._get(
            f"/country_coverage/countries/{country_code}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CountryCoverageRetrieveCountryResponse,
        )


class CountryCoverageResourceWithRawResponse:
    def __init__(self, country_coverage: CountryCoverageResource) -> None:
        self._country_coverage = country_coverage

        self.retrieve = to_raw_response_wrapper(
            country_coverage.retrieve,
        )
        self.retrieve_country = to_raw_response_wrapper(
            country_coverage.retrieve_country,
        )


class AsyncCountryCoverageResourceWithRawResponse:
    def __init__(self, country_coverage: AsyncCountryCoverageResource) -> None:
        self._country_coverage = country_coverage

        self.retrieve = async_to_raw_response_wrapper(
            country_coverage.retrieve,
        )
        self.retrieve_country = async_to_raw_response_wrapper(
            country_coverage.retrieve_country,
        )


class CountryCoverageResourceWithStreamingResponse:
    def __init__(self, country_coverage: CountryCoverageResource) -> None:
        self._country_coverage = country_coverage

        self.retrieve = to_streamed_response_wrapper(
            country_coverage.retrieve,
        )
        self.retrieve_country = to_streamed_response_wrapper(
            country_coverage.retrieve_country,
        )


class AsyncCountryCoverageResourceWithStreamingResponse:
    def __init__(self, country_coverage: AsyncCountryCoverageResource) -> None:
        self._country_coverage = country_coverage

        self.retrieve = async_to_streamed_response_wrapper(
            country_coverage.retrieve,
        )
        self.retrieve_country = async_to_streamed_response_wrapper(
            country_coverage.retrieve_country,
        )

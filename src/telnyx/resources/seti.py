# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import seti_retrieve_black_box_test_results_params
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
from ..types.seti_retrieve_black_box_test_results_response import SetiRetrieveBlackBoxTestResultsResponse

__all__ = ["SetiResource", "AsyncSetiResource"]


class SetiResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SetiResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return SetiResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SetiResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return SetiResourceWithStreamingResponse(self)

    def retrieve_black_box_test_results(
        self,
        *,
        filter: seti_retrieve_black_box_test_results_params.Filter | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SetiRetrieveBlackBoxTestResultsResponse:
        """
        Returns the results of the various black box tests

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[product]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/seti/black_box_test_results",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"filter": filter},
                    seti_retrieve_black_box_test_results_params.SetiRetrieveBlackBoxTestResultsParams,
                ),
            ),
            cast_to=SetiRetrieveBlackBoxTestResultsResponse,
        )


class AsyncSetiResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSetiResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSetiResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSetiResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncSetiResourceWithStreamingResponse(self)

    async def retrieve_black_box_test_results(
        self,
        *,
        filter: seti_retrieve_black_box_test_results_params.Filter | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SetiRetrieveBlackBoxTestResultsResponse:
        """
        Returns the results of the various black box tests

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[product]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/seti/black_box_test_results",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"filter": filter},
                    seti_retrieve_black_box_test_results_params.SetiRetrieveBlackBoxTestResultsParams,
                ),
            ),
            cast_to=SetiRetrieveBlackBoxTestResultsResponse,
        )


class SetiResourceWithRawResponse:
    def __init__(self, seti: SetiResource) -> None:
        self._seti = seti

        self.retrieve_black_box_test_results = to_raw_response_wrapper(
            seti.retrieve_black_box_test_results,
        )


class AsyncSetiResourceWithRawResponse:
    def __init__(self, seti: AsyncSetiResource) -> None:
        self._seti = seti

        self.retrieve_black_box_test_results = async_to_raw_response_wrapper(
            seti.retrieve_black_box_test_results,
        )


class SetiResourceWithStreamingResponse:
    def __init__(self, seti: SetiResource) -> None:
        self._seti = seti

        self.retrieve_black_box_test_results = to_streamed_response_wrapper(
            seti.retrieve_black_box_test_results,
        )


class AsyncSetiResourceWithStreamingResponse:
    def __init__(self, seti: AsyncSetiResource) -> None:
        self._seti = seti

        self.retrieve_black_box_test_results = async_to_streamed_response_wrapper(
            seti.retrieve_black_box_test_results,
        )

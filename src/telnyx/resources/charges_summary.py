# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ..types import charges_summary_retrieve_params
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
from ..types.charges_summary_retrieve_response import ChargesSummaryRetrieveResponse

__all__ = ["ChargesSummaryResource", "AsyncChargesSummaryResource"]


class ChargesSummaryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChargesSummaryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ChargesSummaryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChargesSummaryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ChargesSummaryResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        end_date: Union[str, date],
        start_date: Union[str, date],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChargesSummaryRetrieveResponse:
        """Retrieve a summary of monthly charges for a specified date range.

        The date range
        cannot exceed 31 days.

        Args:
          end_date: End date for the charges summary in ISO date format (YYYY-MM-DD). The date is
              exclusive, data for the end_date itself is not included in the report. The
              interval between start_date and end_date cannot exceed 31 days.

          start_date: Start date for the charges summary in ISO date format (YYYY-MM-DD)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/charges_summary",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    charges_summary_retrieve_params.ChargesSummaryRetrieveParams,
                ),
            ),
            cast_to=ChargesSummaryRetrieveResponse,
        )


class AsyncChargesSummaryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChargesSummaryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChargesSummaryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChargesSummaryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncChargesSummaryResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        end_date: Union[str, date],
        start_date: Union[str, date],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChargesSummaryRetrieveResponse:
        """Retrieve a summary of monthly charges for a specified date range.

        The date range
        cannot exceed 31 days.

        Args:
          end_date: End date for the charges summary in ISO date format (YYYY-MM-DD). The date is
              exclusive, data for the end_date itself is not included in the report. The
              interval between start_date and end_date cannot exceed 31 days.

          start_date: Start date for the charges summary in ISO date format (YYYY-MM-DD)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/charges_summary",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    charges_summary_retrieve_params.ChargesSummaryRetrieveParams,
                ),
            ),
            cast_to=ChargesSummaryRetrieveResponse,
        )


class ChargesSummaryResourceWithRawResponse:
    def __init__(self, charges_summary: ChargesSummaryResource) -> None:
        self._charges_summary = charges_summary

        self.retrieve = to_raw_response_wrapper(
            charges_summary.retrieve,
        )


class AsyncChargesSummaryResourceWithRawResponse:
    def __init__(self, charges_summary: AsyncChargesSummaryResource) -> None:
        self._charges_summary = charges_summary

        self.retrieve = async_to_raw_response_wrapper(
            charges_summary.retrieve,
        )


class ChargesSummaryResourceWithStreamingResponse:
    def __init__(self, charges_summary: ChargesSummaryResource) -> None:
        self._charges_summary = charges_summary

        self.retrieve = to_streamed_response_wrapper(
            charges_summary.retrieve,
        )


class AsyncChargesSummaryResourceWithStreamingResponse:
    def __init__(self, charges_summary: AsyncChargesSummaryResource) -> None:
        self._charges_summary = charges_summary

        self.retrieve = async_to_streamed_response_wrapper(
            charges_summary.retrieve,
        )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal

import httpx

from ..types import charges_breakdown_retrieve_params
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
from ..types.charges_breakdown_retrieve_response import ChargesBreakdownRetrieveResponse

__all__ = ["ChargesBreakdownResource", "AsyncChargesBreakdownResource"]


class ChargesBreakdownResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChargesBreakdownResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ChargesBreakdownResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChargesBreakdownResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ChargesBreakdownResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        start_date: Union[str, date],
        end_date: Union[str, date] | NotGiven = NOT_GIVEN,
        format: Literal["json", "csv"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChargesBreakdownRetrieveResponse:
        """
        Retrieve a detailed breakdown of monthly charges for phone numbers in a
        specified date range. The date range cannot exceed 31 days.

        Args:
          start_date: Start date for the charges breakdown in ISO date format (YYYY-MM-DD)

          end_date: End date for the charges breakdown in ISO date format (YYYY-MM-DD). If not
              provided, defaults to start_date + 1 month. The date is exclusive, data for the
              end_date itself is not included in the report. The interval between start_date
              and end_date cannot exceed 31 days.

          format: Response format

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/charges_breakdown",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "start_date": start_date,
                        "end_date": end_date,
                        "format": format,
                    },
                    charges_breakdown_retrieve_params.ChargesBreakdownRetrieveParams,
                ),
            ),
            cast_to=ChargesBreakdownRetrieveResponse,
        )


class AsyncChargesBreakdownResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChargesBreakdownResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChargesBreakdownResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChargesBreakdownResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncChargesBreakdownResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        start_date: Union[str, date],
        end_date: Union[str, date] | NotGiven = NOT_GIVEN,
        format: Literal["json", "csv"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChargesBreakdownRetrieveResponse:
        """
        Retrieve a detailed breakdown of monthly charges for phone numbers in a
        specified date range. The date range cannot exceed 31 days.

        Args:
          start_date: Start date for the charges breakdown in ISO date format (YYYY-MM-DD)

          end_date: End date for the charges breakdown in ISO date format (YYYY-MM-DD). If not
              provided, defaults to start_date + 1 month. The date is exclusive, data for the
              end_date itself is not included in the report. The interval between start_date
              and end_date cannot exceed 31 days.

          format: Response format

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/charges_breakdown",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "start_date": start_date,
                        "end_date": end_date,
                        "format": format,
                    },
                    charges_breakdown_retrieve_params.ChargesBreakdownRetrieveParams,
                ),
            ),
            cast_to=ChargesBreakdownRetrieveResponse,
        )


class ChargesBreakdownResourceWithRawResponse:
    def __init__(self, charges_breakdown: ChargesBreakdownResource) -> None:
        self._charges_breakdown = charges_breakdown

        self.retrieve = to_raw_response_wrapper(
            charges_breakdown.retrieve,
        )


class AsyncChargesBreakdownResourceWithRawResponse:
    def __init__(self, charges_breakdown: AsyncChargesBreakdownResource) -> None:
        self._charges_breakdown = charges_breakdown

        self.retrieve = async_to_raw_response_wrapper(
            charges_breakdown.retrieve,
        )


class ChargesBreakdownResourceWithStreamingResponse:
    def __init__(self, charges_breakdown: ChargesBreakdownResource) -> None:
        self._charges_breakdown = charges_breakdown

        self.retrieve = to_streamed_response_wrapper(
            charges_breakdown.retrieve,
        )


class AsyncChargesBreakdownResourceWithStreamingResponse:
    def __init__(self, charges_breakdown: AsyncChargesBreakdownResource) -> None:
        self._charges_breakdown = charges_breakdown

        self.retrieve = async_to_streamed_response_wrapper(
            charges_breakdown.retrieve,
        )

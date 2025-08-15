# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

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
from ...types.reports import cdr_usage_report_fetch_sync_params
from ...types.reports.cdr_usage_report_fetch_sync_response import CdrUsageReportFetchSyncResponse

__all__ = ["CdrUsageReportsResource", "AsyncCdrUsageReportsResource"]


class CdrUsageReportsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CdrUsageReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return CdrUsageReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CdrUsageReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return CdrUsageReportsResourceWithStreamingResponse(self)

    def fetch_sync(
        self,
        *,
        aggregation_type: Literal["NO_AGGREGATION", "CONNECTION", "TAG", "BILLING_GROUP"],
        product_breakdown: Literal["NO_BREAKDOWN", "DID_VS_TOLL_FREE", "COUNTRY", "DID_VS_TOLL_FREE_PER_COUNTRY"],
        connections: Iterable[float] | NotGiven = NOT_GIVEN,
        end_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        start_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CdrUsageReportFetchSyncResponse:
        """Generate and fetch voice usage report synchronously.

        This endpoint will both
        generate and fetch the voice report over a specified time period. No polling is
        necessary but the response may take up to a couple of minutes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/reports/cdr_usage_reports/sync",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "aggregation_type": aggregation_type,
                        "product_breakdown": product_breakdown,
                        "connections": connections,
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    cdr_usage_report_fetch_sync_params.CdrUsageReportFetchSyncParams,
                ),
            ),
            cast_to=CdrUsageReportFetchSyncResponse,
        )


class AsyncCdrUsageReportsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCdrUsageReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCdrUsageReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCdrUsageReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncCdrUsageReportsResourceWithStreamingResponse(self)

    async def fetch_sync(
        self,
        *,
        aggregation_type: Literal["NO_AGGREGATION", "CONNECTION", "TAG", "BILLING_GROUP"],
        product_breakdown: Literal["NO_BREAKDOWN", "DID_VS_TOLL_FREE", "COUNTRY", "DID_VS_TOLL_FREE_PER_COUNTRY"],
        connections: Iterable[float] | NotGiven = NOT_GIVEN,
        end_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        start_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CdrUsageReportFetchSyncResponse:
        """Generate and fetch voice usage report synchronously.

        This endpoint will both
        generate and fetch the voice report over a specified time period. No polling is
        necessary but the response may take up to a couple of minutes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/reports/cdr_usage_reports/sync",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "aggregation_type": aggregation_type,
                        "product_breakdown": product_breakdown,
                        "connections": connections,
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    cdr_usage_report_fetch_sync_params.CdrUsageReportFetchSyncParams,
                ),
            ),
            cast_to=CdrUsageReportFetchSyncResponse,
        )


class CdrUsageReportsResourceWithRawResponse:
    def __init__(self, cdr_usage_reports: CdrUsageReportsResource) -> None:
        self._cdr_usage_reports = cdr_usage_reports

        self.fetch_sync = to_raw_response_wrapper(
            cdr_usage_reports.fetch_sync,
        )


class AsyncCdrUsageReportsResourceWithRawResponse:
    def __init__(self, cdr_usage_reports: AsyncCdrUsageReportsResource) -> None:
        self._cdr_usage_reports = cdr_usage_reports

        self.fetch_sync = async_to_raw_response_wrapper(
            cdr_usage_reports.fetch_sync,
        )


class CdrUsageReportsResourceWithStreamingResponse:
    def __init__(self, cdr_usage_reports: CdrUsageReportsResource) -> None:
        self._cdr_usage_reports = cdr_usage_reports

        self.fetch_sync = to_streamed_response_wrapper(
            cdr_usage_reports.fetch_sync,
        )


class AsyncCdrUsageReportsResourceWithStreamingResponse:
    def __init__(self, cdr_usage_reports: AsyncCdrUsageReportsResource) -> None:
        self._cdr_usage_reports = cdr_usage_reports

        self.fetch_sync = async_to_streamed_response_wrapper(
            cdr_usage_reports.fetch_sync,
        )

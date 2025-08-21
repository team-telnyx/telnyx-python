# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import usage_report_list_params, usage_report_get_options_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.usage_report_list_response import UsageReportListResponse
from ..types.usage_report_get_options_response import UsageReportGetOptionsResponse

__all__ = ["UsageReportsResource", "AsyncUsageReportsResource"]


class UsageReportsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsageReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return UsageReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsageReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return UsageReportsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        dimensions: List[str],
        metrics: List[str],
        product: str,
        date_range: str | NotGiven = NOT_GIVEN,
        end_date: str | NotGiven = NOT_GIVEN,
        filter: str | NotGiven = NOT_GIVEN,
        format: Literal["csv", "json"] | NotGiven = NOT_GIVEN,
        managed_accounts: bool | NotGiven = NOT_GIVEN,
        page: usage_report_list_params.Page | NotGiven = NOT_GIVEN,
        sort: List[str] | NotGiven = NOT_GIVEN,
        start_date: str | NotGiven = NOT_GIVEN,
        authorization_bearer: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsageReportListResponse:
        """
        Get Telnyx usage data by product, broken out by the specified dimensions

        Args:
          dimensions: Breakout by specified product dimensions

          metrics: Specified product usage values

          product: Telnyx product

          date_range: A more user-friendly way to specify the timespan you want to filter by. More
              options can be found in the Telnyx API Reference docs.

          end_date: The end date for the time range you are interested in. The maximum time range is
              31 days. Format: YYYY-MM-DDTHH:mm:ssZ

          filter: Filter records on dimensions

          format: Specify the response format (csv or json). JSON is returned by default, even if
              not specified.

          managed_accounts: Return the aggregations for all Managed Accounts under the user making the
              request.

          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          sort: Specifies the sort order for results

          start_date: The start date for the time range you are interested in. The maximum time range
              is 31 days. Format: YYYY-MM-DDTHH:mm:ssZ

          authorization_bearer: Authenticates the request with your Telnyx API V2 KEY

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"authorization_bearer": authorization_bearer}), **(extra_headers or {})}
        return self._get(
            "/usage_reports",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "dimensions": dimensions,
                        "metrics": metrics,
                        "product": product,
                        "date_range": date_range,
                        "end_date": end_date,
                        "filter": filter,
                        "format": format,
                        "managed_accounts": managed_accounts,
                        "page": page,
                        "sort": sort,
                        "start_date": start_date,
                    },
                    usage_report_list_params.UsageReportListParams,
                ),
            ),
            cast_to=UsageReportListResponse,
        )

    def get_options(
        self,
        *,
        product: str | NotGiven = NOT_GIVEN,
        authorization_bearer: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsageReportGetOptionsResponse:
        """
        Get the Usage Reports options for querying usage, including the products
        available and their respective metrics and dimensions

        Args:
          product: Options (dimensions and metrics) for a given product. If none specified, all
              products will be returned.

          authorization_bearer: Authenticates the request with your Telnyx API V2 KEY

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"authorization_bearer": authorization_bearer}), **(extra_headers or {})}
        return self._get(
            "/usage_reports/options",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"product": product}, usage_report_get_options_params.UsageReportGetOptionsParams
                ),
            ),
            cast_to=UsageReportGetOptionsResponse,
        )


class AsyncUsageReportsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsageReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsageReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsageReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncUsageReportsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        dimensions: List[str],
        metrics: List[str],
        product: str,
        date_range: str | NotGiven = NOT_GIVEN,
        end_date: str | NotGiven = NOT_GIVEN,
        filter: str | NotGiven = NOT_GIVEN,
        format: Literal["csv", "json"] | NotGiven = NOT_GIVEN,
        managed_accounts: bool | NotGiven = NOT_GIVEN,
        page: usage_report_list_params.Page | NotGiven = NOT_GIVEN,
        sort: List[str] | NotGiven = NOT_GIVEN,
        start_date: str | NotGiven = NOT_GIVEN,
        authorization_bearer: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsageReportListResponse:
        """
        Get Telnyx usage data by product, broken out by the specified dimensions

        Args:
          dimensions: Breakout by specified product dimensions

          metrics: Specified product usage values

          product: Telnyx product

          date_range: A more user-friendly way to specify the timespan you want to filter by. More
              options can be found in the Telnyx API Reference docs.

          end_date: The end date for the time range you are interested in. The maximum time range is
              31 days. Format: YYYY-MM-DDTHH:mm:ssZ

          filter: Filter records on dimensions

          format: Specify the response format (csv or json). JSON is returned by default, even if
              not specified.

          managed_accounts: Return the aggregations for all Managed Accounts under the user making the
              request.

          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          sort: Specifies the sort order for results

          start_date: The start date for the time range you are interested in. The maximum time range
              is 31 days. Format: YYYY-MM-DDTHH:mm:ssZ

          authorization_bearer: Authenticates the request with your Telnyx API V2 KEY

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"authorization_bearer": authorization_bearer}), **(extra_headers or {})}
        return await self._get(
            "/usage_reports",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "dimensions": dimensions,
                        "metrics": metrics,
                        "product": product,
                        "date_range": date_range,
                        "end_date": end_date,
                        "filter": filter,
                        "format": format,
                        "managed_accounts": managed_accounts,
                        "page": page,
                        "sort": sort,
                        "start_date": start_date,
                    },
                    usage_report_list_params.UsageReportListParams,
                ),
            ),
            cast_to=UsageReportListResponse,
        )

    async def get_options(
        self,
        *,
        product: str | NotGiven = NOT_GIVEN,
        authorization_bearer: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsageReportGetOptionsResponse:
        """
        Get the Usage Reports options for querying usage, including the products
        available and their respective metrics and dimensions

        Args:
          product: Options (dimensions and metrics) for a given product. If none specified, all
              products will be returned.

          authorization_bearer: Authenticates the request with your Telnyx API V2 KEY

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"authorization_bearer": authorization_bearer}), **(extra_headers or {})}
        return await self._get(
            "/usage_reports/options",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"product": product}, usage_report_get_options_params.UsageReportGetOptionsParams
                ),
            ),
            cast_to=UsageReportGetOptionsResponse,
        )


class UsageReportsResourceWithRawResponse:
    def __init__(self, usage_reports: UsageReportsResource) -> None:
        self._usage_reports = usage_reports

        self.list = to_raw_response_wrapper(
            usage_reports.list,
        )
        self.get_options = to_raw_response_wrapper(
            usage_reports.get_options,
        )


class AsyncUsageReportsResourceWithRawResponse:
    def __init__(self, usage_reports: AsyncUsageReportsResource) -> None:
        self._usage_reports = usage_reports

        self.list = async_to_raw_response_wrapper(
            usage_reports.list,
        )
        self.get_options = async_to_raw_response_wrapper(
            usage_reports.get_options,
        )


class UsageReportsResourceWithStreamingResponse:
    def __init__(self, usage_reports: UsageReportsResource) -> None:
        self._usage_reports = usage_reports

        self.list = to_streamed_response_wrapper(
            usage_reports.list,
        )
        self.get_options = to_streamed_response_wrapper(
            usage_reports.get_options,
        )


class AsyncUsageReportsResourceWithStreamingResponse:
    def __init__(self, usage_reports: AsyncUsageReportsResource) -> None:
        self._usage_reports = usage_reports

        self.list = async_to_streamed_response_wrapper(
            usage_reports.list,
        )
        self.get_options = async_to_streamed_response_wrapper(
            usage_reports.get_options,
        )

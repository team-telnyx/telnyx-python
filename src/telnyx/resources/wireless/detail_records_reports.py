# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.wireless import detail_records_report_list_params, detail_records_report_create_params
from ...types.wireless.detail_records_report_list_response import DetailRecordsReportListResponse
from ...types.wireless.detail_records_report_create_response import DetailRecordsReportCreateResponse
from ...types.wireless.detail_records_report_delete_response import DetailRecordsReportDeleteResponse
from ...types.wireless.detail_records_report_retrieve_response import DetailRecordsReportRetrieveResponse

__all__ = ["DetailRecordsReportsResource", "AsyncDetailRecordsReportsResource"]


class DetailRecordsReportsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DetailRecordsReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return DetailRecordsReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DetailRecordsReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return DetailRecordsReportsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        end_time: str | NotGiven = NOT_GIVEN,
        start_time: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetailRecordsReportCreateResponse:
        """
        Asynchronously create a report containing Wireless Detail Records (WDRs) for the
        SIM cards that consumed wireless data in the given time period.

        Args:
          end_time: ISO 8601 formatted date-time indicating the end time.

          start_time: ISO 8601 formatted date-time indicating the start time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/wireless/detail_records_reports",
            body=maybe_transform(
                {
                    "end_time": end_time,
                    "start_time": start_time,
                },
                detail_records_report_create_params.DetailRecordsReportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DetailRecordsReportCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetailRecordsReportRetrieveResponse:
        """
        Returns one specific WDR report

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/wireless/detail_records_reports/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DetailRecordsReportRetrieveResponse,
        )

    def list(
        self,
        *,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetailRecordsReportListResponse:
        """
        Returns the WDR Reports that match the given parameters.

        Args:
          page_number: The page number to load.

          page_size: The size of the page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/wireless/detail_records_reports",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    detail_records_report_list_params.DetailRecordsReportListParams,
                ),
            ),
            cast_to=DetailRecordsReportListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetailRecordsReportDeleteResponse:
        """
        Deletes one specific WDR report.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/wireless/detail_records_reports/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DetailRecordsReportDeleteResponse,
        )


class AsyncDetailRecordsReportsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDetailRecordsReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDetailRecordsReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDetailRecordsReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncDetailRecordsReportsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        end_time: str | NotGiven = NOT_GIVEN,
        start_time: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetailRecordsReportCreateResponse:
        """
        Asynchronously create a report containing Wireless Detail Records (WDRs) for the
        SIM cards that consumed wireless data in the given time period.

        Args:
          end_time: ISO 8601 formatted date-time indicating the end time.

          start_time: ISO 8601 formatted date-time indicating the start time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/wireless/detail_records_reports",
            body=await async_maybe_transform(
                {
                    "end_time": end_time,
                    "start_time": start_time,
                },
                detail_records_report_create_params.DetailRecordsReportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DetailRecordsReportCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetailRecordsReportRetrieveResponse:
        """
        Returns one specific WDR report

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/wireless/detail_records_reports/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DetailRecordsReportRetrieveResponse,
        )

    async def list(
        self,
        *,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetailRecordsReportListResponse:
        """
        Returns the WDR Reports that match the given parameters.

        Args:
          page_number: The page number to load.

          page_size: The size of the page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/wireless/detail_records_reports",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    detail_records_report_list_params.DetailRecordsReportListParams,
                ),
            ),
            cast_to=DetailRecordsReportListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetailRecordsReportDeleteResponse:
        """
        Deletes one specific WDR report.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/wireless/detail_records_reports/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DetailRecordsReportDeleteResponse,
        )


class DetailRecordsReportsResourceWithRawResponse:
    def __init__(self, detail_records_reports: DetailRecordsReportsResource) -> None:
        self._detail_records_reports = detail_records_reports

        self.create = to_raw_response_wrapper(
            detail_records_reports.create,
        )
        self.retrieve = to_raw_response_wrapper(
            detail_records_reports.retrieve,
        )
        self.list = to_raw_response_wrapper(
            detail_records_reports.list,
        )
        self.delete = to_raw_response_wrapper(
            detail_records_reports.delete,
        )


class AsyncDetailRecordsReportsResourceWithRawResponse:
    def __init__(self, detail_records_reports: AsyncDetailRecordsReportsResource) -> None:
        self._detail_records_reports = detail_records_reports

        self.create = async_to_raw_response_wrapper(
            detail_records_reports.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            detail_records_reports.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            detail_records_reports.list,
        )
        self.delete = async_to_raw_response_wrapper(
            detail_records_reports.delete,
        )


class DetailRecordsReportsResourceWithStreamingResponse:
    def __init__(self, detail_records_reports: DetailRecordsReportsResource) -> None:
        self._detail_records_reports = detail_records_reports

        self.create = to_streamed_response_wrapper(
            detail_records_reports.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            detail_records_reports.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            detail_records_reports.list,
        )
        self.delete = to_streamed_response_wrapper(
            detail_records_reports.delete,
        )


class AsyncDetailRecordsReportsResourceWithStreamingResponse:
    def __init__(self, detail_records_reports: AsyncDetailRecordsReportsResource) -> None:
        self._detail_records_reports = detail_records_reports

        self.create = async_to_streamed_response_wrapper(
            detail_records_reports.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            detail_records_reports.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            detail_records_reports.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            detail_records_reports.delete,
        )

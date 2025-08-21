# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
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
from ...types.reports import (
    mdr_usage_report_list_params,
    mdr_usage_report_create_params,
    mdr_usage_report_fetch_sync_params,
)
from ...types.reports.mdr_usage_report_list_response import MdrUsageReportListResponse
from ...types.reports.mdr_usage_report_create_response import MdrUsageReportCreateResponse
from ...types.reports.mdr_usage_report_delete_response import MdrUsageReportDeleteResponse
from ...types.reports.mdr_usage_report_retrieve_response import MdrUsageReportRetrieveResponse
from ...types.reports.mdr_usage_report_fetch_sync_response import MdrUsageReportFetchSyncResponse

__all__ = ["MdrUsageReportsResource", "AsyncMdrUsageReportsResource"]


class MdrUsageReportsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MdrUsageReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return MdrUsageReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MdrUsageReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return MdrUsageReportsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        aggregation_type: Literal["NO_AGGREGATION", "PROFILE", "TAGS"],
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        profiles: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MdrUsageReportCreateResponse:
        """Submit request for new new messaging usage report.

        This endpoint will pull and
        aggregate messaging data in specified time period.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/reports/mdr_usage_reports",
            body=maybe_transform(
                {
                    "aggregation_type": aggregation_type,
                    "end_date": end_date,
                    "start_date": start_date,
                    "profiles": profiles,
                },
                mdr_usage_report_create_params.MdrUsageReportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MdrUsageReportCreateResponse,
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
    ) -> MdrUsageReportRetrieveResponse:
        """
        Fetch a single messaging usage report by id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/reports/mdr_usage_reports/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MdrUsageReportRetrieveResponse,
        )

    def list(
        self,
        *,
        page: mdr_usage_report_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MdrUsageReportListResponse:
        """Fetch all messaging usage reports.

        Usage reports are aggregated messaging data
        for specified time period and breakdown

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/reports/mdr_usage_reports",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"page": page}, mdr_usage_report_list_params.MdrUsageReportListParams),
            ),
            cast_to=MdrUsageReportListResponse,
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
    ) -> MdrUsageReportDeleteResponse:
        """
        Delete messaging usage report by id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/reports/mdr_usage_reports/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MdrUsageReportDeleteResponse,
        )

    def fetch_sync(
        self,
        *,
        aggregation_type: Literal["NO_AGGREGATION", "PROFILE", "TAGS"],
        end_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        profiles: List[str] | NotGiven = NOT_GIVEN,
        start_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MdrUsageReportFetchSyncResponse:
        """Generate and fetch messaging usage report synchronously.

        This endpoint will both
        generate and fetch the messaging report over a specified time period. No polling
        is necessary but the response may take up to a couple of minutes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/reports/mdr_usage_reports/sync",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "aggregation_type": aggregation_type,
                        "end_date": end_date,
                        "profiles": profiles,
                        "start_date": start_date,
                    },
                    mdr_usage_report_fetch_sync_params.MdrUsageReportFetchSyncParams,
                ),
            ),
            cast_to=MdrUsageReportFetchSyncResponse,
        )


class AsyncMdrUsageReportsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMdrUsageReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMdrUsageReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMdrUsageReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncMdrUsageReportsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        aggregation_type: Literal["NO_AGGREGATION", "PROFILE", "TAGS"],
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        profiles: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MdrUsageReportCreateResponse:
        """Submit request for new new messaging usage report.

        This endpoint will pull and
        aggregate messaging data in specified time period.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/reports/mdr_usage_reports",
            body=await async_maybe_transform(
                {
                    "aggregation_type": aggregation_type,
                    "end_date": end_date,
                    "start_date": start_date,
                    "profiles": profiles,
                },
                mdr_usage_report_create_params.MdrUsageReportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MdrUsageReportCreateResponse,
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
    ) -> MdrUsageReportRetrieveResponse:
        """
        Fetch a single messaging usage report by id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/reports/mdr_usage_reports/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MdrUsageReportRetrieveResponse,
        )

    async def list(
        self,
        *,
        page: mdr_usage_report_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MdrUsageReportListResponse:
        """Fetch all messaging usage reports.

        Usage reports are aggregated messaging data
        for specified time period and breakdown

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/reports/mdr_usage_reports",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"page": page}, mdr_usage_report_list_params.MdrUsageReportListParams
                ),
            ),
            cast_to=MdrUsageReportListResponse,
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
    ) -> MdrUsageReportDeleteResponse:
        """
        Delete messaging usage report by id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/reports/mdr_usage_reports/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MdrUsageReportDeleteResponse,
        )

    async def fetch_sync(
        self,
        *,
        aggregation_type: Literal["NO_AGGREGATION", "PROFILE", "TAGS"],
        end_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        profiles: List[str] | NotGiven = NOT_GIVEN,
        start_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MdrUsageReportFetchSyncResponse:
        """Generate and fetch messaging usage report synchronously.

        This endpoint will both
        generate and fetch the messaging report over a specified time period. No polling
        is necessary but the response may take up to a couple of minutes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/reports/mdr_usage_reports/sync",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "aggregation_type": aggregation_type,
                        "end_date": end_date,
                        "profiles": profiles,
                        "start_date": start_date,
                    },
                    mdr_usage_report_fetch_sync_params.MdrUsageReportFetchSyncParams,
                ),
            ),
            cast_to=MdrUsageReportFetchSyncResponse,
        )


class MdrUsageReportsResourceWithRawResponse:
    def __init__(self, mdr_usage_reports: MdrUsageReportsResource) -> None:
        self._mdr_usage_reports = mdr_usage_reports

        self.create = to_raw_response_wrapper(
            mdr_usage_reports.create,
        )
        self.retrieve = to_raw_response_wrapper(
            mdr_usage_reports.retrieve,
        )
        self.list = to_raw_response_wrapper(
            mdr_usage_reports.list,
        )
        self.delete = to_raw_response_wrapper(
            mdr_usage_reports.delete,
        )
        self.fetch_sync = to_raw_response_wrapper(
            mdr_usage_reports.fetch_sync,
        )


class AsyncMdrUsageReportsResourceWithRawResponse:
    def __init__(self, mdr_usage_reports: AsyncMdrUsageReportsResource) -> None:
        self._mdr_usage_reports = mdr_usage_reports

        self.create = async_to_raw_response_wrapper(
            mdr_usage_reports.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            mdr_usage_reports.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            mdr_usage_reports.list,
        )
        self.delete = async_to_raw_response_wrapper(
            mdr_usage_reports.delete,
        )
        self.fetch_sync = async_to_raw_response_wrapper(
            mdr_usage_reports.fetch_sync,
        )


class MdrUsageReportsResourceWithStreamingResponse:
    def __init__(self, mdr_usage_reports: MdrUsageReportsResource) -> None:
        self._mdr_usage_reports = mdr_usage_reports

        self.create = to_streamed_response_wrapper(
            mdr_usage_reports.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            mdr_usage_reports.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            mdr_usage_reports.list,
        )
        self.delete = to_streamed_response_wrapper(
            mdr_usage_reports.delete,
        )
        self.fetch_sync = to_streamed_response_wrapper(
            mdr_usage_reports.fetch_sync,
        )


class AsyncMdrUsageReportsResourceWithStreamingResponse:
    def __init__(self, mdr_usage_reports: AsyncMdrUsageReportsResource) -> None:
        self._mdr_usage_reports = mdr_usage_reports

        self.create = async_to_streamed_response_wrapper(
            mdr_usage_reports.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            mdr_usage_reports.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            mdr_usage_reports.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            mdr_usage_reports.delete,
        )
        self.fetch_sync = async_to_streamed_response_wrapper(
            mdr_usage_reports.fetch_sync,
        )

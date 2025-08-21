# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import sub_number_orders_report_create_params
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
from ..types.sub_number_orders_report_create_response import SubNumberOrdersReportCreateResponse
from ..types.sub_number_orders_report_retrieve_response import SubNumberOrdersReportRetrieveResponse

__all__ = ["SubNumberOrdersReportResource", "AsyncSubNumberOrdersReportResource"]


class SubNumberOrdersReportResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubNumberOrdersReportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return SubNumberOrdersReportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubNumberOrdersReportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return SubNumberOrdersReportResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        country_code: str | NotGiven = NOT_GIVEN,
        created_at_gt: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_at_lt: Union[str, datetime] | NotGiven = NOT_GIVEN,
        customer_reference: str | NotGiven = NOT_GIVEN,
        order_request_id: str | NotGiven = NOT_GIVEN,
        status: Literal["pending", "success", "failure"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubNumberOrdersReportCreateResponse:
        """Create a CSV report for sub number orders.

        The report will be generated
        asynchronously and can be downloaded once complete.

        Args:
          country_code: Filter by country code

          created_at_gt: Filter for orders created after this date

          created_at_lt: Filter for orders created before this date

          customer_reference: Filter by customer reference

          order_request_id: Filter by specific order request ID

          status: Filter by order status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/sub_number_orders_report",
            body=maybe_transform(
                {
                    "country_code": country_code,
                    "created_at_gt": created_at_gt,
                    "created_at_lt": created_at_lt,
                    "customer_reference": customer_reference,
                    "order_request_id": order_request_id,
                    "status": status,
                },
                sub_number_orders_report_create_params.SubNumberOrdersReportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubNumberOrdersReportCreateResponse,
        )

    def retrieve(
        self,
        report_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubNumberOrdersReportRetrieveResponse:
        """
        Get the status and details of a sub number orders report.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not report_id:
            raise ValueError(f"Expected a non-empty value for `report_id` but received {report_id!r}")
        return self._get(
            f"/sub_number_orders_report/{report_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubNumberOrdersReportRetrieveResponse,
        )

    def download(
        self,
        report_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """Download the CSV file for a completed sub number orders report.

        The report
        status must be 'success' before the file can be downloaded.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not report_id:
            raise ValueError(f"Expected a non-empty value for `report_id` but received {report_id!r}")
        extra_headers = {"Accept": "text/csv", **(extra_headers or {})}
        return self._get(
            f"/sub_number_orders_report/{report_id}/download",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncSubNumberOrdersReportResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubNumberOrdersReportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubNumberOrdersReportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubNumberOrdersReportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncSubNumberOrdersReportResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        country_code: str | NotGiven = NOT_GIVEN,
        created_at_gt: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_at_lt: Union[str, datetime] | NotGiven = NOT_GIVEN,
        customer_reference: str | NotGiven = NOT_GIVEN,
        order_request_id: str | NotGiven = NOT_GIVEN,
        status: Literal["pending", "success", "failure"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubNumberOrdersReportCreateResponse:
        """Create a CSV report for sub number orders.

        The report will be generated
        asynchronously and can be downloaded once complete.

        Args:
          country_code: Filter by country code

          created_at_gt: Filter for orders created after this date

          created_at_lt: Filter for orders created before this date

          customer_reference: Filter by customer reference

          order_request_id: Filter by specific order request ID

          status: Filter by order status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sub_number_orders_report",
            body=await async_maybe_transform(
                {
                    "country_code": country_code,
                    "created_at_gt": created_at_gt,
                    "created_at_lt": created_at_lt,
                    "customer_reference": customer_reference,
                    "order_request_id": order_request_id,
                    "status": status,
                },
                sub_number_orders_report_create_params.SubNumberOrdersReportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubNumberOrdersReportCreateResponse,
        )

    async def retrieve(
        self,
        report_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubNumberOrdersReportRetrieveResponse:
        """
        Get the status and details of a sub number orders report.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not report_id:
            raise ValueError(f"Expected a non-empty value for `report_id` but received {report_id!r}")
        return await self._get(
            f"/sub_number_orders_report/{report_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubNumberOrdersReportRetrieveResponse,
        )

    async def download(
        self,
        report_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """Download the CSV file for a completed sub number orders report.

        The report
        status must be 'success' before the file can be downloaded.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not report_id:
            raise ValueError(f"Expected a non-empty value for `report_id` but received {report_id!r}")
        extra_headers = {"Accept": "text/csv", **(extra_headers or {})}
        return await self._get(
            f"/sub_number_orders_report/{report_id}/download",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class SubNumberOrdersReportResourceWithRawResponse:
    def __init__(self, sub_number_orders_report: SubNumberOrdersReportResource) -> None:
        self._sub_number_orders_report = sub_number_orders_report

        self.create = to_raw_response_wrapper(
            sub_number_orders_report.create,
        )
        self.retrieve = to_raw_response_wrapper(
            sub_number_orders_report.retrieve,
        )
        self.download = to_raw_response_wrapper(
            sub_number_orders_report.download,
        )


class AsyncSubNumberOrdersReportResourceWithRawResponse:
    def __init__(self, sub_number_orders_report: AsyncSubNumberOrdersReportResource) -> None:
        self._sub_number_orders_report = sub_number_orders_report

        self.create = async_to_raw_response_wrapper(
            sub_number_orders_report.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            sub_number_orders_report.retrieve,
        )
        self.download = async_to_raw_response_wrapper(
            sub_number_orders_report.download,
        )


class SubNumberOrdersReportResourceWithStreamingResponse:
    def __init__(self, sub_number_orders_report: SubNumberOrdersReportResource) -> None:
        self._sub_number_orders_report = sub_number_orders_report

        self.create = to_streamed_response_wrapper(
            sub_number_orders_report.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            sub_number_orders_report.retrieve,
        )
        self.download = to_streamed_response_wrapper(
            sub_number_orders_report.download,
        )


class AsyncSubNumberOrdersReportResourceWithStreamingResponse:
    def __init__(self, sub_number_orders_report: AsyncSubNumberOrdersReportResource) -> None:
        self._sub_number_orders_report = sub_number_orders_report

        self.create = async_to_streamed_response_wrapper(
            sub_number_orders_report.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            sub_number_orders_report.retrieve,
        )
        self.download = async_to_streamed_response_wrapper(
            sub_number_orders_report.download,
        )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import ledger_billing_group_report_create_params
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
from ..types.ledger_billing_group_report_create_response import LedgerBillingGroupReportCreateResponse
from ..types.ledger_billing_group_report_retrieve_response import LedgerBillingGroupReportRetrieveResponse

__all__ = ["LedgerBillingGroupReportsResource", "AsyncLedgerBillingGroupReportsResource"]


class LedgerBillingGroupReportsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LedgerBillingGroupReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return LedgerBillingGroupReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LedgerBillingGroupReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return LedgerBillingGroupReportsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        month: int | NotGiven = NOT_GIVEN,
        year: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LedgerBillingGroupReportCreateResponse:
        """
        Create a ledger billing group report

        Args:
          month: Month of the ledger billing group report

          year: Year of the ledger billing group report

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ledger_billing_group_reports",
            body=maybe_transform(
                {
                    "month": month,
                    "year": year,
                },
                ledger_billing_group_report_create_params.LedgerBillingGroupReportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LedgerBillingGroupReportCreateResponse,
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
    ) -> LedgerBillingGroupReportRetrieveResponse:
        """
        Get a ledger billing group report

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/ledger_billing_group_reports/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LedgerBillingGroupReportRetrieveResponse,
        )


class AsyncLedgerBillingGroupReportsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLedgerBillingGroupReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLedgerBillingGroupReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLedgerBillingGroupReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncLedgerBillingGroupReportsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        month: int | NotGiven = NOT_GIVEN,
        year: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LedgerBillingGroupReportCreateResponse:
        """
        Create a ledger billing group report

        Args:
          month: Month of the ledger billing group report

          year: Year of the ledger billing group report

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ledger_billing_group_reports",
            body=await async_maybe_transform(
                {
                    "month": month,
                    "year": year,
                },
                ledger_billing_group_report_create_params.LedgerBillingGroupReportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LedgerBillingGroupReportCreateResponse,
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
    ) -> LedgerBillingGroupReportRetrieveResponse:
        """
        Get a ledger billing group report

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/ledger_billing_group_reports/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LedgerBillingGroupReportRetrieveResponse,
        )


class LedgerBillingGroupReportsResourceWithRawResponse:
    def __init__(self, ledger_billing_group_reports: LedgerBillingGroupReportsResource) -> None:
        self._ledger_billing_group_reports = ledger_billing_group_reports

        self.create = to_raw_response_wrapper(
            ledger_billing_group_reports.create,
        )
        self.retrieve = to_raw_response_wrapper(
            ledger_billing_group_reports.retrieve,
        )


class AsyncLedgerBillingGroupReportsResourceWithRawResponse:
    def __init__(self, ledger_billing_group_reports: AsyncLedgerBillingGroupReportsResource) -> None:
        self._ledger_billing_group_reports = ledger_billing_group_reports

        self.create = async_to_raw_response_wrapper(
            ledger_billing_group_reports.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            ledger_billing_group_reports.retrieve,
        )


class LedgerBillingGroupReportsResourceWithStreamingResponse:
    def __init__(self, ledger_billing_group_reports: LedgerBillingGroupReportsResource) -> None:
        self._ledger_billing_group_reports = ledger_billing_group_reports

        self.create = to_streamed_response_wrapper(
            ledger_billing_group_reports.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            ledger_billing_group_reports.retrieve,
        )


class AsyncLedgerBillingGroupReportsResourceWithStreamingResponse:
    def __init__(self, ledger_billing_group_reports: AsyncLedgerBillingGroupReportsResource) -> None:
        self._ledger_billing_group_reports = ledger_billing_group_reports

        self.create = async_to_streamed_response_wrapper(
            ledger_billing_group_reports.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            ledger_billing_group_reports.retrieve,
        )

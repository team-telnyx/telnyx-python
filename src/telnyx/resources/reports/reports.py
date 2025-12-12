# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import report_list_mdrs_params, report_list_wdrs_params
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from ..._base_client import AsyncPaginator, make_request_options
from .cdr_usage_reports import (
    CdrUsageReportsResource,
    AsyncCdrUsageReportsResource,
    CdrUsageReportsResourceWithRawResponse,
    AsyncCdrUsageReportsResourceWithRawResponse,
    CdrUsageReportsResourceWithStreamingResponse,
    AsyncCdrUsageReportsResourceWithStreamingResponse,
)
from .mdr_usage_reports import (
    MdrUsageReportsResource,
    AsyncMdrUsageReportsResource,
    MdrUsageReportsResourceWithRawResponse,
    AsyncMdrUsageReportsResourceWithRawResponse,
    MdrUsageReportsResourceWithStreamingResponse,
    AsyncMdrUsageReportsResourceWithStreamingResponse,
)
from ...types.report_list_mdrs_response import ReportListMdrsResponse
from ...types.report_list_wdrs_response import ReportListWdrsResponse

__all__ = ["ReportsResource", "AsyncReportsResource"]


class ReportsResource(SyncAPIResource):
    @cached_property
    def cdr_usage_reports(self) -> CdrUsageReportsResource:
        return CdrUsageReportsResource(self._client)

    @cached_property
    def mdr_usage_reports(self) -> MdrUsageReportsResource:
        return MdrUsageReportsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ReportsResourceWithStreamingResponse(self)

    def list_mdrs(
        self,
        *,
        id: str | Omit = omit,
        cld: str | Omit = omit,
        cli: str | Omit = omit,
        direction: Literal["INBOUND", "OUTBOUND"] | Omit = omit,
        end_date: str | Omit = omit,
        message_type: Literal["SMS", "MMS"] | Omit = omit,
        profile: str | Omit = omit,
        start_date: str | Omit = omit,
        status: Literal["GW_TIMEOUT", "DELIVERED", "DLR_UNCONFIRMED", "DLR_TIMEOUT", "RECEIVED", "GW_REJECT", "FAILED"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportListMdrsResponse:
        """
        Fetch all Mdr records

        Args:
          id: Message uuid

          cld: Destination number

          cli: Origination number

          direction: Direction (inbound or outbound)

          end_date: Pagination end date

          message_type: Type of message

          profile: Name of the profile

          start_date: Pagination start date

          status: Message status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/reports/mdrs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "cld": cld,
                        "cli": cli,
                        "direction": direction,
                        "end_date": end_date,
                        "message_type": message_type,
                        "profile": profile,
                        "start_date": start_date,
                        "status": status,
                    },
                    report_list_mdrs_params.ReportListMdrsParams,
                ),
            ),
            cast_to=ReportListMdrsResponse,
        )

    def list_wdrs(
        self,
        *,
        id: str | Omit = omit,
        end_date: str | Omit = omit,
        imsi: str | Omit = omit,
        mcc: str | Omit = omit,
        mnc: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        phone_number: str | Omit = omit,
        sim_card_id: str | Omit = omit,
        sim_group_id: str | Omit = omit,
        sim_group_name: str | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[ReportListWdrsResponse]:
        """
        Fetch all Wdr records

        Args:
          id: WDR uuid

          end_date: End date

          imsi: International mobile subscriber identity

          mcc: Mobile country code

          mnc: Mobile network code

          phone_number: Phone number

          sim_card_id: Sim card unique identifier

          sim_group_id: Sim group unique identifier

          sim_group_name: Sim group name

          sort: Field used to order the data. If no field is specified, default value is
              'created_at'

          start_date: Start date

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/reports/wdrs",
            page=SyncDefaultFlatPagination[ReportListWdrsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "end_date": end_date,
                        "imsi": imsi,
                        "mcc": mcc,
                        "mnc": mnc,
                        "page_number": page_number,
                        "page_size": page_size,
                        "phone_number": phone_number,
                        "sim_card_id": sim_card_id,
                        "sim_group_id": sim_group_id,
                        "sim_group_name": sim_group_name,
                        "sort": sort,
                        "start_date": start_date,
                    },
                    report_list_wdrs_params.ReportListWdrsParams,
                ),
            ),
            model=ReportListWdrsResponse,
        )


class AsyncReportsResource(AsyncAPIResource):
    @cached_property
    def cdr_usage_reports(self) -> AsyncCdrUsageReportsResource:
        return AsyncCdrUsageReportsResource(self._client)

    @cached_property
    def mdr_usage_reports(self) -> AsyncMdrUsageReportsResource:
        return AsyncMdrUsageReportsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncReportsResourceWithStreamingResponse(self)

    async def list_mdrs(
        self,
        *,
        id: str | Omit = omit,
        cld: str | Omit = omit,
        cli: str | Omit = omit,
        direction: Literal["INBOUND", "OUTBOUND"] | Omit = omit,
        end_date: str | Omit = omit,
        message_type: Literal["SMS", "MMS"] | Omit = omit,
        profile: str | Omit = omit,
        start_date: str | Omit = omit,
        status: Literal["GW_TIMEOUT", "DELIVERED", "DLR_UNCONFIRMED", "DLR_TIMEOUT", "RECEIVED", "GW_REJECT", "FAILED"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReportListMdrsResponse:
        """
        Fetch all Mdr records

        Args:
          id: Message uuid

          cld: Destination number

          cli: Origination number

          direction: Direction (inbound or outbound)

          end_date: Pagination end date

          message_type: Type of message

          profile: Name of the profile

          start_date: Pagination start date

          status: Message status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/reports/mdrs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "id": id,
                        "cld": cld,
                        "cli": cli,
                        "direction": direction,
                        "end_date": end_date,
                        "message_type": message_type,
                        "profile": profile,
                        "start_date": start_date,
                        "status": status,
                    },
                    report_list_mdrs_params.ReportListMdrsParams,
                ),
            ),
            cast_to=ReportListMdrsResponse,
        )

    def list_wdrs(
        self,
        *,
        id: str | Omit = omit,
        end_date: str | Omit = omit,
        imsi: str | Omit = omit,
        mcc: str | Omit = omit,
        mnc: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        phone_number: str | Omit = omit,
        sim_card_id: str | Omit = omit,
        sim_group_id: str | Omit = omit,
        sim_group_name: str | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ReportListWdrsResponse, AsyncDefaultFlatPagination[ReportListWdrsResponse]]:
        """
        Fetch all Wdr records

        Args:
          id: WDR uuid

          end_date: End date

          imsi: International mobile subscriber identity

          mcc: Mobile country code

          mnc: Mobile network code

          phone_number: Phone number

          sim_card_id: Sim card unique identifier

          sim_group_id: Sim group unique identifier

          sim_group_name: Sim group name

          sort: Field used to order the data. If no field is specified, default value is
              'created_at'

          start_date: Start date

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/reports/wdrs",
            page=AsyncDefaultFlatPagination[ReportListWdrsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "end_date": end_date,
                        "imsi": imsi,
                        "mcc": mcc,
                        "mnc": mnc,
                        "page_number": page_number,
                        "page_size": page_size,
                        "phone_number": phone_number,
                        "sim_card_id": sim_card_id,
                        "sim_group_id": sim_group_id,
                        "sim_group_name": sim_group_name,
                        "sort": sort,
                        "start_date": start_date,
                    },
                    report_list_wdrs_params.ReportListWdrsParams,
                ),
            ),
            model=ReportListWdrsResponse,
        )


class ReportsResourceWithRawResponse:
    def __init__(self, reports: ReportsResource) -> None:
        self._reports = reports

        self.list_mdrs = to_raw_response_wrapper(
            reports.list_mdrs,
        )
        self.list_wdrs = to_raw_response_wrapper(
            reports.list_wdrs,
        )

    @cached_property
    def cdr_usage_reports(self) -> CdrUsageReportsResourceWithRawResponse:
        return CdrUsageReportsResourceWithRawResponse(self._reports.cdr_usage_reports)

    @cached_property
    def mdr_usage_reports(self) -> MdrUsageReportsResourceWithRawResponse:
        return MdrUsageReportsResourceWithRawResponse(self._reports.mdr_usage_reports)


class AsyncReportsResourceWithRawResponse:
    def __init__(self, reports: AsyncReportsResource) -> None:
        self._reports = reports

        self.list_mdrs = async_to_raw_response_wrapper(
            reports.list_mdrs,
        )
        self.list_wdrs = async_to_raw_response_wrapper(
            reports.list_wdrs,
        )

    @cached_property
    def cdr_usage_reports(self) -> AsyncCdrUsageReportsResourceWithRawResponse:
        return AsyncCdrUsageReportsResourceWithRawResponse(self._reports.cdr_usage_reports)

    @cached_property
    def mdr_usage_reports(self) -> AsyncMdrUsageReportsResourceWithRawResponse:
        return AsyncMdrUsageReportsResourceWithRawResponse(self._reports.mdr_usage_reports)


class ReportsResourceWithStreamingResponse:
    def __init__(self, reports: ReportsResource) -> None:
        self._reports = reports

        self.list_mdrs = to_streamed_response_wrapper(
            reports.list_mdrs,
        )
        self.list_wdrs = to_streamed_response_wrapper(
            reports.list_wdrs,
        )

    @cached_property
    def cdr_usage_reports(self) -> CdrUsageReportsResourceWithStreamingResponse:
        return CdrUsageReportsResourceWithStreamingResponse(self._reports.cdr_usage_reports)

    @cached_property
    def mdr_usage_reports(self) -> MdrUsageReportsResourceWithStreamingResponse:
        return MdrUsageReportsResourceWithStreamingResponse(self._reports.mdr_usage_reports)


class AsyncReportsResourceWithStreamingResponse:
    def __init__(self, reports: AsyncReportsResource) -> None:
        self._reports = reports

        self.list_mdrs = async_to_streamed_response_wrapper(
            reports.list_mdrs,
        )
        self.list_wdrs = async_to_streamed_response_wrapper(
            reports.list_wdrs,
        )

    @cached_property
    def cdr_usage_reports(self) -> AsyncCdrUsageReportsResourceWithStreamingResponse:
        return AsyncCdrUsageReportsResourceWithStreamingResponse(self._reports.cdr_usage_reports)

    @cached_property
    def mdr_usage_reports(self) -> AsyncMdrUsageReportsResourceWithStreamingResponse:
        return AsyncMdrUsageReportsResourceWithStreamingResponse(self._reports.mdr_usage_reports)

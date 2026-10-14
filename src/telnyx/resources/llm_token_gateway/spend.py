# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import date

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...types.llm_token_gateway import spend_retrieve_events_params, spend_retrieve_summary_params
from ...types.llm_token_gateway.spend_group_by_param import SpendGroupByParam
from ...types.llm_token_gateway.spend_retrieve_events_response import SpendRetrieveEventsResponse
from ...types.llm_token_gateway.spend_retrieve_summary_response import SpendRetrieveSummaryResponse

__all__ = ["SpendResource", "AsyncSpendResource"]


class SpendResource(SyncAPIResource):
    """Manage and report AI Gateway usage."""

    @cached_property
    def with_raw_response(self) -> SpendResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return SpendResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SpendResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return SpendResourceWithStreamingResponse(self)

    def retrieve_events(
        self,
        *,
        end_date: Union[str, date] | Omit = omit,
        end_user_id: str | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        page_snapshot: str | Omit = omit,
        start_date: Union[str, date] | Omit = omit,
        token_group_id: str | Omit = omit,
        token_key_id: str | Omit = omit,
        token_user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpendRetrieveEventsResponse:
        """Return request-level usage history for the authenticated account.

        Supply both
        UTC dates or neither; omitting both returns the previous full UTC day. Dates use
        a half-open range [start_date, end_date) of at most 31 days. Cost reflects
        budget reference rates, not invoice charges. Unknown spend is excluded and
        reported separately. The report snapshot supports at most 10,000 matching
        requests, independently of page size. Exceeding this bound returns HTTP 503
        without partial results. Narrow the date range or resource filters before
        retrying. A failed report must not be interpreted as zero usage. Request tags
        can filter either report and metadata:<key> can group the summary.

        Args:
          metadata: Request tag filters as metadata[<key>]=<value>, at most 5, combined with AND. A
              value matches the tag's text form exactly (booleans as true/false, integers in
              decimal), so metadata[flag]=true matches both boolean true and the string
              "true". Keys are case-sensitive; reserved-prefix keys are rejected. Unindexed:
              bounded by the account, the date range and the report timeout.

          page_snapshot: Required after page 1; account/filter-bound 15-minute stable snapshot;
              expired/mismatch 409.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/llm_token_gateway/spend/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "end_user_id": end_user_id,
                        "metadata": metadata,
                        "page_number": page_number,
                        "page_size": page_size,
                        "page_snapshot": page_snapshot,
                        "start_date": start_date,
                        "token_group_id": token_group_id,
                        "token_key_id": token_key_id,
                        "token_user_id": token_user_id,
                    },
                    spend_retrieve_events_params.SpendRetrieveEventsParams,
                ),
            ),
            cast_to=SpendRetrieveEventsResponse,
        )

    def retrieve_summary(
        self,
        *,
        end_date: Union[str, date],
        group_by: SpendGroupByParam,
        start_date: Union[str, date],
        end_user_id: str | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        page_snapshot: str | Omit = omit,
        token_group_id: str | Omit = omit,
        token_key_id: str | Omit = omit,
        token_user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpendRetrieveSummaryResponse:
        """
        Return request counts, token counts and reference spend grouped by one
        attribution dimension. Both UTC dates and group_by are required. Dates use a
        half-open range [start_date, end_date) of at most 31 days. Cost reflects budget
        reference rates, not invoice charges. Unknown spend is excluded and reported
        separately. The report snapshot supports at most 10,000 matching requests,
        independently of page size. Exceeding this bound returns HTTP 503 without
        partial results. Narrow the date range or resource filters before retrying. A
        failed report must not be interpreted as zero usage. Request tags can filter
        either report and metadata:<key> can group the summary.

        Args:
          group_by: A scope, or metadata:<key> to group by one request tag's text-form value;
              requests without the key form one group with a null dimension_id.

          metadata: Request tag filters as metadata[<key>]=<value>, at most 5, combined with AND. A
              value matches the tag's text form exactly (booleans as true/false, integers in
              decimal), so metadata[flag]=true matches both boolean true and the string
              "true". Keys are case-sensitive; reserved-prefix keys are rejected. Unindexed:
              bounded by the account, the date range and the report timeout.

          page_snapshot: Required after page 1; account/filter-bound 15-minute stable snapshot;
              expired/mismatch 409.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/llm_token_gateway/spend/summary",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "group_by": group_by,
                        "start_date": start_date,
                        "end_user_id": end_user_id,
                        "metadata": metadata,
                        "page_number": page_number,
                        "page_size": page_size,
                        "page_snapshot": page_snapshot,
                        "token_group_id": token_group_id,
                        "token_key_id": token_key_id,
                        "token_user_id": token_user_id,
                    },
                    spend_retrieve_summary_params.SpendRetrieveSummaryParams,
                ),
            ),
            cast_to=SpendRetrieveSummaryResponse,
        )


class AsyncSpendResource(AsyncAPIResource):
    """Manage and report AI Gateway usage."""

    @cached_property
    def with_raw_response(self) -> AsyncSpendResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSpendResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSpendResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncSpendResourceWithStreamingResponse(self)

    async def retrieve_events(
        self,
        *,
        end_date: Union[str, date] | Omit = omit,
        end_user_id: str | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        page_snapshot: str | Omit = omit,
        start_date: Union[str, date] | Omit = omit,
        token_group_id: str | Omit = omit,
        token_key_id: str | Omit = omit,
        token_user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpendRetrieveEventsResponse:
        """Return request-level usage history for the authenticated account.

        Supply both
        UTC dates or neither; omitting both returns the previous full UTC day. Dates use
        a half-open range [start_date, end_date) of at most 31 days. Cost reflects
        budget reference rates, not invoice charges. Unknown spend is excluded and
        reported separately. The report snapshot supports at most 10,000 matching
        requests, independently of page size. Exceeding this bound returns HTTP 503
        without partial results. Narrow the date range or resource filters before
        retrying. A failed report must not be interpreted as zero usage. Request tags
        can filter either report and metadata:<key> can group the summary.

        Args:
          metadata: Request tag filters as metadata[<key>]=<value>, at most 5, combined with AND. A
              value matches the tag's text form exactly (booleans as true/false, integers in
              decimal), so metadata[flag]=true matches both boolean true and the string
              "true". Keys are case-sensitive; reserved-prefix keys are rejected. Unindexed:
              bounded by the account, the date range and the report timeout.

          page_snapshot: Required after page 1; account/filter-bound 15-minute stable snapshot;
              expired/mismatch 409.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/llm_token_gateway/spend/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "end_user_id": end_user_id,
                        "metadata": metadata,
                        "page_number": page_number,
                        "page_size": page_size,
                        "page_snapshot": page_snapshot,
                        "start_date": start_date,
                        "token_group_id": token_group_id,
                        "token_key_id": token_key_id,
                        "token_user_id": token_user_id,
                    },
                    spend_retrieve_events_params.SpendRetrieveEventsParams,
                ),
            ),
            cast_to=SpendRetrieveEventsResponse,
        )

    async def retrieve_summary(
        self,
        *,
        end_date: Union[str, date],
        group_by: SpendGroupByParam,
        start_date: Union[str, date],
        end_user_id: str | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        page_snapshot: str | Omit = omit,
        token_group_id: str | Omit = omit,
        token_key_id: str | Omit = omit,
        token_user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpendRetrieveSummaryResponse:
        """
        Return request counts, token counts and reference spend grouped by one
        attribution dimension. Both UTC dates and group_by are required. Dates use a
        half-open range [start_date, end_date) of at most 31 days. Cost reflects budget
        reference rates, not invoice charges. Unknown spend is excluded and reported
        separately. The report snapshot supports at most 10,000 matching requests,
        independently of page size. Exceeding this bound returns HTTP 503 without
        partial results. Narrow the date range or resource filters before retrying. A
        failed report must not be interpreted as zero usage. Request tags can filter
        either report and metadata:<key> can group the summary.

        Args:
          group_by: A scope, or metadata:<key> to group by one request tag's text-form value;
              requests without the key form one group with a null dimension_id.

          metadata: Request tag filters as metadata[<key>]=<value>, at most 5, combined with AND. A
              value matches the tag's text form exactly (booleans as true/false, integers in
              decimal), so metadata[flag]=true matches both boolean true and the string
              "true". Keys are case-sensitive; reserved-prefix keys are rejected. Unindexed:
              bounded by the account, the date range and the report timeout.

          page_snapshot: Required after page 1; account/filter-bound 15-minute stable snapshot;
              expired/mismatch 409.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/llm_token_gateway/spend/summary",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "group_by": group_by,
                        "start_date": start_date,
                        "end_user_id": end_user_id,
                        "metadata": metadata,
                        "page_number": page_number,
                        "page_size": page_size,
                        "page_snapshot": page_snapshot,
                        "token_group_id": token_group_id,
                        "token_key_id": token_key_id,
                        "token_user_id": token_user_id,
                    },
                    spend_retrieve_summary_params.SpendRetrieveSummaryParams,
                ),
            ),
            cast_to=SpendRetrieveSummaryResponse,
        )


class SpendResourceWithRawResponse:
    def __init__(self, spend: SpendResource) -> None:
        self._spend = spend

        self.retrieve_events = to_raw_response_wrapper(
            spend.retrieve_events,
        )
        self.retrieve_summary = to_raw_response_wrapper(
            spend.retrieve_summary,
        )


class AsyncSpendResourceWithRawResponse:
    def __init__(self, spend: AsyncSpendResource) -> None:
        self._spend = spend

        self.retrieve_events = async_to_raw_response_wrapper(
            spend.retrieve_events,
        )
        self.retrieve_summary = async_to_raw_response_wrapper(
            spend.retrieve_summary,
        )


class SpendResourceWithStreamingResponse:
    def __init__(self, spend: SpendResource) -> None:
        self._spend = spend

        self.retrieve_events = to_streamed_response_wrapper(
            spend.retrieve_events,
        )
        self.retrieve_summary = to_streamed_response_wrapper(
            spend.retrieve_summary,
        )


class AsyncSpendResourceWithStreamingResponse:
    def __init__(self, spend: AsyncSpendResource) -> None:
        self._spend = spend

        self.retrieve_events = async_to_streamed_response_wrapper(
            spend.retrieve_events,
        )
        self.retrieve_summary = async_to_streamed_response_wrapper(
            spend.retrieve_summary,
        )

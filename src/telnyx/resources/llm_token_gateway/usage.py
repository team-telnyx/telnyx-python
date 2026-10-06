# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
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
from ...types.llm_token_gateway import usage_retrieve_summary_params
from ...types.llm_token_gateway.usage_retrieve_summary_response import UsageRetrieveSummaryResponse

__all__ = ["UsageResource", "AsyncUsageResource"]


class UsageResource(SyncAPIResource):
    """Manage and report AI Gateway traffic."""

    @cached_property
    def with_raw_response(self) -> UsageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return UsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return UsageResourceWithStreamingResponse(self)

    def retrieve_summary(
        self,
        *,
        end_date: Union[str, date],
        start_date: Union[str, date],
        token_group_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageRetrieveSummaryResponse:
        """
        Return complete usage totals, UTC daily and model breakdowns, and guardrail
        event counts for one token group owned by the authenticated account. Requires
        the llm_token_gateway.usage.read permission; spend and guardrail read
        permissions do not grant this combined report. All sections share one database
        snapshot and include the latest usage corrections. Dates use an inclusive start
        and exclusive end spanning 1 to 31 days. Only token_group_id, start_date and
        end_date are accepted; pagination, group_by and other filters are rejected.
        Spend is reference/enforcement USD, not invoice truth or BYOK provider charges.
        Unknown cost is excluded from spend and reported through unknown_requests and
        reserved_spend. Daily rows include zero-activity days. Model rows are ordered by
        request count descending, then model name, and are limited to 1,000. Guardrail
        counts count events, not distinct requests; recent_events contains at most 20
        newest events. A report that exceeds model or query limits returns 503 rather
        than a truncated success.

        Args:
          end_date: Exclusive UTC date in YYYY-MM-DD format. Must follow start_date by 1 to 31 days.

          start_date: Inclusive UTC date in YYYY-MM-DD format. Must precede end_date by 1 to 31 days.

          token_group_id: ID of a token group owned by the authenticated account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/llm_token_gateway/usage/summary",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                        "token_group_id": token_group_id,
                    },
                    usage_retrieve_summary_params.UsageRetrieveSummaryParams,
                ),
            ),
            cast_to=UsageRetrieveSummaryResponse,
        )


class AsyncUsageResource(AsyncAPIResource):
    """Manage and report AI Gateway traffic."""

    @cached_property
    def with_raw_response(self) -> AsyncUsageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncUsageResourceWithStreamingResponse(self)

    async def retrieve_summary(
        self,
        *,
        end_date: Union[str, date],
        start_date: Union[str, date],
        token_group_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageRetrieveSummaryResponse:
        """
        Return complete usage totals, UTC daily and model breakdowns, and guardrail
        event counts for one token group owned by the authenticated account. Requires
        the llm_token_gateway.usage.read permission; spend and guardrail read
        permissions do not grant this combined report. All sections share one database
        snapshot and include the latest usage corrections. Dates use an inclusive start
        and exclusive end spanning 1 to 31 days. Only token_group_id, start_date and
        end_date are accepted; pagination, group_by and other filters are rejected.
        Spend is reference/enforcement USD, not invoice truth or BYOK provider charges.
        Unknown cost is excluded from spend and reported through unknown_requests and
        reserved_spend. Daily rows include zero-activity days. Model rows are ordered by
        request count descending, then model name, and are limited to 1,000. Guardrail
        counts count events, not distinct requests; recent_events contains at most 20
        newest events. A report that exceeds model or query limits returns 503 rather
        than a truncated success.

        Args:
          end_date: Exclusive UTC date in YYYY-MM-DD format. Must follow start_date by 1 to 31 days.

          start_date: Inclusive UTC date in YYYY-MM-DD format. Must precede end_date by 1 to 31 days.

          token_group_id: ID of a token group owned by the authenticated account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/llm_token_gateway/usage/summary",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                        "token_group_id": token_group_id,
                    },
                    usage_retrieve_summary_params.UsageRetrieveSummaryParams,
                ),
            ),
            cast_to=UsageRetrieveSummaryResponse,
        )


class UsageResourceWithRawResponse:
    def __init__(self, usage: UsageResource) -> None:
        self._usage = usage

        self.retrieve_summary = to_raw_response_wrapper(
            usage.retrieve_summary,
        )


class AsyncUsageResourceWithRawResponse:
    def __init__(self, usage: AsyncUsageResource) -> None:
        self._usage = usage

        self.retrieve_summary = async_to_raw_response_wrapper(
            usage.retrieve_summary,
        )


class UsageResourceWithStreamingResponse:
    def __init__(self, usage: UsageResource) -> None:
        self._usage = usage

        self.retrieve_summary = to_streamed_response_wrapper(
            usage.retrieve_summary,
        )


class AsyncUsageResourceWithStreamingResponse:
    def __init__(self, usage: AsyncUsageResource) -> None:
        self._usage = usage

        self.retrieve_summary = async_to_streamed_response_wrapper(
            usage.retrieve_summary,
        )

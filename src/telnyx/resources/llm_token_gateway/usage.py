# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import date, datetime

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
from ...types.llm_token_gateway import usage_retrieve_export_params, usage_retrieve_summary_params
from ...types.llm_token_gateway.usage_retrieve_export_response import UsageRetrieveExportResponse
from ...types.llm_token_gateway.usage_retrieve_summary_response import UsageRetrieveSummaryResponse

__all__ = ["UsageResource", "AsyncUsageResource"]


class UsageResource(SyncAPIResource):
    """Manage and report AI Gateway usage."""

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

    def retrieve_export(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        start_time: Union[str, datetime] | Omit = omit,
        types: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageRetrieveExportResponse:
        """Durable, replayable, content-free usage export for customer pipelines.

        Requires
        the dedicated llm_token_gateway.usage_export.read V2 action; spend.read and
        usage.read do not grant it. Records are inference.request (one per immutable
        ledger revision; a correction adds a new id with supersedes, keep the highest
        revision per request_id) and guardrail.evaluation (one per guardrail event,
        including blocked prompts with no inference record; correlate on request_id).
        Delivery is at least once in commit order: deduplicate on id. Records appear
        after settlement and after every older database transaction has finished
        (meta.horizon_lag_seconds); keep polling with next_cursor, which is always
        returned and is reusable after has_more is false. After a logical database
        restore, restart from start_time and deduplicate on id; a cursor from before it
        may return 409 cursor_expired (no Retry-After). Retention promise 30 days. No
        prompts, responses, provider credentials, supplier or customer rates. Gateway
        reference/enforcement usage, not invoice truth or BYOK provider charges.

        Args:
          cursor: Opaque next_cursor from a previous page; not combinable with start_time. Bound
              to the requested types; the account always comes from the credential.

          start_time: First page only: RFC 3339 with offset, at most 30 days ago and not in the
              future; default now - 24h.

          types: Comma-separated subset of inference.request,guardrail.evaluation; default both.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/llm_token_gateway/usage/export",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "start_time": start_time,
                        "types": types,
                    },
                    usage_retrieve_export_params.UsageRetrieveExportParams,
                ),
            ),
            cast_to=UsageRetrieveExportResponse,
        )

    def retrieve_summary(
        self,
        *,
        end_date: Union[str, date],
        start_date: Union[str, date],
        token_group_id: str,
        metadata: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageRetrieveSummaryResponse:
        """
        Gateway reference/enforcement usage, not invoice truth or BYOK provider charges.
        Requires the dedicated llm_token_gateway.usage.read V2 action for combined spend
        and guardrail reporting; existing spend.read and guardrail_events.read grants do
        not grant this endpoint. All totals, UTC daily buckets, models and latest 20
        guardrail events share one database snapshot. UTC half-open dates, at most 31
        days. Zero-filled days; at most 1000 models (503 rather than truncation on
        overflow/timeout). Known tokens sum independently known categories across latest
        attempt evidence, including corrections; unknown spend is excluded and
        unknown_requests/reserved_spend remain explicit. Guardrail counts count events,
        not distinct requests. No raw spend events, prompts or secrets. This read-only
        report creates no pagination snapshot and accepts no pagination parameters.

        Args:
          metadata: Request tag filters as metadata[<key>]=<value>, at most 5, combined with AND. A
              value matches the tag's text form exactly (booleans as true/false, integers in
              decimal), so metadata[flag]=true matches both boolean true and the string
              "true". Keys are case-sensitive; reserved-prefix keys are rejected. Unindexed:
              bounded by the account, the date range and the report timeout.

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
                        "metadata": metadata,
                    },
                    usage_retrieve_summary_params.UsageRetrieveSummaryParams,
                ),
            ),
            cast_to=UsageRetrieveSummaryResponse,
        )


class AsyncUsageResource(AsyncAPIResource):
    """Manage and report AI Gateway usage."""

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

    async def retrieve_export(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        start_time: Union[str, datetime] | Omit = omit,
        types: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageRetrieveExportResponse:
        """Durable, replayable, content-free usage export for customer pipelines.

        Requires
        the dedicated llm_token_gateway.usage_export.read V2 action; spend.read and
        usage.read do not grant it. Records are inference.request (one per immutable
        ledger revision; a correction adds a new id with supersedes, keep the highest
        revision per request_id) and guardrail.evaluation (one per guardrail event,
        including blocked prompts with no inference record; correlate on request_id).
        Delivery is at least once in commit order: deduplicate on id. Records appear
        after settlement and after every older database transaction has finished
        (meta.horizon_lag_seconds); keep polling with next_cursor, which is always
        returned and is reusable after has_more is false. After a logical database
        restore, restart from start_time and deduplicate on id; a cursor from before it
        may return 409 cursor_expired (no Retry-After). Retention promise 30 days. No
        prompts, responses, provider credentials, supplier or customer rates. Gateway
        reference/enforcement usage, not invoice truth or BYOK provider charges.

        Args:
          cursor: Opaque next_cursor from a previous page; not combinable with start_time. Bound
              to the requested types; the account always comes from the credential.

          start_time: First page only: RFC 3339 with offset, at most 30 days ago and not in the
              future; default now - 24h.

          types: Comma-separated subset of inference.request,guardrail.evaluation; default both.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/llm_token_gateway/usage/export",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "start_time": start_time,
                        "types": types,
                    },
                    usage_retrieve_export_params.UsageRetrieveExportParams,
                ),
            ),
            cast_to=UsageRetrieveExportResponse,
        )

    async def retrieve_summary(
        self,
        *,
        end_date: Union[str, date],
        start_date: Union[str, date],
        token_group_id: str,
        metadata: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageRetrieveSummaryResponse:
        """
        Gateway reference/enforcement usage, not invoice truth or BYOK provider charges.
        Requires the dedicated llm_token_gateway.usage.read V2 action for combined spend
        and guardrail reporting; existing spend.read and guardrail_events.read grants do
        not grant this endpoint. All totals, UTC daily buckets, models and latest 20
        guardrail events share one database snapshot. UTC half-open dates, at most 31
        days. Zero-filled days; at most 1000 models (503 rather than truncation on
        overflow/timeout). Known tokens sum independently known categories across latest
        attempt evidence, including corrections; unknown spend is excluded and
        unknown_requests/reserved_spend remain explicit. Guardrail counts count events,
        not distinct requests. No raw spend events, prompts or secrets. This read-only
        report creates no pagination snapshot and accepts no pagination parameters.

        Args:
          metadata: Request tag filters as metadata[<key>]=<value>, at most 5, combined with AND. A
              value matches the tag's text form exactly (booleans as true/false, integers in
              decimal), so metadata[flag]=true matches both boolean true and the string
              "true". Keys are case-sensitive; reserved-prefix keys are rejected. Unindexed:
              bounded by the account, the date range and the report timeout.

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
                        "metadata": metadata,
                    },
                    usage_retrieve_summary_params.UsageRetrieveSummaryParams,
                ),
            ),
            cast_to=UsageRetrieveSummaryResponse,
        )


class UsageResourceWithRawResponse:
    def __init__(self, usage: UsageResource) -> None:
        self._usage = usage

        self.retrieve_export = to_raw_response_wrapper(
            usage.retrieve_export,
        )
        self.retrieve_summary = to_raw_response_wrapper(
            usage.retrieve_summary,
        )


class AsyncUsageResourceWithRawResponse:
    def __init__(self, usage: AsyncUsageResource) -> None:
        self._usage = usage

        self.retrieve_export = async_to_raw_response_wrapper(
            usage.retrieve_export,
        )
        self.retrieve_summary = async_to_raw_response_wrapper(
            usage.retrieve_summary,
        )


class UsageResourceWithStreamingResponse:
    def __init__(self, usage: UsageResource) -> None:
        self._usage = usage

        self.retrieve_export = to_streamed_response_wrapper(
            usage.retrieve_export,
        )
        self.retrieve_summary = to_streamed_response_wrapper(
            usage.retrieve_summary,
        )


class AsyncUsageResourceWithStreamingResponse:
    def __init__(self, usage: AsyncUsageResource) -> None:
        self._usage = usage

        self.retrieve_export = async_to_streamed_response_wrapper(
            usage.retrieve_export,
        )
        self.retrieve_summary = async_to_streamed_response_wrapper(
            usage.retrieve_summary,
        )

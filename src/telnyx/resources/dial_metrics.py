# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import dial_metric_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncCloudfsCursorPagination, AsyncCloudfsCursorPagination
from .._base_client import AsyncPaginator, make_request_options
from ..types.dial_metric_list_response import DialMetricListResponse

__all__ = ["DialMetricsResource", "AsyncDialMetricsResource"]


class DialMetricsResource(SyncAPIResource):
    """Call information"""

    @cached_property
    def with_raw_response(self) -> DialMetricsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return DialMetricsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DialMetricsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return DialMetricsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        end_time: Union[str, datetime],
        granularity: Literal["second", "minute", "hour"],
        start_time: Union[str, datetime],
        page_after: str | Omit = omit,
        page_limit: int | Omit = omit,
        sort: Literal["-start_time", "start_time"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCloudfsCursorPagination[DialMetricListResponse]:
        """
        Returns dials-per-second (DPS) metrics for your account's outbound dials made
        with the Call Control `Dial` command and TeXML, as time buckets with dial
        counts, accepted and rejected dials, average and peak DPS, and the DPS limit in
        force.

        The result has one record per region per bucket, ordered by `start_time` and
        then `region`, newest first unless `sort=start_time`. Regions are never summed:
        the DPS limit is enforced per region, so a cross-region total cannot be compared
        with it.

        Only buckets that saw dials are returned. Treat a missing bucket as zero dials.

        Only complete 5-second windows are counted, and a window is counted about 15
        seconds after it closes. The newest `granularity=second` record is therefore
        your live DPS, about 20 seconds old. Request the last minute or two with
        `sort=-start_time`; the first record of each `region` is that region's live rate
        (`page[limit]=1` would hide every region but one). If no recent record exists,
        the live rate is zero.

        Results are cursor paginated. Follow `meta.next`, or pass `meta.cursors.after`
        as `page[after]`, until `meta.next` is absent. No total count is returned.

        This endpoint is in development and can change before general availability.

        Args:
          end_time: Exclusive end of the range, ISO 8601. Must be after `start_time`. Buckets that
              start before this time are returned.

          granularity: Bucket size. `second` returns 5-second buckets (the finest resolution) and is
              kept for the last 48 hours. `minute` and `hour` are kept for the last 30 days.

          start_time: Inclusive start of the range, ISO 8601 (for example `2026-09-29T12:00:00.000Z`).
              Buckets that start at or after this time are returned. Must not be older than
              the retention window of the chosen `granularity`.

          page_after: Opaque cursor from `meta.cursors.after` of the previous page. Do not parse or
              construct it. A cursor that matches no records returns an empty page whose
              `meta.cursors.after` and `meta.cursors.before` both echo the given cursor.

          page_limit: Maximum number of buckets per page. Values outside the range are clamped to
              1-10,000.

          sort: Sort order of the buckets by `start_time`. `-start_time` (default) returns the
              newest first, `start_time` the oldest first. `region` follows the same direction
              for buckets with the same `start_time`. To read the live rate, use
              `granularity=second` and `sort=-start_time`, then take the first record of each
              `region`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/dial_metrics",
            page=SyncCloudfsCursorPagination[DialMetricListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_time": end_time,
                        "granularity": granularity,
                        "start_time": start_time,
                        "page_after": page_after,
                        "page_limit": page_limit,
                        "sort": sort,
                    },
                    dial_metric_list_params.DialMetricListParams,
                ),
            ),
            model=DialMetricListResponse,
        )


class AsyncDialMetricsResource(AsyncAPIResource):
    """Call information"""

    @cached_property
    def with_raw_response(self) -> AsyncDialMetricsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDialMetricsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDialMetricsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncDialMetricsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        end_time: Union[str, datetime],
        granularity: Literal["second", "minute", "hour"],
        start_time: Union[str, datetime],
        page_after: str | Omit = omit,
        page_limit: int | Omit = omit,
        sort: Literal["-start_time", "start_time"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[DialMetricListResponse, AsyncCloudfsCursorPagination[DialMetricListResponse]]:
        """
        Returns dials-per-second (DPS) metrics for your account's outbound dials made
        with the Call Control `Dial` command and TeXML, as time buckets with dial
        counts, accepted and rejected dials, average and peak DPS, and the DPS limit in
        force.

        The result has one record per region per bucket, ordered by `start_time` and
        then `region`, newest first unless `sort=start_time`. Regions are never summed:
        the DPS limit is enforced per region, so a cross-region total cannot be compared
        with it.

        Only buckets that saw dials are returned. Treat a missing bucket as zero dials.

        Only complete 5-second windows are counted, and a window is counted about 15
        seconds after it closes. The newest `granularity=second` record is therefore
        your live DPS, about 20 seconds old. Request the last minute or two with
        `sort=-start_time`; the first record of each `region` is that region's live rate
        (`page[limit]=1` would hide every region but one). If no recent record exists,
        the live rate is zero.

        Results are cursor paginated. Follow `meta.next`, or pass `meta.cursors.after`
        as `page[after]`, until `meta.next` is absent. No total count is returned.

        This endpoint is in development and can change before general availability.

        Args:
          end_time: Exclusive end of the range, ISO 8601. Must be after `start_time`. Buckets that
              start before this time are returned.

          granularity: Bucket size. `second` returns 5-second buckets (the finest resolution) and is
              kept for the last 48 hours. `minute` and `hour` are kept for the last 30 days.

          start_time: Inclusive start of the range, ISO 8601 (for example `2026-09-29T12:00:00.000Z`).
              Buckets that start at or after this time are returned. Must not be older than
              the retention window of the chosen `granularity`.

          page_after: Opaque cursor from `meta.cursors.after` of the previous page. Do not parse or
              construct it. A cursor that matches no records returns an empty page whose
              `meta.cursors.after` and `meta.cursors.before` both echo the given cursor.

          page_limit: Maximum number of buckets per page. Values outside the range are clamped to
              1-10,000.

          sort: Sort order of the buckets by `start_time`. `-start_time` (default) returns the
              newest first, `start_time` the oldest first. `region` follows the same direction
              for buckets with the same `start_time`. To read the live rate, use
              `granularity=second` and `sort=-start_time`, then take the first record of each
              `region`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/dial_metrics",
            page=AsyncCloudfsCursorPagination[DialMetricListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_time": end_time,
                        "granularity": granularity,
                        "start_time": start_time,
                        "page_after": page_after,
                        "page_limit": page_limit,
                        "sort": sort,
                    },
                    dial_metric_list_params.DialMetricListParams,
                ),
            ),
            model=DialMetricListResponse,
        )


class DialMetricsResourceWithRawResponse:
    def __init__(self, dial_metrics: DialMetricsResource) -> None:
        self._dial_metrics = dial_metrics

        self.list = to_raw_response_wrapper(
            dial_metrics.list,
        )


class AsyncDialMetricsResourceWithRawResponse:
    def __init__(self, dial_metrics: AsyncDialMetricsResource) -> None:
        self._dial_metrics = dial_metrics

        self.list = async_to_raw_response_wrapper(
            dial_metrics.list,
        )


class DialMetricsResourceWithStreamingResponse:
    def __init__(self, dial_metrics: DialMetricsResource) -> None:
        self._dial_metrics = dial_metrics

        self.list = to_streamed_response_wrapper(
            dial_metrics.list,
        )


class AsyncDialMetricsResourceWithStreamingResponse:
    def __init__(self, dial_metrics: AsyncDialMetricsResource) -> None:
        self._dial_metrics = dial_metrics

        self.list = async_to_streamed_response_wrapper(
            dial_metrics.list,
        )

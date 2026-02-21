# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import messaging_profile_metric_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.messaging_profile_metric_list_response import MessagingProfileMetricListResponse

__all__ = ["MessagingProfileMetricsResource", "AsyncMessagingProfileMetricsResource"]


class MessagingProfileMetricsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MessagingProfileMetricsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return MessagingProfileMetricsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagingProfileMetricsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return MessagingProfileMetricsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        time_frame: Literal["1h", "3h", "24h", "3d", "7d", "30d"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessagingProfileMetricListResponse:
        """
        List high-level metrics for all messaging profiles belonging to the
        authenticated user.

        Args:
          time_frame: The time frame for metrics.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/messaging_profile_metrics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"time_frame": time_frame}, messaging_profile_metric_list_params.MessagingProfileMetricListParams
                ),
            ),
            cast_to=MessagingProfileMetricListResponse,
        )


class AsyncMessagingProfileMetricsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMessagingProfileMetricsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagingProfileMetricsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagingProfileMetricsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncMessagingProfileMetricsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        time_frame: Literal["1h", "3h", "24h", "3d", "7d", "30d"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessagingProfileMetricListResponse:
        """
        List high-level metrics for all messaging profiles belonging to the
        authenticated user.

        Args:
          time_frame: The time frame for metrics.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/messaging_profile_metrics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"time_frame": time_frame}, messaging_profile_metric_list_params.MessagingProfileMetricListParams
                ),
            ),
            cast_to=MessagingProfileMetricListResponse,
        )


class MessagingProfileMetricsResourceWithRawResponse:
    def __init__(self, messaging_profile_metrics: MessagingProfileMetricsResource) -> None:
        self._messaging_profile_metrics = messaging_profile_metrics

        self.list = to_raw_response_wrapper(
            messaging_profile_metrics.list,
        )


class AsyncMessagingProfileMetricsResourceWithRawResponse:
    def __init__(self, messaging_profile_metrics: AsyncMessagingProfileMetricsResource) -> None:
        self._messaging_profile_metrics = messaging_profile_metrics

        self.list = async_to_raw_response_wrapper(
            messaging_profile_metrics.list,
        )


class MessagingProfileMetricsResourceWithStreamingResponse:
    def __init__(self, messaging_profile_metrics: MessagingProfileMetricsResource) -> None:
        self._messaging_profile_metrics = messaging_profile_metrics

        self.list = to_streamed_response_wrapper(
            messaging_profile_metrics.list,
        )


class AsyncMessagingProfileMetricsResourceWithStreamingResponse:
    def __init__(self, messaging_profile_metrics: AsyncMessagingProfileMetricsResource) -> None:
        self._messaging_profile_metrics = messaging_profile_metrics

        self.list = async_to_streamed_response_wrapper(
            messaging_profile_metrics.list,
        )

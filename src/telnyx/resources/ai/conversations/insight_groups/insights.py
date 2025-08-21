# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options

__all__ = ["InsightsResource", "AsyncInsightsResource"]


class InsightsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InsightsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return InsightsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InsightsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return InsightsResourceWithStreamingResponse(self)

    def assign(
        self,
        insight_id: str,
        *,
        group_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Assign an insight to a group

        Args:
          group_id: The ID of the insight group

          insight_id: The ID of the insight

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        if not insight_id:
            raise ValueError(f"Expected a non-empty value for `insight_id` but received {insight_id!r}")
        return self._post(
            f"/ai/conversations/insight-groups/{group_id}/insights/{insight_id}/assign",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def delete_unassign(
        self,
        insight_id: str,
        *,
        group_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Remove an insight from a group

        Args:
          group_id: The ID of the insight group

          insight_id: The ID of the insight

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        if not insight_id:
            raise ValueError(f"Expected a non-empty value for `insight_id` but received {insight_id!r}")
        return self._delete(
            f"/ai/conversations/insight-groups/{group_id}/insights/{insight_id}/unassign",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncInsightsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInsightsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInsightsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInsightsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncInsightsResourceWithStreamingResponse(self)

    async def assign(
        self,
        insight_id: str,
        *,
        group_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Assign an insight to a group

        Args:
          group_id: The ID of the insight group

          insight_id: The ID of the insight

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        if not insight_id:
            raise ValueError(f"Expected a non-empty value for `insight_id` but received {insight_id!r}")
        return await self._post(
            f"/ai/conversations/insight-groups/{group_id}/insights/{insight_id}/assign",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def delete_unassign(
        self,
        insight_id: str,
        *,
        group_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Remove an insight from a group

        Args:
          group_id: The ID of the insight group

          insight_id: The ID of the insight

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        if not insight_id:
            raise ValueError(f"Expected a non-empty value for `insight_id` but received {insight_id!r}")
        return await self._delete(
            f"/ai/conversations/insight-groups/{group_id}/insights/{insight_id}/unassign",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class InsightsResourceWithRawResponse:
    def __init__(self, insights: InsightsResource) -> None:
        self._insights = insights

        self.assign = to_raw_response_wrapper(
            insights.assign,
        )
        self.delete_unassign = to_raw_response_wrapper(
            insights.delete_unassign,
        )


class AsyncInsightsResourceWithRawResponse:
    def __init__(self, insights: AsyncInsightsResource) -> None:
        self._insights = insights

        self.assign = async_to_raw_response_wrapper(
            insights.assign,
        )
        self.delete_unassign = async_to_raw_response_wrapper(
            insights.delete_unassign,
        )


class InsightsResourceWithStreamingResponse:
    def __init__(self, insights: InsightsResource) -> None:
        self._insights = insights

        self.assign = to_streamed_response_wrapper(
            insights.assign,
        )
        self.delete_unassign = to_streamed_response_wrapper(
            insights.delete_unassign,
        )


class AsyncInsightsResourceWithStreamingResponse:
    def __init__(self, insights: AsyncInsightsResource) -> None:
        self._insights = insights

        self.assign = async_to_streamed_response_wrapper(
            insights.assign,
        )
        self.delete_unassign = async_to_streamed_response_wrapper(
            insights.delete_unassign,
        )

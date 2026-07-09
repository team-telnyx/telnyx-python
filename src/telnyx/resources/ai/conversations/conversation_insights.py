# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.ai.conversations import conversation_insight_retrieve_aggregates_params
from ....types.ai.conversations.conversation_insight_retrieve_aggregates_response import (
    ConversationInsightRetrieveAggregatesResponse,
)

__all__ = ["ConversationInsightsResource", "AsyncConversationInsightsResource"]


class ConversationInsightsResource(SyncAPIResource):
    """Manage historical AI assistant conversations"""

    @cached_property
    def with_raw_response(self) -> ConversationInsightsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ConversationInsightsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConversationInsightsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ConversationInsightsResourceWithStreamingResponse(self)

    def retrieve_aggregates(
        self,
        *,
        created_at: str | Omit = omit,
        group_by: SequenceNotStr[str] | Omit = omit,
        insight_id: str | Omit = omit,
        metadata: conversation_insight_retrieve_aggregates_params.Metadata | Omit = omit,
        show: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationInsightRetrieveAggregatesResponse:
        """
        Aggregate conversation insights by specified fields

        Args:
          created_at: Filter by creation datetime to scope the aggregation window. Supports range
              operators (e.g., `created_at=gte.2025-01-01T00:00:00Z` for the start of the
              range, `created_at=lt.2025-01-02T00:00:00Z` for the end). To build per-day time
              series (as the portal does for the 'Insights Over Time' chart), issue one
              request per day bounded by `created_at=gte.<day_start>` and
              `created_at=lt.<next_day_start>`.

          group_by: Fields to group by (can be comma-separated or multiple parameters). Prefix a
              field with 'metadata.' (e.g. 'metadata.assistant_id') to group by the
              conversation's metadata instead of the insight result.

              Common fields used for over-time charts:

              - `score` — Group by the insight's score value (e.g. for Agent Instruction
                Following, User Satisfaction).
              - `metadata.assistant_id` — Group by the assistant that handled the
                conversation.
              - `metadata.assistant_version_id` — Group by the assistant version, useful for
                comparing performance across versions in the portal's 'Insights Over Time'
                chart.
              - `metadata.telnyx_conversation_channel` — Group by conversation channel
                (phone_call, web_chat, etc.).

          insight_id: Optional insight ID to filter conversation insights. Only insights matching this
              ID will be included in the aggregation.

          show: Fields to include in the result (can be comma-separated or multiple parameters).
              Supports the same 'metadata.<key>' prefix as group_by. Each returned row will
              contain the grouped field values plus a `record_count` indicating how many
              conversation insights match that combination.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/ai/conversations/conversation-insights/aggregates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at": created_at,
                        "group_by": group_by,
                        "insight_id": insight_id,
                        "metadata": metadata,
                        "show": show,
                    },
                    conversation_insight_retrieve_aggregates_params.ConversationInsightRetrieveAggregatesParams,
                ),
            ),
            cast_to=ConversationInsightRetrieveAggregatesResponse,
        )


class AsyncConversationInsightsResource(AsyncAPIResource):
    """Manage historical AI assistant conversations"""

    @cached_property
    def with_raw_response(self) -> AsyncConversationInsightsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConversationInsightsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConversationInsightsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncConversationInsightsResourceWithStreamingResponse(self)

    async def retrieve_aggregates(
        self,
        *,
        created_at: str | Omit = omit,
        group_by: SequenceNotStr[str] | Omit = omit,
        insight_id: str | Omit = omit,
        metadata: conversation_insight_retrieve_aggregates_params.Metadata | Omit = omit,
        show: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationInsightRetrieveAggregatesResponse:
        """
        Aggregate conversation insights by specified fields

        Args:
          created_at: Filter by creation datetime to scope the aggregation window. Supports range
              operators (e.g., `created_at=gte.2025-01-01T00:00:00Z` for the start of the
              range, `created_at=lt.2025-01-02T00:00:00Z` for the end). To build per-day time
              series (as the portal does for the 'Insights Over Time' chart), issue one
              request per day bounded by `created_at=gte.<day_start>` and
              `created_at=lt.<next_day_start>`.

          group_by: Fields to group by (can be comma-separated or multiple parameters). Prefix a
              field with 'metadata.' (e.g. 'metadata.assistant_id') to group by the
              conversation's metadata instead of the insight result.

              Common fields used for over-time charts:

              - `score` — Group by the insight's score value (e.g. for Agent Instruction
                Following, User Satisfaction).
              - `metadata.assistant_id` — Group by the assistant that handled the
                conversation.
              - `metadata.assistant_version_id` — Group by the assistant version, useful for
                comparing performance across versions in the portal's 'Insights Over Time'
                chart.
              - `metadata.telnyx_conversation_channel` — Group by conversation channel
                (phone_call, web_chat, etc.).

          insight_id: Optional insight ID to filter conversation insights. Only insights matching this
              ID will be included in the aggregation.

          show: Fields to include in the result (can be comma-separated or multiple parameters).
              Supports the same 'metadata.<key>' prefix as group_by. Each returned row will
              contain the grouped field values plus a `record_count` indicating how many
              conversation insights match that combination.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/ai/conversations/conversation-insights/aggregates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "created_at": created_at,
                        "group_by": group_by,
                        "insight_id": insight_id,
                        "metadata": metadata,
                        "show": show,
                    },
                    conversation_insight_retrieve_aggregates_params.ConversationInsightRetrieveAggregatesParams,
                ),
            ),
            cast_to=ConversationInsightRetrieveAggregatesResponse,
        )


class ConversationInsightsResourceWithRawResponse:
    def __init__(self, conversation_insights: ConversationInsightsResource) -> None:
        self._conversation_insights = conversation_insights

        self.retrieve_aggregates = to_raw_response_wrapper(
            conversation_insights.retrieve_aggregates,
        )


class AsyncConversationInsightsResourceWithRawResponse:
    def __init__(self, conversation_insights: AsyncConversationInsightsResource) -> None:
        self._conversation_insights = conversation_insights

        self.retrieve_aggregates = async_to_raw_response_wrapper(
            conversation_insights.retrieve_aggregates,
        )


class ConversationInsightsResourceWithStreamingResponse:
    def __init__(self, conversation_insights: ConversationInsightsResource) -> None:
        self._conversation_insights = conversation_insights

        self.retrieve_aggregates = to_streamed_response_wrapper(
            conversation_insights.retrieve_aggregates,
        )


class AsyncConversationInsightsResourceWithStreamingResponse:
    def __init__(self, conversation_insights: AsyncConversationInsightsResource) -> None:
        self._conversation_insights = conversation_insights

        self.retrieve_aggregates = async_to_streamed_response_wrapper(
            conversation_insights.retrieve_aggregates,
        )

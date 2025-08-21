# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from .insights import (
    InsightsResource,
    AsyncInsightsResource,
    InsightsResourceWithRawResponse,
    AsyncInsightsResourceWithRawResponse,
    InsightsResourceWithStreamingResponse,
    AsyncInsightsResourceWithStreamingResponse,
)
from .messages import (
    MessagesResource,
    AsyncMessagesResource,
    MessagesResourceWithRawResponse,
    AsyncMessagesResourceWithRawResponse,
    MessagesResourceWithStreamingResponse,
    AsyncMessagesResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.ai import conversation_list_params, conversation_create_params, conversation_update_params
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.ai.conversation import Conversation
from .insight_groups.insight_groups import (
    InsightGroupsResource,
    AsyncInsightGroupsResource,
    InsightGroupsResourceWithRawResponse,
    AsyncInsightGroupsResourceWithRawResponse,
    InsightGroupsResourceWithStreamingResponse,
    AsyncInsightGroupsResourceWithStreamingResponse,
)
from ....types.ai.conversation_list_response import ConversationListResponse
from ....types.ai.conversation_update_response import ConversationUpdateResponse
from ....types.ai.conversation_retrieve_response import ConversationRetrieveResponse
from ....types.ai.conversation_retrieve_conversations_insights_response import (
    ConversationRetrieveConversationsInsightsResponse,
)

__all__ = ["ConversationsResource", "AsyncConversationsResource"]


class ConversationsResource(SyncAPIResource):
    @cached_property
    def insight_groups(self) -> InsightGroupsResource:
        return InsightGroupsResource(self._client)

    @cached_property
    def insights(self) -> InsightsResource:
        return InsightsResource(self._client)

    @cached_property
    def messages(self) -> MessagesResource:
        return MessagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> ConversationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ConversationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConversationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ConversationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Conversation:
        """
        Create a new AI Conversation.

        Args:
          metadata: Metadata associated with the conversation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/conversations",
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "name": name,
                },
                conversation_create_params.ConversationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Conversation,
        )

    def retrieve(
        self,
        conversation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConversationRetrieveResponse:
        """
        Retrieve a specific AI conversation by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return self._get(
            f"/ai/conversations/{conversation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationRetrieveResponse,
        )

    def update(
        self,
        conversation_id: str,
        *,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConversationUpdateResponse:
        """
        Update metadata for a specific conversation.

        Args:
          metadata: Metadata associated with the conversation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return self._put(
            f"/ai/conversations/{conversation_id}",
            body=maybe_transform({"metadata": metadata}, conversation_update_params.ConversationUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationUpdateResponse,
        )

    def list(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        created_at: str | NotGiven = NOT_GIVEN,
        last_message_at: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        metadata_assistant_id: str | NotGiven = NOT_GIVEN,
        metadata_call_control_id: str | NotGiven = NOT_GIVEN,
        metadata_telnyx_agent_target: str | NotGiven = NOT_GIVEN,
        metadata_telnyx_conversation_channel: str | NotGiven = NOT_GIVEN,
        metadata_telnyx_end_user_target: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        or_: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConversationListResponse:
        """Retrieve a list of all AI conversations configured by the user.

        Supports
        [PostgREST-style query parameters](https://postgrest.org/en/stable/api.html#horizontal-filtering-rows)
        for filtering. Examples are included for the standard metadata fields, but you
        can filter on any field in the metadata JSON object. For example, to filter by a
        custom field `metadata->custom_field`, use `metadata->custom_field=eq.value`.

        Args:
          id: Filter by conversation ID (e.g. id=eq.123)

          created_at: Filter by creation datetime (e.g., `created_at=gte.2025-01-01`)

          last_message_at: Filter by last message datetime (e.g., `last_message_at=lte.2025-06-01`)

          limit: Limit the number of returned conversations (e.g., `limit=10`)

          metadata_assistant_id: Filter by assistant ID (e.g., `metadata->assistant_id=eq.assistant-123`)

          metadata_call_control_id: Filter by call control ID (e.g., `metadata->call_control_id=eq.v3:123`)

          metadata_telnyx_agent_target: Filter by the phone number, SIP URI, or other identifier for the agent (e.g.,
              `metadata->telnyx_agent_target=eq.+13128675309`)

          metadata_telnyx_conversation_channel: Filter by conversation channel (e.g.,
              `metadata->telnyx_conversation_channel=eq.phone_call`)

          metadata_telnyx_end_user_target: Filter by the phone number, SIP URI, or other identifier for the end user (e.g.,
              `metadata->telnyx_end_user_target=eq.+13128675309`)

          name: Filter by conversation Name (e.g. `name=like.Voice%`)

          or_: Apply OR conditions using PostgREST syntax (e.g.,
              `or=(created_at.gte.2025-04-01,last_message_at.gte.2025-04-01)`)

          order: Order the results by specific fields (e.g., `order=created_at.desc` or
              `order=last_message_at.asc`)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/ai/conversations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "created_at": created_at,
                        "last_message_at": last_message_at,
                        "limit": limit,
                        "metadata_assistant_id": metadata_assistant_id,
                        "metadata_call_control_id": metadata_call_control_id,
                        "metadata_telnyx_agent_target": metadata_telnyx_agent_target,
                        "metadata_telnyx_conversation_channel": metadata_telnyx_conversation_channel,
                        "metadata_telnyx_end_user_target": metadata_telnyx_end_user_target,
                        "name": name,
                        "or_": or_,
                        "order": order,
                    },
                    conversation_list_params.ConversationListParams,
                ),
            ),
            cast_to=ConversationListResponse,
        )

    def delete(
        self,
        conversation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a specific conversation by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/ai/conversations/{conversation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve_conversations_insights(
        self,
        conversation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConversationRetrieveConversationsInsightsResponse:
        """
        Retrieve insights for a specific conversation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return self._get(
            f"/ai/conversations/{conversation_id}/conversations-insights",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationRetrieveConversationsInsightsResponse,
        )


class AsyncConversationsResource(AsyncAPIResource):
    @cached_property
    def insight_groups(self) -> AsyncInsightGroupsResource:
        return AsyncInsightGroupsResource(self._client)

    @cached_property
    def insights(self) -> AsyncInsightsResource:
        return AsyncInsightsResource(self._client)

    @cached_property
    def messages(self) -> AsyncMessagesResource:
        return AsyncMessagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConversationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConversationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConversationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncConversationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Conversation:
        """
        Create a new AI Conversation.

        Args:
          metadata: Metadata associated with the conversation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/conversations",
            body=await async_maybe_transform(
                {
                    "metadata": metadata,
                    "name": name,
                },
                conversation_create_params.ConversationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Conversation,
        )

    async def retrieve(
        self,
        conversation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConversationRetrieveResponse:
        """
        Retrieve a specific AI conversation by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return await self._get(
            f"/ai/conversations/{conversation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationRetrieveResponse,
        )

    async def update(
        self,
        conversation_id: str,
        *,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConversationUpdateResponse:
        """
        Update metadata for a specific conversation.

        Args:
          metadata: Metadata associated with the conversation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return await self._put(
            f"/ai/conversations/{conversation_id}",
            body=await async_maybe_transform(
                {"metadata": metadata}, conversation_update_params.ConversationUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationUpdateResponse,
        )

    async def list(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        created_at: str | NotGiven = NOT_GIVEN,
        last_message_at: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        metadata_assistant_id: str | NotGiven = NOT_GIVEN,
        metadata_call_control_id: str | NotGiven = NOT_GIVEN,
        metadata_telnyx_agent_target: str | NotGiven = NOT_GIVEN,
        metadata_telnyx_conversation_channel: str | NotGiven = NOT_GIVEN,
        metadata_telnyx_end_user_target: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        or_: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConversationListResponse:
        """Retrieve a list of all AI conversations configured by the user.

        Supports
        [PostgREST-style query parameters](https://postgrest.org/en/stable/api.html#horizontal-filtering-rows)
        for filtering. Examples are included for the standard metadata fields, but you
        can filter on any field in the metadata JSON object. For example, to filter by a
        custom field `metadata->custom_field`, use `metadata->custom_field=eq.value`.

        Args:
          id: Filter by conversation ID (e.g. id=eq.123)

          created_at: Filter by creation datetime (e.g., `created_at=gte.2025-01-01`)

          last_message_at: Filter by last message datetime (e.g., `last_message_at=lte.2025-06-01`)

          limit: Limit the number of returned conversations (e.g., `limit=10`)

          metadata_assistant_id: Filter by assistant ID (e.g., `metadata->assistant_id=eq.assistant-123`)

          metadata_call_control_id: Filter by call control ID (e.g., `metadata->call_control_id=eq.v3:123`)

          metadata_telnyx_agent_target: Filter by the phone number, SIP URI, or other identifier for the agent (e.g.,
              `metadata->telnyx_agent_target=eq.+13128675309`)

          metadata_telnyx_conversation_channel: Filter by conversation channel (e.g.,
              `metadata->telnyx_conversation_channel=eq.phone_call`)

          metadata_telnyx_end_user_target: Filter by the phone number, SIP URI, or other identifier for the end user (e.g.,
              `metadata->telnyx_end_user_target=eq.+13128675309`)

          name: Filter by conversation Name (e.g. `name=like.Voice%`)

          or_: Apply OR conditions using PostgREST syntax (e.g.,
              `or=(created_at.gte.2025-04-01,last_message_at.gte.2025-04-01)`)

          order: Order the results by specific fields (e.g., `order=created_at.desc` or
              `order=last_message_at.asc`)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/ai/conversations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "id": id,
                        "created_at": created_at,
                        "last_message_at": last_message_at,
                        "limit": limit,
                        "metadata_assistant_id": metadata_assistant_id,
                        "metadata_call_control_id": metadata_call_control_id,
                        "metadata_telnyx_agent_target": metadata_telnyx_agent_target,
                        "metadata_telnyx_conversation_channel": metadata_telnyx_conversation_channel,
                        "metadata_telnyx_end_user_target": metadata_telnyx_end_user_target,
                        "name": name,
                        "or_": or_,
                        "order": order,
                    },
                    conversation_list_params.ConversationListParams,
                ),
            ),
            cast_to=ConversationListResponse,
        )

    async def delete(
        self,
        conversation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a specific conversation by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/ai/conversations/{conversation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve_conversations_insights(
        self,
        conversation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConversationRetrieveConversationsInsightsResponse:
        """
        Retrieve insights for a specific conversation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return await self._get(
            f"/ai/conversations/{conversation_id}/conversations-insights",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationRetrieveConversationsInsightsResponse,
        )


class ConversationsResourceWithRawResponse:
    def __init__(self, conversations: ConversationsResource) -> None:
        self._conversations = conversations

        self.create = to_raw_response_wrapper(
            conversations.create,
        )
        self.retrieve = to_raw_response_wrapper(
            conversations.retrieve,
        )
        self.update = to_raw_response_wrapper(
            conversations.update,
        )
        self.list = to_raw_response_wrapper(
            conversations.list,
        )
        self.delete = to_raw_response_wrapper(
            conversations.delete,
        )
        self.retrieve_conversations_insights = to_raw_response_wrapper(
            conversations.retrieve_conversations_insights,
        )

    @cached_property
    def insight_groups(self) -> InsightGroupsResourceWithRawResponse:
        return InsightGroupsResourceWithRawResponse(self._conversations.insight_groups)

    @cached_property
    def insights(self) -> InsightsResourceWithRawResponse:
        return InsightsResourceWithRawResponse(self._conversations.insights)

    @cached_property
    def messages(self) -> MessagesResourceWithRawResponse:
        return MessagesResourceWithRawResponse(self._conversations.messages)


class AsyncConversationsResourceWithRawResponse:
    def __init__(self, conversations: AsyncConversationsResource) -> None:
        self._conversations = conversations

        self.create = async_to_raw_response_wrapper(
            conversations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            conversations.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            conversations.update,
        )
        self.list = async_to_raw_response_wrapper(
            conversations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            conversations.delete,
        )
        self.retrieve_conversations_insights = async_to_raw_response_wrapper(
            conversations.retrieve_conversations_insights,
        )

    @cached_property
    def insight_groups(self) -> AsyncInsightGroupsResourceWithRawResponse:
        return AsyncInsightGroupsResourceWithRawResponse(self._conversations.insight_groups)

    @cached_property
    def insights(self) -> AsyncInsightsResourceWithRawResponse:
        return AsyncInsightsResourceWithRawResponse(self._conversations.insights)

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithRawResponse:
        return AsyncMessagesResourceWithRawResponse(self._conversations.messages)


class ConversationsResourceWithStreamingResponse:
    def __init__(self, conversations: ConversationsResource) -> None:
        self._conversations = conversations

        self.create = to_streamed_response_wrapper(
            conversations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            conversations.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            conversations.update,
        )
        self.list = to_streamed_response_wrapper(
            conversations.list,
        )
        self.delete = to_streamed_response_wrapper(
            conversations.delete,
        )
        self.retrieve_conversations_insights = to_streamed_response_wrapper(
            conversations.retrieve_conversations_insights,
        )

    @cached_property
    def insight_groups(self) -> InsightGroupsResourceWithStreamingResponse:
        return InsightGroupsResourceWithStreamingResponse(self._conversations.insight_groups)

    @cached_property
    def insights(self) -> InsightsResourceWithStreamingResponse:
        return InsightsResourceWithStreamingResponse(self._conversations.insights)

    @cached_property
    def messages(self) -> MessagesResourceWithStreamingResponse:
        return MessagesResourceWithStreamingResponse(self._conversations.messages)


class AsyncConversationsResourceWithStreamingResponse:
    def __init__(self, conversations: AsyncConversationsResource) -> None:
        self._conversations = conversations

        self.create = async_to_streamed_response_wrapper(
            conversations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            conversations.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            conversations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            conversations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            conversations.delete,
        )
        self.retrieve_conversations_insights = async_to_streamed_response_wrapper(
            conversations.retrieve_conversations_insights,
        )

    @cached_property
    def insight_groups(self) -> AsyncInsightGroupsResourceWithStreamingResponse:
        return AsyncInsightGroupsResourceWithStreamingResponse(self._conversations.insight_groups)

    @cached_property
    def insights(self) -> AsyncInsightsResourceWithStreamingResponse:
        return AsyncInsightsResourceWithStreamingResponse(self._conversations.insights)

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithStreamingResponse:
        return AsyncMessagesResourceWithStreamingResponse(self._conversations.messages)

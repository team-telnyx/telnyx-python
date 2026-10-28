# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ......_types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ......_utils import path_template, maybe_transform, async_maybe_transform
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_base_client import make_request_options
from ......types.ai.tests.test_framework.v1 import aiagent_list_params, aiagent_create_params, aiagent_update_params
from ......types.ai.tests.test_framework.v1.test_agent import TestAgent
from ......types.ai.tests.test_framework.v1.aiagent_list_response import AiagentListResponse

__all__ = ["AiagentsResource", "AsyncAiagentsResource"]


class AiagentsResource(SyncAPIResource):
    """
    Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
    """

    @cached_property
    def with_raw_response(self) -> AiagentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AiagentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AiagentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AiagentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        agent_name: str,
        assistant_id: str,
        auto_fetch_calls_enabled: bool | Omit = omit,
        auto_sync_prompt_enabled: bool | Omit = omit,
        auto_update_dropoff_nodes: bool | Omit = omit,
        auto_update_topic_nodes: bool | Omit = omit,
        contact_number: str | Omit = omit,
        description: str | Omit = omit,
        inbound: bool | Omit = omit,
        language: str | Omit = omit,
        llm_max_tokens: int | Omit = omit,
        llm_model: str | Omit = omit,
        llm_system_prompt: str | Omit = omit,
        llm_temperature: float | Omit = omit,
        outbound_auto_call: bool | Omit = omit,
        sip_endpoint: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestAgent:
        """Creates a test agent in your organization.

        The agent wraps a Telnyx AI assistant
        so simulated callers can be sent against it.

        Args:
          agent_name: Name of the test agent.

          assistant_id: ID of the Telnyx AI assistant under test.

          language: ISO language code the test agent converses in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/tests/test_framework/v1/aiagents",
            body=maybe_transform(
                {
                    "agent_name": agent_name,
                    "assistant_id": assistant_id,
                    "auto_fetch_calls_enabled": auto_fetch_calls_enabled,
                    "auto_sync_prompt_enabled": auto_sync_prompt_enabled,
                    "auto_update_dropoff_nodes": auto_update_dropoff_nodes,
                    "auto_update_topic_nodes": auto_update_topic_nodes,
                    "contact_number": contact_number,
                    "description": description,
                    "inbound": inbound,
                    "language": language,
                    "llm_max_tokens": llm_max_tokens,
                    "llm_model": llm_model,
                    "llm_system_prompt": llm_system_prompt,
                    "llm_temperature": llm_temperature,
                    "outbound_auto_call": outbound_auto_call,
                    "sip_endpoint": sip_endpoint,
                },
                aiagent_create_params.AiagentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestAgent,
        )

    def retrieve(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestAgent:
        """
        Returns the specified test agent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/ai/tests/test_framework/v1/aiagents/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestAgent,
        )

    def update(
        self,
        id: int,
        *,
        agent_name: str | Omit = omit,
        assistant_id: str | Omit = omit,
        auto_fetch_calls_enabled: bool | Omit = omit,
        auto_sync_prompt_enabled: bool | Omit = omit,
        auto_update_dropoff_nodes: bool | Omit = omit,
        auto_update_topic_nodes: bool | Omit = omit,
        contact_number: str | Omit = omit,
        description: str | Omit = omit,
        inbound: bool | Omit = omit,
        language: str | Omit = omit,
        llm_max_tokens: int | Omit = omit,
        llm_model: str | Omit = omit,
        llm_system_prompt: str | Omit = omit,
        llm_temperature: float | Omit = omit,
        outbound_auto_call: bool | Omit = omit,
        sip_endpoint: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestAgent:
        """
        Updates the specified test agent.

        Args:
          agent_name: Name of the test agent.

          assistant_id: ID of the Telnyx AI assistant under test.

          language: ISO language code the test agent converses in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            path_template("/ai/tests/test_framework/v1/aiagents/{id}", id=id),
            body=maybe_transform(
                {
                    "agent_name": agent_name,
                    "assistant_id": assistant_id,
                    "auto_fetch_calls_enabled": auto_fetch_calls_enabled,
                    "auto_sync_prompt_enabled": auto_sync_prompt_enabled,
                    "auto_update_dropoff_nodes": auto_update_dropoff_nodes,
                    "auto_update_topic_nodes": auto_update_topic_nodes,
                    "contact_number": contact_number,
                    "description": description,
                    "inbound": inbound,
                    "language": language,
                    "llm_max_tokens": llm_max_tokens,
                    "llm_model": llm_model,
                    "llm_system_prompt": llm_system_prompt,
                    "llm_temperature": llm_temperature,
                    "outbound_auto_call": outbound_auto_call,
                    "sip_endpoint": sip_endpoint,
                },
                aiagent_update_params.AiagentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestAgent,
        )

    def list(
        self,
        *,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AiagentListResponse:
        """Returns a paginated list of test agents in your organization.

        A test agent wraps
        the Telnyx AI assistant under test and drives simulated callers against it.

        Args:
          page: Page number (1-based).

          page_size: Number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/ai/tests/test_framework/v1/aiagents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                    },
                    aiagent_list_params.AiagentListParams,
                ),
            ),
            cast_to=AiagentListResponse,
        )

    def delete(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes the specified test agent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            path_template("/ai/tests/test_framework/v1/aiagents/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncAiagentsResource(AsyncAPIResource):
    """
    Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
    """

    @cached_property
    def with_raw_response(self) -> AsyncAiagentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAiagentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAiagentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncAiagentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        agent_name: str,
        assistant_id: str,
        auto_fetch_calls_enabled: bool | Omit = omit,
        auto_sync_prompt_enabled: bool | Omit = omit,
        auto_update_dropoff_nodes: bool | Omit = omit,
        auto_update_topic_nodes: bool | Omit = omit,
        contact_number: str | Omit = omit,
        description: str | Omit = omit,
        inbound: bool | Omit = omit,
        language: str | Omit = omit,
        llm_max_tokens: int | Omit = omit,
        llm_model: str | Omit = omit,
        llm_system_prompt: str | Omit = omit,
        llm_temperature: float | Omit = omit,
        outbound_auto_call: bool | Omit = omit,
        sip_endpoint: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestAgent:
        """Creates a test agent in your organization.

        The agent wraps a Telnyx AI assistant
        so simulated callers can be sent against it.

        Args:
          agent_name: Name of the test agent.

          assistant_id: ID of the Telnyx AI assistant under test.

          language: ISO language code the test agent converses in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/tests/test_framework/v1/aiagents",
            body=await async_maybe_transform(
                {
                    "agent_name": agent_name,
                    "assistant_id": assistant_id,
                    "auto_fetch_calls_enabled": auto_fetch_calls_enabled,
                    "auto_sync_prompt_enabled": auto_sync_prompt_enabled,
                    "auto_update_dropoff_nodes": auto_update_dropoff_nodes,
                    "auto_update_topic_nodes": auto_update_topic_nodes,
                    "contact_number": contact_number,
                    "description": description,
                    "inbound": inbound,
                    "language": language,
                    "llm_max_tokens": llm_max_tokens,
                    "llm_model": llm_model,
                    "llm_system_prompt": llm_system_prompt,
                    "llm_temperature": llm_temperature,
                    "outbound_auto_call": outbound_auto_call,
                    "sip_endpoint": sip_endpoint,
                },
                aiagent_create_params.AiagentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestAgent,
        )

    async def retrieve(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestAgent:
        """
        Returns the specified test agent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/ai/tests/test_framework/v1/aiagents/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestAgent,
        )

    async def update(
        self,
        id: int,
        *,
        agent_name: str | Omit = omit,
        assistant_id: str | Omit = omit,
        auto_fetch_calls_enabled: bool | Omit = omit,
        auto_sync_prompt_enabled: bool | Omit = omit,
        auto_update_dropoff_nodes: bool | Omit = omit,
        auto_update_topic_nodes: bool | Omit = omit,
        contact_number: str | Omit = omit,
        description: str | Omit = omit,
        inbound: bool | Omit = omit,
        language: str | Omit = omit,
        llm_max_tokens: int | Omit = omit,
        llm_model: str | Omit = omit,
        llm_system_prompt: str | Omit = omit,
        llm_temperature: float | Omit = omit,
        outbound_auto_call: bool | Omit = omit,
        sip_endpoint: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestAgent:
        """
        Updates the specified test agent.

        Args:
          agent_name: Name of the test agent.

          assistant_id: ID of the Telnyx AI assistant under test.

          language: ISO language code the test agent converses in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            path_template("/ai/tests/test_framework/v1/aiagents/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "agent_name": agent_name,
                    "assistant_id": assistant_id,
                    "auto_fetch_calls_enabled": auto_fetch_calls_enabled,
                    "auto_sync_prompt_enabled": auto_sync_prompt_enabled,
                    "auto_update_dropoff_nodes": auto_update_dropoff_nodes,
                    "auto_update_topic_nodes": auto_update_topic_nodes,
                    "contact_number": contact_number,
                    "description": description,
                    "inbound": inbound,
                    "language": language,
                    "llm_max_tokens": llm_max_tokens,
                    "llm_model": llm_model,
                    "llm_system_prompt": llm_system_prompt,
                    "llm_temperature": llm_temperature,
                    "outbound_auto_call": outbound_auto_call,
                    "sip_endpoint": sip_endpoint,
                },
                aiagent_update_params.AiagentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestAgent,
        )

    async def list(
        self,
        *,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AiagentListResponse:
        """Returns a paginated list of test agents in your organization.

        A test agent wraps
        the Telnyx AI assistant under test and drives simulated callers against it.

        Args:
          page: Page number (1-based).

          page_size: Number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/ai/tests/test_framework/v1/aiagents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                    },
                    aiagent_list_params.AiagentListParams,
                ),
            ),
            cast_to=AiagentListResponse,
        )

    async def delete(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes the specified test agent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            path_template("/ai/tests/test_framework/v1/aiagents/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AiagentsResourceWithRawResponse:
    def __init__(self, aiagents: AiagentsResource) -> None:
        self._aiagents = aiagents

        self.create = to_raw_response_wrapper(
            aiagents.create,
        )
        self.retrieve = to_raw_response_wrapper(
            aiagents.retrieve,
        )
        self.update = to_raw_response_wrapper(
            aiagents.update,
        )
        self.list = to_raw_response_wrapper(
            aiagents.list,
        )
        self.delete = to_raw_response_wrapper(
            aiagents.delete,
        )


class AsyncAiagentsResourceWithRawResponse:
    def __init__(self, aiagents: AsyncAiagentsResource) -> None:
        self._aiagents = aiagents

        self.create = async_to_raw_response_wrapper(
            aiagents.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            aiagents.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            aiagents.update,
        )
        self.list = async_to_raw_response_wrapper(
            aiagents.list,
        )
        self.delete = async_to_raw_response_wrapper(
            aiagents.delete,
        )


class AiagentsResourceWithStreamingResponse:
    def __init__(self, aiagents: AiagentsResource) -> None:
        self._aiagents = aiagents

        self.create = to_streamed_response_wrapper(
            aiagents.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            aiagents.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            aiagents.update,
        )
        self.list = to_streamed_response_wrapper(
            aiagents.list,
        )
        self.delete = to_streamed_response_wrapper(
            aiagents.delete,
        )


class AsyncAiagentsResourceWithStreamingResponse:
    def __init__(self, aiagents: AsyncAiagentsResource) -> None:
        self._aiagents = aiagents

        self.create = async_to_streamed_response_wrapper(
            aiagents.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            aiagents.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            aiagents.update,
        )
        self.list = async_to_streamed_response_wrapper(
            aiagents.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            aiagents.delete,
        )

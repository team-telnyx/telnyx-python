# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable

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
from ....types.ai.anthropic import v1_messages_params
from ....types.ai.anthropic.v1_messages_response import V1MessagesResponse

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> V1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return V1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return V1ResourceWithStreamingResponse(self)

    def messages(
        self,
        *,
        max_tokens: int,
        messages: Iterable[Dict[str, object]],
        model: str,
        api_key_ref: str | Omit = omit,
        billing_group_id: str | Omit = omit,
        fallback_config: Dict[str, object] | Omit = omit,
        max_retries: int | Omit = omit,
        mcp_servers: Iterable[Dict[str, object]] | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        service_tier: str | Omit = omit,
        stop_sequences: SequenceNotStr[str] | Omit = omit,
        stream: bool | Omit = omit,
        system: Union[str, Iterable[Dict[str, object]]] | Omit = omit,
        temperature: float | Omit = omit,
        thinking: Dict[str, object] | Omit = omit,
        api_timeout: float | Omit = omit,
        tool_choice: Dict[str, object] | Omit = omit,
        tools: Iterable[Dict[str, object]] | Omit = omit,
        top_k: int | Omit = omit,
        top_p: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1MessagesResponse:
        """Send a message to a language model using the Anthropic Messages API format.

        This
        endpoint is compatible with the
        [Anthropic Messages API](https://docs.anthropic.com/en/api/messages) and may be
        used with the Anthropic JS or Python SDK by setting the base URL to
        `https://api.telnyx.com/v2/ai/anthropic`.

        The endpoint translates Anthropic-format requests into Telnyx's inference
        internals, then translates the response back to the Anthropic message shape.
        Streaming responses use Anthropic SSE event types (`message_start`,
        `content_block_start`, `content_block_delta`, `content_block_stop`,
        `message_delta`, `message_stop`).

        Args:
          max_tokens: The maximum number of tokens to generate in the response.

          messages: The messages to send to the model, following the
              [Anthropic Messages API](https://docs.anthropic.com/en/api/messages) format.

          model: The model to use for generating the response, for example `zai-org/GLM-5.2` or
              another model available from the Telnyx models endpoint.

          api_key_ref: If you are using an external inference provider, this field allows you to pass
              along a reference to your API key. After creating an
              [integration secret](https://developers.telnyx.com/api-reference/integration-secrets/create-a-secret)
              for your API key, pass the secret's `identifier` in this field.

          billing_group_id: The billing group ID to associate with this request.

          fallback_config: Configuration for model fallback behavior when the primary model is unavailable.

          max_retries: Maximum number of retries for the request.

          mcp_servers: List of MCP (Model Context Protocol) servers to make available to the model.

          metadata: An object describing metadata about the request.

          service_tier: Service tier for the request.

          stop_sequences: Custom sequences that will cause the model to stop generating.

          stream: Whether to stream the response as Anthropic-format Server-Sent Events.

          system: System prompt. Can be a string or an array of content blocks following the
              Anthropic API format.

          temperature: Amount of randomness injected into the response. Ranges from 0 to 1.

          thinking: Extended thinking configuration for models that support it. Set `type` to
              `enabled` to turn on extended thinking.

          api_timeout: Request timeout in seconds.

          tool_choice: Controls how the model uses tools, following the Anthropic API format.

          tools: Definitions of tools that the model may use, following the Anthropic API format.

          top_k: Top-k sampling parameter. Only sample from the top K options for each subsequent
              token.

          top_p: Nucleus sampling parameter. Use temperature or top_p, but not both.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/anthropic/v1/messages",
            body=maybe_transform(
                {
                    "max_tokens": max_tokens,
                    "messages": messages,
                    "model": model,
                    "api_key_ref": api_key_ref,
                    "billing_group_id": billing_group_id,
                    "fallback_config": fallback_config,
                    "max_retries": max_retries,
                    "mcp_servers": mcp_servers,
                    "metadata": metadata,
                    "service_tier": service_tier,
                    "stop_sequences": stop_sequences,
                    "stream": stream,
                    "system": system,
                    "temperature": temperature,
                    "thinking": thinking,
                    "api_timeout": api_timeout,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_k": top_k,
                    "top_p": top_p,
                },
                v1_messages_params.V1MessagesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1MessagesResponse,
        )


class AsyncV1Resource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncV1ResourceWithStreamingResponse(self)

    async def messages(
        self,
        *,
        max_tokens: int,
        messages: Iterable[Dict[str, object]],
        model: str,
        api_key_ref: str | Omit = omit,
        billing_group_id: str | Omit = omit,
        fallback_config: Dict[str, object] | Omit = omit,
        max_retries: int | Omit = omit,
        mcp_servers: Iterable[Dict[str, object]] | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        service_tier: str | Omit = omit,
        stop_sequences: SequenceNotStr[str] | Omit = omit,
        stream: bool | Omit = omit,
        system: Union[str, Iterable[Dict[str, object]]] | Omit = omit,
        temperature: float | Omit = omit,
        thinking: Dict[str, object] | Omit = omit,
        api_timeout: float | Omit = omit,
        tool_choice: Dict[str, object] | Omit = omit,
        tools: Iterable[Dict[str, object]] | Omit = omit,
        top_k: int | Omit = omit,
        top_p: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1MessagesResponse:
        """Send a message to a language model using the Anthropic Messages API format.

        This
        endpoint is compatible with the
        [Anthropic Messages API](https://docs.anthropic.com/en/api/messages) and may be
        used with the Anthropic JS or Python SDK by setting the base URL to
        `https://api.telnyx.com/v2/ai/anthropic`.

        The endpoint translates Anthropic-format requests into Telnyx's inference
        internals, then translates the response back to the Anthropic message shape.
        Streaming responses use Anthropic SSE event types (`message_start`,
        `content_block_start`, `content_block_delta`, `content_block_stop`,
        `message_delta`, `message_stop`).

        Args:
          max_tokens: The maximum number of tokens to generate in the response.

          messages: The messages to send to the model, following the
              [Anthropic Messages API](https://docs.anthropic.com/en/api/messages) format.

          model: The model to use for generating the response, for example `zai-org/GLM-5.2` or
              another model available from the Telnyx models endpoint.

          api_key_ref: If you are using an external inference provider, this field allows you to pass
              along a reference to your API key. After creating an
              [integration secret](https://developers.telnyx.com/api-reference/integration-secrets/create-a-secret)
              for your API key, pass the secret's `identifier` in this field.

          billing_group_id: The billing group ID to associate with this request.

          fallback_config: Configuration for model fallback behavior when the primary model is unavailable.

          max_retries: Maximum number of retries for the request.

          mcp_servers: List of MCP (Model Context Protocol) servers to make available to the model.

          metadata: An object describing metadata about the request.

          service_tier: Service tier for the request.

          stop_sequences: Custom sequences that will cause the model to stop generating.

          stream: Whether to stream the response as Anthropic-format Server-Sent Events.

          system: System prompt. Can be a string or an array of content blocks following the
              Anthropic API format.

          temperature: Amount of randomness injected into the response. Ranges from 0 to 1.

          thinking: Extended thinking configuration for models that support it. Set `type` to
              `enabled` to turn on extended thinking.

          api_timeout: Request timeout in seconds.

          tool_choice: Controls how the model uses tools, following the Anthropic API format.

          tools: Definitions of tools that the model may use, following the Anthropic API format.

          top_k: Top-k sampling parameter. Only sample from the top K options for each subsequent
              token.

          top_p: Nucleus sampling parameter. Use temperature or top_p, but not both.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/anthropic/v1/messages",
            body=await async_maybe_transform(
                {
                    "max_tokens": max_tokens,
                    "messages": messages,
                    "model": model,
                    "api_key_ref": api_key_ref,
                    "billing_group_id": billing_group_id,
                    "fallback_config": fallback_config,
                    "max_retries": max_retries,
                    "mcp_servers": mcp_servers,
                    "metadata": metadata,
                    "service_tier": service_tier,
                    "stop_sequences": stop_sequences,
                    "stream": stream,
                    "system": system,
                    "temperature": temperature,
                    "thinking": thinking,
                    "api_timeout": api_timeout,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_k": top_k,
                    "top_p": top_p,
                },
                v1_messages_params.V1MessagesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1MessagesResponse,
        )


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.messages = to_raw_response_wrapper(
            v1.messages,
        )


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.messages = async_to_raw_response_wrapper(
            v1.messages,
        )


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.messages = to_streamed_response_wrapper(
            v1.messages,
        )


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.messages = async_to_streamed_response_wrapper(
            v1.messages,
        )

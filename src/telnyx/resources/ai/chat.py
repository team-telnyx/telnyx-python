# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.ai import chat_create_completion_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.ai.chat_create_completion_response import ChatCreateCompletionResponse

__all__ = ["ChatResource", "AsyncChatResource"]


class ChatResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ChatResourceWithStreamingResponse(self)

    def create_completion(
        self,
        *,
        messages: Iterable[chat_create_completion_params.Message],
        api_key_ref: str | Omit = omit,
        best_of: int | Omit = omit,
        early_stopping: bool | Omit = omit,
        frequency_penalty: float | Omit = omit,
        guided_choice: SequenceNotStr[str] | Omit = omit,
        guided_json: Dict[str, object] | Omit = omit,
        guided_regex: str | Omit = omit,
        length_penalty: float | Omit = omit,
        logprobs: bool | Omit = omit,
        max_tokens: int | Omit = omit,
        min_p: float | Omit = omit,
        model: str | Omit = omit,
        n: float | Omit = omit,
        presence_penalty: float | Omit = omit,
        response_format: chat_create_completion_params.ResponseFormat | Omit = omit,
        stream: bool | Omit = omit,
        temperature: float | Omit = omit,
        tool_choice: Literal["none", "auto", "required"] | Omit = omit,
        tools: Iterable[chat_create_completion_params.Tool] | Omit = omit,
        top_logprobs: int | Omit = omit,
        top_p: float | Omit = omit,
        use_beam_search: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatCreateCompletionResponse:
        """Chat with a language model.

        This endpoint is consistent with the
        [OpenAI Chat Completions API](https://platform.openai.com/docs/api-reference/chat)
        and may be used with the OpenAI JS or Python SDK.

        Args:
          messages: A list of the previous chat messages for context.

          api_key_ref: If you are using an external inference provider like xAI or OpenAI, this field
              allows you to pass along a reference to your API key. After creating an
              [integration secret](https://developers.telnyx.com/api-reference/integration-secrets/create-a-secret)
              for you API key, pass the secret's `identifier` in this field.

          best_of: This is used with `use_beam_search` to determine how many candidate beams to
              explore.

          early_stopping: This is used with `use_beam_search`. If `true`, generation stops as soon as
              there are `best_of` complete candidates; if `false`, a heuristic is applied and
              the generation stops when is it very unlikely to find better candidates.

          frequency_penalty: Higher values will penalize the model from repeating the same output tokens.

          guided_choice: If specified, the output will be exactly one of the choices.

          guided_json: Must be a valid JSON schema. If specified, the output will follow the JSON
              schema.

          guided_regex: If specified, the output will follow the regex pattern.

          length_penalty: This is used with `use_beam_search` to prefer shorter or longer completions.

          logprobs: Whether to return log probabilities of the output tokens or not. If true,
              returns the log probabilities of each output token returned in the `content` of
              `message`.

          max_tokens: Maximum number of completion tokens the model should generate.

          min_p: This is an alternative to `top_p` that
              [many prefer](https://github.com/huggingface/transformers/issues/27670). Must be
              in [0, 1].

          model: The language model to chat with.

          n: This will return multiple choices for you instead of a single chat completion.

          presence_penalty: Higher values will penalize the model from repeating the same output tokens.

          response_format: Use this is you want to guarantee a JSON output without defining a schema. For
              control over the schema, use `guided_json`.

          stream: Whether or not to stream data-only server-sent events as they become available.

          temperature: Adjusts the "creativity" of the model. Lower values make the model more
              deterministic and repetitive, while higher values make the model more random and
              creative.

          tools: The `function` tool type follows the same schema as the
              [OpenAI Chat Completions API](https://platform.openai.com/docs/api-reference/chat).
              The `retrieval` tool type is unique to Telnyx. You may pass a list of
              [embedded storage buckets](https://developers.telnyx.com/api-reference/embeddings/embed-documents)
              for retrieval-augmented generation.

          top_logprobs: This is used with `logprobs`. An integer between 0 and 20 specifying the number
              of most likely tokens to return at each token position, each with an associated
              log probability.

          top_p: An alternative or complement to `temperature`. This adjusts how many of the top
              possibilities to consider.

          use_beam_search: Setting this to `true` will allow the model to
              [explore more completion options](https://huggingface.co/blog/how-to-generate#beam-search).
              This is not supported by OpenAI.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/chat/completions",
            body=maybe_transform(
                {
                    "messages": messages,
                    "api_key_ref": api_key_ref,
                    "best_of": best_of,
                    "early_stopping": early_stopping,
                    "frequency_penalty": frequency_penalty,
                    "guided_choice": guided_choice,
                    "guided_json": guided_json,
                    "guided_regex": guided_regex,
                    "length_penalty": length_penalty,
                    "logprobs": logprobs,
                    "max_tokens": max_tokens,
                    "min_p": min_p,
                    "model": model,
                    "n": n,
                    "presence_penalty": presence_penalty,
                    "response_format": response_format,
                    "stream": stream,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_logprobs": top_logprobs,
                    "top_p": top_p,
                    "use_beam_search": use_beam_search,
                },
                chat_create_completion_params.ChatCreateCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCreateCompletionResponse,
        )


class AsyncChatResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncChatResourceWithStreamingResponse(self)

    async def create_completion(
        self,
        *,
        messages: Iterable[chat_create_completion_params.Message],
        api_key_ref: str | Omit = omit,
        best_of: int | Omit = omit,
        early_stopping: bool | Omit = omit,
        frequency_penalty: float | Omit = omit,
        guided_choice: SequenceNotStr[str] | Omit = omit,
        guided_json: Dict[str, object] | Omit = omit,
        guided_regex: str | Omit = omit,
        length_penalty: float | Omit = omit,
        logprobs: bool | Omit = omit,
        max_tokens: int | Omit = omit,
        min_p: float | Omit = omit,
        model: str | Omit = omit,
        n: float | Omit = omit,
        presence_penalty: float | Omit = omit,
        response_format: chat_create_completion_params.ResponseFormat | Omit = omit,
        stream: bool | Omit = omit,
        temperature: float | Omit = omit,
        tool_choice: Literal["none", "auto", "required"] | Omit = omit,
        tools: Iterable[chat_create_completion_params.Tool] | Omit = omit,
        top_logprobs: int | Omit = omit,
        top_p: float | Omit = omit,
        use_beam_search: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatCreateCompletionResponse:
        """Chat with a language model.

        This endpoint is consistent with the
        [OpenAI Chat Completions API](https://platform.openai.com/docs/api-reference/chat)
        and may be used with the OpenAI JS or Python SDK.

        Args:
          messages: A list of the previous chat messages for context.

          api_key_ref: If you are using an external inference provider like xAI or OpenAI, this field
              allows you to pass along a reference to your API key. After creating an
              [integration secret](https://developers.telnyx.com/api-reference/integration-secrets/create-a-secret)
              for you API key, pass the secret's `identifier` in this field.

          best_of: This is used with `use_beam_search` to determine how many candidate beams to
              explore.

          early_stopping: This is used with `use_beam_search`. If `true`, generation stops as soon as
              there are `best_of` complete candidates; if `false`, a heuristic is applied and
              the generation stops when is it very unlikely to find better candidates.

          frequency_penalty: Higher values will penalize the model from repeating the same output tokens.

          guided_choice: If specified, the output will be exactly one of the choices.

          guided_json: Must be a valid JSON schema. If specified, the output will follow the JSON
              schema.

          guided_regex: If specified, the output will follow the regex pattern.

          length_penalty: This is used with `use_beam_search` to prefer shorter or longer completions.

          logprobs: Whether to return log probabilities of the output tokens or not. If true,
              returns the log probabilities of each output token returned in the `content` of
              `message`.

          max_tokens: Maximum number of completion tokens the model should generate.

          min_p: This is an alternative to `top_p` that
              [many prefer](https://github.com/huggingface/transformers/issues/27670). Must be
              in [0, 1].

          model: The language model to chat with.

          n: This will return multiple choices for you instead of a single chat completion.

          presence_penalty: Higher values will penalize the model from repeating the same output tokens.

          response_format: Use this is you want to guarantee a JSON output without defining a schema. For
              control over the schema, use `guided_json`.

          stream: Whether or not to stream data-only server-sent events as they become available.

          temperature: Adjusts the "creativity" of the model. Lower values make the model more
              deterministic and repetitive, while higher values make the model more random and
              creative.

          tools: The `function` tool type follows the same schema as the
              [OpenAI Chat Completions API](https://platform.openai.com/docs/api-reference/chat).
              The `retrieval` tool type is unique to Telnyx. You may pass a list of
              [embedded storage buckets](https://developers.telnyx.com/api-reference/embeddings/embed-documents)
              for retrieval-augmented generation.

          top_logprobs: This is used with `logprobs`. An integer between 0 and 20 specifying the number
              of most likely tokens to return at each token position, each with an associated
              log probability.

          top_p: An alternative or complement to `temperature`. This adjusts how many of the top
              possibilities to consider.

          use_beam_search: Setting this to `true` will allow the model to
              [explore more completion options](https://huggingface.co/blog/how-to-generate#beam-search).
              This is not supported by OpenAI.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/chat/completions",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "api_key_ref": api_key_ref,
                    "best_of": best_of,
                    "early_stopping": early_stopping,
                    "frequency_penalty": frequency_penalty,
                    "guided_choice": guided_choice,
                    "guided_json": guided_json,
                    "guided_regex": guided_regex,
                    "length_penalty": length_penalty,
                    "logprobs": logprobs,
                    "max_tokens": max_tokens,
                    "min_p": min_p,
                    "model": model,
                    "n": n,
                    "presence_penalty": presence_penalty,
                    "response_format": response_format,
                    "stream": stream,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_logprobs": top_logprobs,
                    "top_p": top_p,
                    "use_beam_search": use_beam_search,
                },
                chat_create_completion_params.ChatCreateCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCreateCompletionResponse,
        )


class ChatResourceWithRawResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.create_completion = to_raw_response_wrapper(
            chat.create_completion,
        )


class AsyncChatResourceWithRawResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.create_completion = async_to_raw_response_wrapper(
            chat.create_completion,
        )


class ChatResourceWithStreamingResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.create_completion = to_streamed_response_wrapper(
            chat.create_completion,
        )


class AsyncChatResourceWithStreamingResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.create_completion = async_to_streamed_response_wrapper(
            chat.create_completion,
        )

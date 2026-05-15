# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from .chat import (
    ChatResource,
    AsyncChatResource,
    ChatResourceWithRawResponse,
    AsyncChatResourceWithRawResponse,
    ChatResourceWithStreamingResponse,
    AsyncChatResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from .embeddings import (
    EmbeddingsResource,
    AsyncEmbeddingsResource,
    EmbeddingsResourceWithRawResponse,
    AsyncEmbeddingsResourceWithRawResponse,
    EmbeddingsResourceWithStreamingResponse,
    AsyncEmbeddingsResourceWithStreamingResponse,
)
from ....types.ai import openai_create_response_params
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.ai.openai_list_models_response import OpenAIListModelsResponse
from ....types.ai.openai_create_response_response import OpenAICreateResponseResponse

__all__ = ["OpenAIResource", "AsyncOpenAIResource"]


class OpenAIResource(SyncAPIResource):
    @cached_property
    def embeddings(self) -> EmbeddingsResource:
        """
        OpenAI-compatible embeddings endpoints for generating vector representations of text
        """
        return EmbeddingsResource(self._client)

    @cached_property
    def chat(self) -> ChatResource:
        return ChatResource(self._client)

    @cached_property
    def with_raw_response(self) -> OpenAIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return OpenAIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OpenAIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return OpenAIResourceWithStreamingResponse(self)

    def create_response(
        self,
        *,
        conversation: str | Omit = omit,
        input: Dict[str, object] | Omit = omit,
        instructions: str | Omit = omit,
        model: str | Omit = omit,
        stream: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OpenAICreateResponseResponse:
        """Create a response using Telnyx's OpenAI-compatible Responses API.

        This endpoint
        is compatible with the
        [OpenAI Responses API](https://developers.openai.com/api/reference/responses/overview)
        and may be used with the OpenAI JS or Python SDK by setting the base URL to
        `https://api.telnyx.com/v2/ai/openai`.

        The `conversation` parameter refers to a Telnyx Conversation rather than an
        OpenAI-hosted conversation object. To persist a thread across turns, first
        [create a conversation](https://developers.telnyx.com/api-reference/conversations/create-a-conversation)
        with `POST /ai/conversations`, then pass that conversation's `id` in the
        Responses request as `conversation`. The endpoint appends the new input,
        assistant output, reasoning, and tool-call messages to that conversation. Reuse
        the same `conversation` id on subsequent Responses requests, including
        tool-result followups, so the model receives the prior context.

        If `conversation` is omitted, the request is processed without persisting
        messages to a Telnyx conversation. Use the Conversations API to manage history:
        [list conversations](https://developers.telnyx.com/api-reference/conversations/list-conversations)
        (optionally filtered by metadata),
        [fetch messages](https://developers.telnyx.com/api-reference/conversations/get-conversation-messages)
        for a conversation, and optionally
        [add messages](https://developers.telnyx.com/api-reference/conversations/create-message)
        outside the Responses flow.

        You can attach arbitrary metadata when creating a conversation (for example to
        tag the conversation's source, channel, or user) and later filter by it when
        listing conversations.

        Args:
          conversation: Optional Telnyx Conversation ID from `POST /ai/conversations`. When provided,
              Telnyx stores this turn on that conversation and uses the conversation's prior
              messages as context. Reuse the same ID for subsequent turns and tool-result
              followups. Omit it for a non-persisted, stateless response.

          input: The input items for this turn, using the OpenAI Responses API input format.

          instructions: Optional system/developer instructions for the model. When used with a persisted
              `conversation`, send these on the first request that creates the thread;
              subsequent turns can rely on the stored history.

          model: Model identifier to use for the response, for example `zai-org/GLM-5.1-FP8` or
              another model available from the Telnyx OpenAI-compatible models endpoint.

          stream: Set to `true` to stream Server-Sent Events, matching OpenAI's Responses
              streaming format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/openai/responses",
            body=maybe_transform(
                {
                    "conversation": conversation,
                    "input": input,
                    "instructions": instructions,
                    "model": model,
                    "stream": stream,
                },
                openai_create_response_params.OpenAICreateResponseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OpenAICreateResponseResponse,
        )

    def list_models(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OpenAIListModelsResponse:
        """
        Lists every model currently available to your account on Telnyx Inference,
        including SOTA open-source LLMs hosted on Telnyx GPUs (for example
        `moonshotai/Kimi-K2.6`, `zai-org/GLM-5.1-FP8`, and `MiniMaxAI/MiniMax-M2.7`),
        embedding models, and any fine-tuned models you have created.

        Each entry is a `ModelMetadata` object describing the model id, owner, task,
        context length, supported languages, billing tier, pricing per 1M tokens,
        deployment regions, and whether the model supports vision or fine-tuning. Use
        this endpoint to discover model ids you can pass to
        `POST /v2/ai/openai/chat/completions`.

        Model ids follow the `{organization}/{model_name}` convention from Hugging Face
        (for example `moonshotai/Kimi-K2.6`). This endpoint is OpenAI-compatible:
        clients pointed at `https://api.telnyx.com/v2/ai/openai` can call
        `client.models.list()` to retrieve the same payload.
        """
        return self._get(
            "/ai/openai/models",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OpenAIListModelsResponse,
        )


class AsyncOpenAIResource(AsyncAPIResource):
    @cached_property
    def embeddings(self) -> AsyncEmbeddingsResource:
        """
        OpenAI-compatible embeddings endpoints for generating vector representations of text
        """
        return AsyncEmbeddingsResource(self._client)

    @cached_property
    def chat(self) -> AsyncChatResource:
        return AsyncChatResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOpenAIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOpenAIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOpenAIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncOpenAIResourceWithStreamingResponse(self)

    async def create_response(
        self,
        *,
        conversation: str | Omit = omit,
        input: Dict[str, object] | Omit = omit,
        instructions: str | Omit = omit,
        model: str | Omit = omit,
        stream: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OpenAICreateResponseResponse:
        """Create a response using Telnyx's OpenAI-compatible Responses API.

        This endpoint
        is compatible with the
        [OpenAI Responses API](https://developers.openai.com/api/reference/responses/overview)
        and may be used with the OpenAI JS or Python SDK by setting the base URL to
        `https://api.telnyx.com/v2/ai/openai`.

        The `conversation` parameter refers to a Telnyx Conversation rather than an
        OpenAI-hosted conversation object. To persist a thread across turns, first
        [create a conversation](https://developers.telnyx.com/api-reference/conversations/create-a-conversation)
        with `POST /ai/conversations`, then pass that conversation's `id` in the
        Responses request as `conversation`. The endpoint appends the new input,
        assistant output, reasoning, and tool-call messages to that conversation. Reuse
        the same `conversation` id on subsequent Responses requests, including
        tool-result followups, so the model receives the prior context.

        If `conversation` is omitted, the request is processed without persisting
        messages to a Telnyx conversation. Use the Conversations API to manage history:
        [list conversations](https://developers.telnyx.com/api-reference/conversations/list-conversations)
        (optionally filtered by metadata),
        [fetch messages](https://developers.telnyx.com/api-reference/conversations/get-conversation-messages)
        for a conversation, and optionally
        [add messages](https://developers.telnyx.com/api-reference/conversations/create-message)
        outside the Responses flow.

        You can attach arbitrary metadata when creating a conversation (for example to
        tag the conversation's source, channel, or user) and later filter by it when
        listing conversations.

        Args:
          conversation: Optional Telnyx Conversation ID from `POST /ai/conversations`. When provided,
              Telnyx stores this turn on that conversation and uses the conversation's prior
              messages as context. Reuse the same ID for subsequent turns and tool-result
              followups. Omit it for a non-persisted, stateless response.

          input: The input items for this turn, using the OpenAI Responses API input format.

          instructions: Optional system/developer instructions for the model. When used with a persisted
              `conversation`, send these on the first request that creates the thread;
              subsequent turns can rely on the stored history.

          model: Model identifier to use for the response, for example `zai-org/GLM-5.1-FP8` or
              another model available from the Telnyx OpenAI-compatible models endpoint.

          stream: Set to `true` to stream Server-Sent Events, matching OpenAI's Responses
              streaming format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/openai/responses",
            body=await async_maybe_transform(
                {
                    "conversation": conversation,
                    "input": input,
                    "instructions": instructions,
                    "model": model,
                    "stream": stream,
                },
                openai_create_response_params.OpenAICreateResponseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OpenAICreateResponseResponse,
        )

    async def list_models(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OpenAIListModelsResponse:
        """
        Lists every model currently available to your account on Telnyx Inference,
        including SOTA open-source LLMs hosted on Telnyx GPUs (for example
        `moonshotai/Kimi-K2.6`, `zai-org/GLM-5.1-FP8`, and `MiniMaxAI/MiniMax-M2.7`),
        embedding models, and any fine-tuned models you have created.

        Each entry is a `ModelMetadata` object describing the model id, owner, task,
        context length, supported languages, billing tier, pricing per 1M tokens,
        deployment regions, and whether the model supports vision or fine-tuning. Use
        this endpoint to discover model ids you can pass to
        `POST /v2/ai/openai/chat/completions`.

        Model ids follow the `{organization}/{model_name}` convention from Hugging Face
        (for example `moonshotai/Kimi-K2.6`). This endpoint is OpenAI-compatible:
        clients pointed at `https://api.telnyx.com/v2/ai/openai` can call
        `client.models.list()` to retrieve the same payload.
        """
        return await self._get(
            "/ai/openai/models",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OpenAIListModelsResponse,
        )


class OpenAIResourceWithRawResponse:
    def __init__(self, openai: OpenAIResource) -> None:
        self._openai = openai

        self.create_response = to_raw_response_wrapper(
            openai.create_response,
        )
        self.list_models = to_raw_response_wrapper(
            openai.list_models,
        )

    @cached_property
    def embeddings(self) -> EmbeddingsResourceWithRawResponse:
        """
        OpenAI-compatible embeddings endpoints for generating vector representations of text
        """
        return EmbeddingsResourceWithRawResponse(self._openai.embeddings)

    @cached_property
    def chat(self) -> ChatResourceWithRawResponse:
        return ChatResourceWithRawResponse(self._openai.chat)


class AsyncOpenAIResourceWithRawResponse:
    def __init__(self, openai: AsyncOpenAIResource) -> None:
        self._openai = openai

        self.create_response = async_to_raw_response_wrapper(
            openai.create_response,
        )
        self.list_models = async_to_raw_response_wrapper(
            openai.list_models,
        )

    @cached_property
    def embeddings(self) -> AsyncEmbeddingsResourceWithRawResponse:
        """
        OpenAI-compatible embeddings endpoints for generating vector representations of text
        """
        return AsyncEmbeddingsResourceWithRawResponse(self._openai.embeddings)

    @cached_property
    def chat(self) -> AsyncChatResourceWithRawResponse:
        return AsyncChatResourceWithRawResponse(self._openai.chat)


class OpenAIResourceWithStreamingResponse:
    def __init__(self, openai: OpenAIResource) -> None:
        self._openai = openai

        self.create_response = to_streamed_response_wrapper(
            openai.create_response,
        )
        self.list_models = to_streamed_response_wrapper(
            openai.list_models,
        )

    @cached_property
    def embeddings(self) -> EmbeddingsResourceWithStreamingResponse:
        """
        OpenAI-compatible embeddings endpoints for generating vector representations of text
        """
        return EmbeddingsResourceWithStreamingResponse(self._openai.embeddings)

    @cached_property
    def chat(self) -> ChatResourceWithStreamingResponse:
        return ChatResourceWithStreamingResponse(self._openai.chat)


class AsyncOpenAIResourceWithStreamingResponse:
    def __init__(self, openai: AsyncOpenAIResource) -> None:
        self._openai = openai

        self.create_response = async_to_streamed_response_wrapper(
            openai.create_response,
        )
        self.list_models = async_to_streamed_response_wrapper(
            openai.list_models,
        )

    @cached_property
    def embeddings(self) -> AsyncEmbeddingsResourceWithStreamingResponse:
        """
        OpenAI-compatible embeddings endpoints for generating vector representations of text
        """
        return AsyncEmbeddingsResourceWithStreamingResponse(self._openai.embeddings)

    @cached_property
    def chat(self) -> AsyncChatResourceWithStreamingResponse:
        return AsyncChatResourceWithStreamingResponse(self._openai.chat)

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
from ...._types import Body, Query, Headers, NotGiven, not_given
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
        body: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OpenAICreateResponseResponse:
        """Chat with a language model.

        This endpoint is consistent with the
        [OpenAI Chat Completions API](https://developers.openai.com/api/reference/resources/responses)
        and may be used with the OpenAI JS or Python SDK. Response id parameter is not
        supported at the moment. Use 'conversation' parameter to leverage persistent
        conversations feature.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/openai/responses",
            body=maybe_transform(body, openai_create_response_params.OpenAICreateResponseParams),
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
        body: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OpenAICreateResponseResponse:
        """Chat with a language model.

        This endpoint is consistent with the
        [OpenAI Chat Completions API](https://developers.openai.com/api/reference/resources/responses)
        and may be used with the OpenAI JS or Python SDK. Response id parameter is not
        supported at the moment. Use 'conversation' parameter to leverage persistent
        conversations feature.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/openai/responses",
            body=await async_maybe_transform(body, openai_create_response_params.OpenAICreateResponseParams),
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

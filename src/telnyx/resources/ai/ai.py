# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .chat import (
    ChatResource,
    AsyncChatResource,
    ChatResourceWithRawResponse,
    AsyncChatResourceWithRawResponse,
    ChatResourceWithStreamingResponse,
    AsyncChatResourceWithStreamingResponse,
)
from .audio import (
    AudioResource,
    AsyncAudioResource,
    AudioResourceWithRawResponse,
    AsyncAudioResourceWithRawResponse,
    AudioResourceWithStreamingResponse,
    AsyncAudioResourceWithStreamingResponse,
)
from ...types import ai_summarize_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from .clusters import (
    ClustersResource,
    AsyncClustersResource,
    ClustersResourceWithRawResponse,
    AsyncClustersResourceWithRawResponse,
    ClustersResourceWithStreamingResponse,
    AsyncClustersResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .assistants.assistants import (
    AssistantsResource,
    AsyncAssistantsResource,
    AssistantsResourceWithRawResponse,
    AsyncAssistantsResourceWithRawResponse,
    AssistantsResourceWithStreamingResponse,
    AsyncAssistantsResourceWithStreamingResponse,
)
from .embeddings.embeddings import (
    EmbeddingsResource,
    AsyncEmbeddingsResource,
    EmbeddingsResourceWithRawResponse,
    AsyncEmbeddingsResourceWithRawResponse,
    EmbeddingsResourceWithStreamingResponse,
    AsyncEmbeddingsResourceWithStreamingResponse,
)
from .fine_tuning.fine_tuning import (
    FineTuningResource,
    AsyncFineTuningResource,
    FineTuningResourceWithRawResponse,
    AsyncFineTuningResourceWithRawResponse,
    FineTuningResourceWithStreamingResponse,
    AsyncFineTuningResourceWithStreamingResponse,
)
from .conversations.conversations import (
    ConversationsResource,
    AsyncConversationsResource,
    ConversationsResourceWithRawResponse,
    AsyncConversationsResourceWithRawResponse,
    ConversationsResourceWithStreamingResponse,
    AsyncConversationsResourceWithStreamingResponse,
)
from ...types.ai_summarize_response import AISummarizeResponse
from ...types.ai_retrieve_models_response import AIRetrieveModelsResponse

__all__ = ["AIResource", "AsyncAIResource"]


class AIResource(SyncAPIResource):
    @cached_property
    def assistants(self) -> AssistantsResource:
        return AssistantsResource(self._client)

    @cached_property
    def audio(self) -> AudioResource:
        return AudioResource(self._client)

    @cached_property
    def chat(self) -> ChatResource:
        return ChatResource(self._client)

    @cached_property
    def clusters(self) -> ClustersResource:
        return ClustersResource(self._client)

    @cached_property
    def conversations(self) -> ConversationsResource:
        return ConversationsResource(self._client)

    @cached_property
    def embeddings(self) -> EmbeddingsResource:
        return EmbeddingsResource(self._client)

    @cached_property
    def fine_tuning(self) -> FineTuningResource:
        return FineTuningResource(self._client)

    @cached_property
    def with_raw_response(self) -> AIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AIResourceWithStreamingResponse(self)

    def retrieve_models(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AIRetrieveModelsResponse:
        """
        This endpoint returns a list of Open Source and OpenAI models that are available
        for use. <br /><br /> **Note**: Model `id`'s will be in the form
        `{source}/{model_name}`. For example `openai/gpt-4` or
        `mistralai/Mistral-7B-Instruct-v0.1` consistent with HuggingFace naming
        conventions.
        """
        return self._get(
            "/ai/models",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AIRetrieveModelsResponse,
        )

    def summarize(
        self,
        *,
        bucket: str,
        filename: str,
        system_prompt: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AISummarizeResponse:
        """
        Generate a summary of a file's contents.

        Supports the following text formats:

        - PDF, HTML, txt, json, csv

        Supports the following media formats (billed for both the transcription and
        summary):

        - flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm
        - Up to 100 MB

        Args:
          bucket: The name of the bucket that contains the file to be summarized.

          filename: The name of the file to be summarized.

          system_prompt: A system prompt to guide the summary generation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/summarize",
            body=maybe_transform(
                {
                    "bucket": bucket,
                    "filename": filename,
                    "system_prompt": system_prompt,
                },
                ai_summarize_params.AISummarizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AISummarizeResponse,
        )


class AsyncAIResource(AsyncAPIResource):
    @cached_property
    def assistants(self) -> AsyncAssistantsResource:
        return AsyncAssistantsResource(self._client)

    @cached_property
    def audio(self) -> AsyncAudioResource:
        return AsyncAudioResource(self._client)

    @cached_property
    def chat(self) -> AsyncChatResource:
        return AsyncChatResource(self._client)

    @cached_property
    def clusters(self) -> AsyncClustersResource:
        return AsyncClustersResource(self._client)

    @cached_property
    def conversations(self) -> AsyncConversationsResource:
        return AsyncConversationsResource(self._client)

    @cached_property
    def embeddings(self) -> AsyncEmbeddingsResource:
        return AsyncEmbeddingsResource(self._client)

    @cached_property
    def fine_tuning(self) -> AsyncFineTuningResource:
        return AsyncFineTuningResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncAIResourceWithStreamingResponse(self)

    async def retrieve_models(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AIRetrieveModelsResponse:
        """
        This endpoint returns a list of Open Source and OpenAI models that are available
        for use. <br /><br /> **Note**: Model `id`'s will be in the form
        `{source}/{model_name}`. For example `openai/gpt-4` or
        `mistralai/Mistral-7B-Instruct-v0.1` consistent with HuggingFace naming
        conventions.
        """
        return await self._get(
            "/ai/models",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AIRetrieveModelsResponse,
        )

    async def summarize(
        self,
        *,
        bucket: str,
        filename: str,
        system_prompt: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AISummarizeResponse:
        """
        Generate a summary of a file's contents.

        Supports the following text formats:

        - PDF, HTML, txt, json, csv

        Supports the following media formats (billed for both the transcription and
        summary):

        - flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm
        - Up to 100 MB

        Args:
          bucket: The name of the bucket that contains the file to be summarized.

          filename: The name of the file to be summarized.

          system_prompt: A system prompt to guide the summary generation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/summarize",
            body=await async_maybe_transform(
                {
                    "bucket": bucket,
                    "filename": filename,
                    "system_prompt": system_prompt,
                },
                ai_summarize_params.AISummarizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AISummarizeResponse,
        )


class AIResourceWithRawResponse:
    def __init__(self, ai: AIResource) -> None:
        self._ai = ai

        self.retrieve_models = to_raw_response_wrapper(
            ai.retrieve_models,
        )
        self.summarize = to_raw_response_wrapper(
            ai.summarize,
        )

    @cached_property
    def assistants(self) -> AssistantsResourceWithRawResponse:
        return AssistantsResourceWithRawResponse(self._ai.assistants)

    @cached_property
    def audio(self) -> AudioResourceWithRawResponse:
        return AudioResourceWithRawResponse(self._ai.audio)

    @cached_property
    def chat(self) -> ChatResourceWithRawResponse:
        return ChatResourceWithRawResponse(self._ai.chat)

    @cached_property
    def clusters(self) -> ClustersResourceWithRawResponse:
        return ClustersResourceWithRawResponse(self._ai.clusters)

    @cached_property
    def conversations(self) -> ConversationsResourceWithRawResponse:
        return ConversationsResourceWithRawResponse(self._ai.conversations)

    @cached_property
    def embeddings(self) -> EmbeddingsResourceWithRawResponse:
        return EmbeddingsResourceWithRawResponse(self._ai.embeddings)

    @cached_property
    def fine_tuning(self) -> FineTuningResourceWithRawResponse:
        return FineTuningResourceWithRawResponse(self._ai.fine_tuning)


class AsyncAIResourceWithRawResponse:
    def __init__(self, ai: AsyncAIResource) -> None:
        self._ai = ai

        self.retrieve_models = async_to_raw_response_wrapper(
            ai.retrieve_models,
        )
        self.summarize = async_to_raw_response_wrapper(
            ai.summarize,
        )

    @cached_property
    def assistants(self) -> AsyncAssistantsResourceWithRawResponse:
        return AsyncAssistantsResourceWithRawResponse(self._ai.assistants)

    @cached_property
    def audio(self) -> AsyncAudioResourceWithRawResponse:
        return AsyncAudioResourceWithRawResponse(self._ai.audio)

    @cached_property
    def chat(self) -> AsyncChatResourceWithRawResponse:
        return AsyncChatResourceWithRawResponse(self._ai.chat)

    @cached_property
    def clusters(self) -> AsyncClustersResourceWithRawResponse:
        return AsyncClustersResourceWithRawResponse(self._ai.clusters)

    @cached_property
    def conversations(self) -> AsyncConversationsResourceWithRawResponse:
        return AsyncConversationsResourceWithRawResponse(self._ai.conversations)

    @cached_property
    def embeddings(self) -> AsyncEmbeddingsResourceWithRawResponse:
        return AsyncEmbeddingsResourceWithRawResponse(self._ai.embeddings)

    @cached_property
    def fine_tuning(self) -> AsyncFineTuningResourceWithRawResponse:
        return AsyncFineTuningResourceWithRawResponse(self._ai.fine_tuning)


class AIResourceWithStreamingResponse:
    def __init__(self, ai: AIResource) -> None:
        self._ai = ai

        self.retrieve_models = to_streamed_response_wrapper(
            ai.retrieve_models,
        )
        self.summarize = to_streamed_response_wrapper(
            ai.summarize,
        )

    @cached_property
    def assistants(self) -> AssistantsResourceWithStreamingResponse:
        return AssistantsResourceWithStreamingResponse(self._ai.assistants)

    @cached_property
    def audio(self) -> AudioResourceWithStreamingResponse:
        return AudioResourceWithStreamingResponse(self._ai.audio)

    @cached_property
    def chat(self) -> ChatResourceWithStreamingResponse:
        return ChatResourceWithStreamingResponse(self._ai.chat)

    @cached_property
    def clusters(self) -> ClustersResourceWithStreamingResponse:
        return ClustersResourceWithStreamingResponse(self._ai.clusters)

    @cached_property
    def conversations(self) -> ConversationsResourceWithStreamingResponse:
        return ConversationsResourceWithStreamingResponse(self._ai.conversations)

    @cached_property
    def embeddings(self) -> EmbeddingsResourceWithStreamingResponse:
        return EmbeddingsResourceWithStreamingResponse(self._ai.embeddings)

    @cached_property
    def fine_tuning(self) -> FineTuningResourceWithStreamingResponse:
        return FineTuningResourceWithStreamingResponse(self._ai.fine_tuning)


class AsyncAIResourceWithStreamingResponse:
    def __init__(self, ai: AsyncAIResource) -> None:
        self._ai = ai

        self.retrieve_models = async_to_streamed_response_wrapper(
            ai.retrieve_models,
        )
        self.summarize = async_to_streamed_response_wrapper(
            ai.summarize,
        )

    @cached_property
    def assistants(self) -> AsyncAssistantsResourceWithStreamingResponse:
        return AsyncAssistantsResourceWithStreamingResponse(self._ai.assistants)

    @cached_property
    def audio(self) -> AsyncAudioResourceWithStreamingResponse:
        return AsyncAudioResourceWithStreamingResponse(self._ai.audio)

    @cached_property
    def chat(self) -> AsyncChatResourceWithStreamingResponse:
        return AsyncChatResourceWithStreamingResponse(self._ai.chat)

    @cached_property
    def clusters(self) -> AsyncClustersResourceWithStreamingResponse:
        return AsyncClustersResourceWithStreamingResponse(self._ai.clusters)

    @cached_property
    def conversations(self) -> AsyncConversationsResourceWithStreamingResponse:
        return AsyncConversationsResourceWithStreamingResponse(self._ai.conversations)

    @cached_property
    def embeddings(self) -> AsyncEmbeddingsResourceWithStreamingResponse:
        return AsyncEmbeddingsResourceWithStreamingResponse(self._ai.embeddings)

    @cached_property
    def fine_tuning(self) -> AsyncFineTuningResourceWithStreamingResponse:
        return AsyncFineTuningResourceWithStreamingResponse(self._ai.fine_tuning)

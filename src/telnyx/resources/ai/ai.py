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
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from .mcp_servers import (
    McpServersResource,
    AsyncMcpServersResource,
    McpServersResourceWithRawResponse,
    AsyncMcpServersResourceWithRawResponse,
    McpServersResourceWithStreamingResponse,
    AsyncMcpServersResourceWithStreamingResponse,
)
from .openai.openai import (
    OpenAIResource,
    AsyncOpenAIResource,
    OpenAIResourceWithRawResponse,
    AsyncOpenAIResourceWithRawResponse,
    OpenAIResourceWithStreamingResponse,
    AsyncOpenAIResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from .missions.missions import (
    MissionsResource,
    AsyncMissionsResource,
    MissionsResourceWithRawResponse,
    AsyncMissionsResourceWithRawResponse,
    MissionsResourceWithStreamingResponse,
    AsyncMissionsResourceWithStreamingResponse,
)
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
from .integrations.integrations import (
    IntegrationsResource,
    AsyncIntegrationsResource,
    IntegrationsResourceWithRawResponse,
    AsyncIntegrationsResourceWithRawResponse,
    IntegrationsResourceWithStreamingResponse,
    AsyncIntegrationsResourceWithStreamingResponse,
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
    """Generate text with LLMs"""

    @cached_property
    def assistants(self) -> AssistantsResource:
        """Configure AI assistant specifications"""
        return AssistantsResource(self._client)

    @cached_property
    def audio(self) -> AudioResource:
        """Turn audio into text or text into audio."""
        return AudioResource(self._client)

    @cached_property
    def chat(self) -> ChatResource:
        """Generate text with LLMs"""
        return ChatResource(self._client)

    @cached_property
    def clusters(self) -> ClustersResource:
        """Identify common themes and patterns in your embedded documents"""
        return ClustersResource(self._client)

    @cached_property
    def conversations(self) -> ConversationsResource:
        """Manage historical AI assistant conversations"""
        return ConversationsResource(self._client)

    @cached_property
    def embeddings(self) -> EmbeddingsResource:
        """Embed documents and perform text searches"""
        return EmbeddingsResource(self._client)

    @cached_property
    def fine_tuning(self) -> FineTuningResource:
        return FineTuningResource(self._client)

    @cached_property
    def integrations(self) -> IntegrationsResource:
        return IntegrationsResource(self._client)

    @cached_property
    def mcp_servers(self) -> McpServersResource:
        return McpServersResource(self._client)

    @cached_property
    def missions(self) -> MissionsResource:
        return MissionsResource(self._client)

    @cached_property
    def openai(self) -> OpenAIResource:
        return OpenAIResource(self._client)

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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        system_prompt: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
    """Generate text with LLMs"""

    @cached_property
    def assistants(self) -> AsyncAssistantsResource:
        """Configure AI assistant specifications"""
        return AsyncAssistantsResource(self._client)

    @cached_property
    def audio(self) -> AsyncAudioResource:
        """Turn audio into text or text into audio."""
        return AsyncAudioResource(self._client)

    @cached_property
    def chat(self) -> AsyncChatResource:
        """Generate text with LLMs"""
        return AsyncChatResource(self._client)

    @cached_property
    def clusters(self) -> AsyncClustersResource:
        """Identify common themes and patterns in your embedded documents"""
        return AsyncClustersResource(self._client)

    @cached_property
    def conversations(self) -> AsyncConversationsResource:
        """Manage historical AI assistant conversations"""
        return AsyncConversationsResource(self._client)

    @cached_property
    def embeddings(self) -> AsyncEmbeddingsResource:
        """Embed documents and perform text searches"""
        return AsyncEmbeddingsResource(self._client)

    @cached_property
    def fine_tuning(self) -> AsyncFineTuningResource:
        return AsyncFineTuningResource(self._client)

    @cached_property
    def integrations(self) -> AsyncIntegrationsResource:
        return AsyncIntegrationsResource(self._client)

    @cached_property
    def mcp_servers(self) -> AsyncMcpServersResource:
        return AsyncMcpServersResource(self._client)

    @cached_property
    def missions(self) -> AsyncMissionsResource:
        return AsyncMissionsResource(self._client)

    @cached_property
    def openai(self) -> AsyncOpenAIResource:
        return AsyncOpenAIResource(self._client)

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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        system_prompt: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        """Configure AI assistant specifications"""
        return AssistantsResourceWithRawResponse(self._ai.assistants)

    @cached_property
    def audio(self) -> AudioResourceWithRawResponse:
        """Turn audio into text or text into audio."""
        return AudioResourceWithRawResponse(self._ai.audio)

    @cached_property
    def chat(self) -> ChatResourceWithRawResponse:
        """Generate text with LLMs"""
        return ChatResourceWithRawResponse(self._ai.chat)

    @cached_property
    def clusters(self) -> ClustersResourceWithRawResponse:
        """Identify common themes and patterns in your embedded documents"""
        return ClustersResourceWithRawResponse(self._ai.clusters)

    @cached_property
    def conversations(self) -> ConversationsResourceWithRawResponse:
        """Manage historical AI assistant conversations"""
        return ConversationsResourceWithRawResponse(self._ai.conversations)

    @cached_property
    def embeddings(self) -> EmbeddingsResourceWithRawResponse:
        """Embed documents and perform text searches"""
        return EmbeddingsResourceWithRawResponse(self._ai.embeddings)

    @cached_property
    def fine_tuning(self) -> FineTuningResourceWithRawResponse:
        return FineTuningResourceWithRawResponse(self._ai.fine_tuning)

    @cached_property
    def integrations(self) -> IntegrationsResourceWithRawResponse:
        return IntegrationsResourceWithRawResponse(self._ai.integrations)

    @cached_property
    def mcp_servers(self) -> McpServersResourceWithRawResponse:
        return McpServersResourceWithRawResponse(self._ai.mcp_servers)

    @cached_property
    def missions(self) -> MissionsResourceWithRawResponse:
        return MissionsResourceWithRawResponse(self._ai.missions)

    @cached_property
    def openai(self) -> OpenAIResourceWithRawResponse:
        return OpenAIResourceWithRawResponse(self._ai.openai)


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
        """Configure AI assistant specifications"""
        return AsyncAssistantsResourceWithRawResponse(self._ai.assistants)

    @cached_property
    def audio(self) -> AsyncAudioResourceWithRawResponse:
        """Turn audio into text or text into audio."""
        return AsyncAudioResourceWithRawResponse(self._ai.audio)

    @cached_property
    def chat(self) -> AsyncChatResourceWithRawResponse:
        """Generate text with LLMs"""
        return AsyncChatResourceWithRawResponse(self._ai.chat)

    @cached_property
    def clusters(self) -> AsyncClustersResourceWithRawResponse:
        """Identify common themes and patterns in your embedded documents"""
        return AsyncClustersResourceWithRawResponse(self._ai.clusters)

    @cached_property
    def conversations(self) -> AsyncConversationsResourceWithRawResponse:
        """Manage historical AI assistant conversations"""
        return AsyncConversationsResourceWithRawResponse(self._ai.conversations)

    @cached_property
    def embeddings(self) -> AsyncEmbeddingsResourceWithRawResponse:
        """Embed documents and perform text searches"""
        return AsyncEmbeddingsResourceWithRawResponse(self._ai.embeddings)

    @cached_property
    def fine_tuning(self) -> AsyncFineTuningResourceWithRawResponse:
        return AsyncFineTuningResourceWithRawResponse(self._ai.fine_tuning)

    @cached_property
    def integrations(self) -> AsyncIntegrationsResourceWithRawResponse:
        return AsyncIntegrationsResourceWithRawResponse(self._ai.integrations)

    @cached_property
    def mcp_servers(self) -> AsyncMcpServersResourceWithRawResponse:
        return AsyncMcpServersResourceWithRawResponse(self._ai.mcp_servers)

    @cached_property
    def missions(self) -> AsyncMissionsResourceWithRawResponse:
        return AsyncMissionsResourceWithRawResponse(self._ai.missions)

    @cached_property
    def openai(self) -> AsyncOpenAIResourceWithRawResponse:
        return AsyncOpenAIResourceWithRawResponse(self._ai.openai)


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
        """Configure AI assistant specifications"""
        return AssistantsResourceWithStreamingResponse(self._ai.assistants)

    @cached_property
    def audio(self) -> AudioResourceWithStreamingResponse:
        """Turn audio into text or text into audio."""
        return AudioResourceWithStreamingResponse(self._ai.audio)

    @cached_property
    def chat(self) -> ChatResourceWithStreamingResponse:
        """Generate text with LLMs"""
        return ChatResourceWithStreamingResponse(self._ai.chat)

    @cached_property
    def clusters(self) -> ClustersResourceWithStreamingResponse:
        """Identify common themes and patterns in your embedded documents"""
        return ClustersResourceWithStreamingResponse(self._ai.clusters)

    @cached_property
    def conversations(self) -> ConversationsResourceWithStreamingResponse:
        """Manage historical AI assistant conversations"""
        return ConversationsResourceWithStreamingResponse(self._ai.conversations)

    @cached_property
    def embeddings(self) -> EmbeddingsResourceWithStreamingResponse:
        """Embed documents and perform text searches"""
        return EmbeddingsResourceWithStreamingResponse(self._ai.embeddings)

    @cached_property
    def fine_tuning(self) -> FineTuningResourceWithStreamingResponse:
        return FineTuningResourceWithStreamingResponse(self._ai.fine_tuning)

    @cached_property
    def integrations(self) -> IntegrationsResourceWithStreamingResponse:
        return IntegrationsResourceWithStreamingResponse(self._ai.integrations)

    @cached_property
    def mcp_servers(self) -> McpServersResourceWithStreamingResponse:
        return McpServersResourceWithStreamingResponse(self._ai.mcp_servers)

    @cached_property
    def missions(self) -> MissionsResourceWithStreamingResponse:
        return MissionsResourceWithStreamingResponse(self._ai.missions)

    @cached_property
    def openai(self) -> OpenAIResourceWithStreamingResponse:
        return OpenAIResourceWithStreamingResponse(self._ai.openai)


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
        """Configure AI assistant specifications"""
        return AsyncAssistantsResourceWithStreamingResponse(self._ai.assistants)

    @cached_property
    def audio(self) -> AsyncAudioResourceWithStreamingResponse:
        """Turn audio into text or text into audio."""
        return AsyncAudioResourceWithStreamingResponse(self._ai.audio)

    @cached_property
    def chat(self) -> AsyncChatResourceWithStreamingResponse:
        """Generate text with LLMs"""
        return AsyncChatResourceWithStreamingResponse(self._ai.chat)

    @cached_property
    def clusters(self) -> AsyncClustersResourceWithStreamingResponse:
        """Identify common themes and patterns in your embedded documents"""
        return AsyncClustersResourceWithStreamingResponse(self._ai.clusters)

    @cached_property
    def conversations(self) -> AsyncConversationsResourceWithStreamingResponse:
        """Manage historical AI assistant conversations"""
        return AsyncConversationsResourceWithStreamingResponse(self._ai.conversations)

    @cached_property
    def embeddings(self) -> AsyncEmbeddingsResourceWithStreamingResponse:
        """Embed documents and perform text searches"""
        return AsyncEmbeddingsResourceWithStreamingResponse(self._ai.embeddings)

    @cached_property
    def fine_tuning(self) -> AsyncFineTuningResourceWithStreamingResponse:
        return AsyncFineTuningResourceWithStreamingResponse(self._ai.fine_tuning)

    @cached_property
    def integrations(self) -> AsyncIntegrationsResourceWithStreamingResponse:
        return AsyncIntegrationsResourceWithStreamingResponse(self._ai.integrations)

    @cached_property
    def mcp_servers(self) -> AsyncMcpServersResourceWithStreamingResponse:
        return AsyncMcpServersResourceWithStreamingResponse(self._ai.mcp_servers)

    @cached_property
    def missions(self) -> AsyncMissionsResourceWithStreamingResponse:
        return AsyncMissionsResourceWithStreamingResponse(self._ai.missions)

    @cached_property
    def openai(self) -> AsyncOpenAIResourceWithStreamingResponse:
        return AsyncOpenAIResourceWithStreamingResponse(self._ai.openai)

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Dict, Union
from datetime import datetime
from typing_extensions import Literal

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
from .tools import (
    ToolsResource,
    AsyncToolsResource,
    ToolsResourceWithRawResponse,
    AsyncToolsResourceWithRawResponse,
    ToolsResourceWithStreamingResponse,
    AsyncToolsResourceWithStreamingResponse,
)
from ...types import ai_summarize_params, ai_create_response_deprecated_params, ai_search_conversation_histories_params
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
from ...types.ai_create_response_deprecated_response import AICreateResponseDeprecatedResponse
from ...types.ai_search_conversation_histories_response import AISearchConversationHistoriesResponse

__all__ = ["AIResource", "AsyncAIResource"]


class AIResource(SyncAPIResource):
    @cached_property
    def assistants(self) -> AssistantsResource:
        """Configure AI assistant specifications"""
        return AssistantsResource(self._client)

    @cached_property
    def audio(self) -> AudioResource:
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
    def tools(self) -> ToolsResource:
        """Configure AI assistant specifications"""
        return ToolsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/telnyx-python#with_streaming_response
        """
        return AIResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    def create_response_deprecated(
        self,
        *,
        body: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AICreateResponseDeprecatedResponse:
        """**Deprecated**: Use `POST /v2/ai/openai/responses` instead.

        This endpoint is
        compatible with the
        [OpenAI Responses API](https://developers.openai.com/api/reference/responses/overview)
        and may be used with the OpenAI JS or Python SDK. Response id parameter is not
        supported at the moment. Use the `conversation` parameter with a Telnyx
        Conversation ID to leverage persistent conversations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/responses",
            body=maybe_transform(body, ai_create_response_deprecated_params.AICreateResponseDeprecatedParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AICreateResponseDeprecatedResponse,
        )

    @typing_extensions.deprecated("deprecated")
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
        **Deprecated**: Use `GET /v2/ai/openai/models` instead.

        Returns the same `ModelsResponse` payload as the OpenAI-compatible endpoint —
        open-source LLMs hosted on Telnyx (e.g. `moonshotai/Kimi-K2.6`,
        `zai-org/GLM-5.1-FP8`, `MiniMaxAI/MiniMax-M2.7`), embedding models, and
        fine-tuned models — kept around for backwards compatibility. New integrations
        should use `/v2/ai/openai/models`.

        Model ids follow the `{organization}/{model_name}` convention from Hugging Face.
        """
        return self._get(
            "/ai/models",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AIRetrieveModelsResponse,
        )

    def search_conversation_histories(
        self,
        *,
        q: str,
        filter_ingested_at_gte: Union[str, datetime] | Omit = omit,
        filter_ingested_at_lte: Union[str, datetime] | Omit = omit,
        filter_record_created_at_gte: Union[str, datetime] | Omit = omit,
        filter_record_created_at_lte: Union[str, datetime] | Omit = omit,
        filter_record_id: str | Omit = omit,
        filter_region_in: str | Omit = omit,
        filter_retention: str | Omit = omit,
        filter_user_id: str | Omit = omit,
        min_score: float | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        region: Literal["USA", "DEU", "AUS", "UAE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AISearchConversationHistoriesResponse:
        """
        Performs semantic vector search across conversation history records.

        **How it works:**

        1. The query text is embedded into a 1024-dimensional vector using the
           multilingual-e5-large model.
        2. The vector is compared against indexed record chunks using semantic
           similarity search.
        3. When no region is specified, all regions are queried in parallel (fan-out)
           and results are merged by score.
        4. Results are ranked by similarity score (descending) and paginated via
           `page[number]` / `page[size]`.

        **Authentication:** Requires a Telnyx API key via `Authorization: Bearer <key>`.
        Results are automatically scoped to the caller's organization —
        `organization_id` is injected from the auth token and cannot be overridden.

        **Chunking:** Records are split into chunks of up to 480 tokens with 64-token
        overlap at ingestion time. Each search result represents a single chunk, with
        `chunk_index` and `chunk_total` indicating its position within the original
        record.

        **Filtering:** Use `filter[field][operator]=value` query parameters to narrow
        results before vector search.

        Top-level filterable fields: `user_id`, `region`, `record_id`,
        `record_created_at`, `ingested_at`, `retention`

        Note: `retention` is filter-only — it can be used to narrow results but is not
        returned in the response body.

        Metadata fields: any field not in the list above is resolved to
        `data.metadata.<field>` (e.g., `filter[language]=en` →
        `data.metadata.language`).

        Supported filter operators:

        - `eq` — exact match (default when no operator specified)
        - `in` — match any of comma-separated values
        - `gte`, `gt`, `lte`, `lt` — range comparisons (useful for date filtering)
        - `contains` — wildcard substring match

        **Examples:**

        ```
        GET /v2/ai/conversation_histories?q=billing+issue&page[size]=10
        GET /v2/ai/conversation_histories?q=setup+guide&region=USA&min_score=0.5
        GET /v2/ai/conversation_histories?q=refund&filter[record_created_at][gte]=2026-01-01T00:00:00Z
        GET /v2/ai/conversation_histories?q=outage&filter[region][in]=USA,DEU
        GET /v2/ai/conversation_histories?q=hold+time&filter[language]=en
        ```

        Args:
          q: Natural language search query. The text is embedded into a 1024-dimensional
              vector and compared against indexed record chunks using semantic similarity.

          filter_ingested_at_gte: Only include records ingested (chunked, embedded, and indexed) on or after this
              ISO 8601 timestamp.

          filter_ingested_at_lte: Only include records ingested (chunked, embedded, and indexed) on or before this
              ISO 8601 timestamp.

          filter_record_created_at_gte: Only include records whose original creation time is on or after this ISO 8601
              timestamp.

          filter_record_created_at_lte: Only include records whose original creation time is on or before this ISO 8601
              timestamp.

          filter_record_id: Filter to chunks belonging to a specific parent record (exact match).

          filter_region_in: Filter by the region stored on the record. Comma-separated to match multiple
              regions (USA, DEU, AUS, UAE). Distinct from the `region` parameter, which
              selects which cluster(s) are queried.

          filter_retention: Filter by retention policy (exact match). Filter-only: not returned in the
              response body.

          filter_user_id: Filter to records owned by a specific user (exact match).

          min_score: Minimum cosine similarity score threshold (0.0 to 1.0). Results below this
              threshold are excluded.

          page_number: Page number to return (1-based). Defaults to 1.

          page_size: Number of results per page. Defaults to 20, maximum 100.

          region: Restrict search to a specific region. When omitted, all regions are queried in
              parallel (fan-out) and results are merged by similarity score.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/ai/conversation_histories",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "filter_ingested_at_gte": filter_ingested_at_gte,
                        "filter_ingested_at_lte": filter_ingested_at_lte,
                        "filter_record_created_at_gte": filter_record_created_at_gte,
                        "filter_record_created_at_lte": filter_record_created_at_lte,
                        "filter_record_id": filter_record_id,
                        "filter_region_in": filter_region_in,
                        "filter_retention": filter_retention,
                        "filter_user_id": filter_user_id,
                        "min_score": min_score,
                        "page_number": page_number,
                        "page_size": page_size,
                        "region": region,
                    },
                    ai_search_conversation_histories_params.AISearchConversationHistoriesParams,
                ),
            ),
            cast_to=AISearchConversationHistoriesResponse,
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
    @cached_property
    def assistants(self) -> AsyncAssistantsResource:
        """Configure AI assistant specifications"""
        return AsyncAssistantsResource(self._client)

    @cached_property
    def audio(self) -> AsyncAudioResource:
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
    def tools(self) -> AsyncToolsResource:
        """Configure AI assistant specifications"""
        return AsyncToolsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/telnyx-python#with_streaming_response
        """
        return AsyncAIResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    async def create_response_deprecated(
        self,
        *,
        body: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AICreateResponseDeprecatedResponse:
        """**Deprecated**: Use `POST /v2/ai/openai/responses` instead.

        This endpoint is
        compatible with the
        [OpenAI Responses API](https://developers.openai.com/api/reference/responses/overview)
        and may be used with the OpenAI JS or Python SDK. Response id parameter is not
        supported at the moment. Use the `conversation` parameter with a Telnyx
        Conversation ID to leverage persistent conversations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/responses",
            body=await async_maybe_transform(
                body, ai_create_response_deprecated_params.AICreateResponseDeprecatedParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AICreateResponseDeprecatedResponse,
        )

    @typing_extensions.deprecated("deprecated")
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
        **Deprecated**: Use `GET /v2/ai/openai/models` instead.

        Returns the same `ModelsResponse` payload as the OpenAI-compatible endpoint —
        open-source LLMs hosted on Telnyx (e.g. `moonshotai/Kimi-K2.6`,
        `zai-org/GLM-5.1-FP8`, `MiniMaxAI/MiniMax-M2.7`), embedding models, and
        fine-tuned models — kept around for backwards compatibility. New integrations
        should use `/v2/ai/openai/models`.

        Model ids follow the `{organization}/{model_name}` convention from Hugging Face.
        """
        return await self._get(
            "/ai/models",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AIRetrieveModelsResponse,
        )

    async def search_conversation_histories(
        self,
        *,
        q: str,
        filter_ingested_at_gte: Union[str, datetime] | Omit = omit,
        filter_ingested_at_lte: Union[str, datetime] | Omit = omit,
        filter_record_created_at_gte: Union[str, datetime] | Omit = omit,
        filter_record_created_at_lte: Union[str, datetime] | Omit = omit,
        filter_record_id: str | Omit = omit,
        filter_region_in: str | Omit = omit,
        filter_retention: str | Omit = omit,
        filter_user_id: str | Omit = omit,
        min_score: float | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        region: Literal["USA", "DEU", "AUS", "UAE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AISearchConversationHistoriesResponse:
        """
        Performs semantic vector search across conversation history records.

        **How it works:**

        1. The query text is embedded into a 1024-dimensional vector using the
           multilingual-e5-large model.
        2. The vector is compared against indexed record chunks using semantic
           similarity search.
        3. When no region is specified, all regions are queried in parallel (fan-out)
           and results are merged by score.
        4. Results are ranked by similarity score (descending) and paginated via
           `page[number]` / `page[size]`.

        **Authentication:** Requires a Telnyx API key via `Authorization: Bearer <key>`.
        Results are automatically scoped to the caller's organization —
        `organization_id` is injected from the auth token and cannot be overridden.

        **Chunking:** Records are split into chunks of up to 480 tokens with 64-token
        overlap at ingestion time. Each search result represents a single chunk, with
        `chunk_index` and `chunk_total` indicating its position within the original
        record.

        **Filtering:** Use `filter[field][operator]=value` query parameters to narrow
        results before vector search.

        Top-level filterable fields: `user_id`, `region`, `record_id`,
        `record_created_at`, `ingested_at`, `retention`

        Note: `retention` is filter-only — it can be used to narrow results but is not
        returned in the response body.

        Metadata fields: any field not in the list above is resolved to
        `data.metadata.<field>` (e.g., `filter[language]=en` →
        `data.metadata.language`).

        Supported filter operators:

        - `eq` — exact match (default when no operator specified)
        - `in` — match any of comma-separated values
        - `gte`, `gt`, `lte`, `lt` — range comparisons (useful for date filtering)
        - `contains` — wildcard substring match

        **Examples:**

        ```
        GET /v2/ai/conversation_histories?q=billing+issue&page[size]=10
        GET /v2/ai/conversation_histories?q=setup+guide&region=USA&min_score=0.5
        GET /v2/ai/conversation_histories?q=refund&filter[record_created_at][gte]=2026-01-01T00:00:00Z
        GET /v2/ai/conversation_histories?q=outage&filter[region][in]=USA,DEU
        GET /v2/ai/conversation_histories?q=hold+time&filter[language]=en
        ```

        Args:
          q: Natural language search query. The text is embedded into a 1024-dimensional
              vector and compared against indexed record chunks using semantic similarity.

          filter_ingested_at_gte: Only include records ingested (chunked, embedded, and indexed) on or after this
              ISO 8601 timestamp.

          filter_ingested_at_lte: Only include records ingested (chunked, embedded, and indexed) on or before this
              ISO 8601 timestamp.

          filter_record_created_at_gte: Only include records whose original creation time is on or after this ISO 8601
              timestamp.

          filter_record_created_at_lte: Only include records whose original creation time is on or before this ISO 8601
              timestamp.

          filter_record_id: Filter to chunks belonging to a specific parent record (exact match).

          filter_region_in: Filter by the region stored on the record. Comma-separated to match multiple
              regions (USA, DEU, AUS, UAE). Distinct from the `region` parameter, which
              selects which cluster(s) are queried.

          filter_retention: Filter by retention policy (exact match). Filter-only: not returned in the
              response body.

          filter_user_id: Filter to records owned by a specific user (exact match).

          min_score: Minimum cosine similarity score threshold (0.0 to 1.0). Results below this
              threshold are excluded.

          page_number: Page number to return (1-based). Defaults to 1.

          page_size: Number of results per page. Defaults to 20, maximum 100.

          region: Restrict search to a specific region. When omitted, all regions are queried in
              parallel (fan-out) and results are merged by similarity score.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/ai/conversation_histories",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "filter_ingested_at_gte": filter_ingested_at_gte,
                        "filter_ingested_at_lte": filter_ingested_at_lte,
                        "filter_record_created_at_gte": filter_record_created_at_gte,
                        "filter_record_created_at_lte": filter_record_created_at_lte,
                        "filter_record_id": filter_record_id,
                        "filter_region_in": filter_region_in,
                        "filter_retention": filter_retention,
                        "filter_user_id": filter_user_id,
                        "min_score": min_score,
                        "page_number": page_number,
                        "page_size": page_size,
                        "region": region,
                    },
                    ai_search_conversation_histories_params.AISearchConversationHistoriesParams,
                ),
            ),
            cast_to=AISearchConversationHistoriesResponse,
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

        self.create_response_deprecated = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                ai.create_response_deprecated,  # pyright: ignore[reportDeprecated],
            )
        )
        self.retrieve_models = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                ai.retrieve_models,  # pyright: ignore[reportDeprecated],
            )
        )
        self.search_conversation_histories = to_raw_response_wrapper(
            ai.search_conversation_histories,
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

    @cached_property
    def tools(self) -> ToolsResourceWithRawResponse:
        """Configure AI assistant specifications"""
        return ToolsResourceWithRawResponse(self._ai.tools)


class AsyncAIResourceWithRawResponse:
    def __init__(self, ai: AsyncAIResource) -> None:
        self._ai = ai

        self.create_response_deprecated = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                ai.create_response_deprecated,  # pyright: ignore[reportDeprecated],
            )
        )
        self.retrieve_models = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                ai.retrieve_models,  # pyright: ignore[reportDeprecated],
            )
        )
        self.search_conversation_histories = async_to_raw_response_wrapper(
            ai.search_conversation_histories,
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

    @cached_property
    def tools(self) -> AsyncToolsResourceWithRawResponse:
        """Configure AI assistant specifications"""
        return AsyncToolsResourceWithRawResponse(self._ai.tools)


class AIResourceWithStreamingResponse:
    def __init__(self, ai: AIResource) -> None:
        self._ai = ai

        self.create_response_deprecated = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                ai.create_response_deprecated,  # pyright: ignore[reportDeprecated],
            )
        )
        self.retrieve_models = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                ai.retrieve_models,  # pyright: ignore[reportDeprecated],
            )
        )
        self.search_conversation_histories = to_streamed_response_wrapper(
            ai.search_conversation_histories,
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

    @cached_property
    def tools(self) -> ToolsResourceWithStreamingResponse:
        """Configure AI assistant specifications"""
        return ToolsResourceWithStreamingResponse(self._ai.tools)


class AsyncAIResourceWithStreamingResponse:
    def __init__(self, ai: AsyncAIResource) -> None:
        self._ai = ai

        self.create_response_deprecated = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                ai.create_response_deprecated,  # pyright: ignore[reportDeprecated],
            )
        )
        self.retrieve_models = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                ai.retrieve_models,  # pyright: ignore[reportDeprecated],
            )
        )
        self.search_conversation_histories = async_to_streamed_response_wrapper(
            ai.search_conversation_histories,
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

    @cached_property
    def tools(self) -> AsyncToolsResourceWithStreamingResponse:
        """Configure AI assistant specifications"""
        return AsyncToolsResourceWithStreamingResponse(self._ai.tools)

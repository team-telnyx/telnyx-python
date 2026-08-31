# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.ai.knowledge import collection_retrieve_documents_params
from ....types.ai.knowledge.collection_retrieve_documents_response import CollectionRetrieveDocumentsResponse

__all__ = ["CollectionsResource", "AsyncCollectionsResource"]


class CollectionsResource(SyncAPIResource):
    """
    Create and manage logical collections of your Telnyx data, tune retrieval settings, manage sources, and run collection-scoped semantic search.
    """

    @cached_property
    def with_raw_response(self) -> CollectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return CollectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CollectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return CollectionsResourceWithStreamingResponse(self)

    def retrieve_documents(
        self,
        slug: str,
        *,
        filter: Dict[str, object] | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        query: str | Omit = omit,
        retrieval_type: Literal["vector", "hybrid", "keyword"] | Omit = omit,
        sources: str | Omit = omit,
        top_k: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionRetrieveDocumentsResponse:
        """
        Runs search over the documents in a collection, ranked by relevance to `query`.
        Searches currently run `vector` retrieval (semantic similarity). The
        collection's `retrieval_type` setting is the forward-compatible selector:
        `hybrid` (vector similarity fused with keyword matching) can be set but cannot
        be searched yet, and `keyword` (lexical BM25 matching) is not accepted yet --
        setting it returns 422 `unsupported_retrieval_type`. A per-request
        `retrieval_type` is accepted but ignored; `meta.retrieval_type` echoes the mode
        that actually ran. When `query` is omitted, returns a plain catalog listing of
        the collection's documents.

        **How it works:**

        1. The `query` text is embedded into a 1024-dimensional vector using the
           multilingual-e5-large model.
        2. The embedding is compared against the collection's indexed document chunks
           using semantic similarity. When `hybrid` and `keyword` execution ship, those
           scores will be fused with, or replaced by, lexical BM25 matching.
        3. Results are ranked by `score` (descending) and paginated via `page[number]` /
           `page[size]`.

        **Authentication:** Requires a Telnyx API key via `Authorization: Bearer <key>`.
        Results are automatically scoped to your organization and cannot be overridden.

        **Filtering:** Use `filter[field][operator]=value` query parameters to narrow
        results before search. Supported operators: `eq` (default), `in`, `gte`, `gt`,
        `lte`, `lt`, `contains`. Metadata fields resolve to `metadata.<field>`.

        **Examples:**

        - `GET /v2/ai/knowledge/collections/my-collection/documents?query=billing+issue&top_k=10`
        - `GET /v2/ai/knowledge/collections/my-collection/documents?query=refund&sources=voice,message`
        - `GET /v2/ai/knowledge/collections/my-collection/documents?query=outage&filter[record_created_at][gte]=2026-01-01T00:00:00Z`

        Args:
          filter: Field filters applied before ranking, using `filter[field][operator]=value`.
              Supported operators: `eq` (default), `in`, `gte`, `gt`, `lte`, `lt`, `contains`.
              Known fields: `record_type`, `record_id`, `user_id`, `record_created_at`,
              `ingested_at`; any other name resolves to a `metadata.<field>` filter. Example:
              `filter[record_id][eq]=rec_123`.

          page_number: Page number to return (1-based). Defaults to 1.

          page_size: Number of results per page. Defaults to 20.

          query: Natural-language search query. When provided, the text is matched against the
              collection's document chunks using the collection's `retrieval_type` (vector or
              hybrid). When omitted, documents are returned as a plain catalog listing.

          retrieval_type: Reserved; not yet functional. A value supplied here is accepted but ignored — it
              does not override the collection's configured strategy, and it is not echoed
              back. Searches run `vector` retrieval, and `meta.retrieval_type` reports the
              mode that actually ran. To change retrieval strategy, set it on the collection's
              settings subresource.

          sources: Comma-separated list of source types to restrict the search to. When omitted,
              all of the collection's sources are searched.

          top_k: Maximum number of ranked results to consider. When omitted, the collection's
              configured `top_k` setting is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            path_template("/ai/knowledge/collections/{slug}/documents", slug=slug),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page_number": page_number,
                        "page_size": page_size,
                        "query": query,
                        "retrieval_type": retrieval_type,
                        "sources": sources,
                        "top_k": top_k,
                    },
                    collection_retrieve_documents_params.CollectionRetrieveDocumentsParams,
                ),
            ),
            cast_to=CollectionRetrieveDocumentsResponse,
        )


class AsyncCollectionsResource(AsyncAPIResource):
    """
    Create and manage logical collections of your Telnyx data, tune retrieval settings, manage sources, and run collection-scoped semantic search.
    """

    @cached_property
    def with_raw_response(self) -> AsyncCollectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCollectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCollectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncCollectionsResourceWithStreamingResponse(self)

    async def retrieve_documents(
        self,
        slug: str,
        *,
        filter: Dict[str, object] | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        query: str | Omit = omit,
        retrieval_type: Literal["vector", "hybrid", "keyword"] | Omit = omit,
        sources: str | Omit = omit,
        top_k: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionRetrieveDocumentsResponse:
        """
        Runs search over the documents in a collection, ranked by relevance to `query`.
        Searches currently run `vector` retrieval (semantic similarity). The
        collection's `retrieval_type` setting is the forward-compatible selector:
        `hybrid` (vector similarity fused with keyword matching) can be set but cannot
        be searched yet, and `keyword` (lexical BM25 matching) is not accepted yet --
        setting it returns 422 `unsupported_retrieval_type`. A per-request
        `retrieval_type` is accepted but ignored; `meta.retrieval_type` echoes the mode
        that actually ran. When `query` is omitted, returns a plain catalog listing of
        the collection's documents.

        **How it works:**

        1. The `query` text is embedded into a 1024-dimensional vector using the
           multilingual-e5-large model.
        2. The embedding is compared against the collection's indexed document chunks
           using semantic similarity. When `hybrid` and `keyword` execution ship, those
           scores will be fused with, or replaced by, lexical BM25 matching.
        3. Results are ranked by `score` (descending) and paginated via `page[number]` /
           `page[size]`.

        **Authentication:** Requires a Telnyx API key via `Authorization: Bearer <key>`.
        Results are automatically scoped to your organization and cannot be overridden.

        **Filtering:** Use `filter[field][operator]=value` query parameters to narrow
        results before search. Supported operators: `eq` (default), `in`, `gte`, `gt`,
        `lte`, `lt`, `contains`. Metadata fields resolve to `metadata.<field>`.

        **Examples:**

        - `GET /v2/ai/knowledge/collections/my-collection/documents?query=billing+issue&top_k=10`
        - `GET /v2/ai/knowledge/collections/my-collection/documents?query=refund&sources=voice,message`
        - `GET /v2/ai/knowledge/collections/my-collection/documents?query=outage&filter[record_created_at][gte]=2026-01-01T00:00:00Z`

        Args:
          filter: Field filters applied before ranking, using `filter[field][operator]=value`.
              Supported operators: `eq` (default), `in`, `gte`, `gt`, `lte`, `lt`, `contains`.
              Known fields: `record_type`, `record_id`, `user_id`, `record_created_at`,
              `ingested_at`; any other name resolves to a `metadata.<field>` filter. Example:
              `filter[record_id][eq]=rec_123`.

          page_number: Page number to return (1-based). Defaults to 1.

          page_size: Number of results per page. Defaults to 20.

          query: Natural-language search query. When provided, the text is matched against the
              collection's document chunks using the collection's `retrieval_type` (vector or
              hybrid). When omitted, documents are returned as a plain catalog listing.

          retrieval_type: Reserved; not yet functional. A value supplied here is accepted but ignored — it
              does not override the collection's configured strategy, and it is not echoed
              back. Searches run `vector` retrieval, and `meta.retrieval_type` reports the
              mode that actually ran. To change retrieval strategy, set it on the collection's
              settings subresource.

          sources: Comma-separated list of source types to restrict the search to. When omitted,
              all of the collection's sources are searched.

          top_k: Maximum number of ranked results to consider. When omitted, the collection's
              configured `top_k` setting is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            path_template("/ai/knowledge/collections/{slug}/documents", slug=slug),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "page_number": page_number,
                        "page_size": page_size,
                        "query": query,
                        "retrieval_type": retrieval_type,
                        "sources": sources,
                        "top_k": top_k,
                    },
                    collection_retrieve_documents_params.CollectionRetrieveDocumentsParams,
                ),
            ),
            cast_to=CollectionRetrieveDocumentsResponse,
        )


class CollectionsResourceWithRawResponse:
    def __init__(self, collections: CollectionsResource) -> None:
        self._collections = collections

        self.retrieve_documents = to_raw_response_wrapper(
            collections.retrieve_documents,
        )


class AsyncCollectionsResourceWithRawResponse:
    def __init__(self, collections: AsyncCollectionsResource) -> None:
        self._collections = collections

        self.retrieve_documents = async_to_raw_response_wrapper(
            collections.retrieve_documents,
        )


class CollectionsResourceWithStreamingResponse:
    def __init__(self, collections: CollectionsResource) -> None:
        self._collections = collections

        self.retrieve_documents = to_streamed_response_wrapper(
            collections.retrieve_documents,
        )


class AsyncCollectionsResourceWithStreamingResponse:
    def __init__(self, collections: AsyncCollectionsResource) -> None:
        self._collections = collections

        self.retrieve_documents = async_to_streamed_response_wrapper(
            collections.retrieve_documents,
        )

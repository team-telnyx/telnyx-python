# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal

import httpx

from .sources import (
    SourcesResource,
    AsyncSourcesResource,
    SourcesResourceWithRawResponse,
    AsyncSourcesResourceWithRawResponse,
    SourcesResourceWithStreamingResponse,
    AsyncSourcesResourceWithStreamingResponse,
)
from .settings import (
    SettingsResource,
    AsyncSettingsResource,
    SettingsResourceWithRawResponse,
    AsyncSettingsResourceWithRawResponse,
    SettingsResourceWithStreamingResponse,
    AsyncSettingsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.ai import (
    collection_list_params,
    collection_create_params,
    collection_update_params,
    collection_retrieve_documents_params,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from ...._base_client import AsyncPaginator, make_request_options
from ....types.ai.collection import Collection
from ....types.ai.collection_envelope import CollectionEnvelope
from ....types.ai.collections.source_request_param import SourceRequestParam
from ....types.ai.collection_retrieve_documents_response import CollectionRetrieveDocumentsResponse
from ....types.ai.collections.retrieval_settings_wrapper_param import RetrievalSettingsWrapperParam

__all__ = ["CollectionsResource", "AsyncCollectionsResource"]


class CollectionsResource(SyncAPIResource):
    """
    Create and manage logical collections of your Telnyx data, tune retrieval settings, manage sources, and run collection-scoped semantic search.
    """

    @cached_property
    def settings(self) -> SettingsResource:
        """
        Create and manage logical collections of your Telnyx data, tune retrieval settings, manage sources, and run collection-scoped semantic search.
        """
        return SettingsResource(self._client)

    @cached_property
    def sources(self) -> SourcesResource:
        """
        Create and manage logical collections of your Telnyx data, tune retrieval settings, manage sources, and run collection-scoped semantic search.
        """
        return SourcesResource(self._client)

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

    def create(
        self,
        *,
        name: str,
        description: str | Omit = omit,
        settings: RetrievalSettingsWrapperParam | Omit = omit,
        slug: str | Omit = omit,
        sources: Iterable[SourceRequestParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionEnvelope:
        """Creates a new collection scoped to your organization.

        Optionally attach sources
        and retrieval settings at creation time. If `slug` is omitted, one is derived
        from `name` and must be unique within your organization.

        Args:
          name: Human-readable collection name.

          description: Optional description.

          settings: Optional retrieval settings.

          slug: Optional slug (unique per organization). Derived from `name` when omitted.

          sources: Optional sources to attach at creation time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/collections",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "settings": settings,
                    "slug": slug,
                    "sources": sources,
                },
                collection_create_params.CollectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionEnvelope,
        )

    def retrieve(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionEnvelope:
        """
        Fetches a single collection by its `slug`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            path_template("/ai/collections/slug/{slug}", slug=slug),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionEnvelope,
        )

    def update(
        self,
        uuid: str,
        *,
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionEnvelope:
        """Updates a collection's metadata (`name` and/or `description`).

        Sources and
        settings are managed through their own sub-resources.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._patch(
            path_template("/ai/collections/{uuid}", uuid=uuid),
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                collection_update_params.CollectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionEnvelope,
        )

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[Collection]:
        """
        Returns a paginated list of collections in your organization.

        Args:
          page_number: Page number to return (1-based). Defaults to 1.

          page_size: Number of results per page. Defaults to 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ai/collections",
            page=SyncDefaultFlatPagination[Collection],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    collection_list_params.CollectionListParams,
                ),
            ),
            model=Collection,
        )

    def delete(
        self,
        uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Soft-deletes a collection.

        Its `slug` is freed and may be reused by a new
        collection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/ai/collections/{uuid}", uuid=uuid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve_by_id(
        self,
        uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionEnvelope:
        """
        Fetches a single collection by its `uuid`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._get(
            path_template("/ai/collections/{uuid}", uuid=uuid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionEnvelope,
        )

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
    ) -> SyncDefaultFlatPagination[CollectionRetrieveDocumentsResponse]:
        """
        Runs search over the documents in a collection, ranked by relevance to `query`.
        The collection's `retrieval_type` setting selects the strategy: `vector`
        (semantic similarity), `hybrid` (vector similarity fused with keyword matching),
        or `keyword` (lexical BM25 matching). When `query` is omitted, returns a plain
        catalog listing of the collection's documents.

        **How it works:**

        1. For `vector` and `hybrid`, the `query` text is embedded into a
           1024-dimensional vector using the multilingual-e5-large model.
        2. For `vector`, the embedding is compared against the collection's indexed
           document chunks using semantic similarity; for `hybrid`, those similarity
           scores are fused with keyword-match scores; for `keyword`, only lexical BM25
           matching is applied.
        3. Results are ranked by `score` (descending) and paginated via `page[number]` /
           `page[size]`.

        **Authentication:** Requires a Telnyx API key via `Authorization: Bearer <key>`.
        Results are automatically scoped to your organization and cannot be overridden.

        **Filtering:** Use `filter[field][operator]=value` query parameters to narrow
        results before search. Supported operators: `eq` (default), `in`, `gte`, `gt`,
        `lte`, `lt`, `contains`. Metadata fields resolve to `metadata.<field>`.

        **Examples:**

        - `GET /v2/ai/collections/my-collection/documents?query=billing+issue&top_k=10`
        - `GET /v2/ai/collections/my-collection/documents?query=refund&sources=voice,message`
        - `GET /v2/ai/collections/my-collection/documents?query=outage&filter[record_created_at][gte]=2026-01-01T00:00:00Z`

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

          retrieval_type: Override the collection's configured retrieval strategy for this request. Echoed
              back in `meta.retrieval_type`.

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
        return self._get_api_list(
            path_template("/ai/collections/{slug}/documents", slug=slug),
            page=SyncDefaultFlatPagination[CollectionRetrieveDocumentsResponse],
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
            model=CollectionRetrieveDocumentsResponse,
        )


class AsyncCollectionsResource(AsyncAPIResource):
    """
    Create and manage logical collections of your Telnyx data, tune retrieval settings, manage sources, and run collection-scoped semantic search.
    """

    @cached_property
    def settings(self) -> AsyncSettingsResource:
        """
        Create and manage logical collections of your Telnyx data, tune retrieval settings, manage sources, and run collection-scoped semantic search.
        """
        return AsyncSettingsResource(self._client)

    @cached_property
    def sources(self) -> AsyncSourcesResource:
        """
        Create and manage logical collections of your Telnyx data, tune retrieval settings, manage sources, and run collection-scoped semantic search.
        """
        return AsyncSourcesResource(self._client)

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

    async def create(
        self,
        *,
        name: str,
        description: str | Omit = omit,
        settings: RetrievalSettingsWrapperParam | Omit = omit,
        slug: str | Omit = omit,
        sources: Iterable[SourceRequestParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionEnvelope:
        """Creates a new collection scoped to your organization.

        Optionally attach sources
        and retrieval settings at creation time. If `slug` is omitted, one is derived
        from `name` and must be unique within your organization.

        Args:
          name: Human-readable collection name.

          description: Optional description.

          settings: Optional retrieval settings.

          slug: Optional slug (unique per organization). Derived from `name` when omitted.

          sources: Optional sources to attach at creation time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/collections",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "settings": settings,
                    "slug": slug,
                    "sources": sources,
                },
                collection_create_params.CollectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionEnvelope,
        )

    async def retrieve(
        self,
        slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionEnvelope:
        """
        Fetches a single collection by its `slug`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            path_template("/ai/collections/slug/{slug}", slug=slug),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionEnvelope,
        )

    async def update(
        self,
        uuid: str,
        *,
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionEnvelope:
        """Updates a collection's metadata (`name` and/or `description`).

        Sources and
        settings are managed through their own sub-resources.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._patch(
            path_template("/ai/collections/{uuid}", uuid=uuid),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                collection_update_params.CollectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionEnvelope,
        )

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Collection, AsyncDefaultFlatPagination[Collection]]:
        """
        Returns a paginated list of collections in your organization.

        Args:
          page_number: Page number to return (1-based). Defaults to 1.

          page_size: Number of results per page. Defaults to 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ai/collections",
            page=AsyncDefaultFlatPagination[Collection],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    collection_list_params.CollectionListParams,
                ),
            ),
            model=Collection,
        )

    async def delete(
        self,
        uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Soft-deletes a collection.

        Its `slug` is freed and may be reused by a new
        collection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/ai/collections/{uuid}", uuid=uuid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve_by_id(
        self,
        uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionEnvelope:
        """
        Fetches a single collection by its `uuid`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._get(
            path_template("/ai/collections/{uuid}", uuid=uuid),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionEnvelope,
        )

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
    ) -> AsyncPaginator[
        CollectionRetrieveDocumentsResponse, AsyncDefaultFlatPagination[CollectionRetrieveDocumentsResponse]
    ]:
        """
        Runs search over the documents in a collection, ranked by relevance to `query`.
        The collection's `retrieval_type` setting selects the strategy: `vector`
        (semantic similarity), `hybrid` (vector similarity fused with keyword matching),
        or `keyword` (lexical BM25 matching). When `query` is omitted, returns a plain
        catalog listing of the collection's documents.

        **How it works:**

        1. For `vector` and `hybrid`, the `query` text is embedded into a
           1024-dimensional vector using the multilingual-e5-large model.
        2. For `vector`, the embedding is compared against the collection's indexed
           document chunks using semantic similarity; for `hybrid`, those similarity
           scores are fused with keyword-match scores; for `keyword`, only lexical BM25
           matching is applied.
        3. Results are ranked by `score` (descending) and paginated via `page[number]` /
           `page[size]`.

        **Authentication:** Requires a Telnyx API key via `Authorization: Bearer <key>`.
        Results are automatically scoped to your organization and cannot be overridden.

        **Filtering:** Use `filter[field][operator]=value` query parameters to narrow
        results before search. Supported operators: `eq` (default), `in`, `gte`, `gt`,
        `lte`, `lt`, `contains`. Metadata fields resolve to `metadata.<field>`.

        **Examples:**

        - `GET /v2/ai/collections/my-collection/documents?query=billing+issue&top_k=10`
        - `GET /v2/ai/collections/my-collection/documents?query=refund&sources=voice,message`
        - `GET /v2/ai/collections/my-collection/documents?query=outage&filter[record_created_at][gte]=2026-01-01T00:00:00Z`

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

          retrieval_type: Override the collection's configured retrieval strategy for this request. Echoed
              back in `meta.retrieval_type`.

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
        return self._get_api_list(
            path_template("/ai/collections/{slug}/documents", slug=slug),
            page=AsyncDefaultFlatPagination[CollectionRetrieveDocumentsResponse],
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
            model=CollectionRetrieveDocumentsResponse,
        )


class CollectionsResourceWithRawResponse:
    def __init__(self, collections: CollectionsResource) -> None:
        self._collections = collections

        self.create = to_raw_response_wrapper(
            collections.create,
        )
        self.retrieve = to_raw_response_wrapper(
            collections.retrieve,
        )
        self.update = to_raw_response_wrapper(
            collections.update,
        )
        self.list = to_raw_response_wrapper(
            collections.list,
        )
        self.delete = to_raw_response_wrapper(
            collections.delete,
        )
        self.retrieve_by_id = to_raw_response_wrapper(
            collections.retrieve_by_id,
        )
        self.retrieve_documents = to_raw_response_wrapper(
            collections.retrieve_documents,
        )

    @cached_property
    def settings(self) -> SettingsResourceWithRawResponse:
        """
        Create and manage logical collections of your Telnyx data, tune retrieval settings, manage sources, and run collection-scoped semantic search.
        """
        return SettingsResourceWithRawResponse(self._collections.settings)

    @cached_property
    def sources(self) -> SourcesResourceWithRawResponse:
        """
        Create and manage logical collections of your Telnyx data, tune retrieval settings, manage sources, and run collection-scoped semantic search.
        """
        return SourcesResourceWithRawResponse(self._collections.sources)


class AsyncCollectionsResourceWithRawResponse:
    def __init__(self, collections: AsyncCollectionsResource) -> None:
        self._collections = collections

        self.create = async_to_raw_response_wrapper(
            collections.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            collections.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            collections.update,
        )
        self.list = async_to_raw_response_wrapper(
            collections.list,
        )
        self.delete = async_to_raw_response_wrapper(
            collections.delete,
        )
        self.retrieve_by_id = async_to_raw_response_wrapper(
            collections.retrieve_by_id,
        )
        self.retrieve_documents = async_to_raw_response_wrapper(
            collections.retrieve_documents,
        )

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithRawResponse:
        """
        Create and manage logical collections of your Telnyx data, tune retrieval settings, manage sources, and run collection-scoped semantic search.
        """
        return AsyncSettingsResourceWithRawResponse(self._collections.settings)

    @cached_property
    def sources(self) -> AsyncSourcesResourceWithRawResponse:
        """
        Create and manage logical collections of your Telnyx data, tune retrieval settings, manage sources, and run collection-scoped semantic search.
        """
        return AsyncSourcesResourceWithRawResponse(self._collections.sources)


class CollectionsResourceWithStreamingResponse:
    def __init__(self, collections: CollectionsResource) -> None:
        self._collections = collections

        self.create = to_streamed_response_wrapper(
            collections.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            collections.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            collections.update,
        )
        self.list = to_streamed_response_wrapper(
            collections.list,
        )
        self.delete = to_streamed_response_wrapper(
            collections.delete,
        )
        self.retrieve_by_id = to_streamed_response_wrapper(
            collections.retrieve_by_id,
        )
        self.retrieve_documents = to_streamed_response_wrapper(
            collections.retrieve_documents,
        )

    @cached_property
    def settings(self) -> SettingsResourceWithStreamingResponse:
        """
        Create and manage logical collections of your Telnyx data, tune retrieval settings, manage sources, and run collection-scoped semantic search.
        """
        return SettingsResourceWithStreamingResponse(self._collections.settings)

    @cached_property
    def sources(self) -> SourcesResourceWithStreamingResponse:
        """
        Create and manage logical collections of your Telnyx data, tune retrieval settings, manage sources, and run collection-scoped semantic search.
        """
        return SourcesResourceWithStreamingResponse(self._collections.sources)


class AsyncCollectionsResourceWithStreamingResponse:
    def __init__(self, collections: AsyncCollectionsResource) -> None:
        self._collections = collections

        self.create = async_to_streamed_response_wrapper(
            collections.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            collections.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            collections.update,
        )
        self.list = async_to_streamed_response_wrapper(
            collections.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            collections.delete,
        )
        self.retrieve_by_id = async_to_streamed_response_wrapper(
            collections.retrieve_by_id,
        )
        self.retrieve_documents = async_to_streamed_response_wrapper(
            collections.retrieve_documents,
        )

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithStreamingResponse:
        """
        Create and manage logical collections of your Telnyx data, tune retrieval settings, manage sources, and run collection-scoped semantic search.
        """
        return AsyncSettingsResourceWithStreamingResponse(self._collections.settings)

    @cached_property
    def sources(self) -> AsyncSourcesResourceWithStreamingResponse:
        """
        Create and manage logical collections of your Telnyx data, tune retrieval settings, manage sources, and run collection-scoped semantic search.
        """
        return AsyncSourcesResourceWithStreamingResponse(self._collections.sources)

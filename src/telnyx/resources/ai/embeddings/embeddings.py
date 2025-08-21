# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from .buckets import (
    BucketsResource,
    AsyncBucketsResource,
    BucketsResourceWithRawResponse,
    AsyncBucketsResourceWithRawResponse,
    BucketsResourceWithStreamingResponse,
    AsyncBucketsResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.ai import (
    embedding_url_params,
    embedding_list_params,
    embedding_create_params,
    embedding_similarity_search_params,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.ai.embedding_response import EmbeddingResponse
from ....types.ai.embedding_list_response import EmbeddingListResponse
from ....types.ai.embedding_retrieve_response import EmbeddingRetrieveResponse
from ....types.ai.embedding_similarity_search_response import EmbeddingSimilaritySearchResponse

__all__ = ["EmbeddingsResource", "AsyncEmbeddingsResource"]


class EmbeddingsResource(SyncAPIResource):
    @cached_property
    def buckets(self) -> BucketsResource:
        return BucketsResource(self._client)

    @cached_property
    def with_raw_response(self) -> EmbeddingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return EmbeddingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmbeddingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return EmbeddingsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        bucket_name: str,
        document_chunk_overlap_size: int | NotGiven = NOT_GIVEN,
        document_chunk_size: int | NotGiven = NOT_GIVEN,
        embedding_model: Literal["thenlper/gte-large", "intfloat/multilingual-e5-large"] | NotGiven = NOT_GIVEN,
        loader: Literal["default", "intercom"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmbeddingResponse:
        """Perform embedding on a Telnyx Storage Bucket using the a embedding model.

        The
        current supported file types are:

        - PDF
        - HTML
        - txt/unstructured text files
        - json
        - csv
        - audio / video (mp3, mp4, mpeg, mpga, m4a, wav, or webm ) - Max of 100mb file
          size.

        Any files not matching the above types will be attempted to be embedded as
        unstructured text.

        This process can be slow, so it runs in the background and the user can check
        the status of the task using the endpoint `/ai/embeddings/{task_id}`.

        **Important Note**: When you update documents in a Telnyx Storage bucket, their
        associated embeddings are automatically kept up to date. If you add or update a
        file, it is automatically embedded. If you delete a file, the embeddings are
        deleted for that particular file.

        You can also specify a custom `loader` param. Currently the only supported
        loader value is `intercom` which loads Intercom article jsons as specified by
        [the Intercom article API](https://developers.intercom.com/docs/references/rest-api/api.intercom.io/Articles/article/)
        This loader will split each article into paragraphs and save additional
        parameters relevant to Intercom docs, such as `article_url` and `heading`. These
        values will be returned by the `/v2/ai/embeddings/similarity-search` endpoint in
        the `loader_metadata` field.

        Args:
          embedding_model: Supported models to vectorize and embed documents.

          loader: Supported types of custom document loaders for embeddings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/embeddings",
            body=maybe_transform(
                {
                    "bucket_name": bucket_name,
                    "document_chunk_overlap_size": document_chunk_overlap_size,
                    "document_chunk_size": document_chunk_size,
                    "embedding_model": embedding_model,
                    "loader": loader,
                },
                embedding_create_params.EmbeddingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmbeddingResponse,
        )

    def retrieve(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmbeddingRetrieveResponse:
        """Check the status of a current embedding task.

        Will be one of the following:

        - `queued` - Task is waiting to be picked up by a worker
        - `processing` - The embedding task is running
        - `success` - Task completed successfully and the bucket is embedded
        - `failure` - Task failed and no files were embedded successfully
        - `partial_success` - Some files were embedded successfully, but at least one
          failed

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return self._get(
            f"/ai/embeddings/{task_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmbeddingRetrieveResponse,
        )

    def list(
        self,
        *,
        status: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmbeddingListResponse:
        """
        Retrieve tasks for the user that are either `queued`, `processing`, `failed`,
        `success` or `partial_success` based on the query string. Defaults to `queued`
        and `processing`.

        Args:
          status: List of task statuses i.e. `status=queued&status=processing`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/ai/embeddings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"status": status}, embedding_list_params.EmbeddingListParams),
            ),
            cast_to=EmbeddingListResponse,
        )

    def similarity_search(
        self,
        *,
        bucket_name: str,
        query: str,
        num_of_docs: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmbeddingSimilaritySearchResponse:
        """
        Perform a similarity search on a Telnyx Storage Bucket, returning the most
        similar `num_docs` document chunks to the query.

        Currently the only available distance metric is cosine similarity which will
        return a `distance` between 0 and 1. The lower the distance, the more similar
        the returned document chunks are to the query. A `certainty` will also be
        returned, which is a value between 0 and 1 where the higher the certainty, the
        more similar the document. You can read more about Weaviate distance metrics
        here:
        [Weaviate Docs](https://weaviate.io/developers/weaviate/config-refs/distances)

        If a bucket was embedded using a custom loader, such as `intercom`, the
        additional metadata will be returned in the `loader_metadata` field.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/embeddings/similarity-search",
            body=maybe_transform(
                {
                    "bucket_name": bucket_name,
                    "query": query,
                    "num_of_docs": num_of_docs,
                },
                embedding_similarity_search_params.EmbeddingSimilaritySearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmbeddingSimilaritySearchResponse,
        )

    def url(
        self,
        *,
        bucket_name: str,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmbeddingResponse:
        """
        Embed website content from a specified URL, including child pages up to 5 levels
        deep within the same domain. The process crawls and loads content from the main
        URL and its linked pages into a Telnyx Cloud Storage bucket. As soon as each
        webpage is added to the bucket, its content is immediately processed for
        embeddings, that can be used for
        [similarity search](https://developers.telnyx.com/api/inference/inference-embedding/post-embedding-similarity-search)
        and [clustering](https://developers.telnyx.com/docs/inference/clusters).

        Args:
          bucket_name: Name of the bucket to store the embeddings. This bucket must already exist.

          url: The URL of the webpage to embed

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/embeddings/url",
            body=maybe_transform(
                {
                    "bucket_name": bucket_name,
                    "url": url,
                },
                embedding_url_params.EmbeddingURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmbeddingResponse,
        )


class AsyncEmbeddingsResource(AsyncAPIResource):
    @cached_property
    def buckets(self) -> AsyncBucketsResource:
        return AsyncBucketsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEmbeddingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmbeddingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmbeddingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncEmbeddingsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        bucket_name: str,
        document_chunk_overlap_size: int | NotGiven = NOT_GIVEN,
        document_chunk_size: int | NotGiven = NOT_GIVEN,
        embedding_model: Literal["thenlper/gte-large", "intfloat/multilingual-e5-large"] | NotGiven = NOT_GIVEN,
        loader: Literal["default", "intercom"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmbeddingResponse:
        """Perform embedding on a Telnyx Storage Bucket using the a embedding model.

        The
        current supported file types are:

        - PDF
        - HTML
        - txt/unstructured text files
        - json
        - csv
        - audio / video (mp3, mp4, mpeg, mpga, m4a, wav, or webm ) - Max of 100mb file
          size.

        Any files not matching the above types will be attempted to be embedded as
        unstructured text.

        This process can be slow, so it runs in the background and the user can check
        the status of the task using the endpoint `/ai/embeddings/{task_id}`.

        **Important Note**: When you update documents in a Telnyx Storage bucket, their
        associated embeddings are automatically kept up to date. If you add or update a
        file, it is automatically embedded. If you delete a file, the embeddings are
        deleted for that particular file.

        You can also specify a custom `loader` param. Currently the only supported
        loader value is `intercom` which loads Intercom article jsons as specified by
        [the Intercom article API](https://developers.intercom.com/docs/references/rest-api/api.intercom.io/Articles/article/)
        This loader will split each article into paragraphs and save additional
        parameters relevant to Intercom docs, such as `article_url` and `heading`. These
        values will be returned by the `/v2/ai/embeddings/similarity-search` endpoint in
        the `loader_metadata` field.

        Args:
          embedding_model: Supported models to vectorize and embed documents.

          loader: Supported types of custom document loaders for embeddings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/embeddings",
            body=await async_maybe_transform(
                {
                    "bucket_name": bucket_name,
                    "document_chunk_overlap_size": document_chunk_overlap_size,
                    "document_chunk_size": document_chunk_size,
                    "embedding_model": embedding_model,
                    "loader": loader,
                },
                embedding_create_params.EmbeddingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmbeddingResponse,
        )

    async def retrieve(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmbeddingRetrieveResponse:
        """Check the status of a current embedding task.

        Will be one of the following:

        - `queued` - Task is waiting to be picked up by a worker
        - `processing` - The embedding task is running
        - `success` - Task completed successfully and the bucket is embedded
        - `failure` - Task failed and no files were embedded successfully
        - `partial_success` - Some files were embedded successfully, but at least one
          failed

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return await self._get(
            f"/ai/embeddings/{task_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmbeddingRetrieveResponse,
        )

    async def list(
        self,
        *,
        status: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmbeddingListResponse:
        """
        Retrieve tasks for the user that are either `queued`, `processing`, `failed`,
        `success` or `partial_success` based on the query string. Defaults to `queued`
        and `processing`.

        Args:
          status: List of task statuses i.e. `status=queued&status=processing`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/ai/embeddings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"status": status}, embedding_list_params.EmbeddingListParams),
            ),
            cast_to=EmbeddingListResponse,
        )

    async def similarity_search(
        self,
        *,
        bucket_name: str,
        query: str,
        num_of_docs: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmbeddingSimilaritySearchResponse:
        """
        Perform a similarity search on a Telnyx Storage Bucket, returning the most
        similar `num_docs` document chunks to the query.

        Currently the only available distance metric is cosine similarity which will
        return a `distance` between 0 and 1. The lower the distance, the more similar
        the returned document chunks are to the query. A `certainty` will also be
        returned, which is a value between 0 and 1 where the higher the certainty, the
        more similar the document. You can read more about Weaviate distance metrics
        here:
        [Weaviate Docs](https://weaviate.io/developers/weaviate/config-refs/distances)

        If a bucket was embedded using a custom loader, such as `intercom`, the
        additional metadata will be returned in the `loader_metadata` field.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/embeddings/similarity-search",
            body=await async_maybe_transform(
                {
                    "bucket_name": bucket_name,
                    "query": query,
                    "num_of_docs": num_of_docs,
                },
                embedding_similarity_search_params.EmbeddingSimilaritySearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmbeddingSimilaritySearchResponse,
        )

    async def url(
        self,
        *,
        bucket_name: str,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmbeddingResponse:
        """
        Embed website content from a specified URL, including child pages up to 5 levels
        deep within the same domain. The process crawls and loads content from the main
        URL and its linked pages into a Telnyx Cloud Storage bucket. As soon as each
        webpage is added to the bucket, its content is immediately processed for
        embeddings, that can be used for
        [similarity search](https://developers.telnyx.com/api/inference/inference-embedding/post-embedding-similarity-search)
        and [clustering](https://developers.telnyx.com/docs/inference/clusters).

        Args:
          bucket_name: Name of the bucket to store the embeddings. This bucket must already exist.

          url: The URL of the webpage to embed

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/embeddings/url",
            body=await async_maybe_transform(
                {
                    "bucket_name": bucket_name,
                    "url": url,
                },
                embedding_url_params.EmbeddingURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmbeddingResponse,
        )


class EmbeddingsResourceWithRawResponse:
    def __init__(self, embeddings: EmbeddingsResource) -> None:
        self._embeddings = embeddings

        self.create = to_raw_response_wrapper(
            embeddings.create,
        )
        self.retrieve = to_raw_response_wrapper(
            embeddings.retrieve,
        )
        self.list = to_raw_response_wrapper(
            embeddings.list,
        )
        self.similarity_search = to_raw_response_wrapper(
            embeddings.similarity_search,
        )
        self.url = to_raw_response_wrapper(
            embeddings.url,
        )

    @cached_property
    def buckets(self) -> BucketsResourceWithRawResponse:
        return BucketsResourceWithRawResponse(self._embeddings.buckets)


class AsyncEmbeddingsResourceWithRawResponse:
    def __init__(self, embeddings: AsyncEmbeddingsResource) -> None:
        self._embeddings = embeddings

        self.create = async_to_raw_response_wrapper(
            embeddings.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            embeddings.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            embeddings.list,
        )
        self.similarity_search = async_to_raw_response_wrapper(
            embeddings.similarity_search,
        )
        self.url = async_to_raw_response_wrapper(
            embeddings.url,
        )

    @cached_property
    def buckets(self) -> AsyncBucketsResourceWithRawResponse:
        return AsyncBucketsResourceWithRawResponse(self._embeddings.buckets)


class EmbeddingsResourceWithStreamingResponse:
    def __init__(self, embeddings: EmbeddingsResource) -> None:
        self._embeddings = embeddings

        self.create = to_streamed_response_wrapper(
            embeddings.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            embeddings.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            embeddings.list,
        )
        self.similarity_search = to_streamed_response_wrapper(
            embeddings.similarity_search,
        )
        self.url = to_streamed_response_wrapper(
            embeddings.url,
        )

    @cached_property
    def buckets(self) -> BucketsResourceWithStreamingResponse:
        return BucketsResourceWithStreamingResponse(self._embeddings.buckets)


class AsyncEmbeddingsResourceWithStreamingResponse:
    def __init__(self, embeddings: AsyncEmbeddingsResource) -> None:
        self._embeddings = embeddings

        self.create = async_to_streamed_response_wrapper(
            embeddings.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            embeddings.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            embeddings.list,
        )
        self.similarity_search = async_to_streamed_response_wrapper(
            embeddings.similarity_search,
        )
        self.url = async_to_streamed_response_wrapper(
            embeddings.url,
        )

    @cached_property
    def buckets(self) -> AsyncBucketsResourceWithStreamingResponse:
        return AsyncBucketsResourceWithStreamingResponse(self._embeddings.buckets)

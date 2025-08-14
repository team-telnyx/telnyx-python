# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.ai import (
    EmbeddingResponse,
    EmbeddingListResponse,
    EmbeddingRetrieveResponse,
    EmbeddingSimilaritySearchResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmbeddings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        embedding = client.ai.embeddings.create(
            bucket_name="bucket_name",
        )
        assert_matches_type(EmbeddingResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        embedding = client.ai.embeddings.create(
            bucket_name="bucket_name",
            document_chunk_overlap_size=0,
            document_chunk_size=0,
            embedding_model="thenlper/gte-large",
            loader="default",
        )
        assert_matches_type(EmbeddingResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.ai.embeddings.with_raw_response.create(
            bucket_name="bucket_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding = response.parse()
        assert_matches_type(EmbeddingResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.ai.embeddings.with_streaming_response.create(
            bucket_name="bucket_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding = response.parse()
            assert_matches_type(EmbeddingResponse, embedding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        embedding = client.ai.embeddings.retrieve(
            "task_id",
        )
        assert_matches_type(EmbeddingRetrieveResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.ai.embeddings.with_raw_response.retrieve(
            "task_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding = response.parse()
        assert_matches_type(EmbeddingRetrieveResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.ai.embeddings.with_streaming_response.retrieve(
            "task_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding = response.parse()
            assert_matches_type(EmbeddingRetrieveResponse, embedding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.ai.embeddings.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        embedding = client.ai.embeddings.list()
        assert_matches_type(EmbeddingListResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        embedding = client.ai.embeddings.list(
            status=["string"],
        )
        assert_matches_type(EmbeddingListResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.ai.embeddings.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding = response.parse()
        assert_matches_type(EmbeddingListResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.ai.embeddings.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding = response.parse()
            assert_matches_type(EmbeddingListResponse, embedding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_similarity_search(self, client: Telnyx) -> None:
        embedding = client.ai.embeddings.similarity_search(
            bucket_name="bucket_name",
            query="query",
        )
        assert_matches_type(EmbeddingSimilaritySearchResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_similarity_search_with_all_params(self, client: Telnyx) -> None:
        embedding = client.ai.embeddings.similarity_search(
            bucket_name="bucket_name",
            query="query",
            num_of_docs=0,
        )
        assert_matches_type(EmbeddingSimilaritySearchResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_similarity_search(self, client: Telnyx) -> None:
        response = client.ai.embeddings.with_raw_response.similarity_search(
            bucket_name="bucket_name",
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding = response.parse()
        assert_matches_type(EmbeddingSimilaritySearchResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_similarity_search(self, client: Telnyx) -> None:
        with client.ai.embeddings.with_streaming_response.similarity_search(
            bucket_name="bucket_name",
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding = response.parse()
            assert_matches_type(EmbeddingSimilaritySearchResponse, embedding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_url(self, client: Telnyx) -> None:
        embedding = client.ai.embeddings.url(
            bucket_name="bucket_name",
            url="url",
        )
        assert_matches_type(EmbeddingResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_url(self, client: Telnyx) -> None:
        response = client.ai.embeddings.with_raw_response.url(
            bucket_name="bucket_name",
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding = response.parse()
        assert_matches_type(EmbeddingResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_url(self, client: Telnyx) -> None:
        with client.ai.embeddings.with_streaming_response.url(
            bucket_name="bucket_name",
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding = response.parse()
            assert_matches_type(EmbeddingResponse, embedding, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEmbeddings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        embedding = await async_client.ai.embeddings.create(
            bucket_name="bucket_name",
        )
        assert_matches_type(EmbeddingResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        embedding = await async_client.ai.embeddings.create(
            bucket_name="bucket_name",
            document_chunk_overlap_size=0,
            document_chunk_size=0,
            embedding_model="thenlper/gte-large",
            loader="default",
        )
        assert_matches_type(EmbeddingResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.embeddings.with_raw_response.create(
            bucket_name="bucket_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding = await response.parse()
        assert_matches_type(EmbeddingResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.embeddings.with_streaming_response.create(
            bucket_name="bucket_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding = await response.parse()
            assert_matches_type(EmbeddingResponse, embedding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        embedding = await async_client.ai.embeddings.retrieve(
            "task_id",
        )
        assert_matches_type(EmbeddingRetrieveResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.embeddings.with_raw_response.retrieve(
            "task_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding = await response.parse()
        assert_matches_type(EmbeddingRetrieveResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.embeddings.with_streaming_response.retrieve(
            "task_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding = await response.parse()
            assert_matches_type(EmbeddingRetrieveResponse, embedding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.ai.embeddings.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        embedding = await async_client.ai.embeddings.list()
        assert_matches_type(EmbeddingListResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        embedding = await async_client.ai.embeddings.list(
            status=["string"],
        )
        assert_matches_type(EmbeddingListResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.embeddings.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding = await response.parse()
        assert_matches_type(EmbeddingListResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.embeddings.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding = await response.parse()
            assert_matches_type(EmbeddingListResponse, embedding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_similarity_search(self, async_client: AsyncTelnyx) -> None:
        embedding = await async_client.ai.embeddings.similarity_search(
            bucket_name="bucket_name",
            query="query",
        )
        assert_matches_type(EmbeddingSimilaritySearchResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_similarity_search_with_all_params(self, async_client: AsyncTelnyx) -> None:
        embedding = await async_client.ai.embeddings.similarity_search(
            bucket_name="bucket_name",
            query="query",
            num_of_docs=0,
        )
        assert_matches_type(EmbeddingSimilaritySearchResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_similarity_search(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.embeddings.with_raw_response.similarity_search(
            bucket_name="bucket_name",
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding = await response.parse()
        assert_matches_type(EmbeddingSimilaritySearchResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_similarity_search(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.embeddings.with_streaming_response.similarity_search(
            bucket_name="bucket_name",
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding = await response.parse()
            assert_matches_type(EmbeddingSimilaritySearchResponse, embedding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_url(self, async_client: AsyncTelnyx) -> None:
        embedding = await async_client.ai.embeddings.url(
            bucket_name="bucket_name",
            url="url",
        )
        assert_matches_type(EmbeddingResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_url(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.embeddings.with_raw_response.url(
            bucket_name="bucket_name",
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding = await response.parse()
        assert_matches_type(EmbeddingResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_url(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.embeddings.with_streaming_response.url(
            bucket_name="bucket_name",
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding = await response.parse()
            assert_matches_type(EmbeddingResponse, embedding, path=["response"])

        assert cast(Any, response.is_closed) is True

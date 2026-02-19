# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.ai.openai import (
    EmbeddingCreateEmbeddingsResponse,
    EmbeddingListEmbeddingModelsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmbeddings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_embeddings(self, client: Telnyx) -> None:
        embedding = client.ai.openai.embeddings.create_embeddings(
            input="The quick brown fox jumps over the lazy dog",
            model="thenlper/gte-large",
        )
        assert_matches_type(EmbeddingCreateEmbeddingsResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_embeddings_with_all_params(self, client: Telnyx) -> None:
        embedding = client.ai.openai.embeddings.create_embeddings(
            input="The quick brown fox jumps over the lazy dog",
            model="thenlper/gte-large",
            dimensions=0,
            encoding_format="float",
            user="user",
        )
        assert_matches_type(EmbeddingCreateEmbeddingsResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_embeddings(self, client: Telnyx) -> None:
        response = client.ai.openai.embeddings.with_raw_response.create_embeddings(
            input="The quick brown fox jumps over the lazy dog",
            model="thenlper/gte-large",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding = response.parse()
        assert_matches_type(EmbeddingCreateEmbeddingsResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_embeddings(self, client: Telnyx) -> None:
        with client.ai.openai.embeddings.with_streaming_response.create_embeddings(
            input="The quick brown fox jumps over the lazy dog",
            model="thenlper/gte-large",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding = response.parse()
            assert_matches_type(EmbeddingCreateEmbeddingsResponse, embedding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_embedding_models(self, client: Telnyx) -> None:
        embedding = client.ai.openai.embeddings.list_embedding_models()
        assert_matches_type(EmbeddingListEmbeddingModelsResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_embedding_models(self, client: Telnyx) -> None:
        response = client.ai.openai.embeddings.with_raw_response.list_embedding_models()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding = response.parse()
        assert_matches_type(EmbeddingListEmbeddingModelsResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_embedding_models(self, client: Telnyx) -> None:
        with client.ai.openai.embeddings.with_streaming_response.list_embedding_models() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding = response.parse()
            assert_matches_type(EmbeddingListEmbeddingModelsResponse, embedding, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEmbeddings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_embeddings(self, async_client: AsyncTelnyx) -> None:
        embedding = await async_client.ai.openai.embeddings.create_embeddings(
            input="The quick brown fox jumps over the lazy dog",
            model="thenlper/gte-large",
        )
        assert_matches_type(EmbeddingCreateEmbeddingsResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_embeddings_with_all_params(self, async_client: AsyncTelnyx) -> None:
        embedding = await async_client.ai.openai.embeddings.create_embeddings(
            input="The quick brown fox jumps over the lazy dog",
            model="thenlper/gte-large",
            dimensions=0,
            encoding_format="float",
            user="user",
        )
        assert_matches_type(EmbeddingCreateEmbeddingsResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_embeddings(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.openai.embeddings.with_raw_response.create_embeddings(
            input="The quick brown fox jumps over the lazy dog",
            model="thenlper/gte-large",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding = await response.parse()
        assert_matches_type(EmbeddingCreateEmbeddingsResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_embeddings(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.openai.embeddings.with_streaming_response.create_embeddings(
            input="The quick brown fox jumps over the lazy dog",
            model="thenlper/gte-large",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding = await response.parse()
            assert_matches_type(EmbeddingCreateEmbeddingsResponse, embedding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_embedding_models(self, async_client: AsyncTelnyx) -> None:
        embedding = await async_client.ai.openai.embeddings.list_embedding_models()
        assert_matches_type(EmbeddingListEmbeddingModelsResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_embedding_models(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.openai.embeddings.with_raw_response.list_embedding_models()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding = await response.parse()
        assert_matches_type(EmbeddingListEmbeddingModelsResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_embedding_models(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.openai.embeddings.with_streaming_response.list_embedding_models() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding = await response.parse()
            assert_matches_type(EmbeddingListEmbeddingModelsResponse, embedding, path=["response"])

        assert cast(Any, response.is_closed) is True

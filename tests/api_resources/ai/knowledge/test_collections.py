# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.ai.knowledge import CollectionRetrieveDocumentsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCollections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_documents(self, client: Telnyx) -> None:
        collection = client.ai.knowledge.collections.retrieve_documents(
            slug="support-transcripts",
        )
        assert_matches_type(CollectionRetrieveDocumentsResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_documents_with_all_params(self, client: Telnyx) -> None:
        collection = client.ai.knowledge.collections.retrieve_documents(
            slug="support-transcripts",
            filter={"foo": "bar"},
            page_number=1,
            page_size=20,
            query="customer called about billing issue",
            retrieval_type="vector",
            sources="voice,message",
            top_k=10,
        )
        assert_matches_type(CollectionRetrieveDocumentsResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_documents(self, client: Telnyx) -> None:
        response = client.ai.knowledge.collections.with_raw_response.retrieve_documents(
            slug="support-transcripts",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(CollectionRetrieveDocumentsResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_documents(self, client: Telnyx) -> None:
        with client.ai.knowledge.collections.with_streaming_response.retrieve_documents(
            slug="support-transcripts",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(CollectionRetrieveDocumentsResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_documents(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            client.ai.knowledge.collections.with_raw_response.retrieve_documents(
                slug="",
            )


class TestAsyncCollections:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_documents(self, async_client: AsyncTelnyx) -> None:
        collection = await async_client.ai.knowledge.collections.retrieve_documents(
            slug="support-transcripts",
        )
        assert_matches_type(CollectionRetrieveDocumentsResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_documents_with_all_params(self, async_client: AsyncTelnyx) -> None:
        collection = await async_client.ai.knowledge.collections.retrieve_documents(
            slug="support-transcripts",
            filter={"foo": "bar"},
            page_number=1,
            page_size=20,
            query="customer called about billing issue",
            retrieval_type="vector",
            sources="voice,message",
            top_k=10,
        )
        assert_matches_type(CollectionRetrieveDocumentsResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_documents(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.knowledge.collections.with_raw_response.retrieve_documents(
            slug="support-transcripts",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(CollectionRetrieveDocumentsResponse, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_documents(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.knowledge.collections.with_streaming_response.retrieve_documents(
            slug="support-transcripts",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(CollectionRetrieveDocumentsResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_documents(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            await async_client.ai.knowledge.collections.with_raw_response.retrieve_documents(
                slug="",
            )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.ai import (
    Collection,
    CollectionEnvelope,
    CollectionRetrieveDocumentsResponse,
)
from telnyx.pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCollections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        collection = client.ai.collections.create(
            name="Support Transcripts",
        )
        assert_matches_type(CollectionEnvelope, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        collection = client.ai.collections.create(
            name="Support Transcripts",
            description="All customer support voice transcripts.",
            settings={
                "retrieval": {
                    "retrieval_type": "vector",
                    "top_k": 5,
                }
            },
            slug="support-transcripts",
            sources=[
                {
                    "source_type": "voice",
                    "bucket_id": "policy-docs",
                }
            ],
        )
        assert_matches_type(CollectionEnvelope, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.ai.collections.with_raw_response.create(
            name="Support Transcripts",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(CollectionEnvelope, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.ai.collections.with_streaming_response.create(
            name="Support Transcripts",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(CollectionEnvelope, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        collection = client.ai.collections.retrieve(
            "support-transcripts",
        )
        assert_matches_type(CollectionEnvelope, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.ai.collections.with_raw_response.retrieve(
            "support-transcripts",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(CollectionEnvelope, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.ai.collections.with_streaming_response.retrieve(
            "support-transcripts",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(CollectionEnvelope, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            client.ai.collections.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        collection = client.ai.collections.update(
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        )
        assert_matches_type(CollectionEnvelope, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        collection = client.ai.collections.update(
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
            description="Updated description.",
            name="Support Transcripts (2026)",
        )
        assert_matches_type(CollectionEnvelope, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.ai.collections.with_raw_response.update(
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(CollectionEnvelope, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.ai.collections.with_streaming_response.update(
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(CollectionEnvelope, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.ai.collections.with_raw_response.update(
                uuid="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        collection = client.ai.collections.list()
        assert_matches_type(SyncDefaultFlatPagination[Collection], collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        collection = client.ai.collections.list(
            page_number=1,
            page_size=20,
        )
        assert_matches_type(SyncDefaultFlatPagination[Collection], collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.ai.collections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(SyncDefaultFlatPagination[Collection], collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.ai.collections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(SyncDefaultFlatPagination[Collection], collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        collection = client.ai.collections.delete(
            "6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        )
        assert collection is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.ai.collections.with_raw_response.delete(
            "6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert collection is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.ai.collections.with_streaming_response.delete(
            "6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert collection is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.ai.collections.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_by_id(self, client: Telnyx) -> None:
        collection = client.ai.collections.retrieve_by_id(
            "6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        )
        assert_matches_type(CollectionEnvelope, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_by_id(self, client: Telnyx) -> None:
        response = client.ai.collections.with_raw_response.retrieve_by_id(
            "6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(CollectionEnvelope, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_by_id(self, client: Telnyx) -> None:
        with client.ai.collections.with_streaming_response.retrieve_by_id(
            "6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(CollectionEnvelope, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_by_id(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.ai.collections.with_raw_response.retrieve_by_id(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_documents(self, client: Telnyx) -> None:
        collection = client.ai.collections.retrieve_documents(
            slug="support-transcripts",
        )
        assert_matches_type(
            SyncDefaultFlatPagination[CollectionRetrieveDocumentsResponse], collection, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_documents_with_all_params(self, client: Telnyx) -> None:
        collection = client.ai.collections.retrieve_documents(
            slug="support-transcripts",
            filter={"foo": "bar"},
            page_number=1,
            page_size=20,
            query="customer called about billing issue",
            retrieval_type="hybrid",
            sources="voice,message",
            top_k=10,
        )
        assert_matches_type(
            SyncDefaultFlatPagination[CollectionRetrieveDocumentsResponse], collection, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_documents(self, client: Telnyx) -> None:
        response = client.ai.collections.with_raw_response.retrieve_documents(
            slug="support-transcripts",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(
            SyncDefaultFlatPagination[CollectionRetrieveDocumentsResponse], collection, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_documents(self, client: Telnyx) -> None:
        with client.ai.collections.with_streaming_response.retrieve_documents(
            slug="support-transcripts",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(
                SyncDefaultFlatPagination[CollectionRetrieveDocumentsResponse], collection, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_documents(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            client.ai.collections.with_raw_response.retrieve_documents(
                slug="",
            )


class TestAsyncCollections:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        collection = await async_client.ai.collections.create(
            name="Support Transcripts",
        )
        assert_matches_type(CollectionEnvelope, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        collection = await async_client.ai.collections.create(
            name="Support Transcripts",
            description="All customer support voice transcripts.",
            settings={
                "retrieval": {
                    "retrieval_type": "vector",
                    "top_k": 5,
                }
            },
            slug="support-transcripts",
            sources=[
                {
                    "source_type": "voice",
                    "bucket_id": "policy-docs",
                }
            ],
        )
        assert_matches_type(CollectionEnvelope, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.collections.with_raw_response.create(
            name="Support Transcripts",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(CollectionEnvelope, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.collections.with_streaming_response.create(
            name="Support Transcripts",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(CollectionEnvelope, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        collection = await async_client.ai.collections.retrieve(
            "support-transcripts",
        )
        assert_matches_type(CollectionEnvelope, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.collections.with_raw_response.retrieve(
            "support-transcripts",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(CollectionEnvelope, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.collections.with_streaming_response.retrieve(
            "support-transcripts",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(CollectionEnvelope, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            await async_client.ai.collections.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        collection = await async_client.ai.collections.update(
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        )
        assert_matches_type(CollectionEnvelope, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        collection = await async_client.ai.collections.update(
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
            description="Updated description.",
            name="Support Transcripts (2026)",
        )
        assert_matches_type(CollectionEnvelope, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.collections.with_raw_response.update(
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(CollectionEnvelope, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.collections.with_streaming_response.update(
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(CollectionEnvelope, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.ai.collections.with_raw_response.update(
                uuid="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        collection = await async_client.ai.collections.list()
        assert_matches_type(AsyncDefaultFlatPagination[Collection], collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        collection = await async_client.ai.collections.list(
            page_number=1,
            page_size=20,
        )
        assert_matches_type(AsyncDefaultFlatPagination[Collection], collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.collections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(AsyncDefaultFlatPagination[Collection], collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.collections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(AsyncDefaultFlatPagination[Collection], collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        collection = await async_client.ai.collections.delete(
            "6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        )
        assert collection is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.collections.with_raw_response.delete(
            "6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert collection is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.collections.with_streaming_response.delete(
            "6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert collection is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.ai.collections.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_by_id(self, async_client: AsyncTelnyx) -> None:
        collection = await async_client.ai.collections.retrieve_by_id(
            "6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        )
        assert_matches_type(CollectionEnvelope, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_by_id(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.collections.with_raw_response.retrieve_by_id(
            "6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(CollectionEnvelope, collection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_by_id(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.collections.with_streaming_response.retrieve_by_id(
            "6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(CollectionEnvelope, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_by_id(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.ai.collections.with_raw_response.retrieve_by_id(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_documents(self, async_client: AsyncTelnyx) -> None:
        collection = await async_client.ai.collections.retrieve_documents(
            slug="support-transcripts",
        )
        assert_matches_type(
            AsyncDefaultFlatPagination[CollectionRetrieveDocumentsResponse], collection, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_documents_with_all_params(self, async_client: AsyncTelnyx) -> None:
        collection = await async_client.ai.collections.retrieve_documents(
            slug="support-transcripts",
            filter={"foo": "bar"},
            page_number=1,
            page_size=20,
            query="customer called about billing issue",
            retrieval_type="hybrid",
            sources="voice,message",
            top_k=10,
        )
        assert_matches_type(
            AsyncDefaultFlatPagination[CollectionRetrieveDocumentsResponse], collection, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_documents(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.collections.with_raw_response.retrieve_documents(
            slug="support-transcripts",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(
            AsyncDefaultFlatPagination[CollectionRetrieveDocumentsResponse], collection, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_documents(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.collections.with_streaming_response.retrieve_documents(
            slug="support-transcripts",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(
                AsyncDefaultFlatPagination[CollectionRetrieveDocumentsResponse], collection, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_documents(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            await async_client.ai.collections.with_raw_response.retrieve_documents(
                slug="",
            )

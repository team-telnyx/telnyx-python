# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from telnyx.types.ai.memory.namespaces.profiles import MemoryListResponse, MemoryRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMemories:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        memory = client.ai.memory.namespaces.profiles.memories.retrieve(
            memory_id="memory_id",
            namespace="namespace",
            profile_id="profile_id",
        )
        assert_matches_type(MemoryRetrieveResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.ai.memory.namespaces.profiles.memories.with_raw_response.retrieve(
            memory_id="memory_id",
            namespace="namespace",
            profile_id="profile_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(MemoryRetrieveResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.ai.memory.namespaces.profiles.memories.with_streaming_response.retrieve(
            memory_id="memory_id",
            namespace="namespace",
            profile_id="profile_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(MemoryRetrieveResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.ai.memory.namespaces.profiles.memories.with_raw_response.retrieve(
                memory_id="memory_id",
                namespace="",
                profile_id="profile_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.ai.memory.namespaces.profiles.memories.with_raw_response.retrieve(
                memory_id="memory_id",
                namespace="namespace",
                profile_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `memory_id` but received ''"):
            client.ai.memory.namespaces.profiles.memories.with_raw_response.retrieve(
                memory_id="",
                namespace="namespace",
                profile_id="profile_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        memory = client.ai.memory.namespaces.profiles.memories.list(
            profile_id="profile_id",
            namespace="namespace",
        )
        assert_matches_type(SyncDefaultFlatPagination[MemoryListResponse], memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        memory = client.ai.memory.namespaces.profiles.memories.list(
            profile_id="profile_id",
            namespace="namespace",
            page_number=1,
            page_size=1,
            session_id="session_id",
            source_id="source_id",
        )
        assert_matches_type(SyncDefaultFlatPagination[MemoryListResponse], memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.ai.memory.namespaces.profiles.memories.with_raw_response.list(
            profile_id="profile_id",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(SyncDefaultFlatPagination[MemoryListResponse], memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.ai.memory.namespaces.profiles.memories.with_streaming_response.list(
            profile_id="profile_id",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(SyncDefaultFlatPagination[MemoryListResponse], memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.ai.memory.namespaces.profiles.memories.with_raw_response.list(
                profile_id="profile_id",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.ai.memory.namespaces.profiles.memories.with_raw_response.list(
                profile_id="",
                namespace="namespace",
            )


class TestAsyncMemories:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        memory = await async_client.ai.memory.namespaces.profiles.memories.retrieve(
            memory_id="memory_id",
            namespace="namespace",
            profile_id="profile_id",
        )
        assert_matches_type(MemoryRetrieveResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.memory.namespaces.profiles.memories.with_raw_response.retrieve(
            memory_id="memory_id",
            namespace="namespace",
            profile_id="profile_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(MemoryRetrieveResponse, memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.memory.namespaces.profiles.memories.with_streaming_response.retrieve(
            memory_id="memory_id",
            namespace="namespace",
            profile_id="profile_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(MemoryRetrieveResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.ai.memory.namespaces.profiles.memories.with_raw_response.retrieve(
                memory_id="memory_id",
                namespace="",
                profile_id="profile_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.ai.memory.namespaces.profiles.memories.with_raw_response.retrieve(
                memory_id="memory_id",
                namespace="namespace",
                profile_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `memory_id` but received ''"):
            await async_client.ai.memory.namespaces.profiles.memories.with_raw_response.retrieve(
                memory_id="",
                namespace="namespace",
                profile_id="profile_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        memory = await async_client.ai.memory.namespaces.profiles.memories.list(
            profile_id="profile_id",
            namespace="namespace",
        )
        assert_matches_type(AsyncDefaultFlatPagination[MemoryListResponse], memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        memory = await async_client.ai.memory.namespaces.profiles.memories.list(
            profile_id="profile_id",
            namespace="namespace",
            page_number=1,
            page_size=1,
            session_id="session_id",
            source_id="source_id",
        )
        assert_matches_type(AsyncDefaultFlatPagination[MemoryListResponse], memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.memory.namespaces.profiles.memories.with_raw_response.list(
            profile_id="profile_id",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(AsyncDefaultFlatPagination[MemoryListResponse], memory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.memory.namespaces.profiles.memories.with_streaming_response.list(
            profile_id="profile_id",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(AsyncDefaultFlatPagination[MemoryListResponse], memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.ai.memory.namespaces.profiles.memories.with_raw_response.list(
                profile_id="profile_id",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.ai.memory.namespaces.profiles.memories.with_raw_response.list(
                profile_id="",
                namespace="namespace",
            )

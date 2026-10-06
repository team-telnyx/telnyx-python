# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from telnyx.types.ai.assistants import DeletedAssistant

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDeleted:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        deleted = client.ai.assistants.deleted.list()
        assert_matches_type(SyncDefaultFlatPagination[DeletedAssistant], deleted, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        deleted = client.ai.assistants.deleted.list(
            page_number=1,
            page_size=1,
        )
        assert_matches_type(SyncDefaultFlatPagination[DeletedAssistant], deleted, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.ai.assistants.deleted.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deleted = response.parse()
        assert_matches_type(SyncDefaultFlatPagination[DeletedAssistant], deleted, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.ai.assistants.deleted.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deleted = response.parse()
            assert_matches_type(SyncDefaultFlatPagination[DeletedAssistant], deleted, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Telnyx) -> None:
        deleted = client.ai.assistants.deleted.get(
            "assistant_id",
        )
        assert_matches_type(DeletedAssistant, deleted, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Telnyx) -> None:
        response = client.ai.assistants.deleted.with_raw_response.get(
            "assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deleted = response.parse()
        assert_matches_type(DeletedAssistant, deleted, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Telnyx) -> None:
        with client.ai.assistants.deleted.with_streaming_response.get(
            "assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deleted = response.parse()
            assert_matches_type(DeletedAssistant, deleted, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            client.ai.assistants.deleted.with_raw_response.get(
                "",
            )


class TestAsyncDeleted:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        deleted = await async_client.ai.assistants.deleted.list()
        assert_matches_type(AsyncDefaultFlatPagination[DeletedAssistant], deleted, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        deleted = await async_client.ai.assistants.deleted.list(
            page_number=1,
            page_size=1,
        )
        assert_matches_type(AsyncDefaultFlatPagination[DeletedAssistant], deleted, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.assistants.deleted.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deleted = await response.parse()
        assert_matches_type(AsyncDefaultFlatPagination[DeletedAssistant], deleted, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.assistants.deleted.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deleted = await response.parse()
            assert_matches_type(AsyncDefaultFlatPagination[DeletedAssistant], deleted, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncTelnyx) -> None:
        deleted = await async_client.ai.assistants.deleted.get(
            "assistant_id",
        )
        assert_matches_type(DeletedAssistant, deleted, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.assistants.deleted.with_raw_response.get(
            "assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deleted = await response.parse()
        assert_matches_type(DeletedAssistant, deleted, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.assistants.deleted.with_streaming_response.get(
            "assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deleted = await response.parse()
            assert_matches_type(DeletedAssistant, deleted, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            await async_client.ai.assistants.deleted.with_raw_response.get(
                "",
            )

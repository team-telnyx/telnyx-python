# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import StorageListMigrationSourceCoverageResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStorage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_migration_source_coverage(self, client: Telnyx) -> None:
        storage = client.storage.list_migration_source_coverage()
        assert_matches_type(StorageListMigrationSourceCoverageResponse, storage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_migration_source_coverage(self, client: Telnyx) -> None:
        response = client.storage.with_raw_response.list_migration_source_coverage()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        storage = response.parse()
        assert_matches_type(StorageListMigrationSourceCoverageResponse, storage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_migration_source_coverage(self, client: Telnyx) -> None:
        with client.storage.with_streaming_response.list_migration_source_coverage() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            storage = response.parse()
            assert_matches_type(StorageListMigrationSourceCoverageResponse, storage, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStorage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_migration_source_coverage(self, async_client: AsyncTelnyx) -> None:
        storage = await async_client.storage.list_migration_source_coverage()
        assert_matches_type(StorageListMigrationSourceCoverageResponse, storage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_migration_source_coverage(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.storage.with_raw_response.list_migration_source_coverage()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        storage = await response.parse()
        assert_matches_type(StorageListMigrationSourceCoverageResponse, storage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_migration_source_coverage(self, async_client: AsyncTelnyx) -> None:
        async with async_client.storage.with_streaming_response.list_migration_source_coverage() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            storage = await response.parse()
            assert_matches_type(StorageListMigrationSourceCoverageResponse, storage, path=["response"])

        assert cast(Any, response.is_closed) is True

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.storage import (
    MigrationListResponse,
    MigrationCreateResponse,
    MigrationRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMigrations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        migration = client.storage.migrations.create(
            source_id="source_id",
            target_bucket_name="target_bucket_name",
            target_region="target_region",
        )
        assert_matches_type(MigrationCreateResponse, migration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        migration = client.storage.migrations.create(
            source_id="source_id",
            target_bucket_name="target_bucket_name",
            target_region="target_region",
            refresh=True,
        )
        assert_matches_type(MigrationCreateResponse, migration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.storage.migrations.with_raw_response.create(
            source_id="source_id",
            target_bucket_name="target_bucket_name",
            target_region="target_region",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        migration = response.parse()
        assert_matches_type(MigrationCreateResponse, migration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.storage.migrations.with_streaming_response.create(
            source_id="source_id",
            target_bucket_name="target_bucket_name",
            target_region="target_region",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            migration = response.parse()
            assert_matches_type(MigrationCreateResponse, migration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        migration = client.storage.migrations.retrieve(
            "id",
        )
        assert_matches_type(MigrationRetrieveResponse, migration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.storage.migrations.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        migration = response.parse()
        assert_matches_type(MigrationRetrieveResponse, migration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.storage.migrations.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            migration = response.parse()
            assert_matches_type(MigrationRetrieveResponse, migration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.storage.migrations.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        migration = client.storage.migrations.list()
        assert_matches_type(MigrationListResponse, migration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.storage.migrations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        migration = response.parse()
        assert_matches_type(MigrationListResponse, migration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.storage.migrations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            migration = response.parse()
            assert_matches_type(MigrationListResponse, migration, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMigrations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        migration = await async_client.storage.migrations.create(
            source_id="source_id",
            target_bucket_name="target_bucket_name",
            target_region="target_region",
        )
        assert_matches_type(MigrationCreateResponse, migration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        migration = await async_client.storage.migrations.create(
            source_id="source_id",
            target_bucket_name="target_bucket_name",
            target_region="target_region",
            refresh=True,
        )
        assert_matches_type(MigrationCreateResponse, migration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.storage.migrations.with_raw_response.create(
            source_id="source_id",
            target_bucket_name="target_bucket_name",
            target_region="target_region",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        migration = await response.parse()
        assert_matches_type(MigrationCreateResponse, migration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.storage.migrations.with_streaming_response.create(
            source_id="source_id",
            target_bucket_name="target_bucket_name",
            target_region="target_region",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            migration = await response.parse()
            assert_matches_type(MigrationCreateResponse, migration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        migration = await async_client.storage.migrations.retrieve(
            "id",
        )
        assert_matches_type(MigrationRetrieveResponse, migration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.storage.migrations.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        migration = await response.parse()
        assert_matches_type(MigrationRetrieveResponse, migration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.storage.migrations.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            migration = await response.parse()
            assert_matches_type(MigrationRetrieveResponse, migration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.storage.migrations.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        migration = await async_client.storage.migrations.list()
        assert_matches_type(MigrationListResponse, migration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.storage.migrations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        migration = await response.parse()
        assert_matches_type(MigrationListResponse, migration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.storage.migrations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            migration = await response.parse()
            assert_matches_type(MigrationListResponse, migration, path=["response"])

        assert cast(Any, response.is_closed) is True

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.storage import (
    MigrationSourceListResponse,
    MigrationSourceCreateResponse,
    MigrationSourceDeleteResponse,
    MigrationSourceRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMigrationSources:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        migration_source = client.storage.migration_sources.create(
            bucket_name="bucket_name",
            provider="aws",
            provider_auth={},
        )
        assert_matches_type(MigrationSourceCreateResponse, migration_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        migration_source = client.storage.migration_sources.create(
            bucket_name="bucket_name",
            provider="aws",
            provider_auth={
                "access_key": "access_key",
                "secret_access_key": "secret_access_key",
            },
            source_region="source_region",
        )
        assert_matches_type(MigrationSourceCreateResponse, migration_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.storage.migration_sources.with_raw_response.create(
            bucket_name="bucket_name",
            provider="aws",
            provider_auth={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        migration_source = response.parse()
        assert_matches_type(MigrationSourceCreateResponse, migration_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.storage.migration_sources.with_streaming_response.create(
            bucket_name="bucket_name",
            provider="aws",
            provider_auth={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            migration_source = response.parse()
            assert_matches_type(MigrationSourceCreateResponse, migration_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        migration_source = client.storage.migration_sources.retrieve(
            "id",
        )
        assert_matches_type(MigrationSourceRetrieveResponse, migration_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.storage.migration_sources.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        migration_source = response.parse()
        assert_matches_type(MigrationSourceRetrieveResponse, migration_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.storage.migration_sources.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            migration_source = response.parse()
            assert_matches_type(MigrationSourceRetrieveResponse, migration_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.storage.migration_sources.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        migration_source = client.storage.migration_sources.list()
        assert_matches_type(MigrationSourceListResponse, migration_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.storage.migration_sources.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        migration_source = response.parse()
        assert_matches_type(MigrationSourceListResponse, migration_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.storage.migration_sources.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            migration_source = response.parse()
            assert_matches_type(MigrationSourceListResponse, migration_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        migration_source = client.storage.migration_sources.delete(
            "id",
        )
        assert_matches_type(MigrationSourceDeleteResponse, migration_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.storage.migration_sources.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        migration_source = response.parse()
        assert_matches_type(MigrationSourceDeleteResponse, migration_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.storage.migration_sources.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            migration_source = response.parse()
            assert_matches_type(MigrationSourceDeleteResponse, migration_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.storage.migration_sources.with_raw_response.delete(
                "",
            )


class TestAsyncMigrationSources:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        migration_source = await async_client.storage.migration_sources.create(
            bucket_name="bucket_name",
            provider="aws",
            provider_auth={},
        )
        assert_matches_type(MigrationSourceCreateResponse, migration_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        migration_source = await async_client.storage.migration_sources.create(
            bucket_name="bucket_name",
            provider="aws",
            provider_auth={
                "access_key": "access_key",
                "secret_access_key": "secret_access_key",
            },
            source_region="source_region",
        )
        assert_matches_type(MigrationSourceCreateResponse, migration_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.storage.migration_sources.with_raw_response.create(
            bucket_name="bucket_name",
            provider="aws",
            provider_auth={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        migration_source = await response.parse()
        assert_matches_type(MigrationSourceCreateResponse, migration_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.storage.migration_sources.with_streaming_response.create(
            bucket_name="bucket_name",
            provider="aws",
            provider_auth={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            migration_source = await response.parse()
            assert_matches_type(MigrationSourceCreateResponse, migration_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        migration_source = await async_client.storage.migration_sources.retrieve(
            "id",
        )
        assert_matches_type(MigrationSourceRetrieveResponse, migration_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.storage.migration_sources.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        migration_source = await response.parse()
        assert_matches_type(MigrationSourceRetrieveResponse, migration_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.storage.migration_sources.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            migration_source = await response.parse()
            assert_matches_type(MigrationSourceRetrieveResponse, migration_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.storage.migration_sources.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        migration_source = await async_client.storage.migration_sources.list()
        assert_matches_type(MigrationSourceListResponse, migration_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.storage.migration_sources.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        migration_source = await response.parse()
        assert_matches_type(MigrationSourceListResponse, migration_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.storage.migration_sources.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            migration_source = await response.parse()
            assert_matches_type(MigrationSourceListResponse, migration_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        migration_source = await async_client.storage.migration_sources.delete(
            "id",
        )
        assert_matches_type(MigrationSourceDeleteResponse, migration_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.storage.migration_sources.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        migration_source = await response.parse()
        assert_matches_type(MigrationSourceDeleteResponse, migration_source, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.storage.migration_sources.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            migration_source = await response.parse()
            assert_matches_type(MigrationSourceDeleteResponse, migration_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.storage.migration_sources.with_raw_response.delete(
                "",
            )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.enterprises import (
    ReputationListResponse,
    ReputationCreateResponse,
    ReputationUpdateFrequencyResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReputation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        reputation = client.enterprises.reputation.create(
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            loa_document_id="doc_01HXYZ1234ABCDEF",
        )
        assert_matches_type(ReputationCreateResponse, reputation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        reputation = client.enterprises.reputation.create(
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            loa_document_id="doc_01HXYZ1234ABCDEF",
            check_frequency="business_daily",
        )
        assert_matches_type(ReputationCreateResponse, reputation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.enterprises.reputation.with_raw_response.create(
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            loa_document_id="doc_01HXYZ1234ABCDEF",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reputation = response.parse()
        assert_matches_type(ReputationCreateResponse, reputation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.enterprises.reputation.with_streaming_response.create(
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            loa_document_id="doc_01HXYZ1234ABCDEF",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reputation = response.parse()
            assert_matches_type(ReputationCreateResponse, reputation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            client.enterprises.reputation.with_raw_response.create(
                enterprise_id="",
                loa_document_id="doc_01HXYZ1234ABCDEF",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        reputation = client.enterprises.reputation.list(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(ReputationListResponse, reputation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.enterprises.reputation.with_raw_response.list(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reputation = response.parse()
        assert_matches_type(ReputationListResponse, reputation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.enterprises.reputation.with_streaming_response.list(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reputation = response.parse()
            assert_matches_type(ReputationListResponse, reputation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            client.enterprises.reputation.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_all(self, client: Telnyx) -> None:
        reputation = client.enterprises.reputation.delete_all(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert reputation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_all(self, client: Telnyx) -> None:
        response = client.enterprises.reputation.with_raw_response.delete_all(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reputation = response.parse()
        assert reputation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_all(self, client: Telnyx) -> None:
        with client.enterprises.reputation.with_streaming_response.delete_all(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reputation = response.parse()
            assert reputation is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_all(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            client.enterprises.reputation.with_raw_response.delete_all(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_frequency(self, client: Telnyx) -> None:
        reputation = client.enterprises.reputation.update_frequency(
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            check_frequency="business_daily",
        )
        assert_matches_type(ReputationUpdateFrequencyResponse, reputation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_frequency(self, client: Telnyx) -> None:
        response = client.enterprises.reputation.with_raw_response.update_frequency(
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            check_frequency="business_daily",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reputation = response.parse()
        assert_matches_type(ReputationUpdateFrequencyResponse, reputation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_frequency(self, client: Telnyx) -> None:
        with client.enterprises.reputation.with_streaming_response.update_frequency(
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            check_frequency="business_daily",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reputation = response.parse()
            assert_matches_type(ReputationUpdateFrequencyResponse, reputation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_frequency(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            client.enterprises.reputation.with_raw_response.update_frequency(
                enterprise_id="",
                check_frequency="business_daily",
            )


class TestAsyncReputation:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        reputation = await async_client.enterprises.reputation.create(
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            loa_document_id="doc_01HXYZ1234ABCDEF",
        )
        assert_matches_type(ReputationCreateResponse, reputation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        reputation = await async_client.enterprises.reputation.create(
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            loa_document_id="doc_01HXYZ1234ABCDEF",
            check_frequency="business_daily",
        )
        assert_matches_type(ReputationCreateResponse, reputation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.enterprises.reputation.with_raw_response.create(
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            loa_document_id="doc_01HXYZ1234ABCDEF",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reputation = await response.parse()
        assert_matches_type(ReputationCreateResponse, reputation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.enterprises.reputation.with_streaming_response.create(
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            loa_document_id="doc_01HXYZ1234ABCDEF",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reputation = await response.parse()
            assert_matches_type(ReputationCreateResponse, reputation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            await async_client.enterprises.reputation.with_raw_response.create(
                enterprise_id="",
                loa_document_id="doc_01HXYZ1234ABCDEF",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        reputation = await async_client.enterprises.reputation.list(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(ReputationListResponse, reputation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.enterprises.reputation.with_raw_response.list(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reputation = await response.parse()
        assert_matches_type(ReputationListResponse, reputation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.enterprises.reputation.with_streaming_response.list(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reputation = await response.parse()
            assert_matches_type(ReputationListResponse, reputation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            await async_client.enterprises.reputation.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_all(self, async_client: AsyncTelnyx) -> None:
        reputation = await async_client.enterprises.reputation.delete_all(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert reputation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_all(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.enterprises.reputation.with_raw_response.delete_all(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reputation = await response.parse()
        assert reputation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_all(self, async_client: AsyncTelnyx) -> None:
        async with async_client.enterprises.reputation.with_streaming_response.delete_all(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reputation = await response.parse()
            assert reputation is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_all(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            await async_client.enterprises.reputation.with_raw_response.delete_all(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_frequency(self, async_client: AsyncTelnyx) -> None:
        reputation = await async_client.enterprises.reputation.update_frequency(
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            check_frequency="business_daily",
        )
        assert_matches_type(ReputationUpdateFrequencyResponse, reputation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_frequency(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.enterprises.reputation.with_raw_response.update_frequency(
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            check_frequency="business_daily",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reputation = await response.parse()
        assert_matches_type(ReputationUpdateFrequencyResponse, reputation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_frequency(self, async_client: AsyncTelnyx) -> None:
        async with async_client.enterprises.reputation.with_streaming_response.update_frequency(
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            check_frequency="business_daily",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reputation = await response.parse()
            assert_matches_type(ReputationUpdateFrequencyResponse, reputation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_frequency(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            await async_client.enterprises.reputation.with_raw_response.update_frequency(
                enterprise_id="",
                check_frequency="business_daily",
            )

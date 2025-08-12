# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import OtaUpdateListResponse, OtaUpdateRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOtaUpdates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        ota_update = client.ota_updates.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(OtaUpdateRetrieveResponse, ota_update, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.ota_updates.with_raw_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ota_update = response.parse()
        assert_matches_type(OtaUpdateRetrieveResponse, ota_update, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.ota_updates.with_streaming_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ota_update = response.parse()
            assert_matches_type(OtaUpdateRetrieveResponse, ota_update, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ota_updates.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        ota_update = client.ota_updates.list()
        assert_matches_type(OtaUpdateListResponse, ota_update, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        ota_update = client.ota_updates.list(
            filter={
                "sim_card_id": "sim_card_id",
                "status": "in-progress",
                "type": "sim_card_network_preferences",
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(OtaUpdateListResponse, ota_update, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.ota_updates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ota_update = response.parse()
        assert_matches_type(OtaUpdateListResponse, ota_update, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.ota_updates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ota_update = response.parse()
            assert_matches_type(OtaUpdateListResponse, ota_update, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOtaUpdates:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        ota_update = await async_client.ota_updates.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(OtaUpdateRetrieveResponse, ota_update, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ota_updates.with_raw_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ota_update = await response.parse()
        assert_matches_type(OtaUpdateRetrieveResponse, ota_update, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ota_updates.with_streaming_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ota_update = await response.parse()
            assert_matches_type(OtaUpdateRetrieveResponse, ota_update, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ota_updates.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        ota_update = await async_client.ota_updates.list()
        assert_matches_type(OtaUpdateListResponse, ota_update, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        ota_update = await async_client.ota_updates.list(
            filter={
                "sim_card_id": "sim_card_id",
                "status": "in-progress",
                "type": "sim_card_network_preferences",
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(OtaUpdateListResponse, ota_update, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ota_updates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ota_update = await response.parse()
        assert_matches_type(OtaUpdateListResponse, ota_update, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ota_updates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ota_update = await response.parse()
            assert_matches_type(OtaUpdateListResponse, ota_update, path=["response"])

        assert cast(Any, response.is_closed) is True

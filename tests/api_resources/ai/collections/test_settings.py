# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.ai.collections import (
    SettingsEnvelope,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSettings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        setting = client.ai.collections.settings.create(
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        )
        assert_matches_type(SettingsEnvelope, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        setting = client.ai.collections.settings.create(
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
            retrieval={
                "retrieval_type": "vector",
                "top_k": 5,
            },
        )
        assert_matches_type(SettingsEnvelope, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.ai.collections.settings.with_raw_response.create(
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(SettingsEnvelope, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.ai.collections.settings.with_streaming_response.create(
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(SettingsEnvelope, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.ai.collections.settings.with_raw_response.create(
                uuid="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        setting = client.ai.collections.settings.list(
            "6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        )
        assert_matches_type(SettingsEnvelope, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.ai.collections.settings.with_raw_response.list(
            "6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(SettingsEnvelope, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.ai.collections.settings.with_streaming_response.list(
            "6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(SettingsEnvelope, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.ai.collections.settings.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_patch_all(self, client: Telnyx) -> None:
        setting = client.ai.collections.settings.patch_all(
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        )
        assert_matches_type(SettingsEnvelope, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_patch_all_with_all_params(self, client: Telnyx) -> None:
        setting = client.ai.collections.settings.patch_all(
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
            retrieval={
                "retrieval_type": "vector",
                "top_k": 5,
            },
        )
        assert_matches_type(SettingsEnvelope, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_patch_all(self, client: Telnyx) -> None:
        response = client.ai.collections.settings.with_raw_response.patch_all(
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(SettingsEnvelope, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_patch_all(self, client: Telnyx) -> None:
        with client.ai.collections.settings.with_streaming_response.patch_all(
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(SettingsEnvelope, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_patch_all(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.ai.collections.settings.with_raw_response.patch_all(
                uuid="",
            )


class TestAsyncSettings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        setting = await async_client.ai.collections.settings.create(
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        )
        assert_matches_type(SettingsEnvelope, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        setting = await async_client.ai.collections.settings.create(
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
            retrieval={
                "retrieval_type": "vector",
                "top_k": 5,
            },
        )
        assert_matches_type(SettingsEnvelope, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.collections.settings.with_raw_response.create(
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(SettingsEnvelope, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.collections.settings.with_streaming_response.create(
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(SettingsEnvelope, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.ai.collections.settings.with_raw_response.create(
                uuid="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        setting = await async_client.ai.collections.settings.list(
            "6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        )
        assert_matches_type(SettingsEnvelope, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.collections.settings.with_raw_response.list(
            "6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(SettingsEnvelope, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.collections.settings.with_streaming_response.list(
            "6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(SettingsEnvelope, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.ai.collections.settings.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_patch_all(self, async_client: AsyncTelnyx) -> None:
        setting = await async_client.ai.collections.settings.patch_all(
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        )
        assert_matches_type(SettingsEnvelope, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_patch_all_with_all_params(self, async_client: AsyncTelnyx) -> None:
        setting = await async_client.ai.collections.settings.patch_all(
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
            retrieval={
                "retrieval_type": "vector",
                "top_k": 5,
            },
        )
        assert_matches_type(SettingsEnvelope, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_patch_all(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.collections.settings.with_raw_response.patch_all(
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(SettingsEnvelope, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_patch_all(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.collections.settings.with_streaming_response.patch_all(
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(SettingsEnvelope, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_patch_all(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.ai.collections.settings.with_raw_response.patch_all(
                uuid="",
            )

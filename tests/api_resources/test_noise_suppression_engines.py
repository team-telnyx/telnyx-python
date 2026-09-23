# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import NoiseSuppressionEngineListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNoiseSuppressionEngines:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        noise_suppression_engine = client.noise_suppression_engines.list()
        assert_matches_type(NoiseSuppressionEngineListResponse, noise_suppression_engine, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.noise_suppression_engines.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        noise_suppression_engine = response.parse()
        assert_matches_type(NoiseSuppressionEngineListResponse, noise_suppression_engine, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.noise_suppression_engines.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            noise_suppression_engine = response.parse()
            assert_matches_type(NoiseSuppressionEngineListResponse, noise_suppression_engine, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncNoiseSuppressionEngines:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        noise_suppression_engine = await async_client.noise_suppression_engines.list()
        assert_matches_type(NoiseSuppressionEngineListResponse, noise_suppression_engine, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.noise_suppression_engines.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        noise_suppression_engine = await response.parse()
        assert_matches_type(NoiseSuppressionEngineListResponse, noise_suppression_engine, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.noise_suppression_engines.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            noise_suppression_engine = await response.parse()
            assert_matches_type(NoiseSuppressionEngineListResponse, noise_suppression_engine, path=["response"])

        assert cast(Any, response.is_closed) is True

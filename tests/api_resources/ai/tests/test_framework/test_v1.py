# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.ai.tests.test_framework import V1RetrievePersonalitiesResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV1:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_personalities(self, client: Telnyx) -> None:
        v1 = client.ai.tests.test_framework.v1.retrieve_personalities()
        assert_matches_type(V1RetrievePersonalitiesResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_personalities(self, client: Telnyx) -> None:
        response = client.ai.tests.test_framework.v1.with_raw_response.retrieve_personalities()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1RetrievePersonalitiesResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_personalities(self, client: Telnyx) -> None:
        with client.ai.tests.test_framework.v1.with_streaming_response.retrieve_personalities() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1RetrievePersonalitiesResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncV1:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_personalities(self, async_client: AsyncTelnyx) -> None:
        v1 = await async_client.ai.tests.test_framework.v1.retrieve_personalities()
        assert_matches_type(V1RetrievePersonalitiesResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_personalities(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.tests.test_framework.v1.with_raw_response.retrieve_personalities()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1RetrievePersonalitiesResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_personalities(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.tests.test_framework.v1.with_streaming_response.retrieve_personalities() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1RetrievePersonalitiesResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

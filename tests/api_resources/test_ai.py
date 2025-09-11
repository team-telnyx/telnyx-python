# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import AISummarizeResponse, AIRetrieveModelsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAI:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_models(self, client: Telnyx) -> None:
        ai = client.ai.retrieve_models()
        assert_matches_type(AIRetrieveModelsResponse, ai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_models(self, client: Telnyx) -> None:
        response = client.ai.with_raw_response.retrieve_models()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(AIRetrieveModelsResponse, ai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_models(self, client: Telnyx) -> None:
        with client.ai.with_streaming_response.retrieve_models() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(AIRetrieveModelsResponse, ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_summarize(self, client: Telnyx) -> None:
        ai = client.ai.summarize(
            bucket="bucket",
            filename="filename",
        )
        assert_matches_type(AISummarizeResponse, ai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_summarize_with_all_params(self, client: Telnyx) -> None:
        ai = client.ai.summarize(
            bucket="bucket",
            filename="filename",
            system_prompt="system_prompt",
        )
        assert_matches_type(AISummarizeResponse, ai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_summarize(self, client: Telnyx) -> None:
        response = client.ai.with_raw_response.summarize(
            bucket="bucket",
            filename="filename",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(AISummarizeResponse, ai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_summarize(self, client: Telnyx) -> None:
        with client.ai.with_streaming_response.summarize(
            bucket="bucket",
            filename="filename",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(AISummarizeResponse, ai, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAI:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_models(self, async_client: AsyncTelnyx) -> None:
        ai = await async_client.ai.retrieve_models()
        assert_matches_type(AIRetrieveModelsResponse, ai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_models(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.with_raw_response.retrieve_models()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(AIRetrieveModelsResponse, ai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_models(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.with_streaming_response.retrieve_models() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(AIRetrieveModelsResponse, ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_summarize(self, async_client: AsyncTelnyx) -> None:
        ai = await async_client.ai.summarize(
            bucket="bucket",
            filename="filename",
        )
        assert_matches_type(AISummarizeResponse, ai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_summarize_with_all_params(self, async_client: AsyncTelnyx) -> None:
        ai = await async_client.ai.summarize(
            bucket="bucket",
            filename="filename",
            system_prompt="system_prompt",
        )
        assert_matches_type(AISummarizeResponse, ai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_summarize(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.with_raw_response.summarize(
            bucket="bucket",
            filename="filename",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(AISummarizeResponse, ai, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_summarize(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.with_streaming_response.summarize(
            bucket="bucket",
            filename="filename",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(AISummarizeResponse, ai, path=["response"])

        assert cast(Any, response.is_closed) is True

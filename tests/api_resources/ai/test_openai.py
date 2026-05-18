# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.ai import OpenAIListModelsResponse, OpenAICreateResponseResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOpenAI:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_response(self, client: Telnyx) -> None:
        openai = client.ai.openai.create_response()
        assert_matches_type(OpenAICreateResponseResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_response_with_all_params(self, client: Telnyx) -> None:
        openai = client.ai.openai.create_response(
            conversation="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            input=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": "Hello, world!",
                        }
                    ],
                }
            ],
            instructions="You are a friendly chatbot.",
            model="zai-org/GLM-5.1-FP8",
            stream=True,
        )
        assert_matches_type(OpenAICreateResponseResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_response(self, client: Telnyx) -> None:
        response = client.ai.openai.with_raw_response.create_response()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        openai = response.parse()
        assert_matches_type(OpenAICreateResponseResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_response(self, client: Telnyx) -> None:
        with client.ai.openai.with_streaming_response.create_response() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            openai = response.parse()
            assert_matches_type(OpenAICreateResponseResponse, openai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_models(self, client: Telnyx) -> None:
        openai = client.ai.openai.list_models()
        assert_matches_type(OpenAIListModelsResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_models(self, client: Telnyx) -> None:
        response = client.ai.openai.with_raw_response.list_models()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        openai = response.parse()
        assert_matches_type(OpenAIListModelsResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_models(self, client: Telnyx) -> None:
        with client.ai.openai.with_streaming_response.list_models() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            openai = response.parse()
            assert_matches_type(OpenAIListModelsResponse, openai, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOpenAI:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_response(self, async_client: AsyncTelnyx) -> None:
        openai = await async_client.ai.openai.create_response()
        assert_matches_type(OpenAICreateResponseResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_response_with_all_params(self, async_client: AsyncTelnyx) -> None:
        openai = await async_client.ai.openai.create_response(
            conversation="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            input=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": "Hello, world!",
                        }
                    ],
                }
            ],
            instructions="You are a friendly chatbot.",
            model="zai-org/GLM-5.1-FP8",
            stream=True,
        )
        assert_matches_type(OpenAICreateResponseResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_response(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.openai.with_raw_response.create_response()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        openai = await response.parse()
        assert_matches_type(OpenAICreateResponseResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_response(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.openai.with_streaming_response.create_response() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            openai = await response.parse()
            assert_matches_type(OpenAICreateResponseResponse, openai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_models(self, async_client: AsyncTelnyx) -> None:
        openai = await async_client.ai.openai.list_models()
        assert_matches_type(OpenAIListModelsResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_models(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.openai.with_raw_response.list_models()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        openai = await response.parse()
        assert_matches_type(OpenAIListModelsResponse, openai, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_models(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.openai.with_streaming_response.list_models() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            openai = await response.parse()
            assert_matches_type(OpenAIListModelsResponse, openai, path=["response"])

        assert cast(Any, response.is_closed) is True

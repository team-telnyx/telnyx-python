# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChat:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_completion(self, client: Telnyx) -> None:
        chat = client.ai.chat.create_completion(
            messages=[
                {
                    "content": "You are a friendly chatbot.",
                    "role": "system",
                },
                {
                    "content": "Hello, world!",
                    "role": "user",
                },
            ],
        )
        assert_matches_type(object, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_completion_with_all_params(self, client: Telnyx) -> None:
        chat = client.ai.chat.create_completion(
            messages=[
                {
                    "content": "You are a friendly chatbot.",
                    "role": "system",
                },
                {
                    "content": "Hello, world!",
                    "role": "user",
                },
            ],
            api_key_ref="api_key_ref",
            best_of=0,
            early_stopping=True,
            frequency_penalty=0,
            guided_choice=["string"],
            guided_json={"foo": "bar"},
            guided_regex="guided_regex",
            length_penalty=0,
            logprobs=True,
            max_tokens=0,
            min_p=0,
            model="model",
            n=0,
            presence_penalty=0,
            response_format={"type": "text"},
            stream=True,
            temperature=0,
            tool_choice="none",
            tools=[
                {
                    "function": {
                        "name": "name",
                        "description": "description",
                        "parameters": {"foo": "bar"},
                    },
                    "type": "function",
                }
            ],
            top_logprobs=0,
            top_p=0,
            use_beam_search=True,
        )
        assert_matches_type(object, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_completion(self, client: Telnyx) -> None:
        response = client.ai.chat.with_raw_response.create_completion(
            messages=[
                {
                    "content": "You are a friendly chatbot.",
                    "role": "system",
                },
                {
                    "content": "Hello, world!",
                    "role": "user",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(object, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_completion(self, client: Telnyx) -> None:
        with client.ai.chat.with_streaming_response.create_completion(
            messages=[
                {
                    "content": "You are a friendly chatbot.",
                    "role": "system",
                },
                {
                    "content": "Hello, world!",
                    "role": "user",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(object, chat, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncChat:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_completion(self, async_client: AsyncTelnyx) -> None:
        chat = await async_client.ai.chat.create_completion(
            messages=[
                {
                    "content": "You are a friendly chatbot.",
                    "role": "system",
                },
                {
                    "content": "Hello, world!",
                    "role": "user",
                },
            ],
        )
        assert_matches_type(object, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_completion_with_all_params(self, async_client: AsyncTelnyx) -> None:
        chat = await async_client.ai.chat.create_completion(
            messages=[
                {
                    "content": "You are a friendly chatbot.",
                    "role": "system",
                },
                {
                    "content": "Hello, world!",
                    "role": "user",
                },
            ],
            api_key_ref="api_key_ref",
            best_of=0,
            early_stopping=True,
            frequency_penalty=0,
            guided_choice=["string"],
            guided_json={"foo": "bar"},
            guided_regex="guided_regex",
            length_penalty=0,
            logprobs=True,
            max_tokens=0,
            min_p=0,
            model="model",
            n=0,
            presence_penalty=0,
            response_format={"type": "text"},
            stream=True,
            temperature=0,
            tool_choice="none",
            tools=[
                {
                    "function": {
                        "name": "name",
                        "description": "description",
                        "parameters": {"foo": "bar"},
                    },
                    "type": "function",
                }
            ],
            top_logprobs=0,
            top_p=0,
            use_beam_search=True,
        )
        assert_matches_type(object, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_completion(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.chat.with_raw_response.create_completion(
            messages=[
                {
                    "content": "You are a friendly chatbot.",
                    "role": "system",
                },
                {
                    "content": "Hello, world!",
                    "role": "user",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(object, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_completion(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.chat.with_streaming_response.create_completion(
            messages=[
                {
                    "content": "You are a friendly chatbot.",
                    "role": "system",
                },
                {
                    "content": "Hello, world!",
                    "role": "user",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(object, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

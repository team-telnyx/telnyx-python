# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.ai.anthropic import V1MessagesResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV1:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_messages(self, client: Telnyx) -> None:
        v1 = client.ai.anthropic.v1.messages(
            max_tokens=1024,
            messages=[
                {
                    "role": "bar",
                    "content": "bar",
                }
            ],
            model="zai-org/GLM-5.2",
        )
        assert_matches_type(V1MessagesResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_messages_with_all_params(self, client: Telnyx) -> None:
        v1 = client.ai.anthropic.v1.messages(
            max_tokens=1024,
            messages=[
                {
                    "role": "bar",
                    "content": "bar",
                }
            ],
            model="zai-org/GLM-5.2",
            api_key_ref="api_key_ref",
            billing_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            fallback_config={"foo": "bar"},
            max_retries=0,
            mcp_servers=[{"foo": "bar"}],
            metadata={"foo": "bar"},
            service_tier="service_tier",
            stop_sequences=["string"],
            stream=True,
            system="You are a friendly chatbot.",
            temperature=0,
            thinking={"foo": "bar"},
            api_timeout=0,
            tool_choice={"foo": "bar"},
            tools=[{"foo": "bar"}],
            top_k=0,
            top_p=0,
        )
        assert_matches_type(V1MessagesResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_messages(self, client: Telnyx) -> None:
        response = client.ai.anthropic.v1.with_raw_response.messages(
            max_tokens=1024,
            messages=[
                {
                    "role": "bar",
                    "content": "bar",
                }
            ],
            model="zai-org/GLM-5.2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1MessagesResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_messages(self, client: Telnyx) -> None:
        with client.ai.anthropic.v1.with_streaming_response.messages(
            max_tokens=1024,
            messages=[
                {
                    "role": "bar",
                    "content": "bar",
                }
            ],
            model="zai-org/GLM-5.2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1MessagesResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncV1:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_messages(self, async_client: AsyncTelnyx) -> None:
        v1 = await async_client.ai.anthropic.v1.messages(
            max_tokens=1024,
            messages=[
                {
                    "role": "bar",
                    "content": "bar",
                }
            ],
            model="zai-org/GLM-5.2",
        )
        assert_matches_type(V1MessagesResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_messages_with_all_params(self, async_client: AsyncTelnyx) -> None:
        v1 = await async_client.ai.anthropic.v1.messages(
            max_tokens=1024,
            messages=[
                {
                    "role": "bar",
                    "content": "bar",
                }
            ],
            model="zai-org/GLM-5.2",
            api_key_ref="api_key_ref",
            billing_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            fallback_config={"foo": "bar"},
            max_retries=0,
            mcp_servers=[{"foo": "bar"}],
            metadata={"foo": "bar"},
            service_tier="service_tier",
            stop_sequences=["string"],
            stream=True,
            system="You are a friendly chatbot.",
            temperature=0,
            thinking={"foo": "bar"},
            api_timeout=0,
            tool_choice={"foo": "bar"},
            tools=[{"foo": "bar"}],
            top_k=0,
            top_p=0,
        )
        assert_matches_type(V1MessagesResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_messages(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.anthropic.v1.with_raw_response.messages(
            max_tokens=1024,
            messages=[
                {
                    "role": "bar",
                    "content": "bar",
                }
            ],
            model="zai-org/GLM-5.2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1MessagesResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_messages(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.anthropic.v1.with_streaming_response.messages(
            max_tokens=1024,
            messages=[
                {
                    "role": "bar",
                    "content": "bar",
                }
            ],
            model="zai-org/GLM-5.2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1MessagesResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

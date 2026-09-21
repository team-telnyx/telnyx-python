# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import BotChallengeCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBotChallenge:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        bot_challenge = client.bot_challenge.create()
        assert_matches_type(BotChallengeCreateResponse, bot_challenge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        bot_challenge = client.bot_challenge.create(
            llm_model_name="claude-opus-4",
            llm_parameter_count="175B",
            llm_quantization="int8",
        )
        assert_matches_type(BotChallengeCreateResponse, bot_challenge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.bot_challenge.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot_challenge = response.parse()
        assert_matches_type(BotChallengeCreateResponse, bot_challenge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.bot_challenge.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot_challenge = response.parse()
            assert_matches_type(BotChallengeCreateResponse, bot_challenge, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBotChallenge:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        bot_challenge = await async_client.bot_challenge.create()
        assert_matches_type(BotChallengeCreateResponse, bot_challenge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        bot_challenge = await async_client.bot_challenge.create(
            llm_model_name="claude-opus-4",
            llm_parameter_count="175B",
            llm_quantization="int8",
        )
        assert_matches_type(BotChallengeCreateResponse, bot_challenge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.bot_challenge.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot_challenge = await response.parse()
        assert_matches_type(BotChallengeCreateResponse, bot_challenge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.bot_challenge.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot_challenge = await response.parse()
            assert_matches_type(BotChallengeCreateResponse, bot_challenge, path=["response"])

        assert cast(Any, response.is_closed) is True

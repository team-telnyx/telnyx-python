# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import SuccessResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBotSignup:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        bot_signup = client.bot_signup.create(
            bot_challenge_answer="35",
            bot_challenge_nonce="c6feda4e-6501-4db9-a21f-665e5b4ce2ba",
            privacy_policy_url="https://telnyx.com/privacy-policy",
            terms_and_conditions_url="https://telnyx.com/terms-and-conditions-of-service",
            terms_of_service=True,
        )
        assert_matches_type(SuccessResponse, bot_signup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        bot_signup = client.bot_signup.create(
            bot_challenge_answer="35",
            bot_challenge_nonce="c6feda4e-6501-4db9-a21f-665e5b4ce2ba",
            privacy_policy_url="https://telnyx.com/privacy-policy",
            terms_and_conditions_url="https://telnyx.com/terms-and-conditions-of-service",
            terms_of_service=True,
            email="agent-owner@example.com",
            terms_and_conditions_eu_url="https://telnyx.com/terms-and-conditions-of-service-eu",
            terms_of_service_eu=True,
        )
        assert_matches_type(SuccessResponse, bot_signup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.bot_signup.with_raw_response.create(
            bot_challenge_answer="35",
            bot_challenge_nonce="c6feda4e-6501-4db9-a21f-665e5b4ce2ba",
            privacy_policy_url="https://telnyx.com/privacy-policy",
            terms_and_conditions_url="https://telnyx.com/terms-and-conditions-of-service",
            terms_of_service=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot_signup = response.parse()
        assert_matches_type(SuccessResponse, bot_signup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.bot_signup.with_streaming_response.create(
            bot_challenge_answer="35",
            bot_challenge_nonce="c6feda4e-6501-4db9-a21f-665e5b4ce2ba",
            privacy_policy_url="https://telnyx.com/privacy-policy",
            terms_and_conditions_url="https://telnyx.com/terms-and-conditions-of-service",
            terms_of_service=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot_signup = response.parse()
            assert_matches_type(SuccessResponse, bot_signup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_resend_magic_link(self, client: Telnyx) -> None:
        bot_signup = client.bot_signup.resend_magic_link(
            email="agent-owner@example.com",
        )
        assert_matches_type(SuccessResponse, bot_signup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_resend_magic_link(self, client: Telnyx) -> None:
        response = client.bot_signup.with_raw_response.resend_magic_link(
            email="agent-owner@example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot_signup = response.parse()
        assert_matches_type(SuccessResponse, bot_signup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_resend_magic_link(self, client: Telnyx) -> None:
        with client.bot_signup.with_streaming_response.resend_magic_link(
            email="agent-owner@example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot_signup = response.parse()
            assert_matches_type(SuccessResponse, bot_signup, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBotSignup:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        bot_signup = await async_client.bot_signup.create(
            bot_challenge_answer="35",
            bot_challenge_nonce="c6feda4e-6501-4db9-a21f-665e5b4ce2ba",
            privacy_policy_url="https://telnyx.com/privacy-policy",
            terms_and_conditions_url="https://telnyx.com/terms-and-conditions-of-service",
            terms_of_service=True,
        )
        assert_matches_type(SuccessResponse, bot_signup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        bot_signup = await async_client.bot_signup.create(
            bot_challenge_answer="35",
            bot_challenge_nonce="c6feda4e-6501-4db9-a21f-665e5b4ce2ba",
            privacy_policy_url="https://telnyx.com/privacy-policy",
            terms_and_conditions_url="https://telnyx.com/terms-and-conditions-of-service",
            terms_of_service=True,
            email="agent-owner@example.com",
            terms_and_conditions_eu_url="https://telnyx.com/terms-and-conditions-of-service-eu",
            terms_of_service_eu=True,
        )
        assert_matches_type(SuccessResponse, bot_signup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.bot_signup.with_raw_response.create(
            bot_challenge_answer="35",
            bot_challenge_nonce="c6feda4e-6501-4db9-a21f-665e5b4ce2ba",
            privacy_policy_url="https://telnyx.com/privacy-policy",
            terms_and_conditions_url="https://telnyx.com/terms-and-conditions-of-service",
            terms_of_service=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot_signup = await response.parse()
        assert_matches_type(SuccessResponse, bot_signup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.bot_signup.with_streaming_response.create(
            bot_challenge_answer="35",
            bot_challenge_nonce="c6feda4e-6501-4db9-a21f-665e5b4ce2ba",
            privacy_policy_url="https://telnyx.com/privacy-policy",
            terms_and_conditions_url="https://telnyx.com/terms-and-conditions-of-service",
            terms_of_service=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot_signup = await response.parse()
            assert_matches_type(SuccessResponse, bot_signup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_resend_magic_link(self, async_client: AsyncTelnyx) -> None:
        bot_signup = await async_client.bot_signup.resend_magic_link(
            email="agent-owner@example.com",
        )
        assert_matches_type(SuccessResponse, bot_signup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_resend_magic_link(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.bot_signup.with_raw_response.resend_magic_link(
            email="agent-owner@example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot_signup = await response.parse()
        assert_matches_type(SuccessResponse, bot_signup, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_resend_magic_link(self, async_client: AsyncTelnyx) -> None:
        async with async_client.bot_signup.with_streaming_response.resend_magic_link(
            email="agent-owner@example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot_signup = await response.parse()
            assert_matches_type(SuccessResponse, bot_signup, path=["response"])

        assert cast(Any, response.is_closed) is True

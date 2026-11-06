# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCalendar:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_oauth_callback(self, client: Telnyx) -> None:
        calendar = client.meeting_bot.calendar.retrieve_oauth_callback()
        assert_matches_type(str, calendar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_oauth_callback_with_all_params(self, client: Telnyx) -> None:
        calendar = client.meeting_bot.calendar.retrieve_oauth_callback(
            code="code",
            error="error",
            state="state",
        )
        assert_matches_type(str, calendar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_oauth_callback(self, client: Telnyx) -> None:
        response = client.meeting_bot.calendar.with_raw_response.retrieve_oauth_callback()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calendar = response.parse()
        assert_matches_type(str, calendar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_oauth_callback(self, client: Telnyx) -> None:
        with client.meeting_bot.calendar.with_streaming_response.retrieve_oauth_callback() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calendar = response.parse()
            assert_matches_type(str, calendar, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCalendar:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_oauth_callback(self, async_client: AsyncTelnyx) -> None:
        calendar = await async_client.meeting_bot.calendar.retrieve_oauth_callback()
        assert_matches_type(str, calendar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_oauth_callback_with_all_params(self, async_client: AsyncTelnyx) -> None:
        calendar = await async_client.meeting_bot.calendar.retrieve_oauth_callback(
            code="code",
            error="error",
            state="state",
        )
        assert_matches_type(str, calendar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_oauth_callback(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.meeting_bot.calendar.with_raw_response.retrieve_oauth_callback()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calendar = await response.parse()
        assert_matches_type(str, calendar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_oauth_callback(self, async_client: AsyncTelnyx) -> None:
        async with async_client.meeting_bot.calendar.with_streaming_response.retrieve_oauth_callback() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calendar = await response.parse()
            assert_matches_type(str, calendar, path=["response"])

        assert cast(Any, response.is_closed) is True

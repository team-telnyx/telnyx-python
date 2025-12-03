# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import MessagingOptoutListResponse
from telnyx._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessagingOptouts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        messaging_optout = client.messaging_optouts.list()
        assert_matches_type(MessagingOptoutListResponse, messaging_optout, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        messaging_optout = client.messaging_optouts.list(
            created_at={
                "gte": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lte": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            filter={
                "from": "from",
                "messaging_profile_id": "messaging_profile_id",
            },
            page={
                "number": 1,
                "size": 1,
            },
            redaction_enabled="redaction_enabled",
        )
        assert_matches_type(MessagingOptoutListResponse, messaging_optout, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.messaging_optouts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_optout = response.parse()
        assert_matches_type(MessagingOptoutListResponse, messaging_optout, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.messaging_optouts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_optout = response.parse()
            assert_matches_type(MessagingOptoutListResponse, messaging_optout, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMessagingOptouts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        messaging_optout = await async_client.messaging_optouts.list()
        assert_matches_type(MessagingOptoutListResponse, messaging_optout, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        messaging_optout = await async_client.messaging_optouts.list(
            created_at={
                "gte": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lte": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            filter={
                "from": "from",
                "messaging_profile_id": "messaging_profile_id",
            },
            page={
                "number": 1,
                "size": 1,
            },
            redaction_enabled="redaction_enabled",
        )
        assert_matches_type(MessagingOptoutListResponse, messaging_optout, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messaging_optouts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_optout = await response.parse()
        assert_matches_type(MessagingOptoutListResponse, messaging_optout, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messaging_optouts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_optout = await response.parse()
            assert_matches_type(MessagingOptoutListResponse, messaging_optout, path=["response"])

        assert cast(Any, response.is_closed) is True

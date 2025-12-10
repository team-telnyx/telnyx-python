# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import Messaging10dlcGetEnumResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessaging10dlc:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_enum(self, client: Telnyx) -> None:
        messaging_10dlc = client.messaging_10dlc.get_enum(
            "mno",
        )
        assert_matches_type(Messaging10dlcGetEnumResponse, messaging_10dlc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_enum(self, client: Telnyx) -> None:
        response = client.messaging_10dlc.with_raw_response.get_enum(
            "mno",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_10dlc = response.parse()
        assert_matches_type(Messaging10dlcGetEnumResponse, messaging_10dlc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_enum(self, client: Telnyx) -> None:
        with client.messaging_10dlc.with_streaming_response.get_enum(
            "mno",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_10dlc = response.parse()
            assert_matches_type(Messaging10dlcGetEnumResponse, messaging_10dlc, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMessaging10dlc:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_enum(self, async_client: AsyncTelnyx) -> None:
        messaging_10dlc = await async_client.messaging_10dlc.get_enum(
            "mno",
        )
        assert_matches_type(Messaging10dlcGetEnumResponse, messaging_10dlc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_enum(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messaging_10dlc.with_raw_response.get_enum(
            "mno",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_10dlc = await response.parse()
        assert_matches_type(Messaging10dlcGetEnumResponse, messaging_10dlc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_enum(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messaging_10dlc.with_streaming_response.get_enum(
            "mno",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_10dlc = await response.parse()
            assert_matches_type(Messaging10dlcGetEnumResponse, messaging_10dlc, path=["response"])

        assert cast(Any, response.is_closed) is True

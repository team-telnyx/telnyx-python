# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNumberReputation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_agree(self, client: Telnyx) -> None:
        number_reputation = client.terms_of_service.number_reputation.agree()
        assert number_reputation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_agree(self, client: Telnyx) -> None:
        response = client.terms_of_service.number_reputation.with_raw_response.agree()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_reputation = response.parse()
        assert number_reputation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_agree(self, client: Telnyx) -> None:
        with client.terms_of_service.number_reputation.with_streaming_response.agree() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_reputation = response.parse()
            assert number_reputation is None

        assert cast(Any, response.is_closed) is True


class TestAsyncNumberReputation:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_agree(self, async_client: AsyncTelnyx) -> None:
        number_reputation = await async_client.terms_of_service.number_reputation.agree()
        assert number_reputation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_agree(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.terms_of_service.number_reputation.with_raw_response.agree()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_reputation = await response.parse()
        assert number_reputation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_agree(self, async_client: AsyncTelnyx) -> None:
        async with async_client.terms_of_service.number_reputation.with_streaming_response.agree() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_reputation = await response.parse()
            assert number_reputation is None

        assert cast(Any, response.is_closed) is True

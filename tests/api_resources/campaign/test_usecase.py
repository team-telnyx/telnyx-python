# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.campaign import UsecaseGetCostResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsecase:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_cost(self, client: Telnyx) -> None:
        usecase = client.campaign.usecase.get_cost(
            usecase="usecase",
        )
        assert_matches_type(UsecaseGetCostResponse, usecase, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_cost(self, client: Telnyx) -> None:
        response = client.campaign.usecase.with_raw_response.get_cost(
            usecase="usecase",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usecase = response.parse()
        assert_matches_type(UsecaseGetCostResponse, usecase, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_cost(self, client: Telnyx) -> None:
        with client.campaign.usecase.with_streaming_response.get_cost(
            usecase="usecase",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usecase = response.parse()
            assert_matches_type(UsecaseGetCostResponse, usecase, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsecase:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_cost(self, async_client: AsyncTelnyx) -> None:
        usecase = await async_client.campaign.usecase.get_cost(
            usecase="usecase",
        )
        assert_matches_type(UsecaseGetCostResponse, usecase, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_cost(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.campaign.usecase.with_raw_response.get_cost(
            usecase="usecase",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usecase = await response.parse()
        assert_matches_type(UsecaseGetCostResponse, usecase, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_cost(self, async_client: AsyncTelnyx) -> None:
        async with async_client.campaign.usecase.with_streaming_response.get_cost(
            usecase="usecase",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usecase = await response.parse()
            assert_matches_type(UsecaseGetCostResponse, usecase, path=["response"])

        assert cast(Any, response.is_closed) is True

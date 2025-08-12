# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import PortingListUkCarriersResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPorting:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_uk_carriers(self, client: Telnyx) -> None:
        porting = client.porting.list_uk_carriers()
        assert_matches_type(PortingListUkCarriersResponse, porting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_uk_carriers(self, client: Telnyx) -> None:
        response = client.porting.with_raw_response.list_uk_carriers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        porting = response.parse()
        assert_matches_type(PortingListUkCarriersResponse, porting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_uk_carriers(self, client: Telnyx) -> None:
        with client.porting.with_streaming_response.list_uk_carriers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            porting = response.parse()
            assert_matches_type(PortingListUkCarriersResponse, porting, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPorting:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_uk_carriers(self, async_client: AsyncTelnyx) -> None:
        porting = await async_client.porting.list_uk_carriers()
        assert_matches_type(PortingListUkCarriersResponse, porting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_uk_carriers(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.porting.with_raw_response.list_uk_carriers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        porting = await response.parse()
        assert_matches_type(PortingListUkCarriersResponse, porting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_uk_carriers(self, async_client: AsyncTelnyx) -> None:
        async with async_client.porting.with_streaming_response.list_uk_carriers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            porting = await response.parse()
            assert_matches_type(PortingListUkCarriersResponse, porting, path=["response"])

        assert cast(Any, response.is_closed) is True

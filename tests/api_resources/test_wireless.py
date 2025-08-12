# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import WirelessRetrieveRegionsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWireless:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_regions(self, client: Telnyx) -> None:
        wireless = client.wireless.retrieve_regions(
            product="public_ips",
        )
        assert_matches_type(WirelessRetrieveRegionsResponse, wireless, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_regions(self, client: Telnyx) -> None:
        response = client.wireless.with_raw_response.retrieve_regions(
            product="public_ips",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wireless = response.parse()
        assert_matches_type(WirelessRetrieveRegionsResponse, wireless, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_regions(self, client: Telnyx) -> None:
        with client.wireless.with_streaming_response.retrieve_regions(
            product="public_ips",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wireless = response.parse()
            assert_matches_type(WirelessRetrieveRegionsResponse, wireless, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWireless:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_regions(self, async_client: AsyncTelnyx) -> None:
        wireless = await async_client.wireless.retrieve_regions(
            product="public_ips",
        )
        assert_matches_type(WirelessRetrieveRegionsResponse, wireless, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_regions(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.wireless.with_raw_response.retrieve_regions(
            product="public_ips",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wireless = await response.parse()
        assert_matches_type(WirelessRetrieveRegionsResponse, wireless, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_regions(self, async_client: AsyncTelnyx) -> None:
        async with async_client.wireless.with_streaming_response.retrieve_regions(
            product="public_ips",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wireless = await response.parse()
            assert_matches_type(WirelessRetrieveRegionsResponse, wireless, path=["response"])

        assert cast(Any, response.is_closed) is True

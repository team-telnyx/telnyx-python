# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import MobileNetworkOperatorListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMobileNetworkOperators:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        mobile_network_operator = client.mobile_network_operators.list()
        assert_matches_type(MobileNetworkOperatorListResponse, mobile_network_operator, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        mobile_network_operator = client.mobile_network_operators.list(
            filter={
                "country_code": "US",
                "mcc": "310",
                "mnc": "410",
                "name": {
                    "contains": "T&T",
                    "ends_with": "T",
                    "starts_with": "AT",
                },
                "network_preferences_enabled": True,
                "tadig": "USACG",
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(MobileNetworkOperatorListResponse, mobile_network_operator, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.mobile_network_operators.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mobile_network_operator = response.parse()
        assert_matches_type(MobileNetworkOperatorListResponse, mobile_network_operator, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.mobile_network_operators.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mobile_network_operator = response.parse()
            assert_matches_type(MobileNetworkOperatorListResponse, mobile_network_operator, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMobileNetworkOperators:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        mobile_network_operator = await async_client.mobile_network_operators.list()
        assert_matches_type(MobileNetworkOperatorListResponse, mobile_network_operator, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        mobile_network_operator = await async_client.mobile_network_operators.list(
            filter={
                "country_code": "US",
                "mcc": "310",
                "mnc": "410",
                "name": {
                    "contains": "T&T",
                    "ends_with": "T",
                    "starts_with": "AT",
                },
                "network_preferences_enabled": True,
                "tadig": "USACG",
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(MobileNetworkOperatorListResponse, mobile_network_operator, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.mobile_network_operators.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mobile_network_operator = await response.parse()
        assert_matches_type(MobileNetworkOperatorListResponse, mobile_network_operator, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.mobile_network_operators.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mobile_network_operator = await response.parse()
            assert_matches_type(MobileNetworkOperatorListResponse, mobile_network_operator, path=["response"])

        assert cast(Any, response.is_closed) is True

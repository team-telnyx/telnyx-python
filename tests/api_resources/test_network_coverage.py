# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import NetworkCoverageListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNetworkCoverage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        network_coverage = client.network_coverage.list()
        assert_matches_type(NetworkCoverageListResponse, network_coverage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        network_coverage = client.network_coverage.list(
            filter={
                "location_code": "silicon_valley-ca",
                "location_pop": "SV1",
                "location_region": "AMER",
                "location_site": "SJC",
            },
            filters={"available_services": "cloud_vpn"},
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(NetworkCoverageListResponse, network_coverage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.network_coverage.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network_coverage = response.parse()
        assert_matches_type(NetworkCoverageListResponse, network_coverage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.network_coverage.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network_coverage = response.parse()
            assert_matches_type(NetworkCoverageListResponse, network_coverage, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncNetworkCoverage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        network_coverage = await async_client.network_coverage.list()
        assert_matches_type(NetworkCoverageListResponse, network_coverage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        network_coverage = await async_client.network_coverage.list(
            filter={
                "location_code": "silicon_valley-ca",
                "location_pop": "SV1",
                "location_region": "AMER",
                "location_site": "SJC",
            },
            filters={"available_services": "cloud_vpn"},
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(NetworkCoverageListResponse, network_coverage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.network_coverage.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network_coverage = await response.parse()
        assert_matches_type(NetworkCoverageListResponse, network_coverage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.network_coverage.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network_coverage = await response.parse()
            assert_matches_type(NetworkCoverageListResponse, network_coverage, path=["response"])

        assert cast(Any, response.is_closed) is True

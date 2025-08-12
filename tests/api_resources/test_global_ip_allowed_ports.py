# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import GlobalIPAllowedPortListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGlobalIPAllowedPorts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        global_ip_allowed_port = client.global_ip_allowed_ports.list()
        assert_matches_type(GlobalIPAllowedPortListResponse, global_ip_allowed_port, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.global_ip_allowed_ports.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        global_ip_allowed_port = response.parse()
        assert_matches_type(GlobalIPAllowedPortListResponse, global_ip_allowed_port, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.global_ip_allowed_ports.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            global_ip_allowed_port = response.parse()
            assert_matches_type(GlobalIPAllowedPortListResponse, global_ip_allowed_port, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGlobalIPAllowedPorts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        global_ip_allowed_port = await async_client.global_ip_allowed_ports.list()
        assert_matches_type(GlobalIPAllowedPortListResponse, global_ip_allowed_port, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.global_ip_allowed_ports.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        global_ip_allowed_port = await response.parse()
        assert_matches_type(GlobalIPAllowedPortListResponse, global_ip_allowed_port, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.global_ip_allowed_ports.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            global_ip_allowed_port = await response.parse()
            assert_matches_type(GlobalIPAllowedPortListResponse, global_ip_allowed_port, path=["response"])

        assert cast(Any, response.is_closed) is True

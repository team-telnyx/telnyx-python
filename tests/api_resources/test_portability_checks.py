# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import PortabilityCheckRunResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPortabilityChecks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run(self, client: Telnyx) -> None:
        portability_check = client.portability_checks.run()
        assert_matches_type(PortabilityCheckRunResponse, portability_check, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_with_all_params(self, client: Telnyx) -> None:
        portability_check = client.portability_checks.run(
            phone_numbers=["+13035550000", "+13035550001", "+13035550002"],
        )
        assert_matches_type(PortabilityCheckRunResponse, portability_check, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_run(self, client: Telnyx) -> None:
        response = client.portability_checks.with_raw_response.run()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portability_check = response.parse()
        assert_matches_type(PortabilityCheckRunResponse, portability_check, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_run(self, client: Telnyx) -> None:
        with client.portability_checks.with_streaming_response.run() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portability_check = response.parse()
            assert_matches_type(PortabilityCheckRunResponse, portability_check, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPortabilityChecks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run(self, async_client: AsyncTelnyx) -> None:
        portability_check = await async_client.portability_checks.run()
        assert_matches_type(PortabilityCheckRunResponse, portability_check, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncTelnyx) -> None:
        portability_check = await async_client.portability_checks.run(
            phone_numbers=["+13035550000", "+13035550001", "+13035550002"],
        )
        assert_matches_type(PortabilityCheckRunResponse, portability_check, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.portability_checks.with_raw_response.run()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portability_check = await response.parse()
        assert_matches_type(PortabilityCheckRunResponse, portability_check, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncTelnyx) -> None:
        async with async_client.portability_checks.with_streaming_response.run() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portability_check = await response.parse()
            assert_matches_type(PortabilityCheckRunResponse, portability_check, path=["response"])

        assert cast(Any, response.is_closed) is True

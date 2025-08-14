# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.operator_connect import ActionRefreshResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestActions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_refresh(self, client: Telnyx) -> None:
        action = client.operator_connect.actions.refresh()
        assert_matches_type(ActionRefreshResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_refresh(self, client: Telnyx) -> None:
        response = client.operator_connect.actions.with_raw_response.refresh()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionRefreshResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_refresh(self, client: Telnyx) -> None:
        with client.operator_connect.actions.with_streaming_response.refresh() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionRefreshResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncActions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_refresh(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.operator_connect.actions.refresh()
        assert_matches_type(ActionRefreshResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_refresh(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.operator_connect.actions.with_raw_response.refresh()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionRefreshResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_refresh(self, async_client: AsyncTelnyx) -> None:
        async with async_client.operator_connect.actions.with_streaming_response.refresh() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionRefreshResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

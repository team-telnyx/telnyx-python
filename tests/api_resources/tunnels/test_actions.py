# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.tunnels import ActionRotateTokenResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestActions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rotate_token(self, client: Telnyx) -> None:
        action = client.tunnels.actions.rotate_token(
            "62d438d2-8a51-4c5e-9d0c-1f6b2a7e4c39",
        )
        assert_matches_type(ActionRotateTokenResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rotate_token(self, client: Telnyx) -> None:
        response = client.tunnels.actions.with_raw_response.rotate_token(
            "62d438d2-8a51-4c5e-9d0c-1f6b2a7e4c39",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionRotateTokenResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rotate_token(self, client: Telnyx) -> None:
        with client.tunnels.actions.with_streaming_response.rotate_token(
            "62d438d2-8a51-4c5e-9d0c-1f6b2a7e4c39",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionRotateTokenResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_rotate_token(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tunnels.actions.with_raw_response.rotate_token(
                "",
            )


class TestAsyncActions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rotate_token(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.tunnels.actions.rotate_token(
            "62d438d2-8a51-4c5e-9d0c-1f6b2a7e4c39",
        )
        assert_matches_type(ActionRotateTokenResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rotate_token(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.tunnels.actions.with_raw_response.rotate_token(
            "62d438d2-8a51-4c5e-9d0c-1f6b2a7e4c39",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionRotateTokenResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rotate_token(self, async_client: AsyncTelnyx) -> None:
        async with async_client.tunnels.actions.with_streaming_response.rotate_token(
            "62d438d2-8a51-4c5e-9d0c-1f6b2a7e4c39",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionRotateTokenResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_rotate_token(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tunnels.actions.with_raw_response.rotate_token(
                "",
            )

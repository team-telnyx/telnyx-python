# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.actions import RegisterCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRegister:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        register = client.actions.register.create(
            registration_codes=["0000000001", "0000000002", "0000000003"],
        )
        assert_matches_type(RegisterCreateResponse, register, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        register = client.actions.register.create(
            registration_codes=["0000000001", "0000000002", "0000000003"],
            sim_card_group_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            status="standby",
            tags=["personal", "customers", "active-customers"],
        )
        assert_matches_type(RegisterCreateResponse, register, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.actions.register.with_raw_response.create(
            registration_codes=["0000000001", "0000000002", "0000000003"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        register = response.parse()
        assert_matches_type(RegisterCreateResponse, register, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.actions.register.with_streaming_response.create(
            registration_codes=["0000000001", "0000000002", "0000000003"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            register = response.parse()
            assert_matches_type(RegisterCreateResponse, register, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRegister:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        register = await async_client.actions.register.create(
            registration_codes=["0000000001", "0000000002", "0000000003"],
        )
        assert_matches_type(RegisterCreateResponse, register, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        register = await async_client.actions.register.create(
            registration_codes=["0000000001", "0000000002", "0000000003"],
            sim_card_group_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            status="standby",
            tags=["personal", "customers", "active-customers"],
        )
        assert_matches_type(RegisterCreateResponse, register, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.actions.register.with_raw_response.create(
            registration_codes=["0000000001", "0000000002", "0000000003"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        register = await response.parse()
        assert_matches_type(RegisterCreateResponse, register, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.actions.register.with_streaming_response.create(
            registration_codes=["0000000001", "0000000002", "0000000003"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            register = await response.parse()
            assert_matches_type(RegisterCreateResponse, register, path=["response"])

        assert cast(Any, response.is_closed) is True

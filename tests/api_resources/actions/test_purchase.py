# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.actions import PurchaseCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPurchase:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        purchase = client.actions.purchase.create(
            amount=10,
        )
        assert_matches_type(PurchaseCreateResponse, purchase, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        purchase = client.actions.purchase.create(
            amount=10,
            product="whitelabel",
            sim_card_group_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            status="standby",
            tags=["personal", "customers", "active-customers"],
            whitelabel_name="Custom SPN",
        )
        assert_matches_type(PurchaseCreateResponse, purchase, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.actions.purchase.with_raw_response.create(
            amount=10,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purchase = response.parse()
        assert_matches_type(PurchaseCreateResponse, purchase, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.actions.purchase.with_streaming_response.create(
            amount=10,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purchase = response.parse()
            assert_matches_type(PurchaseCreateResponse, purchase, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPurchase:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        purchase = await async_client.actions.purchase.create(
            amount=10,
        )
        assert_matches_type(PurchaseCreateResponse, purchase, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        purchase = await async_client.actions.purchase.create(
            amount=10,
            product="whitelabel",
            sim_card_group_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            status="standby",
            tags=["personal", "customers", "active-customers"],
            whitelabel_name="Custom SPN",
        )
        assert_matches_type(PurchaseCreateResponse, purchase, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.actions.purchase.with_raw_response.create(
            amount=10,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purchase = await response.parse()
        assert_matches_type(PurchaseCreateResponse, purchase, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.actions.purchase.with_streaming_response.create(
            amount=10,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purchase = await response.parse()
            assert_matches_type(PurchaseCreateResponse, purchase, path=["response"])

        assert cast(Any, response.is_closed) is True

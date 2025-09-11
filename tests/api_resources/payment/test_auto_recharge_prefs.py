# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.payment import (
    AutoRechargePrefListResponse,
    AutoRechargePrefUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAutoRechargePrefs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        auto_recharge_pref = client.payment.auto_recharge_prefs.update()
        assert_matches_type(AutoRechargePrefUpdateResponse, auto_recharge_pref, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        auto_recharge_pref = client.payment.auto_recharge_prefs.update(
            enabled=True,
            invoice_enabled=True,
            preference="credit_paypal",
            recharge_amount="104.00",
            threshold_amount="104.00",
        )
        assert_matches_type(AutoRechargePrefUpdateResponse, auto_recharge_pref, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.payment.auto_recharge_prefs.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auto_recharge_pref = response.parse()
        assert_matches_type(AutoRechargePrefUpdateResponse, auto_recharge_pref, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.payment.auto_recharge_prefs.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auto_recharge_pref = response.parse()
            assert_matches_type(AutoRechargePrefUpdateResponse, auto_recharge_pref, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        auto_recharge_pref = client.payment.auto_recharge_prefs.list()
        assert_matches_type(AutoRechargePrefListResponse, auto_recharge_pref, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.payment.auto_recharge_prefs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auto_recharge_pref = response.parse()
        assert_matches_type(AutoRechargePrefListResponse, auto_recharge_pref, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.payment.auto_recharge_prefs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auto_recharge_pref = response.parse()
            assert_matches_type(AutoRechargePrefListResponse, auto_recharge_pref, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAutoRechargePrefs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        auto_recharge_pref = await async_client.payment.auto_recharge_prefs.update()
        assert_matches_type(AutoRechargePrefUpdateResponse, auto_recharge_pref, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        auto_recharge_pref = await async_client.payment.auto_recharge_prefs.update(
            enabled=True,
            invoice_enabled=True,
            preference="credit_paypal",
            recharge_amount="104.00",
            threshold_amount="104.00",
        )
        assert_matches_type(AutoRechargePrefUpdateResponse, auto_recharge_pref, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.payment.auto_recharge_prefs.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auto_recharge_pref = await response.parse()
        assert_matches_type(AutoRechargePrefUpdateResponse, auto_recharge_pref, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.payment.auto_recharge_prefs.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auto_recharge_pref = await response.parse()
            assert_matches_type(AutoRechargePrefUpdateResponse, auto_recharge_pref, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        auto_recharge_pref = await async_client.payment.auto_recharge_prefs.list()
        assert_matches_type(AutoRechargePrefListResponse, auto_recharge_pref, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.payment.auto_recharge_prefs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auto_recharge_pref = await response.parse()
        assert_matches_type(AutoRechargePrefListResponse, auto_recharge_pref, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.payment.auto_recharge_prefs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auto_recharge_pref = await response.parse()
            assert_matches_type(AutoRechargePrefListResponse, auto_recharge_pref, path=["response"])

        assert cast(Any, response.is_closed) is True

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import MachinePaymentAccountCreditResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMachinePayments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_account_credit(self, client: Telnyx) -> None:
        machine_payment = client.machine_payments.account_credit(
            amount_usd="10.00",
        )
        assert_matches_type(MachinePaymentAccountCreditResponse, machine_payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_account_credit(self, client: Telnyx) -> None:
        response = client.machine_payments.with_raw_response.account_credit(
            amount_usd="10.00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        machine_payment = response.parse()
        assert_matches_type(MachinePaymentAccountCreditResponse, machine_payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_account_credit(self, client: Telnyx) -> None:
        with client.machine_payments.with_streaming_response.account_credit(
            amount_usd="10.00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            machine_payment = response.parse()
            assert_matches_type(MachinePaymentAccountCreditResponse, machine_payment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMachinePayments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_account_credit(self, async_client: AsyncTelnyx) -> None:
        machine_payment = await async_client.machine_payments.account_credit(
            amount_usd="10.00",
        )
        assert_matches_type(MachinePaymentAccountCreditResponse, machine_payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_account_credit(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.machine_payments.with_raw_response.account_credit(
            amount_usd="10.00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        machine_payment = await response.parse()
        assert_matches_type(MachinePaymentAccountCreditResponse, machine_payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_account_credit(self, async_client: AsyncTelnyx) -> None:
        async with async_client.machine_payments.with_streaming_response.account_credit(
            amount_usd="10.00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            machine_payment = await response.parse()
            assert_matches_type(MachinePaymentAccountCreditResponse, machine_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

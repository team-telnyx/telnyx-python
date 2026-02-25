# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import PaymentCreateStoredPaymentTransactionResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPayment:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_stored_payment_transaction(self, client: Telnyx) -> None:
        payment = client.payment.create_stored_payment_transaction(
            amount="120.00",
        )
        assert_matches_type(PaymentCreateStoredPaymentTransactionResponse, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_stored_payment_transaction(self, client: Telnyx) -> None:
        response = client.payment.with_raw_response.create_stored_payment_transaction(
            amount="120.00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentCreateStoredPaymentTransactionResponse, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_stored_payment_transaction(self, client: Telnyx) -> None:
        with client.payment.with_streaming_response.create_stored_payment_transaction(
            amount="120.00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(PaymentCreateStoredPaymentTransactionResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPayment:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_stored_payment_transaction(self, async_client: AsyncTelnyx) -> None:
        payment = await async_client.payment.create_stored_payment_transaction(
            amount="120.00",
        )
        assert_matches_type(PaymentCreateStoredPaymentTransactionResponse, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_stored_payment_transaction(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.payment.with_raw_response.create_stored_payment_transaction(
            amount="120.00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(PaymentCreateStoredPaymentTransactionResponse, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_stored_payment_transaction(self, async_client: AsyncTelnyx) -> None:
        async with async_client.payment.with_streaming_response.create_stored_payment_transaction(
            amount="120.00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(PaymentCreateStoredPaymentTransactionResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

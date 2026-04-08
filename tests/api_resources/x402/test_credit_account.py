# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.x402 import (
    CreditAccountSettleResponse,
    CreditAccountCreateQuoteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCreditAccount:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_quote(self, client: Telnyx) -> None:
        credit_account = client.x402.credit_account.create_quote(
            amount_usd="50.00",
        )
        assert_matches_type(CreditAccountCreateQuoteResponse, credit_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_quote(self, client: Telnyx) -> None:
        response = client.x402.credit_account.with_raw_response.create_quote(
            amount_usd="50.00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_account = response.parse()
        assert_matches_type(CreditAccountCreateQuoteResponse, credit_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_quote(self, client: Telnyx) -> None:
        with client.x402.credit_account.with_streaming_response.create_quote(
            amount_usd="50.00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_account = response.parse()
            assert_matches_type(CreditAccountCreateQuoteResponse, credit_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_settle(self, client: Telnyx) -> None:
        credit_account = client.x402.credit_account.settle(
            id="quote_abc123",
        )
        assert_matches_type(CreditAccountSettleResponse, credit_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_settle_with_all_params(self, client: Telnyx) -> None:
        credit_account = client.x402.credit_account.settle(
            id="quote_abc123",
            body_payment_signature="0xabc123...",
            header_payment_signature="PAYMENT-SIGNATURE",
        )
        assert_matches_type(CreditAccountSettleResponse, credit_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_settle(self, client: Telnyx) -> None:
        response = client.x402.credit_account.with_raw_response.settle(
            id="quote_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_account = response.parse()
        assert_matches_type(CreditAccountSettleResponse, credit_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_settle(self, client: Telnyx) -> None:
        with client.x402.credit_account.with_streaming_response.settle(
            id="quote_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_account = response.parse()
            assert_matches_type(CreditAccountSettleResponse, credit_account, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCreditAccount:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_quote(self, async_client: AsyncTelnyx) -> None:
        credit_account = await async_client.x402.credit_account.create_quote(
            amount_usd="50.00",
        )
        assert_matches_type(CreditAccountCreateQuoteResponse, credit_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_quote(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.x402.credit_account.with_raw_response.create_quote(
            amount_usd="50.00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_account = await response.parse()
        assert_matches_type(CreditAccountCreateQuoteResponse, credit_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_quote(self, async_client: AsyncTelnyx) -> None:
        async with async_client.x402.credit_account.with_streaming_response.create_quote(
            amount_usd="50.00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_account = await response.parse()
            assert_matches_type(CreditAccountCreateQuoteResponse, credit_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_settle(self, async_client: AsyncTelnyx) -> None:
        credit_account = await async_client.x402.credit_account.settle(
            id="quote_abc123",
        )
        assert_matches_type(CreditAccountSettleResponse, credit_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_settle_with_all_params(self, async_client: AsyncTelnyx) -> None:
        credit_account = await async_client.x402.credit_account.settle(
            id="quote_abc123",
            body_payment_signature="0xabc123...",
            header_payment_signature="PAYMENT-SIGNATURE",
        )
        assert_matches_type(CreditAccountSettleResponse, credit_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_settle(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.x402.credit_account.with_raw_response.settle(
            id="quote_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_account = await response.parse()
        assert_matches_type(CreditAccountSettleResponse, credit_account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_settle(self, async_client: AsyncTelnyx) -> None:
        async with async_client.x402.credit_account.with_streaming_response.settle(
            id="quote_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_account = await response.parse()
            assert_matches_type(CreditAccountSettleResponse, credit_account, path=["response"])

        assert cast(Any, response.is_closed) is True

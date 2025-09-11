# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import ChargesBreakdownRetrieveResponse
from telnyx._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChargesBreakdown:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        charges_breakdown = client.charges_breakdown.retrieve(
            start_date=parse_date("2025-05-01"),
        )
        assert_matches_type(ChargesBreakdownRetrieveResponse, charges_breakdown, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Telnyx) -> None:
        charges_breakdown = client.charges_breakdown.retrieve(
            start_date=parse_date("2025-05-01"),
            end_date=parse_date("2025-06-01"),
            format="json",
        )
        assert_matches_type(ChargesBreakdownRetrieveResponse, charges_breakdown, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.charges_breakdown.with_raw_response.retrieve(
            start_date=parse_date("2025-05-01"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        charges_breakdown = response.parse()
        assert_matches_type(ChargesBreakdownRetrieveResponse, charges_breakdown, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.charges_breakdown.with_streaming_response.retrieve(
            start_date=parse_date("2025-05-01"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            charges_breakdown = response.parse()
            assert_matches_type(ChargesBreakdownRetrieveResponse, charges_breakdown, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncChargesBreakdown:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        charges_breakdown = await async_client.charges_breakdown.retrieve(
            start_date=parse_date("2025-05-01"),
        )
        assert_matches_type(ChargesBreakdownRetrieveResponse, charges_breakdown, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncTelnyx) -> None:
        charges_breakdown = await async_client.charges_breakdown.retrieve(
            start_date=parse_date("2025-05-01"),
            end_date=parse_date("2025-06-01"),
            format="json",
        )
        assert_matches_type(ChargesBreakdownRetrieveResponse, charges_breakdown, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.charges_breakdown.with_raw_response.retrieve(
            start_date=parse_date("2025-05-01"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        charges_breakdown = await response.parse()
        assert_matches_type(ChargesBreakdownRetrieveResponse, charges_breakdown, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.charges_breakdown.with_streaming_response.retrieve(
            start_date=parse_date("2025-05-01"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            charges_breakdown = await response.parse()
            assert_matches_type(ChargesBreakdownRetrieveResponse, charges_breakdown, path=["response"])

        assert cast(Any, response.is_closed) is True

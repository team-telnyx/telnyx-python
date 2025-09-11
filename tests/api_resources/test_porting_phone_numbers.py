# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import PortingPhoneNumberListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPortingPhoneNumbers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        porting_phone_number = client.porting_phone_numbers.list()
        assert_matches_type(PortingPhoneNumberListResponse, porting_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        porting_phone_number = client.porting_phone_numbers.list(
            filter={"porting_order_status": "in-process"},
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(PortingPhoneNumberListResponse, porting_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.porting_phone_numbers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        porting_phone_number = response.parse()
        assert_matches_type(PortingPhoneNumberListResponse, porting_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.porting_phone_numbers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            porting_phone_number = response.parse()
            assert_matches_type(PortingPhoneNumberListResponse, porting_phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPortingPhoneNumbers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        porting_phone_number = await async_client.porting_phone_numbers.list()
        assert_matches_type(PortingPhoneNumberListResponse, porting_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        porting_phone_number = await async_client.porting_phone_numbers.list(
            filter={"porting_order_status": "in-process"},
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(PortingPhoneNumberListResponse, porting_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.porting_phone_numbers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        porting_phone_number = await response.parse()
        assert_matches_type(PortingPhoneNumberListResponse, porting_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.porting_phone_numbers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            porting_phone_number = await response.parse()
            assert_matches_type(PortingPhoneNumberListResponse, porting_phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

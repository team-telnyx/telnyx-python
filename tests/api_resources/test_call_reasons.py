# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    CallReasonListResponse,
    CallReasonValidateResponse,
)
from telnyx.pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCallReasons:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        call_reason = client.call_reasons.list()
        assert_matches_type(SyncDefaultFlatPagination[CallReasonListResponse], call_reason, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        call_reason = client.call_reasons.list(
            page_number=1,
            page_size=100,
        )
        assert_matches_type(SyncDefaultFlatPagination[CallReasonListResponse], call_reason, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.call_reasons.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call_reason = response.parse()
        assert_matches_type(SyncDefaultFlatPagination[CallReasonListResponse], call_reason, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.call_reasons.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call_reason = response.parse()
            assert_matches_type(SyncDefaultFlatPagination[CallReasonListResponse], call_reason, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_validate(self, client: Telnyx) -> None:
        call_reason = client.call_reasons.validate(
            body=["Appointment reminders", "Billing inquiries"],
        )
        assert_matches_type(CallReasonValidateResponse, call_reason, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_validate(self, client: Telnyx) -> None:
        response = client.call_reasons.with_raw_response.validate(
            body=["Appointment reminders", "Billing inquiries"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call_reason = response.parse()
        assert_matches_type(CallReasonValidateResponse, call_reason, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_validate(self, client: Telnyx) -> None:
        with client.call_reasons.with_streaming_response.validate(
            body=["Appointment reminders", "Billing inquiries"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call_reason = response.parse()
            assert_matches_type(CallReasonValidateResponse, call_reason, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCallReasons:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        call_reason = await async_client.call_reasons.list()
        assert_matches_type(AsyncDefaultFlatPagination[CallReasonListResponse], call_reason, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        call_reason = await async_client.call_reasons.list(
            page_number=1,
            page_size=100,
        )
        assert_matches_type(AsyncDefaultFlatPagination[CallReasonListResponse], call_reason, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.call_reasons.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call_reason = await response.parse()
        assert_matches_type(AsyncDefaultFlatPagination[CallReasonListResponse], call_reason, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.call_reasons.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call_reason = await response.parse()
            assert_matches_type(AsyncDefaultFlatPagination[CallReasonListResponse], call_reason, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_validate(self, async_client: AsyncTelnyx) -> None:
        call_reason = await async_client.call_reasons.validate(
            body=["Appointment reminders", "Billing inquiries"],
        )
        assert_matches_type(CallReasonValidateResponse, call_reason, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.call_reasons.with_raw_response.validate(
            body=["Appointment reminders", "Billing inquiries"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call_reason = await response.parse()
        assert_matches_type(CallReasonValidateResponse, call_reason, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncTelnyx) -> None:
        async with async_client.call_reasons.with_streaming_response.validate(
            body=["Appointment reminders", "Billing inquiries"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call_reason = await response.parse()
            assert_matches_type(CallReasonValidateResponse, call_reason, path=["response"])

        assert cast(Any, response.is_closed) is True

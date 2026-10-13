# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx._utils import parse_date
from telnyx.types.llm_token_gateway import (
    SpendRetrieveEventsResponse,
    SpendRetrieveSummaryResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSpend:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_events(self, client: Telnyx) -> None:
        spend = client.llm_token_gateway.spend.retrieve_events()
        assert_matches_type(SpendRetrieveEventsResponse, spend, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_events_with_all_params(self, client: Telnyx) -> None:
        spend = client.llm_token_gateway.spend.retrieve_events(
            end_date=parse_date("2019-12-27"),
            end_user_id="end_user_id",
            metadata={"foo": "J!Q0Ok0bzJb7"},
            page_number=1,
            page_size=1,
            page_snapshot="page[snapshot]",
            start_date=parse_date("2019-12-27"),
            token_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            token_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            token_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SpendRetrieveEventsResponse, spend, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_events(self, client: Telnyx) -> None:
        response = client.llm_token_gateway.spend.with_raw_response.retrieve_events()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spend = response.parse()
        assert_matches_type(SpendRetrieveEventsResponse, spend, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_events(self, client: Telnyx) -> None:
        with client.llm_token_gateway.spend.with_streaming_response.retrieve_events() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spend = response.parse()
            assert_matches_type(SpendRetrieveEventsResponse, spend, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_summary(self, client: Telnyx) -> None:
        spend = client.llm_token_gateway.spend.retrieve_summary(
            end_date=parse_date("2019-12-27"),
            group_by="token_group",
            start_date=parse_date("2019-12-27"),
        )
        assert_matches_type(SpendRetrieveSummaryResponse, spend, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_summary_with_all_params(self, client: Telnyx) -> None:
        spend = client.llm_token_gateway.spend.retrieve_summary(
            end_date=parse_date("2019-12-27"),
            group_by="token_group",
            start_date=parse_date("2019-12-27"),
            end_user_id="end_user_id",
            metadata={"foo": "J!Q0Ok0bzJb7"},
            page_number=1,
            page_size=1,
            page_snapshot="page[snapshot]",
            token_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            token_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            token_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SpendRetrieveSummaryResponse, spend, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_summary(self, client: Telnyx) -> None:
        response = client.llm_token_gateway.spend.with_raw_response.retrieve_summary(
            end_date=parse_date("2019-12-27"),
            group_by="token_group",
            start_date=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spend = response.parse()
        assert_matches_type(SpendRetrieveSummaryResponse, spend, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_summary(self, client: Telnyx) -> None:
        with client.llm_token_gateway.spend.with_streaming_response.retrieve_summary(
            end_date=parse_date("2019-12-27"),
            group_by="token_group",
            start_date=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spend = response.parse()
            assert_matches_type(SpendRetrieveSummaryResponse, spend, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSpend:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_events(self, async_client: AsyncTelnyx) -> None:
        spend = await async_client.llm_token_gateway.spend.retrieve_events()
        assert_matches_type(SpendRetrieveEventsResponse, spend, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_events_with_all_params(self, async_client: AsyncTelnyx) -> None:
        spend = await async_client.llm_token_gateway.spend.retrieve_events(
            end_date=parse_date("2019-12-27"),
            end_user_id="end_user_id",
            metadata={"foo": "J!Q0Ok0bzJb7"},
            page_number=1,
            page_size=1,
            page_snapshot="page[snapshot]",
            start_date=parse_date("2019-12-27"),
            token_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            token_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            token_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SpendRetrieveEventsResponse, spend, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_events(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.llm_token_gateway.spend.with_raw_response.retrieve_events()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spend = await response.parse()
        assert_matches_type(SpendRetrieveEventsResponse, spend, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_events(self, async_client: AsyncTelnyx) -> None:
        async with async_client.llm_token_gateway.spend.with_streaming_response.retrieve_events() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spend = await response.parse()
            assert_matches_type(SpendRetrieveEventsResponse, spend, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_summary(self, async_client: AsyncTelnyx) -> None:
        spend = await async_client.llm_token_gateway.spend.retrieve_summary(
            end_date=parse_date("2019-12-27"),
            group_by="token_group",
            start_date=parse_date("2019-12-27"),
        )
        assert_matches_type(SpendRetrieveSummaryResponse, spend, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_summary_with_all_params(self, async_client: AsyncTelnyx) -> None:
        spend = await async_client.llm_token_gateway.spend.retrieve_summary(
            end_date=parse_date("2019-12-27"),
            group_by="token_group",
            start_date=parse_date("2019-12-27"),
            end_user_id="end_user_id",
            metadata={"foo": "J!Q0Ok0bzJb7"},
            page_number=1,
            page_size=1,
            page_snapshot="page[snapshot]",
            token_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            token_key_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            token_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SpendRetrieveSummaryResponse, spend, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_summary(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.llm_token_gateway.spend.with_raw_response.retrieve_summary(
            end_date=parse_date("2019-12-27"),
            group_by="token_group",
            start_date=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spend = await response.parse()
        assert_matches_type(SpendRetrieveSummaryResponse, spend, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_summary(self, async_client: AsyncTelnyx) -> None:
        async with async_client.llm_token_gateway.spend.with_streaming_response.retrieve_summary(
            end_date=parse_date("2019-12-27"),
            group_by="token_group",
            start_date=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spend = await response.parse()
            assert_matches_type(SpendRetrieveSummaryResponse, spend, path=["response"])

        assert cast(Any, response.is_closed) is True

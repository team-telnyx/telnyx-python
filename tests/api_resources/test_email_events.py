# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    EmailEventListResponse,
    EmailEventRetrieveStatsResponse,
)
from telnyx._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmailEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        email_event = client.email_events.list()
        assert_matches_type(EmailEventListResponse, email_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        email_event = client.email_events.list(
            email_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            event_type="string",
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            page_cursor="page_cursor",
            page_size=1,
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(EmailEventListResponse, email_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.email_events.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_event = response.parse()
        assert_matches_type(EmailEventListResponse, email_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.email_events.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_event = response.parse()
            assert_matches_type(EmailEventListResponse, email_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_stats(self, client: Telnyx) -> None:
        email_event = client.email_events.retrieve_stats()
        assert_matches_type(EmailEventRetrieveStatsResponse, email_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_stats_with_all_params(self, client: Telnyx) -> None:
        email_event = client.email_events.retrieve_stats(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(EmailEventRetrieveStatsResponse, email_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_stats(self, client: Telnyx) -> None:
        response = client.email_events.with_raw_response.retrieve_stats()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_event = response.parse()
        assert_matches_type(EmailEventRetrieveStatsResponse, email_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_stats(self, client: Telnyx) -> None:
        with client.email_events.with_streaming_response.retrieve_stats() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_event = response.parse()
            assert_matches_type(EmailEventRetrieveStatsResponse, email_event, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEmailEvents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        email_event = await async_client.email_events.list()
        assert_matches_type(EmailEventListResponse, email_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        email_event = await async_client.email_events.list(
            email_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            event_type="string",
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            page_cursor="page_cursor",
            page_size=1,
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(EmailEventListResponse, email_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_events.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_event = await response.parse()
        assert_matches_type(EmailEventListResponse, email_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_events.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_event = await response.parse()
            assert_matches_type(EmailEventListResponse, email_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_stats(self, async_client: AsyncTelnyx) -> None:
        email_event = await async_client.email_events.retrieve_stats()
        assert_matches_type(EmailEventRetrieveStatsResponse, email_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_stats_with_all_params(self, async_client: AsyncTelnyx) -> None:
        email_event = await async_client.email_events.retrieve_stats(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(EmailEventRetrieveStatsResponse, email_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_stats(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email_events.with_raw_response.retrieve_stats()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_event = await response.parse()
        assert_matches_type(EmailEventRetrieveStatsResponse, email_event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_stats(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email_events.with_streaming_response.retrieve_stats() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_event = await response.parse()
            assert_matches_type(EmailEventRetrieveStatsResponse, email_event, path=["response"])

        assert cast(Any, response.is_closed) is True

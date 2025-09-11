# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import CallEventListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCallEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        call_event = client.call_events.list()
        assert_matches_type(CallEventListResponse, call_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        call_event = client.call_events.list(
            filter={
                "application_name": {"contains": "contains"},
                "application_session_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "connection_id": "connection_id",
                "failed": False,
                "from": "+12025550142",
                "leg_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "name": "name",
                "occurred_at": {
                    "eq": "2019-03-29T11:10:00Z",
                    "gt": "2019-03-29T11:10:00Z",
                    "gte": "2019-03-29T11:10:00Z",
                    "lt": "2019-03-29T11:10:00Z",
                    "lte": "2019-03-29T11:10:00Z",
                },
                "outbound_outbound_voice_profile_id": "outbound.outbound_voice_profile_id",
                "product": "texml",
                "status": "init",
                "to": "+12025550142",
                "type": "webhook",
            },
            page={
                "after": "after",
                "before": "before",
                "limit": 1,
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(CallEventListResponse, call_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.call_events.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call_event = response.parse()
        assert_matches_type(CallEventListResponse, call_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.call_events.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call_event = response.parse()
            assert_matches_type(CallEventListResponse, call_event, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCallEvents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        call_event = await async_client.call_events.list()
        assert_matches_type(CallEventListResponse, call_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        call_event = await async_client.call_events.list(
            filter={
                "application_name": {"contains": "contains"},
                "application_session_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "connection_id": "connection_id",
                "failed": False,
                "from": "+12025550142",
                "leg_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "name": "name",
                "occurred_at": {
                    "eq": "2019-03-29T11:10:00Z",
                    "gt": "2019-03-29T11:10:00Z",
                    "gte": "2019-03-29T11:10:00Z",
                    "lt": "2019-03-29T11:10:00Z",
                    "lte": "2019-03-29T11:10:00Z",
                },
                "outbound_outbound_voice_profile_id": "outbound.outbound_voice_profile_id",
                "product": "texml",
                "status": "init",
                "to": "+12025550142",
                "type": "webhook",
            },
            page={
                "after": "after",
                "before": "before",
                "limit": 1,
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(CallEventListResponse, call_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.call_events.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call_event = await response.parse()
        assert_matches_type(CallEventListResponse, call_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.call_events.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call_event = await response.parse()
            assert_matches_type(CallEventListResponse, call_event, path=["response"])

        assert cast(Any, response.is_closed) is True

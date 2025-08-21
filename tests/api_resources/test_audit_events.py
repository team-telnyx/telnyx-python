# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import AuditEventListResponse
from telnyx._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuditEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        audit_event = client.audit_events.list()
        assert_matches_type(AuditEventListResponse, audit_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        audit_event = client.audit_events.list(
            filter={
                "created_after": parse_datetime("2021-01-01T00:00:00Z"),
                "created_before": parse_datetime("2021-01-01T00:00:00Z"),
            },
            page={
                "number": 1,
                "size": 10,
            },
            sort="desc",
        )
        assert_matches_type(AuditEventListResponse, audit_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.audit_events.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_event = response.parse()
        assert_matches_type(AuditEventListResponse, audit_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.audit_events.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_event = response.parse()
            assert_matches_type(AuditEventListResponse, audit_event, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAuditEvents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        audit_event = await async_client.audit_events.list()
        assert_matches_type(AuditEventListResponse, audit_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        audit_event = await async_client.audit_events.list(
            filter={
                "created_after": parse_datetime("2021-01-01T00:00:00Z"),
                "created_before": parse_datetime("2021-01-01T00:00:00Z"),
            },
            page={
                "number": 1,
                "size": 10,
            },
            sort="desc",
        )
        assert_matches_type(AuditEventListResponse, audit_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.audit_events.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_event = await response.parse()
        assert_matches_type(AuditEventListResponse, audit_event, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.audit_events.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_event = await response.parse()
            assert_matches_type(AuditEventListResponse, audit_event, path=["response"])

        assert cast(Any, response.is_closed) is True

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx._utils import parse_datetime
from telnyx.types.reports import CdrUsageReportFetchSyncResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCdrUsageReports:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_fetch_sync(self, client: Telnyx) -> None:
        cdr_usage_report = client.reports.cdr_usage_reports.fetch_sync(
            aggregation_type="NO_AGGREGATION",
            product_breakdown="NO_BREAKDOWN",
        )
        assert_matches_type(CdrUsageReportFetchSyncResponse, cdr_usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_fetch_sync_with_all_params(self, client: Telnyx) -> None:
        cdr_usage_report = client.reports.cdr_usage_reports.fetch_sync(
            aggregation_type="NO_AGGREGATION",
            product_breakdown="NO_BREAKDOWN",
            connections=[1234567890123],
            end_date=parse_datetime("2020-07-01T00:00:00-06:00"),
            start_date=parse_datetime("2020-07-01T00:00:00-06:00"),
        )
        assert_matches_type(CdrUsageReportFetchSyncResponse, cdr_usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_fetch_sync(self, client: Telnyx) -> None:
        response = client.reports.cdr_usage_reports.with_raw_response.fetch_sync(
            aggregation_type="NO_AGGREGATION",
            product_breakdown="NO_BREAKDOWN",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cdr_usage_report = response.parse()
        assert_matches_type(CdrUsageReportFetchSyncResponse, cdr_usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_fetch_sync(self, client: Telnyx) -> None:
        with client.reports.cdr_usage_reports.with_streaming_response.fetch_sync(
            aggregation_type="NO_AGGREGATION",
            product_breakdown="NO_BREAKDOWN",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cdr_usage_report = response.parse()
            assert_matches_type(CdrUsageReportFetchSyncResponse, cdr_usage_report, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCdrUsageReports:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_fetch_sync(self, async_client: AsyncTelnyx) -> None:
        cdr_usage_report = await async_client.reports.cdr_usage_reports.fetch_sync(
            aggregation_type="NO_AGGREGATION",
            product_breakdown="NO_BREAKDOWN",
        )
        assert_matches_type(CdrUsageReportFetchSyncResponse, cdr_usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_fetch_sync_with_all_params(self, async_client: AsyncTelnyx) -> None:
        cdr_usage_report = await async_client.reports.cdr_usage_reports.fetch_sync(
            aggregation_type="NO_AGGREGATION",
            product_breakdown="NO_BREAKDOWN",
            connections=[1234567890123],
            end_date=parse_datetime("2020-07-01T00:00:00-06:00"),
            start_date=parse_datetime("2020-07-01T00:00:00-06:00"),
        )
        assert_matches_type(CdrUsageReportFetchSyncResponse, cdr_usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_fetch_sync(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.reports.cdr_usage_reports.with_raw_response.fetch_sync(
            aggregation_type="NO_AGGREGATION",
            product_breakdown="NO_BREAKDOWN",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cdr_usage_report = await response.parse()
        assert_matches_type(CdrUsageReportFetchSyncResponse, cdr_usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_fetch_sync(self, async_client: AsyncTelnyx) -> None:
        async with async_client.reports.cdr_usage_reports.with_streaming_response.fetch_sync(
            aggregation_type="NO_AGGREGATION",
            product_breakdown="NO_BREAKDOWN",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cdr_usage_report = await response.parse()
            assert_matches_type(CdrUsageReportFetchSyncResponse, cdr_usage_report, path=["response"])

        assert cast(Any, response.is_closed) is True

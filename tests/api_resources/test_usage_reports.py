# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    UsageReportListResponse,
    UsageReportGetOptionsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsageReports:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        usage_report = client.usage_reports.list(
            dimensions=["string"],
            metrics=["string"],
            product="product",
        )
        assert_matches_type(UsageReportListResponse, usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        usage_report = client.usage_reports.list(
            dimensions=["string"],
            metrics=["string"],
            product="product",
            date_range="date_range",
            end_date="end_date",
            filter="filter",
            format="csv",
            managed_accounts=True,
            page={
                "number": 2,
                "size": 5000,
            },
            sort=["string"],
            start_date="start_date",
            authorization_bearer="authorization_bearer",
        )
        assert_matches_type(UsageReportListResponse, usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.usage_reports.with_raw_response.list(
            dimensions=["string"],
            metrics=["string"],
            product="product",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage_report = response.parse()
        assert_matches_type(UsageReportListResponse, usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.usage_reports.with_streaming_response.list(
            dimensions=["string"],
            metrics=["string"],
            product="product",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage_report = response.parse()
            assert_matches_type(UsageReportListResponse, usage_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_options(self, client: Telnyx) -> None:
        usage_report = client.usage_reports.get_options()
        assert_matches_type(UsageReportGetOptionsResponse, usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_options_with_all_params(self, client: Telnyx) -> None:
        usage_report = client.usage_reports.get_options(
            product="product",
            authorization_bearer="authorization_bearer",
        )
        assert_matches_type(UsageReportGetOptionsResponse, usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_options(self, client: Telnyx) -> None:
        response = client.usage_reports.with_raw_response.get_options()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage_report = response.parse()
        assert_matches_type(UsageReportGetOptionsResponse, usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_options(self, client: Telnyx) -> None:
        with client.usage_reports.with_streaming_response.get_options() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage_report = response.parse()
            assert_matches_type(UsageReportGetOptionsResponse, usage_report, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsageReports:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        usage_report = await async_client.usage_reports.list(
            dimensions=["string"],
            metrics=["string"],
            product="product",
        )
        assert_matches_type(UsageReportListResponse, usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        usage_report = await async_client.usage_reports.list(
            dimensions=["string"],
            metrics=["string"],
            product="product",
            date_range="date_range",
            end_date="end_date",
            filter="filter",
            format="csv",
            managed_accounts=True,
            page={
                "number": 2,
                "size": 5000,
            },
            sort=["string"],
            start_date="start_date",
            authorization_bearer="authorization_bearer",
        )
        assert_matches_type(UsageReportListResponse, usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.usage_reports.with_raw_response.list(
            dimensions=["string"],
            metrics=["string"],
            product="product",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage_report = await response.parse()
        assert_matches_type(UsageReportListResponse, usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.usage_reports.with_streaming_response.list(
            dimensions=["string"],
            metrics=["string"],
            product="product",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage_report = await response.parse()
            assert_matches_type(UsageReportListResponse, usage_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_options(self, async_client: AsyncTelnyx) -> None:
        usage_report = await async_client.usage_reports.get_options()
        assert_matches_type(UsageReportGetOptionsResponse, usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_options_with_all_params(self, async_client: AsyncTelnyx) -> None:
        usage_report = await async_client.usage_reports.get_options(
            product="product",
            authorization_bearer="authorization_bearer",
        )
        assert_matches_type(UsageReportGetOptionsResponse, usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_options(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.usage_reports.with_raw_response.get_options()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage_report = await response.parse()
        assert_matches_type(UsageReportGetOptionsResponse, usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_options(self, async_client: AsyncTelnyx) -> None:
        async with async_client.usage_reports.with_streaming_response.get_options() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage_report = await response.parse()
            assert_matches_type(UsageReportGetOptionsResponse, usage_report, path=["response"])

        assert cast(Any, response.is_closed) is True

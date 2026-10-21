# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import DialMetricListResponse
from telnyx._utils import parse_datetime
from telnyx.pagination import SyncCloudfsCursorPagination, AsyncCloudfsCursorPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDialMetrics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        dial_metric = client.dial_metrics.list(
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            granularity="second",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncCloudfsCursorPagination[DialMetricListResponse], dial_metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        dial_metric = client.dial_metrics.list(
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            granularity="second",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            page_after="page[after]",
            page_limit=1,
            sort="-start_time",
        )
        assert_matches_type(SyncCloudfsCursorPagination[DialMetricListResponse], dial_metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.dial_metrics.with_raw_response.list(
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            granularity="second",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dial_metric = response.parse()
        assert_matches_type(SyncCloudfsCursorPagination[DialMetricListResponse], dial_metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.dial_metrics.with_streaming_response.list(
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            granularity="second",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dial_metric = response.parse()
            assert_matches_type(SyncCloudfsCursorPagination[DialMetricListResponse], dial_metric, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDialMetrics:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        dial_metric = await async_client.dial_metrics.list(
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            granularity="second",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncCloudfsCursorPagination[DialMetricListResponse], dial_metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        dial_metric = await async_client.dial_metrics.list(
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            granularity="second",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            page_after="page[after]",
            page_limit=1,
            sort="-start_time",
        )
        assert_matches_type(AsyncCloudfsCursorPagination[DialMetricListResponse], dial_metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.dial_metrics.with_raw_response.list(
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            granularity="second",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dial_metric = await response.parse()
        assert_matches_type(AsyncCloudfsCursorPagination[DialMetricListResponse], dial_metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.dial_metrics.with_streaming_response.list(
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            granularity="second",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dial_metric = await response.parse()
            assert_matches_type(AsyncCloudfsCursorPagination[DialMetricListResponse], dial_metric, path=["response"])

        assert cast(Any, response.is_closed) is True

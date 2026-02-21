# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import MessagingProfileMetricListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessagingProfileMetrics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        messaging_profile_metric = client.messaging_profile_metrics.list()
        assert_matches_type(MessagingProfileMetricListResponse, messaging_profile_metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        messaging_profile_metric = client.messaging_profile_metrics.list(
            time_frame="1h",
        )
        assert_matches_type(MessagingProfileMetricListResponse, messaging_profile_metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.messaging_profile_metrics.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_profile_metric = response.parse()
        assert_matches_type(MessagingProfileMetricListResponse, messaging_profile_metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.messaging_profile_metrics.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_profile_metric = response.parse()
            assert_matches_type(MessagingProfileMetricListResponse, messaging_profile_metric, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMessagingProfileMetrics:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        messaging_profile_metric = await async_client.messaging_profile_metrics.list()
        assert_matches_type(MessagingProfileMetricListResponse, messaging_profile_metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        messaging_profile_metric = await async_client.messaging_profile_metrics.list(
            time_frame="1h",
        )
        assert_matches_type(MessagingProfileMetricListResponse, messaging_profile_metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messaging_profile_metrics.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_profile_metric = await response.parse()
        assert_matches_type(MessagingProfileMetricListResponse, messaging_profile_metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messaging_profile_metrics.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_profile_metric = await response.parse()
            assert_matches_type(MessagingProfileMetricListResponse, messaging_profile_metric, path=["response"])

        assert cast(Any, response.is_closed) is True

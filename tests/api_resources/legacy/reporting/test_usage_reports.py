# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx._utils import parse_datetime
from telnyx.types.legacy.reporting import (
    UsageReportRetrieveSpeechToTextResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsageReports:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_speech_to_text(self, client: Telnyx) -> None:
        usage_report = client.legacy.reporting.usage_reports.retrieve_speech_to_text()
        assert_matches_type(UsageReportRetrieveSpeechToTextResponse, usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_speech_to_text_with_all_params(self, client: Telnyx) -> None:
        usage_report = client.legacy.reporting.usage_reports.retrieve_speech_to_text(
            end_date=parse_datetime("2020-07-01T00:00:00-06:00"),
            start_date=parse_datetime("2020-07-01T00:00:00-06:00"),
        )
        assert_matches_type(UsageReportRetrieveSpeechToTextResponse, usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_speech_to_text(self, client: Telnyx) -> None:
        response = client.legacy.reporting.usage_reports.with_raw_response.retrieve_speech_to_text()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage_report = response.parse()
        assert_matches_type(UsageReportRetrieveSpeechToTextResponse, usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_speech_to_text(self, client: Telnyx) -> None:
        with client.legacy.reporting.usage_reports.with_streaming_response.retrieve_speech_to_text() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage_report = response.parse()
            assert_matches_type(UsageReportRetrieveSpeechToTextResponse, usage_report, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsageReports:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_speech_to_text(self, async_client: AsyncTelnyx) -> None:
        usage_report = await async_client.legacy.reporting.usage_reports.retrieve_speech_to_text()
        assert_matches_type(UsageReportRetrieveSpeechToTextResponse, usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_speech_to_text_with_all_params(self, async_client: AsyncTelnyx) -> None:
        usage_report = await async_client.legacy.reporting.usage_reports.retrieve_speech_to_text(
            end_date=parse_datetime("2020-07-01T00:00:00-06:00"),
            start_date=parse_datetime("2020-07-01T00:00:00-06:00"),
        )
        assert_matches_type(UsageReportRetrieveSpeechToTextResponse, usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_speech_to_text(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.legacy.reporting.usage_reports.with_raw_response.retrieve_speech_to_text()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage_report = await response.parse()
        assert_matches_type(UsageReportRetrieveSpeechToTextResponse, usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_speech_to_text(self, async_client: AsyncTelnyx) -> None:
        async with (
            async_client.legacy.reporting.usage_reports.with_streaming_response.retrieve_speech_to_text()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage_report = await response.parse()
            assert_matches_type(UsageReportRetrieveSpeechToTextResponse, usage_report, path=["response"])

        assert cast(Any, response.is_closed) is True

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import VoiceSDKCallReport, VoiceSDKCallReportRetrieveResponse
from telnyx.pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVoiceSDKCallReports:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        voice_sdk_call_report = client.voice_sdk_call_reports.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(VoiceSDKCallReportRetrieveResponse, voice_sdk_call_report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.voice_sdk_call_reports.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice_sdk_call_report = response.parse()
        assert_matches_type(VoiceSDKCallReportRetrieveResponse, voice_sdk_call_report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.voice_sdk_call_reports.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice_sdk_call_report = response.parse()
            assert_matches_type(VoiceSDKCallReportRetrieveResponse, voice_sdk_call_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            client.voice_sdk_call_reports.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        voice_sdk_call_report = client.voice_sdk_call_reports.list()
        assert_matches_type(SyncDefaultFlatPagination[VoiceSDKCallReport], voice_sdk_call_report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        voice_sdk_call_report = client.voice_sdk_call_reports.list(
            page_number=0,
            page_size=0,
            sort="-created_at",
        )
        assert_matches_type(SyncDefaultFlatPagination[VoiceSDKCallReport], voice_sdk_call_report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.voice_sdk_call_reports.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice_sdk_call_report = response.parse()
        assert_matches_type(SyncDefaultFlatPagination[VoiceSDKCallReport], voice_sdk_call_report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.voice_sdk_call_reports.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice_sdk_call_report = response.parse()
            assert_matches_type(SyncDefaultFlatPagination[VoiceSDKCallReport], voice_sdk_call_report, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVoiceSDKCallReports:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        voice_sdk_call_report = await async_client.voice_sdk_call_reports.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(VoiceSDKCallReportRetrieveResponse, voice_sdk_call_report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.voice_sdk_call_reports.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice_sdk_call_report = await response.parse()
        assert_matches_type(VoiceSDKCallReportRetrieveResponse, voice_sdk_call_report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.voice_sdk_call_reports.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice_sdk_call_report = await response.parse()
            assert_matches_type(VoiceSDKCallReportRetrieveResponse, voice_sdk_call_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            await async_client.voice_sdk_call_reports.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        voice_sdk_call_report = await async_client.voice_sdk_call_reports.list()
        assert_matches_type(AsyncDefaultFlatPagination[VoiceSDKCallReport], voice_sdk_call_report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        voice_sdk_call_report = await async_client.voice_sdk_call_reports.list(
            page_number=0,
            page_size=0,
            sort="-created_at",
        )
        assert_matches_type(AsyncDefaultFlatPagination[VoiceSDKCallReport], voice_sdk_call_report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.voice_sdk_call_reports.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice_sdk_call_report = await response.parse()
        assert_matches_type(AsyncDefaultFlatPagination[VoiceSDKCallReport], voice_sdk_call_report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.voice_sdk_call_reports.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice_sdk_call_report = await response.parse()
            assert_matches_type(
                AsyncDefaultFlatPagination[VoiceSDKCallReport], voice_sdk_call_report, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

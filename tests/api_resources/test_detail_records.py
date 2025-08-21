# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import DetailRecordListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDetailRecords:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        detail_record = client.detail_records.list()
        assert_matches_type(DetailRecordListResponse, detail_record, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        detail_record = client.detail_records.list(
            filter={
                "record_type": "ai-voice-assistant",
                "date_range": "yesterday",
            },
            page={
                "number": 1,
                "size": 1,
            },
            sort=["string"],
        )
        assert_matches_type(DetailRecordListResponse, detail_record, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.detail_records.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail_record = response.parse()
        assert_matches_type(DetailRecordListResponse, detail_record, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.detail_records.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail_record = response.parse()
            assert_matches_type(DetailRecordListResponse, detail_record, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDetailRecords:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        detail_record = await async_client.detail_records.list()
        assert_matches_type(DetailRecordListResponse, detail_record, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        detail_record = await async_client.detail_records.list(
            filter={
                "record_type": "ai-voice-assistant",
                "date_range": "yesterday",
            },
            page={
                "number": 1,
                "size": 1,
            },
            sort=["string"],
        )
        assert_matches_type(DetailRecordListResponse, detail_record, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.detail_records.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail_record = await response.parse()
        assert_matches_type(DetailRecordListResponse, detail_record, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.detail_records.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail_record = await response.parse()
            assert_matches_type(DetailRecordListResponse, detail_record, path=["response"])

        assert cast(Any, response.is_closed) is True

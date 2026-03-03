# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import SessionAnalysisRetrieveResponse
from telnyx._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSessionAnalysis:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        session_analysis = client.session_analysis.retrieve(
            event_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            record_type="record_type",
        )
        assert_matches_type(SessionAnalysisRetrieveResponse, session_analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Telnyx) -> None:
        session_analysis = client.session_analysis.retrieve(
            event_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            record_type="record_type",
            date_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            expand="record",
            include_children=True,
            max_depth=1,
        )
        assert_matches_type(SessionAnalysisRetrieveResponse, session_analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.session_analysis.with_raw_response.retrieve(
            event_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            record_type="record_type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session_analysis = response.parse()
        assert_matches_type(SessionAnalysisRetrieveResponse, session_analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.session_analysis.with_streaming_response.retrieve(
            event_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            record_type="record_type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session_analysis = response.parse()
            assert_matches_type(SessionAnalysisRetrieveResponse, session_analysis, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `record_type` but received ''"):
            client.session_analysis.with_raw_response.retrieve(
                event_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                record_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.session_analysis.with_raw_response.retrieve(
                event_id="",
                record_type="record_type",
            )


class TestAsyncSessionAnalysis:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        session_analysis = await async_client.session_analysis.retrieve(
            event_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            record_type="record_type",
        )
        assert_matches_type(SessionAnalysisRetrieveResponse, session_analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncTelnyx) -> None:
        session_analysis = await async_client.session_analysis.retrieve(
            event_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            record_type="record_type",
            date_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            expand="record",
            include_children=True,
            max_depth=1,
        )
        assert_matches_type(SessionAnalysisRetrieveResponse, session_analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.session_analysis.with_raw_response.retrieve(
            event_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            record_type="record_type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session_analysis = await response.parse()
        assert_matches_type(SessionAnalysisRetrieveResponse, session_analysis, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.session_analysis.with_streaming_response.retrieve(
            event_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            record_type="record_type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session_analysis = await response.parse()
            assert_matches_type(SessionAnalysisRetrieveResponse, session_analysis, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `record_type` but received ''"):
            await async_client.session_analysis.with_raw_response.retrieve(
                event_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                record_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await async_client.session_analysis.with_raw_response.retrieve(
                event_id="",
                record_type="record_type",
            )

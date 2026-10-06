# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx._utils import parse_date
from telnyx.types.llm_token_gateway import UsageRetrieveSummaryResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_summary(self, client: Telnyx) -> None:
        usage = client.llm_token_gateway.usage.retrieve_summary(
            end_date=parse_date("2019-12-27"),
            start_date=parse_date("2019-12-27"),
            token_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UsageRetrieveSummaryResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_summary(self, client: Telnyx) -> None:
        response = client.llm_token_gateway.usage.with_raw_response.retrieve_summary(
            end_date=parse_date("2019-12-27"),
            start_date=parse_date("2019-12-27"),
            token_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageRetrieveSummaryResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_summary(self, client: Telnyx) -> None:
        with client.llm_token_gateway.usage.with_streaming_response.retrieve_summary(
            end_date=parse_date("2019-12-27"),
            start_date=parse_date("2019-12-27"),
            token_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageRetrieveSummaryResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_summary(self, async_client: AsyncTelnyx) -> None:
        usage = await async_client.llm_token_gateway.usage.retrieve_summary(
            end_date=parse_date("2019-12-27"),
            start_date=parse_date("2019-12-27"),
            token_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UsageRetrieveSummaryResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_summary(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.llm_token_gateway.usage.with_raw_response.retrieve_summary(
            end_date=parse_date("2019-12-27"),
            start_date=parse_date("2019-12-27"),
            token_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageRetrieveSummaryResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_summary(self, async_client: AsyncTelnyx) -> None:
        async with async_client.llm_token_gateway.usage.with_streaming_response.retrieve_summary(
            end_date=parse_date("2019-12-27"),
            start_date=parse_date("2019-12-27"),
            token_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageRetrieveSummaryResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

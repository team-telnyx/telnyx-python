# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    ReportListMdrsResponse,
    ReportListWdrsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReports:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_mdrs(self, client: Telnyx) -> None:
        report = client.reports.list_mdrs()
        assert_matches_type(ReportListMdrsResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_mdrs_with_all_params(self, client: Telnyx) -> None:
        report = client.reports.list_mdrs(
            id="e093fbe0-5bde-11eb-ae93-0242ac130002",
            cld="+15551237654",
            cli="+15551237654",
            direction="INBOUND",
            end_date="end_date",
            message_type="SMS",
            profile="My profile",
            start_date="start_date",
            status="DELIVERED",
        )
        assert_matches_type(ReportListMdrsResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_mdrs(self, client: Telnyx) -> None:
        response = client.reports.with_raw_response.list_mdrs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportListMdrsResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_mdrs(self, client: Telnyx) -> None:
        with client.reports.with_streaming_response.list_mdrs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportListMdrsResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_wdrs(self, client: Telnyx) -> None:
        report = client.reports.list_wdrs()
        assert_matches_type(ReportListWdrsResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_wdrs_with_all_params(self, client: Telnyx) -> None:
        report = client.reports.list_wdrs(
            id="e093fbe0-5bde-11eb-ae93-0242ac130002",
            end_date="2021-06-01T00:00:00Z",
            imsi="123456",
            mcc="204",
            mnc="01",
            page={
                "number": 0,
                "size": 0,
            },
            phone_number="+12345678910",
            sim_card_id="877f80a6-e5b2-4687-9a04-88076265720f",
            sim_group_id="f05a189f-7c46-4531-ac56-1460dc465a42",
            sim_group_name="sim name",
            sort=["string"],
            start_date="2021-05-01T00:00:00Z",
        )
        assert_matches_type(ReportListWdrsResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_wdrs(self, client: Telnyx) -> None:
        response = client.reports.with_raw_response.list_wdrs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportListWdrsResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_wdrs(self, client: Telnyx) -> None:
        with client.reports.with_streaming_response.list_wdrs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportListWdrsResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncReports:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_mdrs(self, async_client: AsyncTelnyx) -> None:
        report = await async_client.reports.list_mdrs()
        assert_matches_type(ReportListMdrsResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_mdrs_with_all_params(self, async_client: AsyncTelnyx) -> None:
        report = await async_client.reports.list_mdrs(
            id="e093fbe0-5bde-11eb-ae93-0242ac130002",
            cld="+15551237654",
            cli="+15551237654",
            direction="INBOUND",
            end_date="end_date",
            message_type="SMS",
            profile="My profile",
            start_date="start_date",
            status="DELIVERED",
        )
        assert_matches_type(ReportListMdrsResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_mdrs(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.reports.with_raw_response.list_mdrs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportListMdrsResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_mdrs(self, async_client: AsyncTelnyx) -> None:
        async with async_client.reports.with_streaming_response.list_mdrs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportListMdrsResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_wdrs(self, async_client: AsyncTelnyx) -> None:
        report = await async_client.reports.list_wdrs()
        assert_matches_type(ReportListWdrsResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_wdrs_with_all_params(self, async_client: AsyncTelnyx) -> None:
        report = await async_client.reports.list_wdrs(
            id="e093fbe0-5bde-11eb-ae93-0242ac130002",
            end_date="2021-06-01T00:00:00Z",
            imsi="123456",
            mcc="204",
            mnc="01",
            page={
                "number": 0,
                "size": 0,
            },
            phone_number="+12345678910",
            sim_card_id="877f80a6-e5b2-4687-9a04-88076265720f",
            sim_group_id="f05a189f-7c46-4531-ac56-1460dc465a42",
            sim_group_name="sim name",
            sort=["string"],
            start_date="2021-05-01T00:00:00Z",
        )
        assert_matches_type(ReportListWdrsResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_wdrs(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.reports.with_raw_response.list_wdrs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportListWdrsResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_wdrs(self, async_client: AsyncTelnyx) -> None:
        async with async_client.reports.with_streaming_response.list_wdrs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportListWdrsResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

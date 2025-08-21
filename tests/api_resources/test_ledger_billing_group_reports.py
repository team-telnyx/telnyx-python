# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    LedgerBillingGroupReportCreateResponse,
    LedgerBillingGroupReportRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLedgerBillingGroupReports:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        ledger_billing_group_report = client.ledger_billing_group_reports.create()
        assert_matches_type(LedgerBillingGroupReportCreateResponse, ledger_billing_group_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        ledger_billing_group_report = client.ledger_billing_group_reports.create(
            month=10,
            year=2019,
        )
        assert_matches_type(LedgerBillingGroupReportCreateResponse, ledger_billing_group_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.ledger_billing_group_reports.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_billing_group_report = response.parse()
        assert_matches_type(LedgerBillingGroupReportCreateResponse, ledger_billing_group_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.ledger_billing_group_reports.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_billing_group_report = response.parse()
            assert_matches_type(LedgerBillingGroupReportCreateResponse, ledger_billing_group_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        ledger_billing_group_report = client.ledger_billing_group_reports.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(LedgerBillingGroupReportRetrieveResponse, ledger_billing_group_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.ledger_billing_group_reports.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_billing_group_report = response.parse()
        assert_matches_type(LedgerBillingGroupReportRetrieveResponse, ledger_billing_group_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.ledger_billing_group_reports.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_billing_group_report = response.parse()
            assert_matches_type(
                LedgerBillingGroupReportRetrieveResponse, ledger_billing_group_report, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.ledger_billing_group_reports.with_raw_response.retrieve(
                "",
            )


class TestAsyncLedgerBillingGroupReports:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        ledger_billing_group_report = await async_client.ledger_billing_group_reports.create()
        assert_matches_type(LedgerBillingGroupReportCreateResponse, ledger_billing_group_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        ledger_billing_group_report = await async_client.ledger_billing_group_reports.create(
            month=10,
            year=2019,
        )
        assert_matches_type(LedgerBillingGroupReportCreateResponse, ledger_billing_group_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ledger_billing_group_reports.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_billing_group_report = await response.parse()
        assert_matches_type(LedgerBillingGroupReportCreateResponse, ledger_billing_group_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ledger_billing_group_reports.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_billing_group_report = await response.parse()
            assert_matches_type(LedgerBillingGroupReportCreateResponse, ledger_billing_group_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        ledger_billing_group_report = await async_client.ledger_billing_group_reports.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(LedgerBillingGroupReportRetrieveResponse, ledger_billing_group_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ledger_billing_group_reports.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ledger_billing_group_report = await response.parse()
        assert_matches_type(LedgerBillingGroupReportRetrieveResponse, ledger_billing_group_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ledger_billing_group_reports.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ledger_billing_group_report = await response.parse()
            assert_matches_type(
                LedgerBillingGroupReportRetrieveResponse, ledger_billing_group_report, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.ledger_billing_group_reports.with_raw_response.retrieve(
                "",
            )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx._utils import parse_datetime
from telnyx.types.reports import (
    MdrUsageReportListResponse,
    MdrUsageReportCreateResponse,
    MdrUsageReportDeleteResponse,
    MdrUsageReportRetrieveResponse,
    MdrUsageReportFetchSyncResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMdrUsageReports:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        mdr_usage_report = client.reports.mdr_usage_reports.create(
            aggregation_type="NO_AGGREGATION",
            end_date=parse_datetime("2020-07-01T00:00:00-06:00"),
            start_date=parse_datetime("2020-07-01T00:00:00-06:00"),
        )
        assert_matches_type(MdrUsageReportCreateResponse, mdr_usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        mdr_usage_report = client.reports.mdr_usage_reports.create(
            aggregation_type="NO_AGGREGATION",
            end_date=parse_datetime("2020-07-01T00:00:00-06:00"),
            start_date=parse_datetime("2020-07-01T00:00:00-06:00"),
            profiles="My profile",
        )
        assert_matches_type(MdrUsageReportCreateResponse, mdr_usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.reports.mdr_usage_reports.with_raw_response.create(
            aggregation_type="NO_AGGREGATION",
            end_date=parse_datetime("2020-07-01T00:00:00-06:00"),
            start_date=parse_datetime("2020-07-01T00:00:00-06:00"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mdr_usage_report = response.parse()
        assert_matches_type(MdrUsageReportCreateResponse, mdr_usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.reports.mdr_usage_reports.with_streaming_response.create(
            aggregation_type="NO_AGGREGATION",
            end_date=parse_datetime("2020-07-01T00:00:00-06:00"),
            start_date=parse_datetime("2020-07-01T00:00:00-06:00"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mdr_usage_report = response.parse()
            assert_matches_type(MdrUsageReportCreateResponse, mdr_usage_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        mdr_usage_report = client.reports.mdr_usage_reports.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MdrUsageReportRetrieveResponse, mdr_usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.reports.mdr_usage_reports.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mdr_usage_report = response.parse()
        assert_matches_type(MdrUsageReportRetrieveResponse, mdr_usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.reports.mdr_usage_reports.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mdr_usage_report = response.parse()
            assert_matches_type(MdrUsageReportRetrieveResponse, mdr_usage_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.reports.mdr_usage_reports.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        mdr_usage_report = client.reports.mdr_usage_reports.list()
        assert_matches_type(MdrUsageReportListResponse, mdr_usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        mdr_usage_report = client.reports.mdr_usage_reports.list(
            page={
                "number": 0,
                "size": 0,
            },
        )
        assert_matches_type(MdrUsageReportListResponse, mdr_usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.reports.mdr_usage_reports.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mdr_usage_report = response.parse()
        assert_matches_type(MdrUsageReportListResponse, mdr_usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.reports.mdr_usage_reports.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mdr_usage_report = response.parse()
            assert_matches_type(MdrUsageReportListResponse, mdr_usage_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        mdr_usage_report = client.reports.mdr_usage_reports.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MdrUsageReportDeleteResponse, mdr_usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.reports.mdr_usage_reports.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mdr_usage_report = response.parse()
        assert_matches_type(MdrUsageReportDeleteResponse, mdr_usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.reports.mdr_usage_reports.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mdr_usage_report = response.parse()
            assert_matches_type(MdrUsageReportDeleteResponse, mdr_usage_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.reports.mdr_usage_reports.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_fetch_sync(self, client: Telnyx) -> None:
        mdr_usage_report = client.reports.mdr_usage_reports.fetch_sync(
            aggregation_type="NO_AGGREGATION",
        )
        assert_matches_type(MdrUsageReportFetchSyncResponse, mdr_usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_fetch_sync_with_all_params(self, client: Telnyx) -> None:
        mdr_usage_report = client.reports.mdr_usage_reports.fetch_sync(
            aggregation_type="NO_AGGREGATION",
            end_date=parse_datetime("2020-07-01T00:00:00-06:00"),
            profiles=["My profile"],
            start_date=parse_datetime("2020-07-01T00:00:00-06:00"),
        )
        assert_matches_type(MdrUsageReportFetchSyncResponse, mdr_usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_fetch_sync(self, client: Telnyx) -> None:
        response = client.reports.mdr_usage_reports.with_raw_response.fetch_sync(
            aggregation_type="NO_AGGREGATION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mdr_usage_report = response.parse()
        assert_matches_type(MdrUsageReportFetchSyncResponse, mdr_usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_fetch_sync(self, client: Telnyx) -> None:
        with client.reports.mdr_usage_reports.with_streaming_response.fetch_sync(
            aggregation_type="NO_AGGREGATION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mdr_usage_report = response.parse()
            assert_matches_type(MdrUsageReportFetchSyncResponse, mdr_usage_report, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMdrUsageReports:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        mdr_usage_report = await async_client.reports.mdr_usage_reports.create(
            aggregation_type="NO_AGGREGATION",
            end_date=parse_datetime("2020-07-01T00:00:00-06:00"),
            start_date=parse_datetime("2020-07-01T00:00:00-06:00"),
        )
        assert_matches_type(MdrUsageReportCreateResponse, mdr_usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        mdr_usage_report = await async_client.reports.mdr_usage_reports.create(
            aggregation_type="NO_AGGREGATION",
            end_date=parse_datetime("2020-07-01T00:00:00-06:00"),
            start_date=parse_datetime("2020-07-01T00:00:00-06:00"),
            profiles="My profile",
        )
        assert_matches_type(MdrUsageReportCreateResponse, mdr_usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.reports.mdr_usage_reports.with_raw_response.create(
            aggregation_type="NO_AGGREGATION",
            end_date=parse_datetime("2020-07-01T00:00:00-06:00"),
            start_date=parse_datetime("2020-07-01T00:00:00-06:00"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mdr_usage_report = await response.parse()
        assert_matches_type(MdrUsageReportCreateResponse, mdr_usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.reports.mdr_usage_reports.with_streaming_response.create(
            aggregation_type="NO_AGGREGATION",
            end_date=parse_datetime("2020-07-01T00:00:00-06:00"),
            start_date=parse_datetime("2020-07-01T00:00:00-06:00"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mdr_usage_report = await response.parse()
            assert_matches_type(MdrUsageReportCreateResponse, mdr_usage_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        mdr_usage_report = await async_client.reports.mdr_usage_reports.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MdrUsageReportRetrieveResponse, mdr_usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.reports.mdr_usage_reports.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mdr_usage_report = await response.parse()
        assert_matches_type(MdrUsageReportRetrieveResponse, mdr_usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.reports.mdr_usage_reports.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mdr_usage_report = await response.parse()
            assert_matches_type(MdrUsageReportRetrieveResponse, mdr_usage_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.reports.mdr_usage_reports.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        mdr_usage_report = await async_client.reports.mdr_usage_reports.list()
        assert_matches_type(MdrUsageReportListResponse, mdr_usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        mdr_usage_report = await async_client.reports.mdr_usage_reports.list(
            page={
                "number": 0,
                "size": 0,
            },
        )
        assert_matches_type(MdrUsageReportListResponse, mdr_usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.reports.mdr_usage_reports.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mdr_usage_report = await response.parse()
        assert_matches_type(MdrUsageReportListResponse, mdr_usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.reports.mdr_usage_reports.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mdr_usage_report = await response.parse()
            assert_matches_type(MdrUsageReportListResponse, mdr_usage_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        mdr_usage_report = await async_client.reports.mdr_usage_reports.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MdrUsageReportDeleteResponse, mdr_usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.reports.mdr_usage_reports.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mdr_usage_report = await response.parse()
        assert_matches_type(MdrUsageReportDeleteResponse, mdr_usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.reports.mdr_usage_reports.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mdr_usage_report = await response.parse()
            assert_matches_type(MdrUsageReportDeleteResponse, mdr_usage_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.reports.mdr_usage_reports.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_fetch_sync(self, async_client: AsyncTelnyx) -> None:
        mdr_usage_report = await async_client.reports.mdr_usage_reports.fetch_sync(
            aggregation_type="NO_AGGREGATION",
        )
        assert_matches_type(MdrUsageReportFetchSyncResponse, mdr_usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_fetch_sync_with_all_params(self, async_client: AsyncTelnyx) -> None:
        mdr_usage_report = await async_client.reports.mdr_usage_reports.fetch_sync(
            aggregation_type="NO_AGGREGATION",
            end_date=parse_datetime("2020-07-01T00:00:00-06:00"),
            profiles=["My profile"],
            start_date=parse_datetime("2020-07-01T00:00:00-06:00"),
        )
        assert_matches_type(MdrUsageReportFetchSyncResponse, mdr_usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_fetch_sync(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.reports.mdr_usage_reports.with_raw_response.fetch_sync(
            aggregation_type="NO_AGGREGATION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mdr_usage_report = await response.parse()
        assert_matches_type(MdrUsageReportFetchSyncResponse, mdr_usage_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_fetch_sync(self, async_client: AsyncTelnyx) -> None:
        async with async_client.reports.mdr_usage_reports.with_streaming_response.fetch_sync(
            aggregation_type="NO_AGGREGATION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mdr_usage_report = await response.parse()
            assert_matches_type(MdrUsageReportFetchSyncResponse, mdr_usage_report, path=["response"])

        assert cast(Any, response.is_closed) is True

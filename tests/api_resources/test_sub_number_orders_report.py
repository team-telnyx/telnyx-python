# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    SubNumberOrdersReportCreateResponse,
    SubNumberOrdersReportRetrieveResponse,
)
from telnyx._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubNumberOrdersReport:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        sub_number_orders_report = client.sub_number_orders_report.create()
        assert_matches_type(SubNumberOrdersReportCreateResponse, sub_number_orders_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        sub_number_orders_report = client.sub_number_orders_report.create(
            country_code="US",
            created_at_gt=parse_datetime("2023-04-05T10:22:08.230549Z"),
            created_at_lt=parse_datetime("2025-06-05T10:22:08.230549Z"),
            customer_reference="STRING",
            order_request_id="12ade33a-21c0-473b-b055-b3c836e1c293",
            status="success",
        )
        assert_matches_type(SubNumberOrdersReportCreateResponse, sub_number_orders_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.sub_number_orders_report.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sub_number_orders_report = response.parse()
        assert_matches_type(SubNumberOrdersReportCreateResponse, sub_number_orders_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.sub_number_orders_report.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sub_number_orders_report = response.parse()
            assert_matches_type(SubNumberOrdersReportCreateResponse, sub_number_orders_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        sub_number_orders_report = client.sub_number_orders_report.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SubNumberOrdersReportRetrieveResponse, sub_number_orders_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.sub_number_orders_report.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sub_number_orders_report = response.parse()
        assert_matches_type(SubNumberOrdersReportRetrieveResponse, sub_number_orders_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.sub_number_orders_report.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sub_number_orders_report = response.parse()
            assert_matches_type(SubNumberOrdersReportRetrieveResponse, sub_number_orders_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_id` but received ''"):
            client.sub_number_orders_report.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_download(self, client: Telnyx) -> None:
        sub_number_orders_report = client.sub_number_orders_report.download(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(str, sub_number_orders_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_download(self, client: Telnyx) -> None:
        response = client.sub_number_orders_report.with_raw_response.download(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sub_number_orders_report = response.parse()
        assert_matches_type(str, sub_number_orders_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_download(self, client: Telnyx) -> None:
        with client.sub_number_orders_report.with_streaming_response.download(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sub_number_orders_report = response.parse()
            assert_matches_type(str, sub_number_orders_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_download(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_id` but received ''"):
            client.sub_number_orders_report.with_raw_response.download(
                "",
            )


class TestAsyncSubNumberOrdersReport:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        sub_number_orders_report = await async_client.sub_number_orders_report.create()
        assert_matches_type(SubNumberOrdersReportCreateResponse, sub_number_orders_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        sub_number_orders_report = await async_client.sub_number_orders_report.create(
            country_code="US",
            created_at_gt=parse_datetime("2023-04-05T10:22:08.230549Z"),
            created_at_lt=parse_datetime("2025-06-05T10:22:08.230549Z"),
            customer_reference="STRING",
            order_request_id="12ade33a-21c0-473b-b055-b3c836e1c293",
            status="success",
        )
        assert_matches_type(SubNumberOrdersReportCreateResponse, sub_number_orders_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.sub_number_orders_report.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sub_number_orders_report = await response.parse()
        assert_matches_type(SubNumberOrdersReportCreateResponse, sub_number_orders_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.sub_number_orders_report.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sub_number_orders_report = await response.parse()
            assert_matches_type(SubNumberOrdersReportCreateResponse, sub_number_orders_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        sub_number_orders_report = await async_client.sub_number_orders_report.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SubNumberOrdersReportRetrieveResponse, sub_number_orders_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.sub_number_orders_report.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sub_number_orders_report = await response.parse()
        assert_matches_type(SubNumberOrdersReportRetrieveResponse, sub_number_orders_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.sub_number_orders_report.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sub_number_orders_report = await response.parse()
            assert_matches_type(SubNumberOrdersReportRetrieveResponse, sub_number_orders_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_id` but received ''"):
            await async_client.sub_number_orders_report.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_download(self, async_client: AsyncTelnyx) -> None:
        sub_number_orders_report = await async_client.sub_number_orders_report.download(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(str, sub_number_orders_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_download(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.sub_number_orders_report.with_raw_response.download(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sub_number_orders_report = await response.parse()
        assert_matches_type(str, sub_number_orders_report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_download(self, async_client: AsyncTelnyx) -> None:
        async with async_client.sub_number_orders_report.with_streaming_response.download(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sub_number_orders_report = await response.parse()
            assert_matches_type(str, sub_number_orders_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_download(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_id` but received ''"):
            await async_client.sub_number_orders_report.with_raw_response.download(
                "",
            )

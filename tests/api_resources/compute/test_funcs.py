# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx._utils import parse_datetime
from telnyx.types.compute import (
    FuncRetrieveLogsResponse,
    FuncRetrieveRevisionsResponse,
    FuncRetrieveShipInspectionResponse,
    FuncRetrieveMetricAggregatesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFuncs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_logs(self, client: Telnyx) -> None:
        func = client.compute.funcs.retrieve_logs(
            id="id",
        )
        assert_matches_type(FuncRetrieveLogsResponse, func, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_logs_with_all_params(self, client: Telnyx) -> None:
        func = client.compute.funcs.retrieve_logs(
            id="id",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1,
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="runtime",
        )
        assert_matches_type(FuncRetrieveLogsResponse, func, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_logs(self, client: Telnyx) -> None:
        response = client.compute.funcs.with_raw_response.retrieve_logs(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        func = response.parse()
        assert_matches_type(FuncRetrieveLogsResponse, func, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_logs(self, client: Telnyx) -> None:
        with client.compute.funcs.with_streaming_response.retrieve_logs(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            func = response.parse()
            assert_matches_type(FuncRetrieveLogsResponse, func, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_logs(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.compute.funcs.with_raw_response.retrieve_logs(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_metric_aggregates(self, client: Telnyx) -> None:
        func = client.compute.funcs.retrieve_metric_aggregates(
            id="id",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(FuncRetrieveMetricAggregatesResponse, func, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_metric_aggregates_with_all_params(self, client: Telnyx) -> None:
        func = client.compute.funcs.retrieve_metric_aggregates(
            id="id",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            filter_edge_site="filter[edge_site]",
            filter_namespace="filter[namespace]",
            page_number=0,
            page_size=1,
        )
        assert_matches_type(FuncRetrieveMetricAggregatesResponse, func, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_metric_aggregates(self, client: Telnyx) -> None:
        response = client.compute.funcs.with_raw_response.retrieve_metric_aggregates(
            id="id",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        func = response.parse()
        assert_matches_type(FuncRetrieveMetricAggregatesResponse, func, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_metric_aggregates(self, client: Telnyx) -> None:
        with client.compute.funcs.with_streaming_response.retrieve_metric_aggregates(
            id="id",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            func = response.parse()
            assert_matches_type(FuncRetrieveMetricAggregatesResponse, func, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_metric_aggregates(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.compute.funcs.with_raw_response.retrieve_metric_aggregates(
                id="",
                end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
                start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_revisions(self, client: Telnyx) -> None:
        func = client.compute.funcs.retrieve_revisions(
            id="id",
        )
        assert_matches_type(FuncRetrieveRevisionsResponse, func, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_revisions_with_all_params(self, client: Telnyx) -> None:
        func = client.compute.funcs.retrieve_revisions(
            id="id",
            page_number=1,
            page_size=1,
        )
        assert_matches_type(FuncRetrieveRevisionsResponse, func, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_revisions(self, client: Telnyx) -> None:
        response = client.compute.funcs.with_raw_response.retrieve_revisions(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        func = response.parse()
        assert_matches_type(FuncRetrieveRevisionsResponse, func, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_revisions(self, client: Telnyx) -> None:
        with client.compute.funcs.with_streaming_response.retrieve_revisions(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            func = response.parse()
            assert_matches_type(FuncRetrieveRevisionsResponse, func, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_revisions(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.compute.funcs.with_raw_response.retrieve_revisions(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_ship_inspection(self, client: Telnyx) -> None:
        func = client.compute.funcs.retrieve_ship_inspection(
            "id",
        )
        assert_matches_type(FuncRetrieveShipInspectionResponse, func, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_ship_inspection(self, client: Telnyx) -> None:
        response = client.compute.funcs.with_raw_response.retrieve_ship_inspection(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        func = response.parse()
        assert_matches_type(FuncRetrieveShipInspectionResponse, func, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_ship_inspection(self, client: Telnyx) -> None:
        with client.compute.funcs.with_streaming_response.retrieve_ship_inspection(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            func = response.parse()
            assert_matches_type(FuncRetrieveShipInspectionResponse, func, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_ship_inspection(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.compute.funcs.with_raw_response.retrieve_ship_inspection(
                "",
            )


class TestAsyncFuncs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_logs(self, async_client: AsyncTelnyx) -> None:
        func = await async_client.compute.funcs.retrieve_logs(
            id="id",
        )
        assert_matches_type(FuncRetrieveLogsResponse, func, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_logs_with_all_params(self, async_client: AsyncTelnyx) -> None:
        func = await async_client.compute.funcs.retrieve_logs(
            id="id",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1,
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            type="runtime",
        )
        assert_matches_type(FuncRetrieveLogsResponse, func, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_logs(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.compute.funcs.with_raw_response.retrieve_logs(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        func = await response.parse()
        assert_matches_type(FuncRetrieveLogsResponse, func, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_logs(self, async_client: AsyncTelnyx) -> None:
        async with async_client.compute.funcs.with_streaming_response.retrieve_logs(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            func = await response.parse()
            assert_matches_type(FuncRetrieveLogsResponse, func, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_logs(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.compute.funcs.with_raw_response.retrieve_logs(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_metric_aggregates(self, async_client: AsyncTelnyx) -> None:
        func = await async_client.compute.funcs.retrieve_metric_aggregates(
            id="id",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(FuncRetrieveMetricAggregatesResponse, func, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_metric_aggregates_with_all_params(self, async_client: AsyncTelnyx) -> None:
        func = await async_client.compute.funcs.retrieve_metric_aggregates(
            id="id",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            filter_edge_site="filter[edge_site]",
            filter_namespace="filter[namespace]",
            page_number=0,
            page_size=1,
        )
        assert_matches_type(FuncRetrieveMetricAggregatesResponse, func, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_metric_aggregates(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.compute.funcs.with_raw_response.retrieve_metric_aggregates(
            id="id",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        func = await response.parse()
        assert_matches_type(FuncRetrieveMetricAggregatesResponse, func, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_metric_aggregates(self, async_client: AsyncTelnyx) -> None:
        async with async_client.compute.funcs.with_streaming_response.retrieve_metric_aggregates(
            id="id",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            func = await response.parse()
            assert_matches_type(FuncRetrieveMetricAggregatesResponse, func, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_metric_aggregates(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.compute.funcs.with_raw_response.retrieve_metric_aggregates(
                id="",
                end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
                start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_revisions(self, async_client: AsyncTelnyx) -> None:
        func = await async_client.compute.funcs.retrieve_revisions(
            id="id",
        )
        assert_matches_type(FuncRetrieveRevisionsResponse, func, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_revisions_with_all_params(self, async_client: AsyncTelnyx) -> None:
        func = await async_client.compute.funcs.retrieve_revisions(
            id="id",
            page_number=1,
            page_size=1,
        )
        assert_matches_type(FuncRetrieveRevisionsResponse, func, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_revisions(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.compute.funcs.with_raw_response.retrieve_revisions(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        func = await response.parse()
        assert_matches_type(FuncRetrieveRevisionsResponse, func, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_revisions(self, async_client: AsyncTelnyx) -> None:
        async with async_client.compute.funcs.with_streaming_response.retrieve_revisions(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            func = await response.parse()
            assert_matches_type(FuncRetrieveRevisionsResponse, func, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_revisions(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.compute.funcs.with_raw_response.retrieve_revisions(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_ship_inspection(self, async_client: AsyncTelnyx) -> None:
        func = await async_client.compute.funcs.retrieve_ship_inspection(
            "id",
        )
        assert_matches_type(FuncRetrieveShipInspectionResponse, func, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_ship_inspection(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.compute.funcs.with_raw_response.retrieve_ship_inspection(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        func = await response.parse()
        assert_matches_type(FuncRetrieveShipInspectionResponse, func, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_ship_inspection(self, async_client: AsyncTelnyx) -> None:
        async with async_client.compute.funcs.with_streaming_response.retrieve_ship_inspection(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            func = await response.parse()
            assert_matches_type(FuncRetrieveShipInspectionResponse, func, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_ship_inspection(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.compute.funcs.with_raw_response.retrieve_ship_inspection(
                "",
            )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.phone_numbers import (
    CsvDownloadListResponse,
    CsvDownloadCreateResponse,
    CsvDownloadRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCsvDownloads:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        csv_download = client.phone_numbers.csv_downloads.create()
        assert_matches_type(CsvDownloadCreateResponse, csv_download, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        csv_download = client.phone_numbers.csv_downloads.create(
            csv_format="V2",
            filter={
                "billing_group_id": "62e4bf2e-c278-4282-b524-488d9c9c43b2",
                "connection_id": "1521916448077776306",
                "customer_reference": "customer_reference",
                "emergency_address_id": "9102160989215728032",
                "has_bundle": "has_bundle",
                "phone_number": "phone_number",
                "status": "active",
                "tag": "tag",
                "voice_connection_name": {
                    "contains": "test",
                    "ends_with": "test",
                    "eq": "test",
                    "starts_with": "test",
                },
                "voice_usage_payment_method": "channel",
            },
        )
        assert_matches_type(CsvDownloadCreateResponse, csv_download, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.phone_numbers.csv_downloads.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        csv_download = response.parse()
        assert_matches_type(CsvDownloadCreateResponse, csv_download, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.phone_numbers.csv_downloads.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            csv_download = response.parse()
            assert_matches_type(CsvDownloadCreateResponse, csv_download, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        csv_download = client.phone_numbers.csv_downloads.retrieve(
            "id",
        )
        assert_matches_type(CsvDownloadRetrieveResponse, csv_download, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.phone_numbers.csv_downloads.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        csv_download = response.parse()
        assert_matches_type(CsvDownloadRetrieveResponse, csv_download, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.phone_numbers.csv_downloads.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            csv_download = response.parse()
            assert_matches_type(CsvDownloadRetrieveResponse, csv_download, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.phone_numbers.csv_downloads.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        csv_download = client.phone_numbers.csv_downloads.list()
        assert_matches_type(CsvDownloadListResponse, csv_download, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        csv_download = client.phone_numbers.csv_downloads.list(
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(CsvDownloadListResponse, csv_download, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.phone_numbers.csv_downloads.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        csv_download = response.parse()
        assert_matches_type(CsvDownloadListResponse, csv_download, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.phone_numbers.csv_downloads.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            csv_download = response.parse()
            assert_matches_type(CsvDownloadListResponse, csv_download, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCsvDownloads:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        csv_download = await async_client.phone_numbers.csv_downloads.create()
        assert_matches_type(CsvDownloadCreateResponse, csv_download, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        csv_download = await async_client.phone_numbers.csv_downloads.create(
            csv_format="V2",
            filter={
                "billing_group_id": "62e4bf2e-c278-4282-b524-488d9c9c43b2",
                "connection_id": "1521916448077776306",
                "customer_reference": "customer_reference",
                "emergency_address_id": "9102160989215728032",
                "has_bundle": "has_bundle",
                "phone_number": "phone_number",
                "status": "active",
                "tag": "tag",
                "voice_connection_name": {
                    "contains": "test",
                    "ends_with": "test",
                    "eq": "test",
                    "starts_with": "test",
                },
                "voice_usage_payment_method": "channel",
            },
        )
        assert_matches_type(CsvDownloadCreateResponse, csv_download, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.phone_numbers.csv_downloads.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        csv_download = await response.parse()
        assert_matches_type(CsvDownloadCreateResponse, csv_download, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.phone_numbers.csv_downloads.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            csv_download = await response.parse()
            assert_matches_type(CsvDownloadCreateResponse, csv_download, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        csv_download = await async_client.phone_numbers.csv_downloads.retrieve(
            "id",
        )
        assert_matches_type(CsvDownloadRetrieveResponse, csv_download, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.phone_numbers.csv_downloads.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        csv_download = await response.parse()
        assert_matches_type(CsvDownloadRetrieveResponse, csv_download, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.phone_numbers.csv_downloads.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            csv_download = await response.parse()
            assert_matches_type(CsvDownloadRetrieveResponse, csv_download, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.phone_numbers.csv_downloads.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        csv_download = await async_client.phone_numbers.csv_downloads.list()
        assert_matches_type(CsvDownloadListResponse, csv_download, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        csv_download = await async_client.phone_numbers.csv_downloads.list(
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(CsvDownloadListResponse, csv_download, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.phone_numbers.csv_downloads.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        csv_download = await response.parse()
        assert_matches_type(CsvDownloadListResponse, csv_download, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.phone_numbers.csv_downloads.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            csv_download = await response.parse()
            assert_matches_type(CsvDownloadListResponse, csv_download, path=["response"])

        assert cast(Any, response.is_closed) is True

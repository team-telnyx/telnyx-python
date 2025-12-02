# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx._utils import parse_date
from telnyx.types.legacy.reporting.usage_reports import (
    NumberLookupListResponse,
    NumberLookupCreateResponse,
    NumberLookupRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNumberLookup:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        number_lookup = client.legacy.reporting.usage_reports.number_lookup.create()
        assert_matches_type(NumberLookupCreateResponse, number_lookup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        number_lookup = client.legacy.reporting.usage_reports.number_lookup.create(
            aggregation_type="ALL",
            end_date=parse_date("2025-02-10"),
            managed_accounts=["f47ac10b-58cc-4372-a567-0e02b2c3d479", "6ba7b810-9dad-11d1-80b4-00c04fd430c8"],
            start_date=parse_date("2025-02-10"),
        )
        assert_matches_type(NumberLookupCreateResponse, number_lookup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.legacy.reporting.usage_reports.number_lookup.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_lookup = response.parse()
        assert_matches_type(NumberLookupCreateResponse, number_lookup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.legacy.reporting.usage_reports.number_lookup.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_lookup = response.parse()
            assert_matches_type(NumberLookupCreateResponse, number_lookup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        number_lookup = client.legacy.reporting.usage_reports.number_lookup.retrieve(
            "id",
        )
        assert_matches_type(NumberLookupRetrieveResponse, number_lookup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.legacy.reporting.usage_reports.number_lookup.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_lookup = response.parse()
        assert_matches_type(NumberLookupRetrieveResponse, number_lookup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.legacy.reporting.usage_reports.number_lookup.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_lookup = response.parse()
            assert_matches_type(NumberLookupRetrieveResponse, number_lookup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.legacy.reporting.usage_reports.number_lookup.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        number_lookup = client.legacy.reporting.usage_reports.number_lookup.list()
        assert_matches_type(NumberLookupListResponse, number_lookup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.legacy.reporting.usage_reports.number_lookup.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_lookup = response.parse()
        assert_matches_type(NumberLookupListResponse, number_lookup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.legacy.reporting.usage_reports.number_lookup.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_lookup = response.parse()
            assert_matches_type(NumberLookupListResponse, number_lookup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        number_lookup = client.legacy.reporting.usage_reports.number_lookup.delete(
            "id",
        )
        assert number_lookup is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.legacy.reporting.usage_reports.number_lookup.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_lookup = response.parse()
        assert number_lookup is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.legacy.reporting.usage_reports.number_lookup.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_lookup = response.parse()
            assert number_lookup is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.legacy.reporting.usage_reports.number_lookup.with_raw_response.delete(
                "",
            )


class TestAsyncNumberLookup:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        number_lookup = await async_client.legacy.reporting.usage_reports.number_lookup.create()
        assert_matches_type(NumberLookupCreateResponse, number_lookup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        number_lookup = await async_client.legacy.reporting.usage_reports.number_lookup.create(
            aggregation_type="ALL",
            end_date=parse_date("2025-02-10"),
            managed_accounts=["f47ac10b-58cc-4372-a567-0e02b2c3d479", "6ba7b810-9dad-11d1-80b4-00c04fd430c8"],
            start_date=parse_date("2025-02-10"),
        )
        assert_matches_type(NumberLookupCreateResponse, number_lookup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.legacy.reporting.usage_reports.number_lookup.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_lookup = await response.parse()
        assert_matches_type(NumberLookupCreateResponse, number_lookup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with (
            async_client.legacy.reporting.usage_reports.number_lookup.with_streaming_response.create()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_lookup = await response.parse()
            assert_matches_type(NumberLookupCreateResponse, number_lookup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        number_lookup = await async_client.legacy.reporting.usage_reports.number_lookup.retrieve(
            "id",
        )
        assert_matches_type(NumberLookupRetrieveResponse, number_lookup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.legacy.reporting.usage_reports.number_lookup.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_lookup = await response.parse()
        assert_matches_type(NumberLookupRetrieveResponse, number_lookup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.legacy.reporting.usage_reports.number_lookup.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_lookup = await response.parse()
            assert_matches_type(NumberLookupRetrieveResponse, number_lookup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.legacy.reporting.usage_reports.number_lookup.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        number_lookup = await async_client.legacy.reporting.usage_reports.number_lookup.list()
        assert_matches_type(NumberLookupListResponse, number_lookup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.legacy.reporting.usage_reports.number_lookup.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_lookup = await response.parse()
        assert_matches_type(NumberLookupListResponse, number_lookup, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.legacy.reporting.usage_reports.number_lookup.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_lookup = await response.parse()
            assert_matches_type(NumberLookupListResponse, number_lookup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        number_lookup = await async_client.legacy.reporting.usage_reports.number_lookup.delete(
            "id",
        )
        assert number_lookup is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.legacy.reporting.usage_reports.number_lookup.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_lookup = await response.parse()
        assert number_lookup is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.legacy.reporting.usage_reports.number_lookup.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_lookup = await response.parse()
            assert number_lookup is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.legacy.reporting.usage_reports.number_lookup.with_raw_response.delete(
                "",
            )

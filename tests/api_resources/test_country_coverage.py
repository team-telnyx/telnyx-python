# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import CountryCoverageRetrieveResponse, CountryCoverageRetrieveCountryResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCountryCoverage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        country_coverage = client.country_coverage.retrieve()
        assert_matches_type(CountryCoverageRetrieveResponse, country_coverage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.country_coverage.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country_coverage = response.parse()
        assert_matches_type(CountryCoverageRetrieveResponse, country_coverage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.country_coverage.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country_coverage = response.parse()
            assert_matches_type(CountryCoverageRetrieveResponse, country_coverage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_country(self, client: Telnyx) -> None:
        country_coverage = client.country_coverage.retrieve_country(
            "US",
        )
        assert_matches_type(CountryCoverageRetrieveCountryResponse, country_coverage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_country(self, client: Telnyx) -> None:
        response = client.country_coverage.with_raw_response.retrieve_country(
            "US",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country_coverage = response.parse()
        assert_matches_type(CountryCoverageRetrieveCountryResponse, country_coverage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_country(self, client: Telnyx) -> None:
        with client.country_coverage.with_streaming_response.retrieve_country(
            "US",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country_coverage = response.parse()
            assert_matches_type(CountryCoverageRetrieveCountryResponse, country_coverage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_country(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `country_code` but received ''"):
            client.country_coverage.with_raw_response.retrieve_country(
                "",
            )


class TestAsyncCountryCoverage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        country_coverage = await async_client.country_coverage.retrieve()
        assert_matches_type(CountryCoverageRetrieveResponse, country_coverage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.country_coverage.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country_coverage = await response.parse()
        assert_matches_type(CountryCoverageRetrieveResponse, country_coverage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.country_coverage.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country_coverage = await response.parse()
            assert_matches_type(CountryCoverageRetrieveResponse, country_coverage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_country(self, async_client: AsyncTelnyx) -> None:
        country_coverage = await async_client.country_coverage.retrieve_country(
            "US",
        )
        assert_matches_type(CountryCoverageRetrieveCountryResponse, country_coverage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_country(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.country_coverage.with_raw_response.retrieve_country(
            "US",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country_coverage = await response.parse()
        assert_matches_type(CountryCoverageRetrieveCountryResponse, country_coverage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_country(self, async_client: AsyncTelnyx) -> None:
        async with async_client.country_coverage.with_streaming_response.retrieve_country(
            "US",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country_coverage = await response.parse()
            assert_matches_type(CountryCoverageRetrieveCountryResponse, country_coverage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_country(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `country_code` but received ''"):
            await async_client.country_coverage.with_raw_response.retrieve_country(
                "",
            )

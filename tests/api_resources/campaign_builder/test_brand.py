# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.campaign_builder import BrandQualifyByUsecaseResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBrand:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_qualify_by_usecase(self, client: Telnyx) -> None:
        brand = client.campaign_builder.brand.qualify_by_usecase(
            usecase="usecase",
            brand_id="brandId",
        )
        assert_matches_type(BrandQualifyByUsecaseResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_qualify_by_usecase(self, client: Telnyx) -> None:
        response = client.campaign_builder.brand.with_raw_response.qualify_by_usecase(
            usecase="usecase",
            brand_id="brandId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(BrandQualifyByUsecaseResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_qualify_by_usecase(self, client: Telnyx) -> None:
        with client.campaign_builder.brand.with_streaming_response.qualify_by_usecase(
            usecase="usecase",
            brand_id="brandId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(BrandQualifyByUsecaseResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_qualify_by_usecase(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            client.campaign_builder.brand.with_raw_response.qualify_by_usecase(
                usecase="usecase",
                brand_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `usecase` but received ''"):
            client.campaign_builder.brand.with_raw_response.qualify_by_usecase(
                usecase="",
                brand_id="brandId",
            )


class TestAsyncBrand:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_qualify_by_usecase(self, async_client: AsyncTelnyx) -> None:
        brand = await async_client.campaign_builder.brand.qualify_by_usecase(
            usecase="usecase",
            brand_id="brandId",
        )
        assert_matches_type(BrandQualifyByUsecaseResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_qualify_by_usecase(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.campaign_builder.brand.with_raw_response.qualify_by_usecase(
            usecase="usecase",
            brand_id="brandId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(BrandQualifyByUsecaseResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_qualify_by_usecase(self, async_client: AsyncTelnyx) -> None:
        async with async_client.campaign_builder.brand.with_streaming_response.qualify_by_usecase(
            usecase="usecase",
            brand_id="brandId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(BrandQualifyByUsecaseResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_qualify_by_usecase(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            await async_client.campaign_builder.brand.with_raw_response.qualify_by_usecase(
                usecase="usecase",
                brand_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `usecase` but received ''"):
            await async_client.campaign_builder.brand.with_raw_response.qualify_by_usecase(
                usecase="",
                brand_id="brandId",
            )

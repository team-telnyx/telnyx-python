# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.brand import (
    ExternalVettingImportResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExternalVetting:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        external_vetting = client.brand.external_vetting.list(
            "brandId",
        )
        assert_matches_type(object, external_vetting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.brand.external_vetting.with_raw_response.list(
            "brandId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_vetting = response.parse()
        assert_matches_type(object, external_vetting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.brand.external_vetting.with_streaming_response.list(
            "brandId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_vetting = response.parse()
            assert_matches_type(object, external_vetting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            client.brand.external_vetting.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_import(self, client: Telnyx) -> None:
        external_vetting = client.brand.external_vetting.import_(
            brand_id="brandId",
            evp_id="evpId",
            vetting_id="vettingId",
        )
        assert_matches_type(ExternalVettingImportResponse, external_vetting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_import_with_all_params(self, client: Telnyx) -> None:
        external_vetting = client.brand.external_vetting.import_(
            brand_id="brandId",
            evp_id="evpId",
            vetting_id="vettingId",
            vetting_token="vettingToken",
        )
        assert_matches_type(ExternalVettingImportResponse, external_vetting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_import(self, client: Telnyx) -> None:
        response = client.brand.external_vetting.with_raw_response.import_(
            brand_id="brandId",
            evp_id="evpId",
            vetting_id="vettingId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_vetting = response.parse()
        assert_matches_type(ExternalVettingImportResponse, external_vetting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_import(self, client: Telnyx) -> None:
        with client.brand.external_vetting.with_streaming_response.import_(
            brand_id="brandId",
            evp_id="evpId",
            vetting_id="vettingId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_vetting = response.parse()
            assert_matches_type(ExternalVettingImportResponse, external_vetting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_import(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            client.brand.external_vetting.with_raw_response.import_(
                brand_id="",
                evp_id="evpId",
                vetting_id="vettingId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_order(self, client: Telnyx) -> None:
        external_vetting = client.brand.external_vetting.order(
            brand_id="brandId",
            evp_id="evpId",
            vetting_class="vettingClass",
        )
        assert_matches_type(object, external_vetting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_order(self, client: Telnyx) -> None:
        response = client.brand.external_vetting.with_raw_response.order(
            brand_id="brandId",
            evp_id="evpId",
            vetting_class="vettingClass",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_vetting = response.parse()
        assert_matches_type(object, external_vetting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_order(self, client: Telnyx) -> None:
        with client.brand.external_vetting.with_streaming_response.order(
            brand_id="brandId",
            evp_id="evpId",
            vetting_class="vettingClass",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_vetting = response.parse()
            assert_matches_type(object, external_vetting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_order(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            client.brand.external_vetting.with_raw_response.order(
                brand_id="",
                evp_id="evpId",
                vetting_class="vettingClass",
            )


class TestAsyncExternalVetting:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        external_vetting = await async_client.brand.external_vetting.list(
            "brandId",
        )
        assert_matches_type(object, external_vetting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.brand.external_vetting.with_raw_response.list(
            "brandId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_vetting = await response.parse()
        assert_matches_type(object, external_vetting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.brand.external_vetting.with_streaming_response.list(
            "brandId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_vetting = await response.parse()
            assert_matches_type(object, external_vetting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            await async_client.brand.external_vetting.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_import(self, async_client: AsyncTelnyx) -> None:
        external_vetting = await async_client.brand.external_vetting.import_(
            brand_id="brandId",
            evp_id="evpId",
            vetting_id="vettingId",
        )
        assert_matches_type(ExternalVettingImportResponse, external_vetting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_import_with_all_params(self, async_client: AsyncTelnyx) -> None:
        external_vetting = await async_client.brand.external_vetting.import_(
            brand_id="brandId",
            evp_id="evpId",
            vetting_id="vettingId",
            vetting_token="vettingToken",
        )
        assert_matches_type(ExternalVettingImportResponse, external_vetting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_import(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.brand.external_vetting.with_raw_response.import_(
            brand_id="brandId",
            evp_id="evpId",
            vetting_id="vettingId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_vetting = await response.parse()
        assert_matches_type(ExternalVettingImportResponse, external_vetting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_import(self, async_client: AsyncTelnyx) -> None:
        async with async_client.brand.external_vetting.with_streaming_response.import_(
            brand_id="brandId",
            evp_id="evpId",
            vetting_id="vettingId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_vetting = await response.parse()
            assert_matches_type(ExternalVettingImportResponse, external_vetting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_import(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            await async_client.brand.external_vetting.with_raw_response.import_(
                brand_id="",
                evp_id="evpId",
                vetting_id="vettingId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_order(self, async_client: AsyncTelnyx) -> None:
        external_vetting = await async_client.brand.external_vetting.order(
            brand_id="brandId",
            evp_id="evpId",
            vetting_class="vettingClass",
        )
        assert_matches_type(object, external_vetting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_order(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.brand.external_vetting.with_raw_response.order(
            brand_id="brandId",
            evp_id="evpId",
            vetting_class="vettingClass",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_vetting = await response.parse()
        assert_matches_type(object, external_vetting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_order(self, async_client: AsyncTelnyx) -> None:
        async with async_client.brand.external_vetting.with_streaming_response.order(
            brand_id="brandId",
            evp_id="evpId",
            vetting_class="vettingClass",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_vetting = await response.parse()
            assert_matches_type(object, external_vetting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_order(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            await async_client.brand.external_vetting.with_raw_response.order(
                brand_id="",
                evp_id="evpId",
                vetting_class="vettingClass",
            )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.number_10dlc.brand import (
    ExternalVettingExternalVettingResponse,
    ExternalVettingUpdateExternalVettingResponse,
    ExternalVettingRetrieveExternalVettingResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExternalVetting:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_external_vetting(self, client: Telnyx) -> None:
        external_vetting = client.number_10dlc.brand.external_vetting.external_vetting(
            brand_id="brandId",
            evp_id="evpId",
            vetting_class="vettingClass",
        )
        assert_matches_type(ExternalVettingExternalVettingResponse, external_vetting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_external_vetting(self, client: Telnyx) -> None:
        response = client.number_10dlc.brand.external_vetting.with_raw_response.external_vetting(
            brand_id="brandId",
            evp_id="evpId",
            vetting_class="vettingClass",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_vetting = response.parse()
        assert_matches_type(ExternalVettingExternalVettingResponse, external_vetting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_external_vetting(self, client: Telnyx) -> None:
        with client.number_10dlc.brand.external_vetting.with_streaming_response.external_vetting(
            brand_id="brandId",
            evp_id="evpId",
            vetting_class="vettingClass",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_vetting = response.parse()
            assert_matches_type(ExternalVettingExternalVettingResponse, external_vetting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_external_vetting(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            client.number_10dlc.brand.external_vetting.with_raw_response.external_vetting(
                brand_id="",
                evp_id="evpId",
                vetting_class="vettingClass",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_external_vetting(self, client: Telnyx) -> None:
        external_vetting = client.number_10dlc.brand.external_vetting.retrieve_external_vetting(
            "brandId",
        )
        assert_matches_type(ExternalVettingRetrieveExternalVettingResponse, external_vetting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_external_vetting(self, client: Telnyx) -> None:
        response = client.number_10dlc.brand.external_vetting.with_raw_response.retrieve_external_vetting(
            "brandId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_vetting = response.parse()
        assert_matches_type(ExternalVettingRetrieveExternalVettingResponse, external_vetting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_external_vetting(self, client: Telnyx) -> None:
        with client.number_10dlc.brand.external_vetting.with_streaming_response.retrieve_external_vetting(
            "brandId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_vetting = response.parse()
            assert_matches_type(ExternalVettingRetrieveExternalVettingResponse, external_vetting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_external_vetting(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            client.number_10dlc.brand.external_vetting.with_raw_response.retrieve_external_vetting(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_external_vetting(self, client: Telnyx) -> None:
        external_vetting = client.number_10dlc.brand.external_vetting.update_external_vetting(
            brand_id="brandId",
            evp_id="evpId",
            vetting_id="vettingId",
        )
        assert_matches_type(ExternalVettingUpdateExternalVettingResponse, external_vetting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_external_vetting_with_all_params(self, client: Telnyx) -> None:
        external_vetting = client.number_10dlc.brand.external_vetting.update_external_vetting(
            brand_id="brandId",
            evp_id="evpId",
            vetting_id="vettingId",
            vetting_token="vettingToken",
        )
        assert_matches_type(ExternalVettingUpdateExternalVettingResponse, external_vetting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_external_vetting(self, client: Telnyx) -> None:
        response = client.number_10dlc.brand.external_vetting.with_raw_response.update_external_vetting(
            brand_id="brandId",
            evp_id="evpId",
            vetting_id="vettingId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_vetting = response.parse()
        assert_matches_type(ExternalVettingUpdateExternalVettingResponse, external_vetting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_external_vetting(self, client: Telnyx) -> None:
        with client.number_10dlc.brand.external_vetting.with_streaming_response.update_external_vetting(
            brand_id="brandId",
            evp_id="evpId",
            vetting_id="vettingId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_vetting = response.parse()
            assert_matches_type(ExternalVettingUpdateExternalVettingResponse, external_vetting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_external_vetting(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            client.number_10dlc.brand.external_vetting.with_raw_response.update_external_vetting(
                brand_id="",
                evp_id="evpId",
                vetting_id="vettingId",
            )


class TestAsyncExternalVetting:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_external_vetting(self, async_client: AsyncTelnyx) -> None:
        external_vetting = await async_client.number_10dlc.brand.external_vetting.external_vetting(
            brand_id="brandId",
            evp_id="evpId",
            vetting_class="vettingClass",
        )
        assert_matches_type(ExternalVettingExternalVettingResponse, external_vetting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_external_vetting(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.number_10dlc.brand.external_vetting.with_raw_response.external_vetting(
            brand_id="brandId",
            evp_id="evpId",
            vetting_class="vettingClass",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_vetting = await response.parse()
        assert_matches_type(ExternalVettingExternalVettingResponse, external_vetting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_external_vetting(self, async_client: AsyncTelnyx) -> None:
        async with async_client.number_10dlc.brand.external_vetting.with_streaming_response.external_vetting(
            brand_id="brandId",
            evp_id="evpId",
            vetting_class="vettingClass",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_vetting = await response.parse()
            assert_matches_type(ExternalVettingExternalVettingResponse, external_vetting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_external_vetting(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            await async_client.number_10dlc.brand.external_vetting.with_raw_response.external_vetting(
                brand_id="",
                evp_id="evpId",
                vetting_class="vettingClass",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_external_vetting(self, async_client: AsyncTelnyx) -> None:
        external_vetting = await async_client.number_10dlc.brand.external_vetting.retrieve_external_vetting(
            "brandId",
        )
        assert_matches_type(ExternalVettingRetrieveExternalVettingResponse, external_vetting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_external_vetting(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.number_10dlc.brand.external_vetting.with_raw_response.retrieve_external_vetting(
            "brandId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_vetting = await response.parse()
        assert_matches_type(ExternalVettingRetrieveExternalVettingResponse, external_vetting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_external_vetting(self, async_client: AsyncTelnyx) -> None:
        async with async_client.number_10dlc.brand.external_vetting.with_streaming_response.retrieve_external_vetting(
            "brandId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_vetting = await response.parse()
            assert_matches_type(ExternalVettingRetrieveExternalVettingResponse, external_vetting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_external_vetting(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            await async_client.number_10dlc.brand.external_vetting.with_raw_response.retrieve_external_vetting(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_external_vetting(self, async_client: AsyncTelnyx) -> None:
        external_vetting = await async_client.number_10dlc.brand.external_vetting.update_external_vetting(
            brand_id="brandId",
            evp_id="evpId",
            vetting_id="vettingId",
        )
        assert_matches_type(ExternalVettingUpdateExternalVettingResponse, external_vetting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_external_vetting_with_all_params(self, async_client: AsyncTelnyx) -> None:
        external_vetting = await async_client.number_10dlc.brand.external_vetting.update_external_vetting(
            brand_id="brandId",
            evp_id="evpId",
            vetting_id="vettingId",
            vetting_token="vettingToken",
        )
        assert_matches_type(ExternalVettingUpdateExternalVettingResponse, external_vetting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_external_vetting(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.number_10dlc.brand.external_vetting.with_raw_response.update_external_vetting(
            brand_id="brandId",
            evp_id="evpId",
            vetting_id="vettingId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_vetting = await response.parse()
        assert_matches_type(ExternalVettingUpdateExternalVettingResponse, external_vetting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_external_vetting(self, async_client: AsyncTelnyx) -> None:
        async with async_client.number_10dlc.brand.external_vetting.with_streaming_response.update_external_vetting(
            brand_id="brandId",
            evp_id="evpId",
            vetting_id="vettingId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_vetting = await response.parse()
            assert_matches_type(ExternalVettingUpdateExternalVettingResponse, external_vetting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_external_vetting(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            await async_client.number_10dlc.brand.external_vetting.with_raw_response.update_external_vetting(
                brand_id="",
                evp_id="evpId",
                vetting_id="vettingId",
            )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    TelnyxBrand,
    BrandListResponse,
    BrandRetrieveResponse,
    BrandGetFeedbackResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBrand:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        brand = client.brand.create(
            country="US",
            display_name="ABC Mobile",
            email="email",
            entity_type="PRIVATE_PROFIT",
            vertical="TECHNOLOGY",
        )
        assert_matches_type(TelnyxBrand, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        brand = client.brand.create(
            country="US",
            display_name="ABC Mobile",
            email="email",
            entity_type="PRIVATE_PROFIT",
            vertical="TECHNOLOGY",
            business_contact_email="name@example.com",
            city="New York",
            company_name="ABC Inc.",
            ein="111111111",
            first_name="John",
            ip_address="ipAddress",
            is_reseller=True,
            last_name="Smith",
            mobile_phone="+12024567890",
            mock=True,
            phone="+12024567890",
            postal_code="10001",
            state="NY",
            stock_exchange="NASDAQ",
            stock_symbol="ABC",
            street="123",
            webhook_failover_url="https://webhook.com/9010a453-4df8-4be6-a551-1070892888d6",
            webhook_url="https://webhook.com/67ea78a8-9f32-4d04-b62d-f9502e8e5f93",
            website="http://www.abcmobile.com",
        )
        assert_matches_type(TelnyxBrand, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.brand.with_raw_response.create(
            country="US",
            display_name="ABC Mobile",
            email="email",
            entity_type="PRIVATE_PROFIT",
            vertical="TECHNOLOGY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(TelnyxBrand, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.brand.with_streaming_response.create(
            country="US",
            display_name="ABC Mobile",
            email="email",
            entity_type="PRIVATE_PROFIT",
            vertical="TECHNOLOGY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(TelnyxBrand, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        brand = client.brand.retrieve(
            "brandId",
        )
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.brand.with_raw_response.retrieve(
            "brandId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.brand.with_streaming_response.retrieve(
            "brandId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            client.brand.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        brand = client.brand.update(
            brand_id="brandId",
            country="US",
            display_name="ABC Mobile",
            email="email",
            entity_type="PRIVATE_PROFIT",
            vertical="TECHNOLOGY",
        )
        assert_matches_type(TelnyxBrand, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        brand = client.brand.update(
            brand_id="brandId",
            country="US",
            display_name="ABC Mobile",
            email="email",
            entity_type="PRIVATE_PROFIT",
            vertical="TECHNOLOGY",
            alt_business_id="altBusiness_id",
            alt_business_id_type="NONE",
            business_contact_email="name@example.com",
            city="New York",
            company_name="ABC Inc.",
            ein="111111111",
            first_name="John",
            identity_status="VERIFIED",
            ip_address="ipAddress",
            is_reseller=True,
            last_name="Smith",
            phone="+12024567890",
            postal_code="10001",
            state="NY",
            stock_exchange="NASDAQ",
            stock_symbol="ABC",
            street="123",
            webhook_failover_url="https://webhook.com/9010a453-4df8-4be6-a551-1070892888d6",
            webhook_url="https://webhook.com/67ea78a8-9f32-4d04-b62d-f9502e8e5f93",
            website="http://www.abcmobile.com",
        )
        assert_matches_type(TelnyxBrand, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.brand.with_raw_response.update(
            brand_id="brandId",
            country="US",
            display_name="ABC Mobile",
            email="email",
            entity_type="PRIVATE_PROFIT",
            vertical="TECHNOLOGY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(TelnyxBrand, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.brand.with_streaming_response.update(
            brand_id="brandId",
            country="US",
            display_name="ABC Mobile",
            email="email",
            entity_type="PRIVATE_PROFIT",
            vertical="TECHNOLOGY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(TelnyxBrand, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            client.brand.with_raw_response.update(
                brand_id="",
                country="US",
                display_name="ABC Mobile",
                email="email",
                entity_type="PRIVATE_PROFIT",
                vertical="TECHNOLOGY",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        brand = client.brand.list()
        assert_matches_type(BrandListResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        brand = client.brand.list(
            brand_id="826ef77a-348c-445b-81a5-a9b13c68fbfe",
            country="country",
            display_name="displayName",
            entity_type="entityType",
            page=1,
            records_per_page=0,
            sort="assignedCampaignsCount",
            state="state",
            tcr_brand_id="BBAND1",
        )
        assert_matches_type(BrandListResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.brand.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(BrandListResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.brand.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(BrandListResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        brand = client.brand.delete(
            "brandId",
        )
        assert_matches_type(object, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.brand.with_raw_response.delete(
            "brandId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(object, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.brand.with_streaming_response.delete(
            "brandId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(object, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            client.brand.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_feedback(self, client: Telnyx) -> None:
        brand = client.brand.get_feedback(
            "brandId",
        )
        assert_matches_type(BrandGetFeedbackResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_feedback(self, client: Telnyx) -> None:
        response = client.brand.with_raw_response.get_feedback(
            "brandId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(BrandGetFeedbackResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_feedback(self, client: Telnyx) -> None:
        with client.brand.with_streaming_response.get_feedback(
            "brandId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(BrandGetFeedbackResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_feedback(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            client.brand.with_raw_response.get_feedback(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_resend_2fa_email(self, client: Telnyx) -> None:
        brand = client.brand.resend_2fa_email(
            "brandId",
        )
        assert brand is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_resend_2fa_email(self, client: Telnyx) -> None:
        response = client.brand.with_raw_response.resend_2fa_email(
            "brandId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert brand is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_resend_2fa_email(self, client: Telnyx) -> None:
        with client.brand.with_streaming_response.resend_2fa_email(
            "brandId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert brand is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_resend_2fa_email(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            client.brand.with_raw_response.resend_2fa_email(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_revet(self, client: Telnyx) -> None:
        brand = client.brand.revet(
            "brandId",
        )
        assert_matches_type(object, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_revet(self, client: Telnyx) -> None:
        response = client.brand.with_raw_response.revet(
            "brandId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(object, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_revet(self, client: Telnyx) -> None:
        with client.brand.with_streaming_response.revet(
            "brandId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(object, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_revet(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            client.brand.with_raw_response.revet(
                "",
            )


class TestAsyncBrand:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        brand = await async_client.brand.create(
            country="US",
            display_name="ABC Mobile",
            email="email",
            entity_type="PRIVATE_PROFIT",
            vertical="TECHNOLOGY",
        )
        assert_matches_type(TelnyxBrand, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        brand = await async_client.brand.create(
            country="US",
            display_name="ABC Mobile",
            email="email",
            entity_type="PRIVATE_PROFIT",
            vertical="TECHNOLOGY",
            business_contact_email="name@example.com",
            city="New York",
            company_name="ABC Inc.",
            ein="111111111",
            first_name="John",
            ip_address="ipAddress",
            is_reseller=True,
            last_name="Smith",
            mobile_phone="+12024567890",
            mock=True,
            phone="+12024567890",
            postal_code="10001",
            state="NY",
            stock_exchange="NASDAQ",
            stock_symbol="ABC",
            street="123",
            webhook_failover_url="https://webhook.com/9010a453-4df8-4be6-a551-1070892888d6",
            webhook_url="https://webhook.com/67ea78a8-9f32-4d04-b62d-f9502e8e5f93",
            website="http://www.abcmobile.com",
        )
        assert_matches_type(TelnyxBrand, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.brand.with_raw_response.create(
            country="US",
            display_name="ABC Mobile",
            email="email",
            entity_type="PRIVATE_PROFIT",
            vertical="TECHNOLOGY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(TelnyxBrand, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.brand.with_streaming_response.create(
            country="US",
            display_name="ABC Mobile",
            email="email",
            entity_type="PRIVATE_PROFIT",
            vertical="TECHNOLOGY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(TelnyxBrand, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        brand = await async_client.brand.retrieve(
            "brandId",
        )
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.brand.with_raw_response.retrieve(
            "brandId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.brand.with_streaming_response.retrieve(
            "brandId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            await async_client.brand.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        brand = await async_client.brand.update(
            brand_id="brandId",
            country="US",
            display_name="ABC Mobile",
            email="email",
            entity_type="PRIVATE_PROFIT",
            vertical="TECHNOLOGY",
        )
        assert_matches_type(TelnyxBrand, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        brand = await async_client.brand.update(
            brand_id="brandId",
            country="US",
            display_name="ABC Mobile",
            email="email",
            entity_type="PRIVATE_PROFIT",
            vertical="TECHNOLOGY",
            alt_business_id="altBusiness_id",
            alt_business_id_type="NONE",
            business_contact_email="name@example.com",
            city="New York",
            company_name="ABC Inc.",
            ein="111111111",
            first_name="John",
            identity_status="VERIFIED",
            ip_address="ipAddress",
            is_reseller=True,
            last_name="Smith",
            phone="+12024567890",
            postal_code="10001",
            state="NY",
            stock_exchange="NASDAQ",
            stock_symbol="ABC",
            street="123",
            webhook_failover_url="https://webhook.com/9010a453-4df8-4be6-a551-1070892888d6",
            webhook_url="https://webhook.com/67ea78a8-9f32-4d04-b62d-f9502e8e5f93",
            website="http://www.abcmobile.com",
        )
        assert_matches_type(TelnyxBrand, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.brand.with_raw_response.update(
            brand_id="brandId",
            country="US",
            display_name="ABC Mobile",
            email="email",
            entity_type="PRIVATE_PROFIT",
            vertical="TECHNOLOGY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(TelnyxBrand, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.brand.with_streaming_response.update(
            brand_id="brandId",
            country="US",
            display_name="ABC Mobile",
            email="email",
            entity_type="PRIVATE_PROFIT",
            vertical="TECHNOLOGY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(TelnyxBrand, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            await async_client.brand.with_raw_response.update(
                brand_id="",
                country="US",
                display_name="ABC Mobile",
                email="email",
                entity_type="PRIVATE_PROFIT",
                vertical="TECHNOLOGY",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        brand = await async_client.brand.list()
        assert_matches_type(BrandListResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        brand = await async_client.brand.list(
            brand_id="826ef77a-348c-445b-81a5-a9b13c68fbfe",
            country="country",
            display_name="displayName",
            entity_type="entityType",
            page=1,
            records_per_page=0,
            sort="assignedCampaignsCount",
            state="state",
            tcr_brand_id="BBAND1",
        )
        assert_matches_type(BrandListResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.brand.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(BrandListResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.brand.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(BrandListResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        brand = await async_client.brand.delete(
            "brandId",
        )
        assert_matches_type(object, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.brand.with_raw_response.delete(
            "brandId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(object, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.brand.with_streaming_response.delete(
            "brandId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(object, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            await async_client.brand.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_feedback(self, async_client: AsyncTelnyx) -> None:
        brand = await async_client.brand.get_feedback(
            "brandId",
        )
        assert_matches_type(BrandGetFeedbackResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_feedback(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.brand.with_raw_response.get_feedback(
            "brandId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(BrandGetFeedbackResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_feedback(self, async_client: AsyncTelnyx) -> None:
        async with async_client.brand.with_streaming_response.get_feedback(
            "brandId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(BrandGetFeedbackResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_feedback(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            await async_client.brand.with_raw_response.get_feedback(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_resend_2fa_email(self, async_client: AsyncTelnyx) -> None:
        brand = await async_client.brand.resend_2fa_email(
            "brandId",
        )
        assert brand is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_resend_2fa_email(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.brand.with_raw_response.resend_2fa_email(
            "brandId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert brand is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_resend_2fa_email(self, async_client: AsyncTelnyx) -> None:
        async with async_client.brand.with_streaming_response.resend_2fa_email(
            "brandId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert brand is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_resend_2fa_email(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            await async_client.brand.with_raw_response.resend_2fa_email(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_revet(self, async_client: AsyncTelnyx) -> None:
        brand = await async_client.brand.revet(
            "brandId",
        )
        assert_matches_type(object, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_revet(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.brand.with_raw_response.revet(
            "brandId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(object, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_revet(self, async_client: AsyncTelnyx) -> None:
        async with async_client.brand.with_streaming_response.revet(
            "brandId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(object, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_revet(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            await async_client.brand.with_raw_response.revet(
                "",
            )

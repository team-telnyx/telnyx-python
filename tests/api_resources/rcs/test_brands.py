# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.rcs import (
    BrandResponse,
    BrandListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBrands:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        brand = client.rcs.brands.create(
            addresses={
                "primary": {
                    "administrative_area": "IL",
                    "city": "Chicago",
                    "country_code": "US",
                    "line_1": "1 Main Street",
                    "postal_code": "60601",
                }
            },
            contacts={
                "brand": {
                    "contact_type": "BRAND",
                    "email": "jane@example.com",
                    "first_name": "Jane",
                    "last_name": "Doe",
                    "phone_number": "+13125550100",
                }
            },
            display_name="Acme",
            identifiers={
                "ein": {
                    "identifier_type": "EIN",
                    "value": "12-3456789",
                }
            },
            legal_entity_type="LIMITED_LIABILITY_COMPANY",
            legal_name="Acme LLC",
            organization_type="PRIVATE_PROFIT",
            website_url="https://www.example.com",
        )
        assert_matches_type(BrandResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        brand = client.rcs.brands.create(
            addresses={
                "primary": {
                    "administrative_area": "IL",
                    "city": "Chicago",
                    "country_code": "US",
                    "line_1": "1 Main Street",
                    "postal_code": "60601",
                    "line_2": "x",
                }
            },
            contacts={
                "brand": {
                    "contact_type": "BRAND",
                    "email": "jane@example.com",
                    "first_name": "Jane",
                    "last_name": "Doe",
                    "phone_number": "+13125550100",
                    "title": "Messaging Operations Manager",
                }
            },
            display_name="Acme",
            identifiers={
                "ein": {
                    "identifier_type": "EIN",
                    "value": "12-3456789",
                },
                "stock_symbol": {
                    "identifier_type": "STOCK_SYMBOL",
                    "value": "J!Q0Ok0bzJb7:pro",
                },
            },
            legal_entity_type="LIMITED_LIABILITY_COMPANY",
            legal_name="Acme LLC",
            organization_type="PRIVATE_PROFIT",
            website_url="https://www.example.com",
            profile_id="40000000-0000-0000-0000-000000000001",
        )
        assert_matches_type(BrandResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.rcs.brands.with_raw_response.create(
            addresses={
                "primary": {
                    "administrative_area": "IL",
                    "city": "Chicago",
                    "country_code": "US",
                    "line_1": "1 Main Street",
                    "postal_code": "60601",
                }
            },
            contacts={
                "brand": {
                    "contact_type": "BRAND",
                    "email": "jane@example.com",
                    "first_name": "Jane",
                    "last_name": "Doe",
                    "phone_number": "+13125550100",
                }
            },
            display_name="Acme",
            identifiers={
                "ein": {
                    "identifier_type": "EIN",
                    "value": "12-3456789",
                }
            },
            legal_entity_type="LIMITED_LIABILITY_COMPANY",
            legal_name="Acme LLC",
            organization_type="PRIVATE_PROFIT",
            website_url="https://www.example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(BrandResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.rcs.brands.with_streaming_response.create(
            addresses={
                "primary": {
                    "administrative_area": "IL",
                    "city": "Chicago",
                    "country_code": "US",
                    "line_1": "1 Main Street",
                    "postal_code": "60601",
                }
            },
            contacts={
                "brand": {
                    "contact_type": "BRAND",
                    "email": "jane@example.com",
                    "first_name": "Jane",
                    "last_name": "Doe",
                    "phone_number": "+13125550100",
                }
            },
            display_name="Acme",
            identifiers={
                "ein": {
                    "identifier_type": "EIN",
                    "value": "12-3456789",
                }
            },
            legal_entity_type="LIMITED_LIABILITY_COMPANY",
            legal_name="Acme LLC",
            organization_type="PRIVATE_PROFIT",
            website_url="https://www.example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(BrandResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        brand = client.rcs.brands.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BrandResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.rcs.brands.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(BrandResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.rcs.brands.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(BrandResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.rcs.brands.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        brand = client.rcs.brands.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BrandResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        brand = client.rcs.brands.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            addresses={
                "foo": {
                    "administrative_area": "x",
                    "city": "x",
                    "country_code": "SE",
                    "line_1": "x",
                    "postal_code": "x",
                    "line_2": "x",
                }
            },
            contacts={
                "brand": {
                    "contact_type": "BRAND",
                    "email": "dev@stainless.com",
                    "first_name": "x",
                    "last_name": "x",
                    "phone_number": "+49605132",
                    "title": "x",
                }
            },
            display_name="Acme Communications",
            identifiers={
                "ein": {
                    "identifier_type": "EIN",
                    "value": "29-1051329",
                },
                "stock_symbol": {
                    "identifier_type": "STOCK_SYMBOL",
                    "value": "J!Q0Ok0bzJb7:pro",
                },
            },
            legal_entity_type="LIMITED_LIABILITY_COMPANY",
            legal_name="x",
            organization_type="PRIVATE_PROFIT",
            profile_id="profile_id",
            website_url="https://example.com",
        )
        assert_matches_type(BrandResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.rcs.brands.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(BrandResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.rcs.brands.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(BrandResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.rcs.brands.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        brand = client.rcs.brands.list()
        assert_matches_type(BrandListResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.rcs.brands.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(BrandListResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.rcs.brands.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(BrandListResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit(self, client: Telnyx) -> None:
        brand = client.rcs.brands.submit(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BrandResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_submit(self, client: Telnyx) -> None:
        response = client.rcs.brands.with_raw_response.submit(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(BrandResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_submit(self, client: Telnyx) -> None:
        with client.rcs.brands.with_streaming_response.submit(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(BrandResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_submit(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.rcs.brands.with_raw_response.submit(
                "",
            )


class TestAsyncBrands:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        brand = await async_client.rcs.brands.create(
            addresses={
                "primary": {
                    "administrative_area": "IL",
                    "city": "Chicago",
                    "country_code": "US",
                    "line_1": "1 Main Street",
                    "postal_code": "60601",
                }
            },
            contacts={
                "brand": {
                    "contact_type": "BRAND",
                    "email": "jane@example.com",
                    "first_name": "Jane",
                    "last_name": "Doe",
                    "phone_number": "+13125550100",
                }
            },
            display_name="Acme",
            identifiers={
                "ein": {
                    "identifier_type": "EIN",
                    "value": "12-3456789",
                }
            },
            legal_entity_type="LIMITED_LIABILITY_COMPANY",
            legal_name="Acme LLC",
            organization_type="PRIVATE_PROFIT",
            website_url="https://www.example.com",
        )
        assert_matches_type(BrandResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        brand = await async_client.rcs.brands.create(
            addresses={
                "primary": {
                    "administrative_area": "IL",
                    "city": "Chicago",
                    "country_code": "US",
                    "line_1": "1 Main Street",
                    "postal_code": "60601",
                    "line_2": "x",
                }
            },
            contacts={
                "brand": {
                    "contact_type": "BRAND",
                    "email": "jane@example.com",
                    "first_name": "Jane",
                    "last_name": "Doe",
                    "phone_number": "+13125550100",
                    "title": "Messaging Operations Manager",
                }
            },
            display_name="Acme",
            identifiers={
                "ein": {
                    "identifier_type": "EIN",
                    "value": "12-3456789",
                },
                "stock_symbol": {
                    "identifier_type": "STOCK_SYMBOL",
                    "value": "J!Q0Ok0bzJb7:pro",
                },
            },
            legal_entity_type="LIMITED_LIABILITY_COMPANY",
            legal_name="Acme LLC",
            organization_type="PRIVATE_PROFIT",
            website_url="https://www.example.com",
            profile_id="40000000-0000-0000-0000-000000000001",
        )
        assert_matches_type(BrandResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.rcs.brands.with_raw_response.create(
            addresses={
                "primary": {
                    "administrative_area": "IL",
                    "city": "Chicago",
                    "country_code": "US",
                    "line_1": "1 Main Street",
                    "postal_code": "60601",
                }
            },
            contacts={
                "brand": {
                    "contact_type": "BRAND",
                    "email": "jane@example.com",
                    "first_name": "Jane",
                    "last_name": "Doe",
                    "phone_number": "+13125550100",
                }
            },
            display_name="Acme",
            identifiers={
                "ein": {
                    "identifier_type": "EIN",
                    "value": "12-3456789",
                }
            },
            legal_entity_type="LIMITED_LIABILITY_COMPANY",
            legal_name="Acme LLC",
            organization_type="PRIVATE_PROFIT",
            website_url="https://www.example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(BrandResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.rcs.brands.with_streaming_response.create(
            addresses={
                "primary": {
                    "administrative_area": "IL",
                    "city": "Chicago",
                    "country_code": "US",
                    "line_1": "1 Main Street",
                    "postal_code": "60601",
                }
            },
            contacts={
                "brand": {
                    "contact_type": "BRAND",
                    "email": "jane@example.com",
                    "first_name": "Jane",
                    "last_name": "Doe",
                    "phone_number": "+13125550100",
                }
            },
            display_name="Acme",
            identifiers={
                "ein": {
                    "identifier_type": "EIN",
                    "value": "12-3456789",
                }
            },
            legal_entity_type="LIMITED_LIABILITY_COMPANY",
            legal_name="Acme LLC",
            organization_type="PRIVATE_PROFIT",
            website_url="https://www.example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(BrandResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        brand = await async_client.rcs.brands.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BrandResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.rcs.brands.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(BrandResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.rcs.brands.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(BrandResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.rcs.brands.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        brand = await async_client.rcs.brands.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BrandResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        brand = await async_client.rcs.brands.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            addresses={
                "foo": {
                    "administrative_area": "x",
                    "city": "x",
                    "country_code": "SE",
                    "line_1": "x",
                    "postal_code": "x",
                    "line_2": "x",
                }
            },
            contacts={
                "brand": {
                    "contact_type": "BRAND",
                    "email": "dev@stainless.com",
                    "first_name": "x",
                    "last_name": "x",
                    "phone_number": "+49605132",
                    "title": "x",
                }
            },
            display_name="Acme Communications",
            identifiers={
                "ein": {
                    "identifier_type": "EIN",
                    "value": "29-1051329",
                },
                "stock_symbol": {
                    "identifier_type": "STOCK_SYMBOL",
                    "value": "J!Q0Ok0bzJb7:pro",
                },
            },
            legal_entity_type="LIMITED_LIABILITY_COMPANY",
            legal_name="x",
            organization_type="PRIVATE_PROFIT",
            profile_id="profile_id",
            website_url="https://example.com",
        )
        assert_matches_type(BrandResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.rcs.brands.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(BrandResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.rcs.brands.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(BrandResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.rcs.brands.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        brand = await async_client.rcs.brands.list()
        assert_matches_type(BrandListResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.rcs.brands.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(BrandListResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.rcs.brands.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(BrandListResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit(self, async_client: AsyncTelnyx) -> None:
        brand = await async_client.rcs.brands.submit(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BrandResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_submit(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.rcs.brands.with_raw_response.submit(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(BrandResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_submit(self, async_client: AsyncTelnyx) -> None:
        async with async_client.rcs.brands.with_streaming_response.submit(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(BrandResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_submit(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.rcs.brands.with_raw_response.submit(
                "",
            )

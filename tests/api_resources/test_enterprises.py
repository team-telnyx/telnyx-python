# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    EnterprisePublic,
    EnterpriseCreateResponse,
    EnterpriseUpdateResponse,
    EnterpriseRetrieveResponse,
)
from telnyx.pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEnterprises:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        enterprise = client.enterprises.create(
            billing_address={
                "administrative_area": "Illinois",
                "city": "Chicago",
                "country": "United States",
                "postal_code": "60601",
                "street_address": "123 Main St",
            },
            billing_contact={
                "email": "billing@acme.com",
                "first_name": "John",
                "last_name": "Doe",
                "phone_number": "15551234568",
            },
            country_code="US",
            doing_business_as="Acme",
            fein="12-3456789",
            industry="technology",
            legal_name="Acme Corp Inc.",
            number_of_employees="51-200",
            organization_contact={
                "email": "jane.smith@acme.com",
                "first_name": "Jane",
                "job_title": "VP of Engineering",
                "last_name": "Smith",
                "phone": "+16035551234",
            },
            organization_legal_type="corporation",
            organization_physical_address={
                "administrative_area": "Illinois",
                "city": "Chicago",
                "country": "United States",
                "postal_code": "60601",
                "street_address": "123 Main St",
            },
            organization_type="commercial",
            website="https://acme.com",
        )
        assert_matches_type(EnterpriseCreateResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        enterprise = client.enterprises.create(
            billing_address={
                "administrative_area": "Illinois",
                "city": "Chicago",
                "country": "United States",
                "postal_code": "60601",
                "street_address": "123 Main St",
                "extended_address": "Suite 400",
            },
            billing_contact={
                "email": "billing@acme.com",
                "first_name": "John",
                "last_name": "Doe",
                "phone_number": "15551234568",
            },
            country_code="US",
            doing_business_as="Acme",
            fein="12-3456789",
            industry="technology",
            legal_name="Acme Corp Inc.",
            number_of_employees="51-200",
            organization_contact={
                "email": "jane.smith@acme.com",
                "first_name": "Jane",
                "job_title": "VP of Engineering",
                "last_name": "Smith",
                "phone": "+16035551234",
            },
            organization_legal_type="corporation",
            organization_physical_address={
                "administrative_area": "Illinois",
                "city": "Chicago",
                "country": "United States",
                "postal_code": "60601",
                "street_address": "123 Main St",
                "extended_address": "Suite 400",
            },
            organization_type="commercial",
            website="https://acme.com",
            corporate_registration_number="corporate_registration_number",
            customer_reference="customer_reference",
            dun_bradstreet_number="dun_bradstreet_number",
            primary_business_domain_sic_code="7372",
            professional_license_number="professional_license_number",
            role_type="enterprise",
        )
        assert_matches_type(EnterpriseCreateResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.enterprises.with_raw_response.create(
            billing_address={
                "administrative_area": "Illinois",
                "city": "Chicago",
                "country": "United States",
                "postal_code": "60601",
                "street_address": "123 Main St",
            },
            billing_contact={
                "email": "billing@acme.com",
                "first_name": "John",
                "last_name": "Doe",
                "phone_number": "15551234568",
            },
            country_code="US",
            doing_business_as="Acme",
            fein="12-3456789",
            industry="technology",
            legal_name="Acme Corp Inc.",
            number_of_employees="51-200",
            organization_contact={
                "email": "jane.smith@acme.com",
                "first_name": "Jane",
                "job_title": "VP of Engineering",
                "last_name": "Smith",
                "phone": "+16035551234",
            },
            organization_legal_type="corporation",
            organization_physical_address={
                "administrative_area": "Illinois",
                "city": "Chicago",
                "country": "United States",
                "postal_code": "60601",
                "street_address": "123 Main St",
            },
            organization_type="commercial",
            website="https://acme.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enterprise = response.parse()
        assert_matches_type(EnterpriseCreateResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.enterprises.with_streaming_response.create(
            billing_address={
                "administrative_area": "Illinois",
                "city": "Chicago",
                "country": "United States",
                "postal_code": "60601",
                "street_address": "123 Main St",
            },
            billing_contact={
                "email": "billing@acme.com",
                "first_name": "John",
                "last_name": "Doe",
                "phone_number": "15551234568",
            },
            country_code="US",
            doing_business_as="Acme",
            fein="12-3456789",
            industry="technology",
            legal_name="Acme Corp Inc.",
            number_of_employees="51-200",
            organization_contact={
                "email": "jane.smith@acme.com",
                "first_name": "Jane",
                "job_title": "VP of Engineering",
                "last_name": "Smith",
                "phone": "+16035551234",
            },
            organization_legal_type="corporation",
            organization_physical_address={
                "administrative_area": "Illinois",
                "city": "Chicago",
                "country": "United States",
                "postal_code": "60601",
                "street_address": "123 Main St",
            },
            organization_type="commercial",
            website="https://acme.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enterprise = response.parse()
            assert_matches_type(EnterpriseCreateResponse, enterprise, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        enterprise = client.enterprises.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(EnterpriseRetrieveResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.enterprises.with_raw_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enterprise = response.parse()
        assert_matches_type(EnterpriseRetrieveResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.enterprises.with_streaming_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enterprise = response.parse()
            assert_matches_type(EnterpriseRetrieveResponse, enterprise, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            client.enterprises.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        enterprise = client.enterprises.update(
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(EnterpriseUpdateResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        enterprise = client.enterprises.update(
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            billing_address={
                "administrative_area": "Illinois",
                "city": "Chicago",
                "country": "United States",
                "postal_code": "60601",
                "street_address": "123 Main St",
                "extended_address": "Suite 400",
            },
            billing_contact={
                "email": "billing@acme.com",
                "first_name": "John",
                "last_name": "Doe",
                "phone_number": "15551234568",
            },
            corporate_registration_number="corporate_registration_number",
            customer_reference="customer_reference",
            doing_business_as="doing_business_as",
            dun_bradstreet_number="dun_bradstreet_number",
            fein="fein",
            industry="industry",
            legal_name="xxx",
            number_of_employees="1-10",
            organization_contact={
                "email": "jane.smith@acme.com",
                "first_name": "Jane",
                "job_title": "VP of Engineering",
                "last_name": "Smith",
                "phone": "+16035551234",
            },
            organization_legal_type="corporation",
            organization_physical_address={
                "administrative_area": "Illinois",
                "city": "Chicago",
                "country": "United States",
                "postal_code": "60601",
                "street_address": "123 Main St",
                "extended_address": "Suite 400",
            },
            primary_business_domain_sic_code="primary_business_domain_sic_code",
            professional_license_number="professional_license_number",
            website="website",
        )
        assert_matches_type(EnterpriseUpdateResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.enterprises.with_raw_response.update(
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enterprise = response.parse()
        assert_matches_type(EnterpriseUpdateResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.enterprises.with_streaming_response.update(
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enterprise = response.parse()
            assert_matches_type(EnterpriseUpdateResponse, enterprise, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            client.enterprises.with_raw_response.update(
                enterprise_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        enterprise = client.enterprises.list()
        assert_matches_type(SyncDefaultFlatPagination[EnterprisePublic], enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        enterprise = client.enterprises.list(
            legal_name="Acme",
            page_number=1,
            page_size=1,
        )
        assert_matches_type(SyncDefaultFlatPagination[EnterprisePublic], enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.enterprises.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enterprise = response.parse()
        assert_matches_type(SyncDefaultFlatPagination[EnterprisePublic], enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.enterprises.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enterprise = response.parse()
            assert_matches_type(SyncDefaultFlatPagination[EnterprisePublic], enterprise, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        enterprise = client.enterprises.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert enterprise is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.enterprises.with_raw_response.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enterprise = response.parse()
        assert enterprise is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.enterprises.with_streaming_response.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enterprise = response.parse()
            assert enterprise is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            client.enterprises.with_raw_response.delete(
                "",
            )


class TestAsyncEnterprises:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        enterprise = await async_client.enterprises.create(
            billing_address={
                "administrative_area": "Illinois",
                "city": "Chicago",
                "country": "United States",
                "postal_code": "60601",
                "street_address": "123 Main St",
            },
            billing_contact={
                "email": "billing@acme.com",
                "first_name": "John",
                "last_name": "Doe",
                "phone_number": "15551234568",
            },
            country_code="US",
            doing_business_as="Acme",
            fein="12-3456789",
            industry="technology",
            legal_name="Acme Corp Inc.",
            number_of_employees="51-200",
            organization_contact={
                "email": "jane.smith@acme.com",
                "first_name": "Jane",
                "job_title": "VP of Engineering",
                "last_name": "Smith",
                "phone": "+16035551234",
            },
            organization_legal_type="corporation",
            organization_physical_address={
                "administrative_area": "Illinois",
                "city": "Chicago",
                "country": "United States",
                "postal_code": "60601",
                "street_address": "123 Main St",
            },
            organization_type="commercial",
            website="https://acme.com",
        )
        assert_matches_type(EnterpriseCreateResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        enterprise = await async_client.enterprises.create(
            billing_address={
                "administrative_area": "Illinois",
                "city": "Chicago",
                "country": "United States",
                "postal_code": "60601",
                "street_address": "123 Main St",
                "extended_address": "Suite 400",
            },
            billing_contact={
                "email": "billing@acme.com",
                "first_name": "John",
                "last_name": "Doe",
                "phone_number": "15551234568",
            },
            country_code="US",
            doing_business_as="Acme",
            fein="12-3456789",
            industry="technology",
            legal_name="Acme Corp Inc.",
            number_of_employees="51-200",
            organization_contact={
                "email": "jane.smith@acme.com",
                "first_name": "Jane",
                "job_title": "VP of Engineering",
                "last_name": "Smith",
                "phone": "+16035551234",
            },
            organization_legal_type="corporation",
            organization_physical_address={
                "administrative_area": "Illinois",
                "city": "Chicago",
                "country": "United States",
                "postal_code": "60601",
                "street_address": "123 Main St",
                "extended_address": "Suite 400",
            },
            organization_type="commercial",
            website="https://acme.com",
            corporate_registration_number="corporate_registration_number",
            customer_reference="customer_reference",
            dun_bradstreet_number="dun_bradstreet_number",
            primary_business_domain_sic_code="7372",
            professional_license_number="professional_license_number",
            role_type="enterprise",
        )
        assert_matches_type(EnterpriseCreateResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.enterprises.with_raw_response.create(
            billing_address={
                "administrative_area": "Illinois",
                "city": "Chicago",
                "country": "United States",
                "postal_code": "60601",
                "street_address": "123 Main St",
            },
            billing_contact={
                "email": "billing@acme.com",
                "first_name": "John",
                "last_name": "Doe",
                "phone_number": "15551234568",
            },
            country_code="US",
            doing_business_as="Acme",
            fein="12-3456789",
            industry="technology",
            legal_name="Acme Corp Inc.",
            number_of_employees="51-200",
            organization_contact={
                "email": "jane.smith@acme.com",
                "first_name": "Jane",
                "job_title": "VP of Engineering",
                "last_name": "Smith",
                "phone": "+16035551234",
            },
            organization_legal_type="corporation",
            organization_physical_address={
                "administrative_area": "Illinois",
                "city": "Chicago",
                "country": "United States",
                "postal_code": "60601",
                "street_address": "123 Main St",
            },
            organization_type="commercial",
            website="https://acme.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enterprise = await response.parse()
        assert_matches_type(EnterpriseCreateResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.enterprises.with_streaming_response.create(
            billing_address={
                "administrative_area": "Illinois",
                "city": "Chicago",
                "country": "United States",
                "postal_code": "60601",
                "street_address": "123 Main St",
            },
            billing_contact={
                "email": "billing@acme.com",
                "first_name": "John",
                "last_name": "Doe",
                "phone_number": "15551234568",
            },
            country_code="US",
            doing_business_as="Acme",
            fein="12-3456789",
            industry="technology",
            legal_name="Acme Corp Inc.",
            number_of_employees="51-200",
            organization_contact={
                "email": "jane.smith@acme.com",
                "first_name": "Jane",
                "job_title": "VP of Engineering",
                "last_name": "Smith",
                "phone": "+16035551234",
            },
            organization_legal_type="corporation",
            organization_physical_address={
                "administrative_area": "Illinois",
                "city": "Chicago",
                "country": "United States",
                "postal_code": "60601",
                "street_address": "123 Main St",
            },
            organization_type="commercial",
            website="https://acme.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enterprise = await response.parse()
            assert_matches_type(EnterpriseCreateResponse, enterprise, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        enterprise = await async_client.enterprises.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(EnterpriseRetrieveResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.enterprises.with_raw_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enterprise = await response.parse()
        assert_matches_type(EnterpriseRetrieveResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.enterprises.with_streaming_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enterprise = await response.parse()
            assert_matches_type(EnterpriseRetrieveResponse, enterprise, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            await async_client.enterprises.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        enterprise = await async_client.enterprises.update(
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(EnterpriseUpdateResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        enterprise = await async_client.enterprises.update(
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            billing_address={
                "administrative_area": "Illinois",
                "city": "Chicago",
                "country": "United States",
                "postal_code": "60601",
                "street_address": "123 Main St",
                "extended_address": "Suite 400",
            },
            billing_contact={
                "email": "billing@acme.com",
                "first_name": "John",
                "last_name": "Doe",
                "phone_number": "15551234568",
            },
            corporate_registration_number="corporate_registration_number",
            customer_reference="customer_reference",
            doing_business_as="doing_business_as",
            dun_bradstreet_number="dun_bradstreet_number",
            fein="fein",
            industry="industry",
            legal_name="xxx",
            number_of_employees="1-10",
            organization_contact={
                "email": "jane.smith@acme.com",
                "first_name": "Jane",
                "job_title": "VP of Engineering",
                "last_name": "Smith",
                "phone": "+16035551234",
            },
            organization_legal_type="corporation",
            organization_physical_address={
                "administrative_area": "Illinois",
                "city": "Chicago",
                "country": "United States",
                "postal_code": "60601",
                "street_address": "123 Main St",
                "extended_address": "Suite 400",
            },
            primary_business_domain_sic_code="primary_business_domain_sic_code",
            professional_license_number="professional_license_number",
            website="website",
        )
        assert_matches_type(EnterpriseUpdateResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.enterprises.with_raw_response.update(
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enterprise = await response.parse()
        assert_matches_type(EnterpriseUpdateResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.enterprises.with_streaming_response.update(
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enterprise = await response.parse()
            assert_matches_type(EnterpriseUpdateResponse, enterprise, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            await async_client.enterprises.with_raw_response.update(
                enterprise_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        enterprise = await async_client.enterprises.list()
        assert_matches_type(AsyncDefaultFlatPagination[EnterprisePublic], enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        enterprise = await async_client.enterprises.list(
            legal_name="Acme",
            page_number=1,
            page_size=1,
        )
        assert_matches_type(AsyncDefaultFlatPagination[EnterprisePublic], enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.enterprises.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enterprise = await response.parse()
        assert_matches_type(AsyncDefaultFlatPagination[EnterprisePublic], enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.enterprises.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enterprise = await response.parse()
            assert_matches_type(AsyncDefaultFlatPagination[EnterprisePublic], enterprise, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        enterprise = await async_client.enterprises.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert enterprise is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.enterprises.with_raw_response.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enterprise = await response.parse()
        assert enterprise is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.enterprises.with_streaming_response.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enterprise = await response.parse()
            assert enterprise is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            await async_client.enterprises.with_raw_response.delete(
                "",
            )

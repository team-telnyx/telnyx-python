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
    EnterpriseActivateBrandedCallingResponse,
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
                "administrative_area": "IL",
                "city": "Chicago",
                "country": "US",
                "postal_code": "60601",
                "street_address": "100 Main St",
            },
            billing_contact={
                "email": "billing@run065.example.com",
                "first_name": "Alex",
                "last_name": "Bill",
                "phone_number": "+13125550001",
            },
            country_code="US",
            doing_business_as="Run 065 Debug",
            fein="12-3456789",
            industry="technology",
            jurisdiction_of_incorporation="Delaware",
            legal_name="Run 065 Debug Co",
            number_of_employees="51-200",
            organization_contact={
                "email": "org@run065.example.com",
                "first_name": "Sam",
                "job_title": "Compliance Lead",
                "last_name": "Org",
                "phone_number": "+13125550000",
            },
            organization_legal_type="llc",
            organization_physical_address={
                "administrative_area": "IL",
                "city": "Chicago",
                "country": "US",
                "postal_code": "60601",
                "street_address": "100 Main St",
            },
            organization_type="commercial",
            website="https://run065.example.com",
        )
        assert_matches_type(EnterpriseCreateResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        enterprise = client.enterprises.create(
            billing_address={
                "administrative_area": "IL",
                "city": "Chicago",
                "country": "US",
                "postal_code": "60601",
                "street_address": "100 Main St",
                "extended_address": "Suite 504",
            },
            billing_contact={
                "email": "billing@run065.example.com",
                "first_name": "Alex",
                "last_name": "Bill",
                "phone_number": "+13125550001",
            },
            country_code="US",
            doing_business_as="Run 065 Debug",
            fein="12-3456789",
            industry="technology",
            jurisdiction_of_incorporation="Delaware",
            legal_name="Run 065 Debug Co",
            number_of_employees="51-200",
            organization_contact={
                "email": "org@run065.example.com",
                "first_name": "Sam",
                "job_title": "Compliance Lead",
                "last_name": "Org",
                "phone_number": "+13125550000",
            },
            organization_legal_type="llc",
            organization_physical_address={
                "administrative_area": "IL",
                "city": "Chicago",
                "country": "US",
                "postal_code": "60601",
                "street_address": "100 Main St",
                "extended_address": "Suite 504",
            },
            organization_type="commercial",
            website="https://run065.example.com",
            corporate_registration_number="corporate_registration_number",
            customer_reference="internal-id-12345",
            dun_bradstreet_number="dun_bradstreet_number",
            primary_business_domain_sic_code="primary_business_domain_sic_code",
            professional_license_number="professional_license_number",
            role_type="enterprise",
        )
        assert_matches_type(EnterpriseCreateResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.enterprises.with_raw_response.create(
            billing_address={
                "administrative_area": "IL",
                "city": "Chicago",
                "country": "US",
                "postal_code": "60601",
                "street_address": "100 Main St",
            },
            billing_contact={
                "email": "billing@run065.example.com",
                "first_name": "Alex",
                "last_name": "Bill",
                "phone_number": "+13125550001",
            },
            country_code="US",
            doing_business_as="Run 065 Debug",
            fein="12-3456789",
            industry="technology",
            jurisdiction_of_incorporation="Delaware",
            legal_name="Run 065 Debug Co",
            number_of_employees="51-200",
            organization_contact={
                "email": "org@run065.example.com",
                "first_name": "Sam",
                "job_title": "Compliance Lead",
                "last_name": "Org",
                "phone_number": "+13125550000",
            },
            organization_legal_type="llc",
            organization_physical_address={
                "administrative_area": "IL",
                "city": "Chicago",
                "country": "US",
                "postal_code": "60601",
                "street_address": "100 Main St",
            },
            organization_type="commercial",
            website="https://run065.example.com",
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
                "administrative_area": "IL",
                "city": "Chicago",
                "country": "US",
                "postal_code": "60601",
                "street_address": "100 Main St",
            },
            billing_contact={
                "email": "billing@run065.example.com",
                "first_name": "Alex",
                "last_name": "Bill",
                "phone_number": "+13125550001",
            },
            country_code="US",
            doing_business_as="Run 065 Debug",
            fein="12-3456789",
            industry="technology",
            jurisdiction_of_incorporation="Delaware",
            legal_name="Run 065 Debug Co",
            number_of_employees="51-200",
            organization_contact={
                "email": "org@run065.example.com",
                "first_name": "Sam",
                "job_title": "Compliance Lead",
                "last_name": "Org",
                "phone_number": "+13125550000",
            },
            organization_legal_type="llc",
            organization_physical_address={
                "administrative_area": "IL",
                "city": "Chicago",
                "country": "US",
                "postal_code": "60601",
                "street_address": "100 Main St",
            },
            organization_type="commercial",
            website="https://run065.example.com",
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
            "4a6192a4-573d-446d-b3ce-aff9117272a6",
        )
        assert_matches_type(EnterpriseRetrieveResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.enterprises.with_raw_response.retrieve(
            "4a6192a4-573d-446d-b3ce-aff9117272a6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enterprise = response.parse()
        assert_matches_type(EnterpriseRetrieveResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.enterprises.with_streaming_response.retrieve(
            "4a6192a4-573d-446d-b3ce-aff9117272a6",
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
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
        )
        assert_matches_type(EnterpriseUpdateResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        enterprise = client.enterprises.update(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            billing_address={
                "administrative_area": "IL",
                "city": "Chicago",
                "country": "US",
                "postal_code": "60601",
                "street_address": "100 Main St",
                "extended_address": "Suite 504",
            },
            billing_contact={
                "email": "billing@acmeplumbing.example.com",
                "first_name": "Alex",
                "last_name": "Bill",
                "phone_number": "+13125550001",
            },
            corporate_registration_number="corporate_registration_number",
            customer_reference="internal-ref-2026Q2",
            doing_business_as="Acme Plumbing",
            dun_bradstreet_number="dun_bradstreet_number",
            fein="12-3456789",
            industry="business",
            jurisdiction_of_incorporation="Delaware",
            legal_name="Acme Plumbing LLC",
            number_of_employees="51-200",
            organization_contact={
                "email": "sam@acmeplumbing.example.com",
                "first_name": "Sam",
                "job_title": "Compliance Lead",
                "last_name": "Owner",
                "phone_number": "+13125550000",
            },
            organization_legal_type="llc",
            organization_physical_address={
                "administrative_area": "IL",
                "city": "Chicago",
                "country": "US",
                "postal_code": "60601",
                "street_address": "100 Main St",
                "extended_address": "Suite 504",
            },
            primary_business_domain_sic_code="primary_business_domain_sic_code",
            professional_license_number="professional_license_number",
            website="https://acmeplumbing.example.com",
        )
        assert_matches_type(EnterpriseUpdateResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.enterprises.with_raw_response.update(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enterprise = response.parse()
        assert_matches_type(EnterpriseUpdateResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.enterprises.with_streaming_response.update(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
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
            filter_legal_name_contains="Acme",
            legal_name="Acme",
            page_number=1,
            page_size=10,
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
            "4a6192a4-573d-446d-b3ce-aff9117272a6",
        )
        assert enterprise is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.enterprises.with_raw_response.delete(
            "4a6192a4-573d-446d-b3ce-aff9117272a6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enterprise = response.parse()
        assert enterprise is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.enterprises.with_streaming_response.delete(
            "4a6192a4-573d-446d-b3ce-aff9117272a6",
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_activate_branded_calling(self, client: Telnyx) -> None:
        enterprise = client.enterprises.activate_branded_calling(
            "4a6192a4-573d-446d-b3ce-aff9117272a6",
        )
        assert_matches_type(EnterpriseActivateBrandedCallingResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_activate_branded_calling(self, client: Telnyx) -> None:
        response = client.enterprises.with_raw_response.activate_branded_calling(
            "4a6192a4-573d-446d-b3ce-aff9117272a6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enterprise = response.parse()
        assert_matches_type(EnterpriseActivateBrandedCallingResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_activate_branded_calling(self, client: Telnyx) -> None:
        with client.enterprises.with_streaming_response.activate_branded_calling(
            "4a6192a4-573d-446d-b3ce-aff9117272a6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enterprise = response.parse()
            assert_matches_type(EnterpriseActivateBrandedCallingResponse, enterprise, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_activate_branded_calling(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            client.enterprises.with_raw_response.activate_branded_calling(
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
                "administrative_area": "IL",
                "city": "Chicago",
                "country": "US",
                "postal_code": "60601",
                "street_address": "100 Main St",
            },
            billing_contact={
                "email": "billing@run065.example.com",
                "first_name": "Alex",
                "last_name": "Bill",
                "phone_number": "+13125550001",
            },
            country_code="US",
            doing_business_as="Run 065 Debug",
            fein="12-3456789",
            industry="technology",
            jurisdiction_of_incorporation="Delaware",
            legal_name="Run 065 Debug Co",
            number_of_employees="51-200",
            organization_contact={
                "email": "org@run065.example.com",
                "first_name": "Sam",
                "job_title": "Compliance Lead",
                "last_name": "Org",
                "phone_number": "+13125550000",
            },
            organization_legal_type="llc",
            organization_physical_address={
                "administrative_area": "IL",
                "city": "Chicago",
                "country": "US",
                "postal_code": "60601",
                "street_address": "100 Main St",
            },
            organization_type="commercial",
            website="https://run065.example.com",
        )
        assert_matches_type(EnterpriseCreateResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        enterprise = await async_client.enterprises.create(
            billing_address={
                "administrative_area": "IL",
                "city": "Chicago",
                "country": "US",
                "postal_code": "60601",
                "street_address": "100 Main St",
                "extended_address": "Suite 504",
            },
            billing_contact={
                "email": "billing@run065.example.com",
                "first_name": "Alex",
                "last_name": "Bill",
                "phone_number": "+13125550001",
            },
            country_code="US",
            doing_business_as="Run 065 Debug",
            fein="12-3456789",
            industry="technology",
            jurisdiction_of_incorporation="Delaware",
            legal_name="Run 065 Debug Co",
            number_of_employees="51-200",
            organization_contact={
                "email": "org@run065.example.com",
                "first_name": "Sam",
                "job_title": "Compliance Lead",
                "last_name": "Org",
                "phone_number": "+13125550000",
            },
            organization_legal_type="llc",
            organization_physical_address={
                "administrative_area": "IL",
                "city": "Chicago",
                "country": "US",
                "postal_code": "60601",
                "street_address": "100 Main St",
                "extended_address": "Suite 504",
            },
            organization_type="commercial",
            website="https://run065.example.com",
            corporate_registration_number="corporate_registration_number",
            customer_reference="internal-id-12345",
            dun_bradstreet_number="dun_bradstreet_number",
            primary_business_domain_sic_code="primary_business_domain_sic_code",
            professional_license_number="professional_license_number",
            role_type="enterprise",
        )
        assert_matches_type(EnterpriseCreateResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.enterprises.with_raw_response.create(
            billing_address={
                "administrative_area": "IL",
                "city": "Chicago",
                "country": "US",
                "postal_code": "60601",
                "street_address": "100 Main St",
            },
            billing_contact={
                "email": "billing@run065.example.com",
                "first_name": "Alex",
                "last_name": "Bill",
                "phone_number": "+13125550001",
            },
            country_code="US",
            doing_business_as="Run 065 Debug",
            fein="12-3456789",
            industry="technology",
            jurisdiction_of_incorporation="Delaware",
            legal_name="Run 065 Debug Co",
            number_of_employees="51-200",
            organization_contact={
                "email": "org@run065.example.com",
                "first_name": "Sam",
                "job_title": "Compliance Lead",
                "last_name": "Org",
                "phone_number": "+13125550000",
            },
            organization_legal_type="llc",
            organization_physical_address={
                "administrative_area": "IL",
                "city": "Chicago",
                "country": "US",
                "postal_code": "60601",
                "street_address": "100 Main St",
            },
            organization_type="commercial",
            website="https://run065.example.com",
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
                "administrative_area": "IL",
                "city": "Chicago",
                "country": "US",
                "postal_code": "60601",
                "street_address": "100 Main St",
            },
            billing_contact={
                "email": "billing@run065.example.com",
                "first_name": "Alex",
                "last_name": "Bill",
                "phone_number": "+13125550001",
            },
            country_code="US",
            doing_business_as="Run 065 Debug",
            fein="12-3456789",
            industry="technology",
            jurisdiction_of_incorporation="Delaware",
            legal_name="Run 065 Debug Co",
            number_of_employees="51-200",
            organization_contact={
                "email": "org@run065.example.com",
                "first_name": "Sam",
                "job_title": "Compliance Lead",
                "last_name": "Org",
                "phone_number": "+13125550000",
            },
            organization_legal_type="llc",
            organization_physical_address={
                "administrative_area": "IL",
                "city": "Chicago",
                "country": "US",
                "postal_code": "60601",
                "street_address": "100 Main St",
            },
            organization_type="commercial",
            website="https://run065.example.com",
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
            "4a6192a4-573d-446d-b3ce-aff9117272a6",
        )
        assert_matches_type(EnterpriseRetrieveResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.enterprises.with_raw_response.retrieve(
            "4a6192a4-573d-446d-b3ce-aff9117272a6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enterprise = await response.parse()
        assert_matches_type(EnterpriseRetrieveResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.enterprises.with_streaming_response.retrieve(
            "4a6192a4-573d-446d-b3ce-aff9117272a6",
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
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
        )
        assert_matches_type(EnterpriseUpdateResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        enterprise = await async_client.enterprises.update(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            billing_address={
                "administrative_area": "IL",
                "city": "Chicago",
                "country": "US",
                "postal_code": "60601",
                "street_address": "100 Main St",
                "extended_address": "Suite 504",
            },
            billing_contact={
                "email": "billing@acmeplumbing.example.com",
                "first_name": "Alex",
                "last_name": "Bill",
                "phone_number": "+13125550001",
            },
            corporate_registration_number="corporate_registration_number",
            customer_reference="internal-ref-2026Q2",
            doing_business_as="Acme Plumbing",
            dun_bradstreet_number="dun_bradstreet_number",
            fein="12-3456789",
            industry="business",
            jurisdiction_of_incorporation="Delaware",
            legal_name="Acme Plumbing LLC",
            number_of_employees="51-200",
            organization_contact={
                "email": "sam@acmeplumbing.example.com",
                "first_name": "Sam",
                "job_title": "Compliance Lead",
                "last_name": "Owner",
                "phone_number": "+13125550000",
            },
            organization_legal_type="llc",
            organization_physical_address={
                "administrative_area": "IL",
                "city": "Chicago",
                "country": "US",
                "postal_code": "60601",
                "street_address": "100 Main St",
                "extended_address": "Suite 504",
            },
            primary_business_domain_sic_code="primary_business_domain_sic_code",
            professional_license_number="professional_license_number",
            website="https://acmeplumbing.example.com",
        )
        assert_matches_type(EnterpriseUpdateResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.enterprises.with_raw_response.update(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enterprise = await response.parse()
        assert_matches_type(EnterpriseUpdateResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.enterprises.with_streaming_response.update(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
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
            filter_legal_name_contains="Acme",
            legal_name="Acme",
            page_number=1,
            page_size=10,
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
            "4a6192a4-573d-446d-b3ce-aff9117272a6",
        )
        assert enterprise is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.enterprises.with_raw_response.delete(
            "4a6192a4-573d-446d-b3ce-aff9117272a6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enterprise = await response.parse()
        assert enterprise is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.enterprises.with_streaming_response.delete(
            "4a6192a4-573d-446d-b3ce-aff9117272a6",
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_activate_branded_calling(self, async_client: AsyncTelnyx) -> None:
        enterprise = await async_client.enterprises.activate_branded_calling(
            "4a6192a4-573d-446d-b3ce-aff9117272a6",
        )
        assert_matches_type(EnterpriseActivateBrandedCallingResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_activate_branded_calling(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.enterprises.with_raw_response.activate_branded_calling(
            "4a6192a4-573d-446d-b3ce-aff9117272a6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enterprise = await response.parse()
        assert_matches_type(EnterpriseActivateBrandedCallingResponse, enterprise, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_activate_branded_calling(self, async_client: AsyncTelnyx) -> None:
        async with async_client.enterprises.with_streaming_response.activate_branded_calling(
            "4a6192a4-573d-446d-b3ce-aff9117272a6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enterprise = await response.parse()
            assert_matches_type(EnterpriseActivateBrandedCallingResponse, enterprise, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_activate_branded_calling(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            await async_client.enterprises.with_raw_response.activate_branded_calling(
                "",
            )

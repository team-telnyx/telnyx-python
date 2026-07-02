# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx._utils import parse_datetime
from telnyx.pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from telnyx.types.enterprises import DirListResponse, DirCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDir:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        dir = client.enterprises.dir.create(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            authorizer_email="sam@acmeplumbing.example.com",
            authorizer_name="Sam Owner",
            call_reasons=["Appointment reminders", "Billing inquiries"],
            certify_brand_is_accurate=True,
            certify_ip_ownership=True,
            certify_no_shaft_content=True,
            display_name="Acme Plumbing",
        )
        assert_matches_type(DirCreateResponse, dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        dir = client.enterprises.dir.create(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            authorizer_email="sam@acmeplumbing.example.com",
            authorizer_name="Sam Owner",
            call_reasons=["Appointment reminders", "Billing inquiries"],
            certify_brand_is_accurate=True,
            certify_ip_ownership=True,
            certify_no_shaft_content=True,
            display_name="Acme Plumbing",
            documents=[
                {
                    "document_id": "2a7e8337-e803-4057-a4ae-26c40eb0bc6c",
                    "document_type": "business_registration",
                    "description": "Certificate of incorporation.",
                }
            ],
            logo_url="https://acmeplumbing.example.com/logo-256.bmp",
            reselling=False,
        )
        assert_matches_type(DirCreateResponse, dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.enterprises.dir.with_raw_response.create(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            authorizer_email="sam@acmeplumbing.example.com",
            authorizer_name="Sam Owner",
            call_reasons=["Appointment reminders", "Billing inquiries"],
            certify_brand_is_accurate=True,
            certify_ip_ownership=True,
            certify_no_shaft_content=True,
            display_name="Acme Plumbing",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dir = response.parse()
        assert_matches_type(DirCreateResponse, dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.enterprises.dir.with_streaming_response.create(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            authorizer_email="sam@acmeplumbing.example.com",
            authorizer_name="Sam Owner",
            call_reasons=["Appointment reminders", "Billing inquiries"],
            certify_brand_is_accurate=True,
            certify_ip_ownership=True,
            certify_no_shaft_content=True,
            display_name="Acme Plumbing",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dir = response.parse()
            assert_matches_type(DirCreateResponse, dir, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            client.enterprises.dir.with_raw_response.create(
                enterprise_id="",
                authorizer_email="sam@acmeplumbing.example.com",
                authorizer_name="Sam Owner",
                call_reasons=["Appointment reminders", "Billing inquiries"],
                certify_brand_is_accurate=True,
                certify_ip_ownership=True,
                certify_no_shaft_content=True,
                display_name="Acme Plumbing",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        dir = client.enterprises.dir.list(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
        )
        assert_matches_type(SyncDefaultFlatPagination[DirListResponse], dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        dir = client.enterprises.dir.list(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            filter_call_reason_contains="filter[call_reason][contains]",
            filter_display_name_contains="filter[display_name][contains]",
            filter_expiring_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            filter_expiring_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            filter_expiring_within_days=1,
            filter_status="draft",
            page_number=1,
            page_size=20,
            sort="created_at",
        )
        assert_matches_type(SyncDefaultFlatPagination[DirListResponse], dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.enterprises.dir.with_raw_response.list(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dir = response.parse()
        assert_matches_type(SyncDefaultFlatPagination[DirListResponse], dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.enterprises.dir.with_streaming_response.list(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dir = response.parse()
            assert_matches_type(SyncDefaultFlatPagination[DirListResponse], dir, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            client.enterprises.dir.with_raw_response.list(
                enterprise_id="",
            )


class TestAsyncDir:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        dir = await async_client.enterprises.dir.create(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            authorizer_email="sam@acmeplumbing.example.com",
            authorizer_name="Sam Owner",
            call_reasons=["Appointment reminders", "Billing inquiries"],
            certify_brand_is_accurate=True,
            certify_ip_ownership=True,
            certify_no_shaft_content=True,
            display_name="Acme Plumbing",
        )
        assert_matches_type(DirCreateResponse, dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        dir = await async_client.enterprises.dir.create(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            authorizer_email="sam@acmeplumbing.example.com",
            authorizer_name="Sam Owner",
            call_reasons=["Appointment reminders", "Billing inquiries"],
            certify_brand_is_accurate=True,
            certify_ip_ownership=True,
            certify_no_shaft_content=True,
            display_name="Acme Plumbing",
            documents=[
                {
                    "document_id": "2a7e8337-e803-4057-a4ae-26c40eb0bc6c",
                    "document_type": "business_registration",
                    "description": "Certificate of incorporation.",
                }
            ],
            logo_url="https://acmeplumbing.example.com/logo-256.bmp",
            reselling=False,
        )
        assert_matches_type(DirCreateResponse, dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.enterprises.dir.with_raw_response.create(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            authorizer_email="sam@acmeplumbing.example.com",
            authorizer_name="Sam Owner",
            call_reasons=["Appointment reminders", "Billing inquiries"],
            certify_brand_is_accurate=True,
            certify_ip_ownership=True,
            certify_no_shaft_content=True,
            display_name="Acme Plumbing",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dir = await response.parse()
        assert_matches_type(DirCreateResponse, dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.enterprises.dir.with_streaming_response.create(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            authorizer_email="sam@acmeplumbing.example.com",
            authorizer_name="Sam Owner",
            call_reasons=["Appointment reminders", "Billing inquiries"],
            certify_brand_is_accurate=True,
            certify_ip_ownership=True,
            certify_no_shaft_content=True,
            display_name="Acme Plumbing",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dir = await response.parse()
            assert_matches_type(DirCreateResponse, dir, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            await async_client.enterprises.dir.with_raw_response.create(
                enterprise_id="",
                authorizer_email="sam@acmeplumbing.example.com",
                authorizer_name="Sam Owner",
                call_reasons=["Appointment reminders", "Billing inquiries"],
                certify_brand_is_accurate=True,
                certify_ip_ownership=True,
                certify_no_shaft_content=True,
                display_name="Acme Plumbing",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        dir = await async_client.enterprises.dir.list(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
        )
        assert_matches_type(AsyncDefaultFlatPagination[DirListResponse], dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        dir = await async_client.enterprises.dir.list(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            filter_call_reason_contains="filter[call_reason][contains]",
            filter_display_name_contains="filter[display_name][contains]",
            filter_expiring_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            filter_expiring_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            filter_expiring_within_days=1,
            filter_status="draft",
            page_number=1,
            page_size=20,
            sort="created_at",
        )
        assert_matches_type(AsyncDefaultFlatPagination[DirListResponse], dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.enterprises.dir.with_raw_response.list(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dir = await response.parse()
        assert_matches_type(AsyncDefaultFlatPagination[DirListResponse], dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.enterprises.dir.with_streaming_response.list(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dir = await response.parse()
            assert_matches_type(AsyncDefaultFlatPagination[DirListResponse], dir, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            await async_client.enterprises.dir.with_raw_response.list(
                enterprise_id="",
            )

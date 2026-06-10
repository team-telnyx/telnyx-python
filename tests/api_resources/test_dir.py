# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    DirListResponse,
    DirSubmitResponse,
    DirUpdateResponse,
    DirRetrieveResponse,
    DirListDocumentTypesResponse,
    DirUpdateInfringementResponse,
    DirListInfringementClaimsResponse,
)
from telnyx._utils import parse_datetime
from telnyx._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from telnyx.pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDir:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        dir = client.dir.retrieve(
            "16635d38-75a6-4481-82e8-69af60e05011",
        )
        assert_matches_type(DirRetrieveResponse, dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.dir.with_raw_response.retrieve(
            "16635d38-75a6-4481-82e8-69af60e05011",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dir = response.parse()
        assert_matches_type(DirRetrieveResponse, dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.dir.with_streaming_response.retrieve(
            "16635d38-75a6-4481-82e8-69af60e05011",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dir = response.parse()
            assert_matches_type(DirRetrieveResponse, dir, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dir_id` but received ''"):
            client.dir.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        dir = client.dir.update(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
        )
        assert_matches_type(DirUpdateResponse, dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        dir = client.dir.update(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            authorizer_email="dev@stainless.com",
            authorizer_name="authorizer_name",
            call_reasons=["Appointment reminders", "Billing inquiries", "Lab results"],
            certify_brand_is_accurate=True,
            certify_ip_ownership=True,
            certify_no_shaft_content=True,
            display_name="Acme Plumbing & Wellness",
            documents=[
                {
                    "document_id": "2a7e8337-e803-4057-a4ae-26c40eb0bc6c",
                    "document_type": "business_registration",
                    "description": "Certificate of incorporation.",
                }
            ],
            logo_url="https://acmeplumbing.example.com/logo-v2-256.bmp",
            reselling=True,
        )
        assert_matches_type(DirUpdateResponse, dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.dir.with_raw_response.update(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dir = response.parse()
        assert_matches_type(DirUpdateResponse, dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.dir.with_streaming_response.update(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dir = response.parse()
            assert_matches_type(DirUpdateResponse, dir, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dir_id` but received ''"):
            client.dir.with_raw_response.update(
                dir_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        dir = client.dir.list()
        assert_matches_type(SyncDefaultFlatPagination[DirListResponse], dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        dir = client.dir.list(
            filter_call_reason_contains="filter[call_reason][contains]",
            filter_display_name_contains="filter[display_name][contains]",
            filter_enterprise_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filter_expiring_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            filter_expiring_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            filter_status="draft",
            page_number=1,
            page_size=20,
            sort="created_at",
        )
        assert_matches_type(SyncDefaultFlatPagination[DirListResponse], dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.dir.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dir = response.parse()
        assert_matches_type(SyncDefaultFlatPagination[DirListResponse], dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.dir.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dir = response.parse()
            assert_matches_type(SyncDefaultFlatPagination[DirListResponse], dir, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        dir = client.dir.delete(
            "16635d38-75a6-4481-82e8-69af60e05011",
        )
        assert dir is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.dir.with_raw_response.delete(
            "16635d38-75a6-4481-82e8-69af60e05011",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dir = response.parse()
        assert dir is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.dir.with_streaming_response.delete(
            "16635d38-75a6-4481-82e8-69af60e05011",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dir = response.parse()
            assert dir is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dir_id` but received ''"):
            client.dir.with_raw_response.delete(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create_loa(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.post("/dir/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/loa").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        dir = client.dir.create_loa(
            dir_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            phone_numbers=["+13125550000"],
        )
        assert dir.is_closed
        assert dir.json() == {"foo": "bar"}
        assert cast(Any, dir.is_closed) is True
        assert isinstance(dir, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create_loa_with_all_params(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.post("/dir/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/loa").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        dir = client.dir.create_loa(
            dir_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            phone_numbers=["+13125550000"],
            agent={
                "administrative_area": "administrative_area",
                "city": "city",
                "contact_email": "dev@stainless.com",
                "contact_name": "contact_name",
                "contact_phone": "+13125550000",
                "contact_title": "contact_title",
                "country": "US",
                "legal_name": "legal_name",
                "postal_code": "postal_code",
                "street_address": "street_address",
                "dba": "dba",
                "extended_address": "extended_address",
            },
            signature={
                "image_base64": "x",
                "signer_name": "signer_name",
            },
        )
        assert dir.is_closed
        assert dir.json() == {"foo": "bar"}
        assert cast(Any, dir.is_closed) is True
        assert isinstance(dir, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_create_loa(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.post("/dir/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/loa").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        dir = client.dir.with_raw_response.create_loa(
            dir_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            phone_numbers=["+13125550000"],
        )

        assert dir.is_closed is True
        assert dir.http_request.headers.get("X-Stainless-Lang") == "python"
        assert dir.json() == {"foo": "bar"}
        assert isinstance(dir, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_create_loa(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.post("/dir/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/loa").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.dir.with_streaming_response.create_loa(
            dir_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            phone_numbers=["+13125550000"],
        ) as dir:
            assert not dir.is_closed
            assert dir.http_request.headers.get("X-Stainless-Lang") == "python"

            assert dir.json() == {"foo": "bar"}
            assert cast(Any, dir.is_closed) is True
            assert isinstance(dir, StreamedBinaryAPIResponse)

        assert cast(Any, dir.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_create_loa(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dir_id` but received ''"):
            client.dir.with_raw_response.create_loa(
                dir_id="",
                phone_numbers=["+13125550000"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_document_types(self, client: Telnyx) -> None:
        dir = client.dir.list_document_types()
        assert_matches_type(DirListDocumentTypesResponse, dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_document_types(self, client: Telnyx) -> None:
        response = client.dir.with_raw_response.list_document_types()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dir = response.parse()
        assert_matches_type(DirListDocumentTypesResponse, dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_document_types(self, client: Telnyx) -> None:
        with client.dir.with_streaming_response.list_document_types() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dir = response.parse()
            assert_matches_type(DirListDocumentTypesResponse, dir, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_infringement_claims(self, client: Telnyx) -> None:
        dir = client.dir.list_infringement_claims(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
        )
        assert_matches_type(SyncDefaultFlatPagination[DirListInfringementClaimsResponse], dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_infringement_claims_with_all_params(self, client: Telnyx) -> None:
        dir = client.dir.list_infringement_claims(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            page_number=1,
            page_size=20,
        )
        assert_matches_type(SyncDefaultFlatPagination[DirListInfringementClaimsResponse], dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_infringement_claims(self, client: Telnyx) -> None:
        response = client.dir.with_raw_response.list_infringement_claims(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dir = response.parse()
        assert_matches_type(SyncDefaultFlatPagination[DirListInfringementClaimsResponse], dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_infringement_claims(self, client: Telnyx) -> None:
        with client.dir.with_streaming_response.list_infringement_claims(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dir = response.parse()
            assert_matches_type(SyncDefaultFlatPagination[DirListInfringementClaimsResponse], dir, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_infringement_claims(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dir_id` but received ''"):
            client.dir.with_raw_response.list_infringement_claims(
                dir_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit(self, client: Telnyx) -> None:
        dir = client.dir.submit(
            "16635d38-75a6-4481-82e8-69af60e05011",
        )
        assert_matches_type(DirSubmitResponse, dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_submit(self, client: Telnyx) -> None:
        response = client.dir.with_raw_response.submit(
            "16635d38-75a6-4481-82e8-69af60e05011",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dir = response.parse()
        assert_matches_type(DirSubmitResponse, dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_submit(self, client: Telnyx) -> None:
        with client.dir.with_streaming_response.submit(
            "16635d38-75a6-4481-82e8-69af60e05011",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dir = response.parse()
            assert_matches_type(DirSubmitResponse, dir, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_submit(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dir_id` but received ''"):
            client.dir.with_raw_response.submit(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_infringement(self, client: Telnyx) -> None:
        dir = client.dir.update_infringement(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            certify_brand_is_accurate=True,
            certify_ip_ownership=True,
            certify_no_infringement=True,
            certify_no_shaft_content=True,
            infringement_resolution_notes="Updated the display name to remove the disputed mark and re-uploaded the authorization.",
        )
        assert_matches_type(DirUpdateInfringementResponse, dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_infringement_with_all_params(self, client: Telnyx) -> None:
        dir = client.dir.update_infringement(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            certify_brand_is_accurate=True,
            certify_ip_ownership=True,
            certify_no_infringement=True,
            certify_no_shaft_content=True,
            infringement_resolution_notes="Updated the display name to remove the disputed mark and re-uploaded the authorization.",
            call_reasons=["string"],
            display_name="x",
            documents=[
                {
                    "document_id": "2a7e8337-e803-4057-a4ae-26c40eb0bc6c",
                    "document_type": "business_registration",
                    "description": "Certificate of incorporation.",
                }
            ],
            logo_url="logo_url",
        )
        assert_matches_type(DirUpdateInfringementResponse, dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_infringement(self, client: Telnyx) -> None:
        response = client.dir.with_raw_response.update_infringement(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            certify_brand_is_accurate=True,
            certify_ip_ownership=True,
            certify_no_infringement=True,
            certify_no_shaft_content=True,
            infringement_resolution_notes="Updated the display name to remove the disputed mark and re-uploaded the authorization.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dir = response.parse()
        assert_matches_type(DirUpdateInfringementResponse, dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_infringement(self, client: Telnyx) -> None:
        with client.dir.with_streaming_response.update_infringement(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            certify_brand_is_accurate=True,
            certify_ip_ownership=True,
            certify_no_infringement=True,
            certify_no_shaft_content=True,
            infringement_resolution_notes="Updated the display name to remove the disputed mark and re-uploaded the authorization.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dir = response.parse()
            assert_matches_type(DirUpdateInfringementResponse, dir, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_infringement(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dir_id` but received ''"):
            client.dir.with_raw_response.update_infringement(
                dir_id="",
                certify_brand_is_accurate=True,
                certify_ip_ownership=True,
                certify_no_infringement=True,
                certify_no_shaft_content=True,
                infringement_resolution_notes="Updated the display name to remove the disputed mark and re-uploaded the authorization.",
            )


class TestAsyncDir:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        dir = await async_client.dir.retrieve(
            "16635d38-75a6-4481-82e8-69af60e05011",
        )
        assert_matches_type(DirRetrieveResponse, dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.dir.with_raw_response.retrieve(
            "16635d38-75a6-4481-82e8-69af60e05011",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dir = await response.parse()
        assert_matches_type(DirRetrieveResponse, dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.dir.with_streaming_response.retrieve(
            "16635d38-75a6-4481-82e8-69af60e05011",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dir = await response.parse()
            assert_matches_type(DirRetrieveResponse, dir, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dir_id` but received ''"):
            await async_client.dir.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        dir = await async_client.dir.update(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
        )
        assert_matches_type(DirUpdateResponse, dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        dir = await async_client.dir.update(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            authorizer_email="dev@stainless.com",
            authorizer_name="authorizer_name",
            call_reasons=["Appointment reminders", "Billing inquiries", "Lab results"],
            certify_brand_is_accurate=True,
            certify_ip_ownership=True,
            certify_no_shaft_content=True,
            display_name="Acme Plumbing & Wellness",
            documents=[
                {
                    "document_id": "2a7e8337-e803-4057-a4ae-26c40eb0bc6c",
                    "document_type": "business_registration",
                    "description": "Certificate of incorporation.",
                }
            ],
            logo_url="https://acmeplumbing.example.com/logo-v2-256.bmp",
            reselling=True,
        )
        assert_matches_type(DirUpdateResponse, dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.dir.with_raw_response.update(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dir = await response.parse()
        assert_matches_type(DirUpdateResponse, dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.dir.with_streaming_response.update(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dir = await response.parse()
            assert_matches_type(DirUpdateResponse, dir, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dir_id` but received ''"):
            await async_client.dir.with_raw_response.update(
                dir_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        dir = await async_client.dir.list()
        assert_matches_type(AsyncDefaultFlatPagination[DirListResponse], dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        dir = await async_client.dir.list(
            filter_call_reason_contains="filter[call_reason][contains]",
            filter_display_name_contains="filter[display_name][contains]",
            filter_enterprise_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filter_expiring_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            filter_expiring_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            filter_status="draft",
            page_number=1,
            page_size=20,
            sort="created_at",
        )
        assert_matches_type(AsyncDefaultFlatPagination[DirListResponse], dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.dir.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dir = await response.parse()
        assert_matches_type(AsyncDefaultFlatPagination[DirListResponse], dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.dir.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dir = await response.parse()
            assert_matches_type(AsyncDefaultFlatPagination[DirListResponse], dir, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        dir = await async_client.dir.delete(
            "16635d38-75a6-4481-82e8-69af60e05011",
        )
        assert dir is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.dir.with_raw_response.delete(
            "16635d38-75a6-4481-82e8-69af60e05011",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dir = await response.parse()
        assert dir is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.dir.with_streaming_response.delete(
            "16635d38-75a6-4481-82e8-69af60e05011",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dir = await response.parse()
            assert dir is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dir_id` but received ''"):
            await async_client.dir.with_raw_response.delete(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create_loa(self, async_client: AsyncTelnyx, respx_mock: MockRouter) -> None:
        respx_mock.post("/dir/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/loa").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        dir = await async_client.dir.create_loa(
            dir_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            phone_numbers=["+13125550000"],
        )
        assert dir.is_closed
        assert await dir.json() == {"foo": "bar"}
        assert cast(Any, dir.is_closed) is True
        assert isinstance(dir, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create_loa_with_all_params(self, async_client: AsyncTelnyx, respx_mock: MockRouter) -> None:
        respx_mock.post("/dir/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/loa").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        dir = await async_client.dir.create_loa(
            dir_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            phone_numbers=["+13125550000"],
            agent={
                "administrative_area": "administrative_area",
                "city": "city",
                "contact_email": "dev@stainless.com",
                "contact_name": "contact_name",
                "contact_phone": "+13125550000",
                "contact_title": "contact_title",
                "country": "US",
                "legal_name": "legal_name",
                "postal_code": "postal_code",
                "street_address": "street_address",
                "dba": "dba",
                "extended_address": "extended_address",
            },
            signature={
                "image_base64": "x",
                "signer_name": "signer_name",
            },
        )
        assert dir.is_closed
        assert await dir.json() == {"foo": "bar"}
        assert cast(Any, dir.is_closed) is True
        assert isinstance(dir, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_create_loa(self, async_client: AsyncTelnyx, respx_mock: MockRouter) -> None:
        respx_mock.post("/dir/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/loa").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        dir = await async_client.dir.with_raw_response.create_loa(
            dir_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            phone_numbers=["+13125550000"],
        )

        assert dir.is_closed is True
        assert dir.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await dir.json() == {"foo": "bar"}
        assert isinstance(dir, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_create_loa(self, async_client: AsyncTelnyx, respx_mock: MockRouter) -> None:
        respx_mock.post("/dir/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/loa").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.dir.with_streaming_response.create_loa(
            dir_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            phone_numbers=["+13125550000"],
        ) as dir:
            assert not dir.is_closed
            assert dir.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await dir.json() == {"foo": "bar"}
            assert cast(Any, dir.is_closed) is True
            assert isinstance(dir, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, dir.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_create_loa(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dir_id` but received ''"):
            await async_client.dir.with_raw_response.create_loa(
                dir_id="",
                phone_numbers=["+13125550000"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_document_types(self, async_client: AsyncTelnyx) -> None:
        dir = await async_client.dir.list_document_types()
        assert_matches_type(DirListDocumentTypesResponse, dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_document_types(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.dir.with_raw_response.list_document_types()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dir = await response.parse()
        assert_matches_type(DirListDocumentTypesResponse, dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_document_types(self, async_client: AsyncTelnyx) -> None:
        async with async_client.dir.with_streaming_response.list_document_types() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dir = await response.parse()
            assert_matches_type(DirListDocumentTypesResponse, dir, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_infringement_claims(self, async_client: AsyncTelnyx) -> None:
        dir = await async_client.dir.list_infringement_claims(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
        )
        assert_matches_type(AsyncDefaultFlatPagination[DirListInfringementClaimsResponse], dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_infringement_claims_with_all_params(self, async_client: AsyncTelnyx) -> None:
        dir = await async_client.dir.list_infringement_claims(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            page_number=1,
            page_size=20,
        )
        assert_matches_type(AsyncDefaultFlatPagination[DirListInfringementClaimsResponse], dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_infringement_claims(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.dir.with_raw_response.list_infringement_claims(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dir = await response.parse()
        assert_matches_type(AsyncDefaultFlatPagination[DirListInfringementClaimsResponse], dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_infringement_claims(self, async_client: AsyncTelnyx) -> None:
        async with async_client.dir.with_streaming_response.list_infringement_claims(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dir = await response.parse()
            assert_matches_type(AsyncDefaultFlatPagination[DirListInfringementClaimsResponse], dir, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_infringement_claims(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dir_id` but received ''"):
            await async_client.dir.with_raw_response.list_infringement_claims(
                dir_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit(self, async_client: AsyncTelnyx) -> None:
        dir = await async_client.dir.submit(
            "16635d38-75a6-4481-82e8-69af60e05011",
        )
        assert_matches_type(DirSubmitResponse, dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_submit(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.dir.with_raw_response.submit(
            "16635d38-75a6-4481-82e8-69af60e05011",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dir = await response.parse()
        assert_matches_type(DirSubmitResponse, dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_submit(self, async_client: AsyncTelnyx) -> None:
        async with async_client.dir.with_streaming_response.submit(
            "16635d38-75a6-4481-82e8-69af60e05011",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dir = await response.parse()
            assert_matches_type(DirSubmitResponse, dir, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_submit(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dir_id` but received ''"):
            await async_client.dir.with_raw_response.submit(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_infringement(self, async_client: AsyncTelnyx) -> None:
        dir = await async_client.dir.update_infringement(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            certify_brand_is_accurate=True,
            certify_ip_ownership=True,
            certify_no_infringement=True,
            certify_no_shaft_content=True,
            infringement_resolution_notes="Updated the display name to remove the disputed mark and re-uploaded the authorization.",
        )
        assert_matches_type(DirUpdateInfringementResponse, dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_infringement_with_all_params(self, async_client: AsyncTelnyx) -> None:
        dir = await async_client.dir.update_infringement(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            certify_brand_is_accurate=True,
            certify_ip_ownership=True,
            certify_no_infringement=True,
            certify_no_shaft_content=True,
            infringement_resolution_notes="Updated the display name to remove the disputed mark and re-uploaded the authorization.",
            call_reasons=["string"],
            display_name="x",
            documents=[
                {
                    "document_id": "2a7e8337-e803-4057-a4ae-26c40eb0bc6c",
                    "document_type": "business_registration",
                    "description": "Certificate of incorporation.",
                }
            ],
            logo_url="logo_url",
        )
        assert_matches_type(DirUpdateInfringementResponse, dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_infringement(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.dir.with_raw_response.update_infringement(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            certify_brand_is_accurate=True,
            certify_ip_ownership=True,
            certify_no_infringement=True,
            certify_no_shaft_content=True,
            infringement_resolution_notes="Updated the display name to remove the disputed mark and re-uploaded the authorization.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dir = await response.parse()
        assert_matches_type(DirUpdateInfringementResponse, dir, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_infringement(self, async_client: AsyncTelnyx) -> None:
        async with async_client.dir.with_streaming_response.update_infringement(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            certify_brand_is_accurate=True,
            certify_ip_ownership=True,
            certify_no_infringement=True,
            certify_no_shaft_content=True,
            infringement_resolution_notes="Updated the display name to remove the disputed mark and re-uploaded the authorization.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dir = await response.parse()
            assert_matches_type(DirUpdateInfringementResponse, dir, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_infringement(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dir_id` but received ''"):
            await async_client.dir.with_raw_response.update_infringement(
                dir_id="",
                certify_brand_is_accurate=True,
                certify_ip_ownership=True,
                certify_no_infringement=True,
                certify_no_shaft_content=True,
                infringement_resolution_notes="Updated the display name to remove the disputed mark and re-uploaded the authorization.",
            )

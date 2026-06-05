# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from telnyx.types.terms_of_service import AgreementListResponse, AgreementRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgreements:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        agreement = client.terms_of_service.agreements.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(AgreementRetrieveResponse, agreement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.terms_of_service.agreements.with_raw_response.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agreement = response.parse()
        assert_matches_type(AgreementRetrieveResponse, agreement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.terms_of_service.agreements.with_streaming_response.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agreement = response.parse()
            assert_matches_type(AgreementRetrieveResponse, agreement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agreement_id` but received ''"):
            client.terms_of_service.agreements.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        agreement = client.terms_of_service.agreements.list()
        assert_matches_type(SyncDefaultFlatPagination[AgreementListResponse], agreement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        agreement = client.terms_of_service.agreements.list(
            page_number=1,
            page_size=20,
            product_type="branded_calling",
        )
        assert_matches_type(SyncDefaultFlatPagination[AgreementListResponse], agreement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.terms_of_service.agreements.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agreement = response.parse()
        assert_matches_type(SyncDefaultFlatPagination[AgreementListResponse], agreement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.terms_of_service.agreements.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agreement = response.parse()
            assert_matches_type(SyncDefaultFlatPagination[AgreementListResponse], agreement, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAgreements:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        agreement = await async_client.terms_of_service.agreements.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(AgreementRetrieveResponse, agreement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.terms_of_service.agreements.with_raw_response.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agreement = await response.parse()
        assert_matches_type(AgreementRetrieveResponse, agreement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.terms_of_service.agreements.with_streaming_response.retrieve(
            "550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agreement = await response.parse()
            assert_matches_type(AgreementRetrieveResponse, agreement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agreement_id` but received ''"):
            await async_client.terms_of_service.agreements.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        agreement = await async_client.terms_of_service.agreements.list()
        assert_matches_type(AsyncDefaultFlatPagination[AgreementListResponse], agreement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        agreement = await async_client.terms_of_service.agreements.list(
            page_number=1,
            page_size=20,
            product_type="branded_calling",
        )
        assert_matches_type(AsyncDefaultFlatPagination[AgreementListResponse], agreement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.terms_of_service.agreements.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agreement = await response.parse()
        assert_matches_type(AsyncDefaultFlatPagination[AgreementListResponse], agreement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.terms_of_service.agreements.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agreement = await response.parse()
            assert_matches_type(AsyncDefaultFlatPagination[AgreementListResponse], agreement, path=["response"])

        assert cast(Any, response.is_closed) is True

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    TermsOfServiceRetrieveInfoResponse,
    TermsOfServiceRetrieveStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTermsOfService:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_info(self, client: Telnyx) -> None:
        terms_of_service = client.terms_of_service.retrieve_info()
        assert_matches_type(TermsOfServiceRetrieveInfoResponse, terms_of_service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_info_with_all_params(self, client: Telnyx) -> None:
        terms_of_service = client.terms_of_service.retrieve_info(
            product_type="branded_calling",
        )
        assert_matches_type(TermsOfServiceRetrieveInfoResponse, terms_of_service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_info(self, client: Telnyx) -> None:
        response = client.terms_of_service.with_raw_response.retrieve_info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        terms_of_service = response.parse()
        assert_matches_type(TermsOfServiceRetrieveInfoResponse, terms_of_service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_info(self, client: Telnyx) -> None:
        with client.terms_of_service.with_streaming_response.retrieve_info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            terms_of_service = response.parse()
            assert_matches_type(TermsOfServiceRetrieveInfoResponse, terms_of_service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_status(self, client: Telnyx) -> None:
        terms_of_service = client.terms_of_service.retrieve_status()
        assert_matches_type(TermsOfServiceRetrieveStatusResponse, terms_of_service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_status_with_all_params(self, client: Telnyx) -> None:
        terms_of_service = client.terms_of_service.retrieve_status(
            product_type="branded_calling",
        )
        assert_matches_type(TermsOfServiceRetrieveStatusResponse, terms_of_service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_status(self, client: Telnyx) -> None:
        response = client.terms_of_service.with_raw_response.retrieve_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        terms_of_service = response.parse()
        assert_matches_type(TermsOfServiceRetrieveStatusResponse, terms_of_service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_status(self, client: Telnyx) -> None:
        with client.terms_of_service.with_streaming_response.retrieve_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            terms_of_service = response.parse()
            assert_matches_type(TermsOfServiceRetrieveStatusResponse, terms_of_service, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTermsOfService:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_info(self, async_client: AsyncTelnyx) -> None:
        terms_of_service = await async_client.terms_of_service.retrieve_info()
        assert_matches_type(TermsOfServiceRetrieveInfoResponse, terms_of_service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_info_with_all_params(self, async_client: AsyncTelnyx) -> None:
        terms_of_service = await async_client.terms_of_service.retrieve_info(
            product_type="branded_calling",
        )
        assert_matches_type(TermsOfServiceRetrieveInfoResponse, terms_of_service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_info(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.terms_of_service.with_raw_response.retrieve_info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        terms_of_service = await response.parse()
        assert_matches_type(TermsOfServiceRetrieveInfoResponse, terms_of_service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_info(self, async_client: AsyncTelnyx) -> None:
        async with async_client.terms_of_service.with_streaming_response.retrieve_info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            terms_of_service = await response.parse()
            assert_matches_type(TermsOfServiceRetrieveInfoResponse, terms_of_service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_status(self, async_client: AsyncTelnyx) -> None:
        terms_of_service = await async_client.terms_of_service.retrieve_status()
        assert_matches_type(TermsOfServiceRetrieveStatusResponse, terms_of_service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_status_with_all_params(self, async_client: AsyncTelnyx) -> None:
        terms_of_service = await async_client.terms_of_service.retrieve_status(
            product_type="branded_calling",
        )
        assert_matches_type(TermsOfServiceRetrieveStatusResponse, terms_of_service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_status(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.terms_of_service.with_raw_response.retrieve_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        terms_of_service = await response.parse()
        assert_matches_type(TermsOfServiceRetrieveStatusResponse, terms_of_service, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_status(self, async_client: AsyncTelnyx) -> None:
        async with async_client.terms_of_service.with_streaming_response.retrieve_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            terms_of_service = await response.parse()
            assert_matches_type(TermsOfServiceRetrieveStatusResponse, terms_of_service, path=["response"])

        assert cast(Any, response.is_closed) is True

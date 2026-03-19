# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from telnyx.types.whatsapp.business_accounts import (
    PhoneNumberListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPhoneNumbers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        phone_number = client.whatsapp.business_accounts.phone_numbers.list(
            id="id",
        )
        assert_matches_type(SyncDefaultFlatPagination[PhoneNumberListResponse], phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        phone_number = client.whatsapp.business_accounts.phone_numbers.list(
            id="id",
            page_number=0,
            page_size=0,
        )
        assert_matches_type(SyncDefaultFlatPagination[PhoneNumberListResponse], phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.whatsapp.business_accounts.phone_numbers.with_raw_response.list(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert_matches_type(SyncDefaultFlatPagination[PhoneNumberListResponse], phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.whatsapp.business_accounts.phone_numbers.with_streaming_response.list(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert_matches_type(SyncDefaultFlatPagination[PhoneNumberListResponse], phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.whatsapp.business_accounts.phone_numbers.with_raw_response.list(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_verification(self, client: Telnyx) -> None:
        phone_number = client.whatsapp.business_accounts.phone_numbers.create_verification(
            id="id",
            display_name="display_name",
            phone_number="phone_number",
        )
        assert phone_number is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_verification_with_all_params(self, client: Telnyx) -> None:
        phone_number = client.whatsapp.business_accounts.phone_numbers.create_verification(
            id="id",
            display_name="display_name",
            phone_number="phone_number",
            language="language",
            verification_method="sms",
        )
        assert phone_number is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_verification(self, client: Telnyx) -> None:
        response = client.whatsapp.business_accounts.phone_numbers.with_raw_response.create_verification(
            id="id",
            display_name="display_name",
            phone_number="phone_number",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert phone_number is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_verification(self, client: Telnyx) -> None:
        with client.whatsapp.business_accounts.phone_numbers.with_streaming_response.create_verification(
            id="id",
            display_name="display_name",
            phone_number="phone_number",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert phone_number is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_verification(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.whatsapp.business_accounts.phone_numbers.with_raw_response.create_verification(
                id="",
                display_name="display_name",
                phone_number="phone_number",
            )


class TestAsyncPhoneNumbers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        phone_number = await async_client.whatsapp.business_accounts.phone_numbers.list(
            id="id",
        )
        assert_matches_type(AsyncDefaultFlatPagination[PhoneNumberListResponse], phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        phone_number = await async_client.whatsapp.business_accounts.phone_numbers.list(
            id="id",
            page_number=0,
            page_size=0,
        )
        assert_matches_type(AsyncDefaultFlatPagination[PhoneNumberListResponse], phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.whatsapp.business_accounts.phone_numbers.with_raw_response.list(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert_matches_type(AsyncDefaultFlatPagination[PhoneNumberListResponse], phone_number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.whatsapp.business_accounts.phone_numbers.with_streaming_response.list(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert_matches_type(AsyncDefaultFlatPagination[PhoneNumberListResponse], phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.whatsapp.business_accounts.phone_numbers.with_raw_response.list(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_verification(self, async_client: AsyncTelnyx) -> None:
        phone_number = await async_client.whatsapp.business_accounts.phone_numbers.create_verification(
            id="id",
            display_name="display_name",
            phone_number="phone_number",
        )
        assert phone_number is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_verification_with_all_params(self, async_client: AsyncTelnyx) -> None:
        phone_number = await async_client.whatsapp.business_accounts.phone_numbers.create_verification(
            id="id",
            display_name="display_name",
            phone_number="phone_number",
            language="language",
            verification_method="sms",
        )
        assert phone_number is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_verification(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.whatsapp.business_accounts.phone_numbers.with_raw_response.create_verification(
            id="id",
            display_name="display_name",
            phone_number="phone_number",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert phone_number is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_verification(self, async_client: AsyncTelnyx) -> None:
        async with async_client.whatsapp.business_accounts.phone_numbers.with_streaming_response.create_verification(
            id="id",
            display_name="display_name",
            phone_number="phone_number",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert phone_number is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_verification(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.whatsapp.business_accounts.phone_numbers.with_raw_response.create_verification(
                id="",
                display_name="display_name",
                phone_number="phone_number",
            )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    MobilePhoneNumber,
    MobilePhoneNumberUpdateResponse,
    MobilePhoneNumberRetrieveResponse,
)
from telnyx.pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMobilePhoneNumbers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        mobile_phone_number = client.mobile_phone_numbers.retrieve(
            "id",
        )
        assert_matches_type(MobilePhoneNumberRetrieveResponse, mobile_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.mobile_phone_numbers.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mobile_phone_number = response.parse()
        assert_matches_type(MobilePhoneNumberRetrieveResponse, mobile_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.mobile_phone_numbers.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mobile_phone_number = response.parse()
            assert_matches_type(MobilePhoneNumberRetrieveResponse, mobile_phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.mobile_phone_numbers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        mobile_phone_number = client.mobile_phone_numbers.update(
            id="id",
        )
        assert_matches_type(MobilePhoneNumberUpdateResponse, mobile_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        mobile_phone_number = client.mobile_phone_numbers.update(
            id="id",
            call_forwarding={
                "call_forwarding_enabled": True,
                "forwarding_type": "always",
                "forwards_to": "forwards_to",
            },
            call_recording={
                "inbound_call_recording_channels": "single",
                "inbound_call_recording_enabled": True,
                "inbound_call_recording_format": "wav",
            },
            caller_id_name_enabled=True,
            cnam_listing={
                "cnam_listing_details": "cnam_listing_details",
                "cnam_listing_enabled": True,
            },
            connection_id="connection_id",
            customer_reference="customer_reference",
            inbound={"interception_app_id": "interception_app_id"},
            inbound_call_screening="disabled",
            noise_suppression=True,
            outbound={"interception_app_id": "interception_app_id"},
            tags=["string"],
        )
        assert_matches_type(MobilePhoneNumberUpdateResponse, mobile_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.mobile_phone_numbers.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mobile_phone_number = response.parse()
        assert_matches_type(MobilePhoneNumberUpdateResponse, mobile_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.mobile_phone_numbers.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mobile_phone_number = response.parse()
            assert_matches_type(MobilePhoneNumberUpdateResponse, mobile_phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.mobile_phone_numbers.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        mobile_phone_number = client.mobile_phone_numbers.list()
        assert_matches_type(SyncDefaultFlatPagination[MobilePhoneNumber], mobile_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        mobile_phone_number = client.mobile_phone_numbers.list(
            page_number=0,
            page_size=0,
        )
        assert_matches_type(SyncDefaultFlatPagination[MobilePhoneNumber], mobile_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.mobile_phone_numbers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mobile_phone_number = response.parse()
        assert_matches_type(SyncDefaultFlatPagination[MobilePhoneNumber], mobile_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.mobile_phone_numbers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mobile_phone_number = response.parse()
            assert_matches_type(SyncDefaultFlatPagination[MobilePhoneNumber], mobile_phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMobilePhoneNumbers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        mobile_phone_number = await async_client.mobile_phone_numbers.retrieve(
            "id",
        )
        assert_matches_type(MobilePhoneNumberRetrieveResponse, mobile_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.mobile_phone_numbers.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mobile_phone_number = await response.parse()
        assert_matches_type(MobilePhoneNumberRetrieveResponse, mobile_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.mobile_phone_numbers.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mobile_phone_number = await response.parse()
            assert_matches_type(MobilePhoneNumberRetrieveResponse, mobile_phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.mobile_phone_numbers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        mobile_phone_number = await async_client.mobile_phone_numbers.update(
            id="id",
        )
        assert_matches_type(MobilePhoneNumberUpdateResponse, mobile_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        mobile_phone_number = await async_client.mobile_phone_numbers.update(
            id="id",
            call_forwarding={
                "call_forwarding_enabled": True,
                "forwarding_type": "always",
                "forwards_to": "forwards_to",
            },
            call_recording={
                "inbound_call_recording_channels": "single",
                "inbound_call_recording_enabled": True,
                "inbound_call_recording_format": "wav",
            },
            caller_id_name_enabled=True,
            cnam_listing={
                "cnam_listing_details": "cnam_listing_details",
                "cnam_listing_enabled": True,
            },
            connection_id="connection_id",
            customer_reference="customer_reference",
            inbound={"interception_app_id": "interception_app_id"},
            inbound_call_screening="disabled",
            noise_suppression=True,
            outbound={"interception_app_id": "interception_app_id"},
            tags=["string"],
        )
        assert_matches_type(MobilePhoneNumberUpdateResponse, mobile_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.mobile_phone_numbers.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mobile_phone_number = await response.parse()
        assert_matches_type(MobilePhoneNumberUpdateResponse, mobile_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.mobile_phone_numbers.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mobile_phone_number = await response.parse()
            assert_matches_type(MobilePhoneNumberUpdateResponse, mobile_phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.mobile_phone_numbers.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        mobile_phone_number = await async_client.mobile_phone_numbers.list()
        assert_matches_type(AsyncDefaultFlatPagination[MobilePhoneNumber], mobile_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        mobile_phone_number = await async_client.mobile_phone_numbers.list(
            page_number=0,
            page_size=0,
        )
        assert_matches_type(AsyncDefaultFlatPagination[MobilePhoneNumber], mobile_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.mobile_phone_numbers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mobile_phone_number = await response.parse()
        assert_matches_type(AsyncDefaultFlatPagination[MobilePhoneNumber], mobile_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.mobile_phone_numbers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mobile_phone_number = await response.parse()
            assert_matches_type(AsyncDefaultFlatPagination[MobilePhoneNumber], mobile_phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

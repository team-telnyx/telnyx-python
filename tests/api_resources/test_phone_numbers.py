# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    PhoneNumberListResponse,
    PhoneNumberDeleteResponse,
    PhoneNumberUpdateResponse,
    PhoneNumberRetrieveResponse,
    PhoneNumberSlimListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPhoneNumbers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        phone_number = client.phone_numbers.retrieve(
            "1293384261075731499",
        )
        assert_matches_type(PhoneNumberRetrieveResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.phone_numbers.with_raw_response.retrieve(
            "1293384261075731499",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert_matches_type(PhoneNumberRetrieveResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.phone_numbers.with_streaming_response.retrieve(
            "1293384261075731499",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert_matches_type(PhoneNumberRetrieveResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.phone_numbers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        phone_number = client.phone_numbers.update(
            id="1293384261075731499",
        )
        assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        phone_number = client.phone_numbers.update(
            id="1293384261075731499",
            billing_group_id="dc8e4d67-33a0-4cbb-af74-7b58f05bd494",
            connection_id="dc8e4d67-33a0-4cbb-af74-7b58f05bd494",
            customer_reference="customer-reference",
            external_pin="1234",
            hd_voice_enabled=True,
            tags=["tag"],
        )
        assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.phone_numbers.with_raw_response.update(
            id="1293384261075731499",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.phone_numbers.with_streaming_response.update(
            id="1293384261075731499",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.phone_numbers.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        phone_number = client.phone_numbers.list()
        assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        phone_number = client.phone_numbers.list(
            filter={
                "billing_group_id": "62e4bf2e-c278-4282-b524-488d9c9c43b2",
                "connection_id": "1521916448077776306",
                "country_iso_alpha2": "US",
                "customer_reference": "customer_reference",
                "emergency_address_id": "9102160989215728032",
                "number_type": {"eq": "local"},
                "phone_number": "phone_number",
                "source": "ported",
                "status": "active",
                "tag": "tag",
                "voice_connection_name": {
                    "contains": "test",
                    "ends_with": "test",
                    "eq": "test",
                    "starts_with": "test",
                },
                "voice_usage_payment_method": "channel",
            },
            page={
                "number": 1,
                "size": 1,
            },
            sort="connection_name",
        )
        assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.phone_numbers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.phone_numbers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        phone_number = client.phone_numbers.delete(
            "1293384261075731499",
        )
        assert_matches_type(PhoneNumberDeleteResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.phone_numbers.with_raw_response.delete(
            "1293384261075731499",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert_matches_type(PhoneNumberDeleteResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.phone_numbers.with_streaming_response.delete(
            "1293384261075731499",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert_matches_type(PhoneNumberDeleteResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.phone_numbers.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_slim_list(self, client: Telnyx) -> None:
        phone_number = client.phone_numbers.slim_list()
        assert_matches_type(PhoneNumberSlimListResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_slim_list_with_all_params(self, client: Telnyx) -> None:
        phone_number = client.phone_numbers.slim_list(
            filter={
                "billing_group_id": "62e4bf2e-c278-4282-b524-488d9c9c43b2",
                "connection_id": "1521916448077776306",
                "country_iso_alpha2": "US",
                "customer_reference": "customer_reference",
                "emergency_address_id": "9102160989215728032",
                "number_type": {"eq": "local"},
                "phone_number": "phone_number",
                "source": "ported",
                "status": "active",
                "tag": "tag",
                "voice_connection_name": {
                    "contains": "test",
                    "ends_with": "test",
                    "eq": "test",
                    "starts_with": "test",
                },
                "voice_usage_payment_method": "channel",
            },
            include_connection=True,
            include_tags=True,
            page={
                "number": 1,
                "size": 1,
            },
            sort="connection_name",
        )
        assert_matches_type(PhoneNumberSlimListResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_slim_list(self, client: Telnyx) -> None:
        response = client.phone_numbers.with_raw_response.slim_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert_matches_type(PhoneNumberSlimListResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_slim_list(self, client: Telnyx) -> None:
        with client.phone_numbers.with_streaming_response.slim_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert_matches_type(PhoneNumberSlimListResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPhoneNumbers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        phone_number = await async_client.phone_numbers.retrieve(
            "1293384261075731499",
        )
        assert_matches_type(PhoneNumberRetrieveResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.phone_numbers.with_raw_response.retrieve(
            "1293384261075731499",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert_matches_type(PhoneNumberRetrieveResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.phone_numbers.with_streaming_response.retrieve(
            "1293384261075731499",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert_matches_type(PhoneNumberRetrieveResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.phone_numbers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        phone_number = await async_client.phone_numbers.update(
            id="1293384261075731499",
        )
        assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        phone_number = await async_client.phone_numbers.update(
            id="1293384261075731499",
            billing_group_id="dc8e4d67-33a0-4cbb-af74-7b58f05bd494",
            connection_id="dc8e4d67-33a0-4cbb-af74-7b58f05bd494",
            customer_reference="customer-reference",
            external_pin="1234",
            hd_voice_enabled=True,
            tags=["tag"],
        )
        assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.phone_numbers.with_raw_response.update(
            id="1293384261075731499",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.phone_numbers.with_streaming_response.update(
            id="1293384261075731499",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.phone_numbers.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        phone_number = await async_client.phone_numbers.list()
        assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        phone_number = await async_client.phone_numbers.list(
            filter={
                "billing_group_id": "62e4bf2e-c278-4282-b524-488d9c9c43b2",
                "connection_id": "1521916448077776306",
                "country_iso_alpha2": "US",
                "customer_reference": "customer_reference",
                "emergency_address_id": "9102160989215728032",
                "number_type": {"eq": "local"},
                "phone_number": "phone_number",
                "source": "ported",
                "status": "active",
                "tag": "tag",
                "voice_connection_name": {
                    "contains": "test",
                    "ends_with": "test",
                    "eq": "test",
                    "starts_with": "test",
                },
                "voice_usage_payment_method": "channel",
            },
            page={
                "number": 1,
                "size": 1,
            },
            sort="connection_name",
        )
        assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.phone_numbers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.phone_numbers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        phone_number = await async_client.phone_numbers.delete(
            "1293384261075731499",
        )
        assert_matches_type(PhoneNumberDeleteResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.phone_numbers.with_raw_response.delete(
            "1293384261075731499",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert_matches_type(PhoneNumberDeleteResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.phone_numbers.with_streaming_response.delete(
            "1293384261075731499",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert_matches_type(PhoneNumberDeleteResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.phone_numbers.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_slim_list(self, async_client: AsyncTelnyx) -> None:
        phone_number = await async_client.phone_numbers.slim_list()
        assert_matches_type(PhoneNumberSlimListResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_slim_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        phone_number = await async_client.phone_numbers.slim_list(
            filter={
                "billing_group_id": "62e4bf2e-c278-4282-b524-488d9c9c43b2",
                "connection_id": "1521916448077776306",
                "country_iso_alpha2": "US",
                "customer_reference": "customer_reference",
                "emergency_address_id": "9102160989215728032",
                "number_type": {"eq": "local"},
                "phone_number": "phone_number",
                "source": "ported",
                "status": "active",
                "tag": "tag",
                "voice_connection_name": {
                    "contains": "test",
                    "ends_with": "test",
                    "eq": "test",
                    "starts_with": "test",
                },
                "voice_usage_payment_method": "channel",
            },
            include_connection=True,
            include_tags=True,
            page={
                "number": 1,
                "size": 1,
            },
            sort="connection_name",
        )
        assert_matches_type(PhoneNumberSlimListResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_slim_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.phone_numbers.with_raw_response.slim_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert_matches_type(PhoneNumberSlimListResponse, phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_slim_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.phone_numbers.with_streaming_response.slim_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert_matches_type(PhoneNumberSlimListResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

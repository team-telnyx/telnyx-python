# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    UserAddressListResponse,
    UserAddressCreateResponse,
    UserAddressRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUserAddresses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        user_address = client.user_addresses.create(
            business_name="Toy-O'Kon",
            country_code="US",
            first_name="Alfred",
            last_name="Foster",
            locality="Austin",
            street_address="600 Congress Avenue",
        )
        assert_matches_type(UserAddressCreateResponse, user_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        user_address = client.user_addresses.create(
            business_name="Toy-O'Kon",
            country_code="US",
            first_name="Alfred",
            last_name="Foster",
            locality="Austin",
            street_address="600 Congress Avenue",
            administrative_area="TX",
            borough="Guadalajara",
            customer_reference="MY REF 001",
            extended_address="14th Floor",
            neighborhood="Ciudad de los deportes",
            phone_number="+12125559000",
            postal_code="78701",
            skip_address_verification="skip_address_verification",
        )
        assert_matches_type(UserAddressCreateResponse, user_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.user_addresses.with_raw_response.create(
            business_name="Toy-O'Kon",
            country_code="US",
            first_name="Alfred",
            last_name="Foster",
            locality="Austin",
            street_address="600 Congress Avenue",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_address = response.parse()
        assert_matches_type(UserAddressCreateResponse, user_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.user_addresses.with_streaming_response.create(
            business_name="Toy-O'Kon",
            country_code="US",
            first_name="Alfred",
            last_name="Foster",
            locality="Austin",
            street_address="600 Congress Avenue",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_address = response.parse()
            assert_matches_type(UserAddressCreateResponse, user_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        user_address = client.user_addresses.retrieve(
            "id",
        )
        assert_matches_type(UserAddressRetrieveResponse, user_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.user_addresses.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_address = response.parse()
        assert_matches_type(UserAddressRetrieveResponse, user_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.user_addresses.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_address = response.parse()
            assert_matches_type(UserAddressRetrieveResponse, user_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.user_addresses.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        user_address = client.user_addresses.list()
        assert_matches_type(UserAddressListResponse, user_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        user_address = client.user_addresses.list(
            filter={
                "customer_reference": {
                    "contains": "contains",
                    "eq": "eq",
                },
                "street_address": {"contains": "contains"},
            },
            page={
                "number": 1,
                "size": 1,
            },
            sort="street_address",
        )
        assert_matches_type(UserAddressListResponse, user_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.user_addresses.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_address = response.parse()
        assert_matches_type(UserAddressListResponse, user_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.user_addresses.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_address = response.parse()
            assert_matches_type(UserAddressListResponse, user_address, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUserAddresses:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        user_address = await async_client.user_addresses.create(
            business_name="Toy-O'Kon",
            country_code="US",
            first_name="Alfred",
            last_name="Foster",
            locality="Austin",
            street_address="600 Congress Avenue",
        )
        assert_matches_type(UserAddressCreateResponse, user_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        user_address = await async_client.user_addresses.create(
            business_name="Toy-O'Kon",
            country_code="US",
            first_name="Alfred",
            last_name="Foster",
            locality="Austin",
            street_address="600 Congress Avenue",
            administrative_area="TX",
            borough="Guadalajara",
            customer_reference="MY REF 001",
            extended_address="14th Floor",
            neighborhood="Ciudad de los deportes",
            phone_number="+12125559000",
            postal_code="78701",
            skip_address_verification="skip_address_verification",
        )
        assert_matches_type(UserAddressCreateResponse, user_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.user_addresses.with_raw_response.create(
            business_name="Toy-O'Kon",
            country_code="US",
            first_name="Alfred",
            last_name="Foster",
            locality="Austin",
            street_address="600 Congress Avenue",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_address = await response.parse()
        assert_matches_type(UserAddressCreateResponse, user_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.user_addresses.with_streaming_response.create(
            business_name="Toy-O'Kon",
            country_code="US",
            first_name="Alfred",
            last_name="Foster",
            locality="Austin",
            street_address="600 Congress Avenue",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_address = await response.parse()
            assert_matches_type(UserAddressCreateResponse, user_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        user_address = await async_client.user_addresses.retrieve(
            "id",
        )
        assert_matches_type(UserAddressRetrieveResponse, user_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.user_addresses.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_address = await response.parse()
        assert_matches_type(UserAddressRetrieveResponse, user_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.user_addresses.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_address = await response.parse()
            assert_matches_type(UserAddressRetrieveResponse, user_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.user_addresses.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        user_address = await async_client.user_addresses.list()
        assert_matches_type(UserAddressListResponse, user_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        user_address = await async_client.user_addresses.list(
            filter={
                "customer_reference": {
                    "contains": "contains",
                    "eq": "eq",
                },
                "street_address": {"contains": "contains"},
            },
            page={
                "number": 1,
                "size": 1,
            },
            sort="street_address",
        )
        assert_matches_type(UserAddressListResponse, user_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.user_addresses.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_address = await response.parse()
        assert_matches_type(UserAddressListResponse, user_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.user_addresses.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_address = await response.parse()
            assert_matches_type(UserAddressListResponse, user_address, path=["response"])

        assert cast(Any, response.is_closed) is True

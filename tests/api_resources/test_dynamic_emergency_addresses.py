# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    DynamicEmergencyAddressListResponse,
    DynamicEmergencyAddressCreateResponse,
    DynamicEmergencyAddressDeleteResponse,
    DynamicEmergencyAddressRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDynamicEmergencyAddresses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        dynamic_emergency_address = client.dynamic_emergency_addresses.create(
            administrative_area="TX",
            country_code="US",
            house_number="house_number",
            locality="Austin",
            postal_code="78701",
            street_name="Congress",
        )
        assert_matches_type(DynamicEmergencyAddressCreateResponse, dynamic_emergency_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        dynamic_emergency_address = client.dynamic_emergency_addresses.create(
            administrative_area="TX",
            country_code="US",
            house_number="house_number",
            locality="Austin",
            postal_code="78701",
            street_name="Congress",
            extended_address="extended_address",
            house_suffix="house_suffix",
            street_post_directional="street_post_directional",
            street_pre_directional="street_pre_directional",
            street_suffix="St",
        )
        assert_matches_type(DynamicEmergencyAddressCreateResponse, dynamic_emergency_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.dynamic_emergency_addresses.with_raw_response.create(
            administrative_area="TX",
            country_code="US",
            house_number="house_number",
            locality="Austin",
            postal_code="78701",
            street_name="Congress",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dynamic_emergency_address = response.parse()
        assert_matches_type(DynamicEmergencyAddressCreateResponse, dynamic_emergency_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.dynamic_emergency_addresses.with_streaming_response.create(
            administrative_area="TX",
            country_code="US",
            house_number="house_number",
            locality="Austin",
            postal_code="78701",
            street_name="Congress",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dynamic_emergency_address = response.parse()
            assert_matches_type(DynamicEmergencyAddressCreateResponse, dynamic_emergency_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        dynamic_emergency_address = client.dynamic_emergency_addresses.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DynamicEmergencyAddressRetrieveResponse, dynamic_emergency_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.dynamic_emergency_addresses.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dynamic_emergency_address = response.parse()
        assert_matches_type(DynamicEmergencyAddressRetrieveResponse, dynamic_emergency_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.dynamic_emergency_addresses.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dynamic_emergency_address = response.parse()
            assert_matches_type(DynamicEmergencyAddressRetrieveResponse, dynamic_emergency_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.dynamic_emergency_addresses.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        dynamic_emergency_address = client.dynamic_emergency_addresses.list()
        assert_matches_type(DynamicEmergencyAddressListResponse, dynamic_emergency_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        dynamic_emergency_address = client.dynamic_emergency_addresses.list(
            filter={
                "country_code": "country_code",
                "status": "pending",
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(DynamicEmergencyAddressListResponse, dynamic_emergency_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.dynamic_emergency_addresses.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dynamic_emergency_address = response.parse()
        assert_matches_type(DynamicEmergencyAddressListResponse, dynamic_emergency_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.dynamic_emergency_addresses.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dynamic_emergency_address = response.parse()
            assert_matches_type(DynamicEmergencyAddressListResponse, dynamic_emergency_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        dynamic_emergency_address = client.dynamic_emergency_addresses.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DynamicEmergencyAddressDeleteResponse, dynamic_emergency_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.dynamic_emergency_addresses.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dynamic_emergency_address = response.parse()
        assert_matches_type(DynamicEmergencyAddressDeleteResponse, dynamic_emergency_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.dynamic_emergency_addresses.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dynamic_emergency_address = response.parse()
            assert_matches_type(DynamicEmergencyAddressDeleteResponse, dynamic_emergency_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.dynamic_emergency_addresses.with_raw_response.delete(
                "",
            )


class TestAsyncDynamicEmergencyAddresses:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        dynamic_emergency_address = await async_client.dynamic_emergency_addresses.create(
            administrative_area="TX",
            country_code="US",
            house_number="house_number",
            locality="Austin",
            postal_code="78701",
            street_name="Congress",
        )
        assert_matches_type(DynamicEmergencyAddressCreateResponse, dynamic_emergency_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        dynamic_emergency_address = await async_client.dynamic_emergency_addresses.create(
            administrative_area="TX",
            country_code="US",
            house_number="house_number",
            locality="Austin",
            postal_code="78701",
            street_name="Congress",
            extended_address="extended_address",
            house_suffix="house_suffix",
            street_post_directional="street_post_directional",
            street_pre_directional="street_pre_directional",
            street_suffix="St",
        )
        assert_matches_type(DynamicEmergencyAddressCreateResponse, dynamic_emergency_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.dynamic_emergency_addresses.with_raw_response.create(
            administrative_area="TX",
            country_code="US",
            house_number="house_number",
            locality="Austin",
            postal_code="78701",
            street_name="Congress",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dynamic_emergency_address = await response.parse()
        assert_matches_type(DynamicEmergencyAddressCreateResponse, dynamic_emergency_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.dynamic_emergency_addresses.with_streaming_response.create(
            administrative_area="TX",
            country_code="US",
            house_number="house_number",
            locality="Austin",
            postal_code="78701",
            street_name="Congress",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dynamic_emergency_address = await response.parse()
            assert_matches_type(DynamicEmergencyAddressCreateResponse, dynamic_emergency_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        dynamic_emergency_address = await async_client.dynamic_emergency_addresses.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DynamicEmergencyAddressRetrieveResponse, dynamic_emergency_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.dynamic_emergency_addresses.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dynamic_emergency_address = await response.parse()
        assert_matches_type(DynamicEmergencyAddressRetrieveResponse, dynamic_emergency_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.dynamic_emergency_addresses.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dynamic_emergency_address = await response.parse()
            assert_matches_type(DynamicEmergencyAddressRetrieveResponse, dynamic_emergency_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.dynamic_emergency_addresses.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        dynamic_emergency_address = await async_client.dynamic_emergency_addresses.list()
        assert_matches_type(DynamicEmergencyAddressListResponse, dynamic_emergency_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        dynamic_emergency_address = await async_client.dynamic_emergency_addresses.list(
            filter={
                "country_code": "country_code",
                "status": "pending",
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(DynamicEmergencyAddressListResponse, dynamic_emergency_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.dynamic_emergency_addresses.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dynamic_emergency_address = await response.parse()
        assert_matches_type(DynamicEmergencyAddressListResponse, dynamic_emergency_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.dynamic_emergency_addresses.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dynamic_emergency_address = await response.parse()
            assert_matches_type(DynamicEmergencyAddressListResponse, dynamic_emergency_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        dynamic_emergency_address = await async_client.dynamic_emergency_addresses.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DynamicEmergencyAddressDeleteResponse, dynamic_emergency_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.dynamic_emergency_addresses.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dynamic_emergency_address = await response.parse()
        assert_matches_type(DynamicEmergencyAddressDeleteResponse, dynamic_emergency_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.dynamic_emergency_addresses.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dynamic_emergency_address = await response.parse()
            assert_matches_type(DynamicEmergencyAddressDeleteResponse, dynamic_emergency_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.dynamic_emergency_addresses.with_raw_response.delete(
                "",
            )

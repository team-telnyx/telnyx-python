# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.external_connections import (
    CivicAddressListResponse,
    CivicAddressRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCivicAddresses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        civic_address = client.external_connections.civic_addresses.retrieve(
            address_id="318fb664-d341-44d2-8405-e6bfb9ced6d9",
            id="id",
        )
        assert_matches_type(CivicAddressRetrieveResponse, civic_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.external_connections.civic_addresses.with_raw_response.retrieve(
            address_id="318fb664-d341-44d2-8405-e6bfb9ced6d9",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        civic_address = response.parse()
        assert_matches_type(CivicAddressRetrieveResponse, civic_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.external_connections.civic_addresses.with_streaming_response.retrieve(
            address_id="318fb664-d341-44d2-8405-e6bfb9ced6d9",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            civic_address = response.parse()
            assert_matches_type(CivicAddressRetrieveResponse, civic_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.external_connections.civic_addresses.with_raw_response.retrieve(
                address_id="318fb664-d341-44d2-8405-e6bfb9ced6d9",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address_id` but received ''"):
            client.external_connections.civic_addresses.with_raw_response.retrieve(
                address_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        civic_address = client.external_connections.civic_addresses.list(
            id="id",
        )
        assert_matches_type(CivicAddressListResponse, civic_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        civic_address = client.external_connections.civic_addresses.list(
            id="id",
            filter={"country": ["US", "CA", "MX", "BR"]},
        )
        assert_matches_type(CivicAddressListResponse, civic_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.external_connections.civic_addresses.with_raw_response.list(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        civic_address = response.parse()
        assert_matches_type(CivicAddressListResponse, civic_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.external_connections.civic_addresses.with_streaming_response.list(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            civic_address = response.parse()
            assert_matches_type(CivicAddressListResponse, civic_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.external_connections.civic_addresses.with_raw_response.list(
                id="",
            )


class TestAsyncCivicAddresses:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        civic_address = await async_client.external_connections.civic_addresses.retrieve(
            address_id="318fb664-d341-44d2-8405-e6bfb9ced6d9",
            id="id",
        )
        assert_matches_type(CivicAddressRetrieveResponse, civic_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.external_connections.civic_addresses.with_raw_response.retrieve(
            address_id="318fb664-d341-44d2-8405-e6bfb9ced6d9",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        civic_address = await response.parse()
        assert_matches_type(CivicAddressRetrieveResponse, civic_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.external_connections.civic_addresses.with_streaming_response.retrieve(
            address_id="318fb664-d341-44d2-8405-e6bfb9ced6d9",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            civic_address = await response.parse()
            assert_matches_type(CivicAddressRetrieveResponse, civic_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.external_connections.civic_addresses.with_raw_response.retrieve(
                address_id="318fb664-d341-44d2-8405-e6bfb9ced6d9",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address_id` but received ''"):
            await async_client.external_connections.civic_addresses.with_raw_response.retrieve(
                address_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        civic_address = await async_client.external_connections.civic_addresses.list(
            id="id",
        )
        assert_matches_type(CivicAddressListResponse, civic_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        civic_address = await async_client.external_connections.civic_addresses.list(
            id="id",
            filter={"country": ["US", "CA", "MX", "BR"]},
        )
        assert_matches_type(CivicAddressListResponse, civic_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.external_connections.civic_addresses.with_raw_response.list(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        civic_address = await response.parse()
        assert_matches_type(CivicAddressListResponse, civic_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.external_connections.civic_addresses.with_streaming_response.list(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            civic_address = await response.parse()
            assert_matches_type(CivicAddressListResponse, civic_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.external_connections.civic_addresses.with_raw_response.list(
                id="",
            )

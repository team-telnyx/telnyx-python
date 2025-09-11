# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    AccessIPAddressResponse,
    AccessIPAddressListResponse,
)
from telnyx._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccessIPAddress:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        access_ip_address = client.access_ip_address.create(
            ip_address="ip_address",
        )
        assert_matches_type(AccessIPAddressResponse, access_ip_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        access_ip_address = client.access_ip_address.create(
            ip_address="ip_address",
            description="description",
        )
        assert_matches_type(AccessIPAddressResponse, access_ip_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.access_ip_address.with_raw_response.create(
            ip_address="ip_address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_ip_address = response.parse()
        assert_matches_type(AccessIPAddressResponse, access_ip_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.access_ip_address.with_streaming_response.create(
            ip_address="ip_address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_ip_address = response.parse()
            assert_matches_type(AccessIPAddressResponse, access_ip_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        access_ip_address = client.access_ip_address.retrieve(
            "access_ip_address_id",
        )
        assert_matches_type(AccessIPAddressResponse, access_ip_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.access_ip_address.with_raw_response.retrieve(
            "access_ip_address_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_ip_address = response.parse()
        assert_matches_type(AccessIPAddressResponse, access_ip_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.access_ip_address.with_streaming_response.retrieve(
            "access_ip_address_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_ip_address = response.parse()
            assert_matches_type(AccessIPAddressResponse, access_ip_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `access_ip_address_id` but received ''"):
            client.access_ip_address.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        access_ip_address = client.access_ip_address.list()
        assert_matches_type(AccessIPAddressListResponse, access_ip_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        access_ip_address = client.access_ip_address.list(
            filter={
                "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "ip_address": "ip_address",
                "ip_source": "ip_source",
            },
            page={
                "number": 0,
                "size": 250,
            },
        )
        assert_matches_type(AccessIPAddressListResponse, access_ip_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.access_ip_address.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_ip_address = response.parse()
        assert_matches_type(AccessIPAddressListResponse, access_ip_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.access_ip_address.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_ip_address = response.parse()
            assert_matches_type(AccessIPAddressListResponse, access_ip_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        access_ip_address = client.access_ip_address.delete(
            "access_ip_address_id",
        )
        assert_matches_type(AccessIPAddressResponse, access_ip_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.access_ip_address.with_raw_response.delete(
            "access_ip_address_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_ip_address = response.parse()
        assert_matches_type(AccessIPAddressResponse, access_ip_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.access_ip_address.with_streaming_response.delete(
            "access_ip_address_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_ip_address = response.parse()
            assert_matches_type(AccessIPAddressResponse, access_ip_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `access_ip_address_id` but received ''"):
            client.access_ip_address.with_raw_response.delete(
                "",
            )


class TestAsyncAccessIPAddress:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        access_ip_address = await async_client.access_ip_address.create(
            ip_address="ip_address",
        )
        assert_matches_type(AccessIPAddressResponse, access_ip_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        access_ip_address = await async_client.access_ip_address.create(
            ip_address="ip_address",
            description="description",
        )
        assert_matches_type(AccessIPAddressResponse, access_ip_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.access_ip_address.with_raw_response.create(
            ip_address="ip_address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_ip_address = await response.parse()
        assert_matches_type(AccessIPAddressResponse, access_ip_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.access_ip_address.with_streaming_response.create(
            ip_address="ip_address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_ip_address = await response.parse()
            assert_matches_type(AccessIPAddressResponse, access_ip_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        access_ip_address = await async_client.access_ip_address.retrieve(
            "access_ip_address_id",
        )
        assert_matches_type(AccessIPAddressResponse, access_ip_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.access_ip_address.with_raw_response.retrieve(
            "access_ip_address_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_ip_address = await response.parse()
        assert_matches_type(AccessIPAddressResponse, access_ip_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.access_ip_address.with_streaming_response.retrieve(
            "access_ip_address_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_ip_address = await response.parse()
            assert_matches_type(AccessIPAddressResponse, access_ip_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `access_ip_address_id` but received ''"):
            await async_client.access_ip_address.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        access_ip_address = await async_client.access_ip_address.list()
        assert_matches_type(AccessIPAddressListResponse, access_ip_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        access_ip_address = await async_client.access_ip_address.list(
            filter={
                "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "ip_address": "ip_address",
                "ip_source": "ip_source",
            },
            page={
                "number": 0,
                "size": 250,
            },
        )
        assert_matches_type(AccessIPAddressListResponse, access_ip_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.access_ip_address.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_ip_address = await response.parse()
        assert_matches_type(AccessIPAddressListResponse, access_ip_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.access_ip_address.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_ip_address = await response.parse()
            assert_matches_type(AccessIPAddressListResponse, access_ip_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        access_ip_address = await async_client.access_ip_address.delete(
            "access_ip_address_id",
        )
        assert_matches_type(AccessIPAddressResponse, access_ip_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.access_ip_address.with_raw_response.delete(
            "access_ip_address_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_ip_address = await response.parse()
        assert_matches_type(AccessIPAddressResponse, access_ip_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.access_ip_address.with_streaming_response.delete(
            "access_ip_address_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_ip_address = await response.parse()
            assert_matches_type(AccessIPAddressResponse, access_ip_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `access_ip_address_id` but received ''"):
            await async_client.access_ip_address.with_raw_response.delete(
                "",
            )

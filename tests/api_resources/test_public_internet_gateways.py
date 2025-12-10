# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    PublicInternetGatewayListResponse,
    PublicInternetGatewayCreateResponse,
    PublicInternetGatewayDeleteResponse,
    PublicInternetGatewayRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPublicInternetGateways:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        public_internet_gateway = client.public_internet_gateways.create()
        assert_matches_type(PublicInternetGatewayCreateResponse, public_internet_gateway, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        public_internet_gateway = client.public_internet_gateways.create(
            name="test interface",
            network_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            region_code="ashburn-va",
        )
        assert_matches_type(PublicInternetGatewayCreateResponse, public_internet_gateway, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.public_internet_gateways.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        public_internet_gateway = response.parse()
        assert_matches_type(PublicInternetGatewayCreateResponse, public_internet_gateway, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.public_internet_gateways.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            public_internet_gateway = response.parse()
            assert_matches_type(PublicInternetGatewayCreateResponse, public_internet_gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        public_internet_gateway = client.public_internet_gateways.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(PublicInternetGatewayRetrieveResponse, public_internet_gateway, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.public_internet_gateways.with_raw_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        public_internet_gateway = response.parse()
        assert_matches_type(PublicInternetGatewayRetrieveResponse, public_internet_gateway, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.public_internet_gateways.with_streaming_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            public_internet_gateway = response.parse()
            assert_matches_type(PublicInternetGatewayRetrieveResponse, public_internet_gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.public_internet_gateways.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        public_internet_gateway = client.public_internet_gateways.list()
        assert_matches_type(PublicInternetGatewayListResponse, public_internet_gateway, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        public_internet_gateway = client.public_internet_gateways.list(
            filter={"network_id": "6a09cdc3-8948-47f0-aa62-74ac943d6c58"},
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(PublicInternetGatewayListResponse, public_internet_gateway, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.public_internet_gateways.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        public_internet_gateway = response.parse()
        assert_matches_type(PublicInternetGatewayListResponse, public_internet_gateway, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.public_internet_gateways.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            public_internet_gateway = response.parse()
            assert_matches_type(PublicInternetGatewayListResponse, public_internet_gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        public_internet_gateway = client.public_internet_gateways.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(PublicInternetGatewayDeleteResponse, public_internet_gateway, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.public_internet_gateways.with_raw_response.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        public_internet_gateway = response.parse()
        assert_matches_type(PublicInternetGatewayDeleteResponse, public_internet_gateway, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.public_internet_gateways.with_streaming_response.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            public_internet_gateway = response.parse()
            assert_matches_type(PublicInternetGatewayDeleteResponse, public_internet_gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.public_internet_gateways.with_raw_response.delete(
                "",
            )


class TestAsyncPublicInternetGateways:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        public_internet_gateway = await async_client.public_internet_gateways.create()
        assert_matches_type(PublicInternetGatewayCreateResponse, public_internet_gateway, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        public_internet_gateway = await async_client.public_internet_gateways.create(
            name="test interface",
            network_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            region_code="ashburn-va",
        )
        assert_matches_type(PublicInternetGatewayCreateResponse, public_internet_gateway, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.public_internet_gateways.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        public_internet_gateway = await response.parse()
        assert_matches_type(PublicInternetGatewayCreateResponse, public_internet_gateway, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.public_internet_gateways.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            public_internet_gateway = await response.parse()
            assert_matches_type(PublicInternetGatewayCreateResponse, public_internet_gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        public_internet_gateway = await async_client.public_internet_gateways.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(PublicInternetGatewayRetrieveResponse, public_internet_gateway, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.public_internet_gateways.with_raw_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        public_internet_gateway = await response.parse()
        assert_matches_type(PublicInternetGatewayRetrieveResponse, public_internet_gateway, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.public_internet_gateways.with_streaming_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            public_internet_gateway = await response.parse()
            assert_matches_type(PublicInternetGatewayRetrieveResponse, public_internet_gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.public_internet_gateways.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        public_internet_gateway = await async_client.public_internet_gateways.list()
        assert_matches_type(PublicInternetGatewayListResponse, public_internet_gateway, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        public_internet_gateway = await async_client.public_internet_gateways.list(
            filter={"network_id": "6a09cdc3-8948-47f0-aa62-74ac943d6c58"},
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(PublicInternetGatewayListResponse, public_internet_gateway, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.public_internet_gateways.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        public_internet_gateway = await response.parse()
        assert_matches_type(PublicInternetGatewayListResponse, public_internet_gateway, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.public_internet_gateways.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            public_internet_gateway = await response.parse()
            assert_matches_type(PublicInternetGatewayListResponse, public_internet_gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        public_internet_gateway = await async_client.public_internet_gateways.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(PublicInternetGatewayDeleteResponse, public_internet_gateway, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.public_internet_gateways.with_raw_response.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        public_internet_gateway = await response.parse()
        assert_matches_type(PublicInternetGatewayDeleteResponse, public_internet_gateway, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.public_internet_gateways.with_streaming_response.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            public_internet_gateway = await response.parse()
            assert_matches_type(PublicInternetGatewayDeleteResponse, public_internet_gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.public_internet_gateways.with_raw_response.delete(
                "",
            )

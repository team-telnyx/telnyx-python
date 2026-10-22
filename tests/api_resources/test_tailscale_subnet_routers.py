# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    TailscaleSubnetRouter,
    TailscaleSubnetRouterCreateResponse,
    TailscaleSubnetRouterDeleteResponse,
    TailscaleSubnetRouterUpdateResponse,
    TailscaleSubnetRouterRetrieveResponse,
)
from telnyx.pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTailscaleSubnetRouters:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        tailscale_subnet_router = client.tailscale_subnet_routers.create(
            advertised_routes=["172.27.0.0/24"],
            auth_key="tskey-auth-k1AbCdEfGh2IjKlMnOpQrStUv",
            name="tailnet-ashburn",
            network_id="0de011ae-ee53-4df4-ba96-754728eb5aad",
            region_code="ashburn-va",
        )
        assert_matches_type(TailscaleSubnetRouterCreateResponse, tailscale_subnet_router, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.tailscale_subnet_routers.with_raw_response.create(
            advertised_routes=["172.27.0.0/24"],
            auth_key="tskey-auth-k1AbCdEfGh2IjKlMnOpQrStUv",
            name="tailnet-ashburn",
            network_id="0de011ae-ee53-4df4-ba96-754728eb5aad",
            region_code="ashburn-va",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tailscale_subnet_router = response.parse()
        assert_matches_type(TailscaleSubnetRouterCreateResponse, tailscale_subnet_router, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.tailscale_subnet_routers.with_streaming_response.create(
            advertised_routes=["172.27.0.0/24"],
            auth_key="tskey-auth-k1AbCdEfGh2IjKlMnOpQrStUv",
            name="tailnet-ashburn",
            network_id="0de011ae-ee53-4df4-ba96-754728eb5aad",
            region_code="ashburn-va",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tailscale_subnet_router = response.parse()
            assert_matches_type(TailscaleSubnetRouterCreateResponse, tailscale_subnet_router, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        tailscale_subnet_router = client.tailscale_subnet_routers.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(TailscaleSubnetRouterRetrieveResponse, tailscale_subnet_router, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.tailscale_subnet_routers.with_raw_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tailscale_subnet_router = response.parse()
        assert_matches_type(TailscaleSubnetRouterRetrieveResponse, tailscale_subnet_router, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.tailscale_subnet_routers.with_streaming_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tailscale_subnet_router = response.parse()
            assert_matches_type(TailscaleSubnetRouterRetrieveResponse, tailscale_subnet_router, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tailscale_subnet_routers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        tailscale_subnet_router = client.tailscale_subnet_routers.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(TailscaleSubnetRouterUpdateResponse, tailscale_subnet_router, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        tailscale_subnet_router = client.tailscale_subnet_routers.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            advertised_routes=["172.27.0.0/24", "172.27.1.0/24"],
            auth_key="tskey-auth-k1AbCdEfGh2IjKlMnOpQrStUv",
            name="tailnet-ashburn",
        )
        assert_matches_type(TailscaleSubnetRouterUpdateResponse, tailscale_subnet_router, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.tailscale_subnet_routers.with_raw_response.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tailscale_subnet_router = response.parse()
        assert_matches_type(TailscaleSubnetRouterUpdateResponse, tailscale_subnet_router, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.tailscale_subnet_routers.with_streaming_response.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tailscale_subnet_router = response.parse()
            assert_matches_type(TailscaleSubnetRouterUpdateResponse, tailscale_subnet_router, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tailscale_subnet_routers.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        tailscale_subnet_router = client.tailscale_subnet_routers.list()
        assert_matches_type(
            SyncDefaultFlatPagination[TailscaleSubnetRouter], tailscale_subnet_router, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        tailscale_subnet_router = client.tailscale_subnet_routers.list(
            filter={"network_id": "0de011ae-ee53-4df4-ba96-754728eb5aad"},
            page_number=0,
            page_size=0,
        )
        assert_matches_type(
            SyncDefaultFlatPagination[TailscaleSubnetRouter], tailscale_subnet_router, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.tailscale_subnet_routers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tailscale_subnet_router = response.parse()
        assert_matches_type(
            SyncDefaultFlatPagination[TailscaleSubnetRouter], tailscale_subnet_router, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.tailscale_subnet_routers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tailscale_subnet_router = response.parse()
            assert_matches_type(
                SyncDefaultFlatPagination[TailscaleSubnetRouter], tailscale_subnet_router, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        tailscale_subnet_router = client.tailscale_subnet_routers.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(TailscaleSubnetRouterDeleteResponse, tailscale_subnet_router, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.tailscale_subnet_routers.with_raw_response.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tailscale_subnet_router = response.parse()
        assert_matches_type(TailscaleSubnetRouterDeleteResponse, tailscale_subnet_router, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.tailscale_subnet_routers.with_streaming_response.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tailscale_subnet_router = response.parse()
            assert_matches_type(TailscaleSubnetRouterDeleteResponse, tailscale_subnet_router, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tailscale_subnet_routers.with_raw_response.delete(
                "",
            )


class TestAsyncTailscaleSubnetRouters:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        tailscale_subnet_router = await async_client.tailscale_subnet_routers.create(
            advertised_routes=["172.27.0.0/24"],
            auth_key="tskey-auth-k1AbCdEfGh2IjKlMnOpQrStUv",
            name="tailnet-ashburn",
            network_id="0de011ae-ee53-4df4-ba96-754728eb5aad",
            region_code="ashburn-va",
        )
        assert_matches_type(TailscaleSubnetRouterCreateResponse, tailscale_subnet_router, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.tailscale_subnet_routers.with_raw_response.create(
            advertised_routes=["172.27.0.0/24"],
            auth_key="tskey-auth-k1AbCdEfGh2IjKlMnOpQrStUv",
            name="tailnet-ashburn",
            network_id="0de011ae-ee53-4df4-ba96-754728eb5aad",
            region_code="ashburn-va",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tailscale_subnet_router = await response.parse()
        assert_matches_type(TailscaleSubnetRouterCreateResponse, tailscale_subnet_router, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.tailscale_subnet_routers.with_streaming_response.create(
            advertised_routes=["172.27.0.0/24"],
            auth_key="tskey-auth-k1AbCdEfGh2IjKlMnOpQrStUv",
            name="tailnet-ashburn",
            network_id="0de011ae-ee53-4df4-ba96-754728eb5aad",
            region_code="ashburn-va",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tailscale_subnet_router = await response.parse()
            assert_matches_type(TailscaleSubnetRouterCreateResponse, tailscale_subnet_router, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        tailscale_subnet_router = await async_client.tailscale_subnet_routers.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(TailscaleSubnetRouterRetrieveResponse, tailscale_subnet_router, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.tailscale_subnet_routers.with_raw_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tailscale_subnet_router = await response.parse()
        assert_matches_type(TailscaleSubnetRouterRetrieveResponse, tailscale_subnet_router, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.tailscale_subnet_routers.with_streaming_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tailscale_subnet_router = await response.parse()
            assert_matches_type(TailscaleSubnetRouterRetrieveResponse, tailscale_subnet_router, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tailscale_subnet_routers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        tailscale_subnet_router = await async_client.tailscale_subnet_routers.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(TailscaleSubnetRouterUpdateResponse, tailscale_subnet_router, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        tailscale_subnet_router = await async_client.tailscale_subnet_routers.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            advertised_routes=["172.27.0.0/24", "172.27.1.0/24"],
            auth_key="tskey-auth-k1AbCdEfGh2IjKlMnOpQrStUv",
            name="tailnet-ashburn",
        )
        assert_matches_type(TailscaleSubnetRouterUpdateResponse, tailscale_subnet_router, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.tailscale_subnet_routers.with_raw_response.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tailscale_subnet_router = await response.parse()
        assert_matches_type(TailscaleSubnetRouterUpdateResponse, tailscale_subnet_router, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.tailscale_subnet_routers.with_streaming_response.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tailscale_subnet_router = await response.parse()
            assert_matches_type(TailscaleSubnetRouterUpdateResponse, tailscale_subnet_router, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tailscale_subnet_routers.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        tailscale_subnet_router = await async_client.tailscale_subnet_routers.list()
        assert_matches_type(
            AsyncDefaultFlatPagination[TailscaleSubnetRouter], tailscale_subnet_router, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        tailscale_subnet_router = await async_client.tailscale_subnet_routers.list(
            filter={"network_id": "0de011ae-ee53-4df4-ba96-754728eb5aad"},
            page_number=0,
            page_size=0,
        )
        assert_matches_type(
            AsyncDefaultFlatPagination[TailscaleSubnetRouter], tailscale_subnet_router, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.tailscale_subnet_routers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tailscale_subnet_router = await response.parse()
        assert_matches_type(
            AsyncDefaultFlatPagination[TailscaleSubnetRouter], tailscale_subnet_router, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.tailscale_subnet_routers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tailscale_subnet_router = await response.parse()
            assert_matches_type(
                AsyncDefaultFlatPagination[TailscaleSubnetRouter], tailscale_subnet_router, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        tailscale_subnet_router = await async_client.tailscale_subnet_routers.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(TailscaleSubnetRouterDeleteResponse, tailscale_subnet_router, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.tailscale_subnet_routers.with_raw_response.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tailscale_subnet_router = await response.parse()
        assert_matches_type(TailscaleSubnetRouterDeleteResponse, tailscale_subnet_router, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.tailscale_subnet_routers.with_streaming_response.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tailscale_subnet_router = await response.parse()
            assert_matches_type(TailscaleSubnetRouterDeleteResponse, tailscale_subnet_router, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tailscale_subnet_routers.with_raw_response.delete(
                "",
            )

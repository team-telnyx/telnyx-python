# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    NetworkRouteListResponse,
    NetworkRouteCreateResponse,
    NetworkRouteRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNetworkRoutes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        network_route = client.network_routes.create(
            cidr="10.20.0.0/16",
            network_id="91446ee3-5b1c-4f0e-8d2a-6c7e9b0a1f24",
            next_hop={
                "id": "62d438d2-8a51-4c5e-9d0c-1f6b2a7e4c39",
                "type": "tunnel",
            },
        )
        assert_matches_type(NetworkRouteCreateResponse, network_route, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.network_routes.with_raw_response.create(
            cidr="10.20.0.0/16",
            network_id="91446ee3-5b1c-4f0e-8d2a-6c7e9b0a1f24",
            next_hop={
                "id": "62d438d2-8a51-4c5e-9d0c-1f6b2a7e4c39",
                "type": "tunnel",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network_route = response.parse()
        assert_matches_type(NetworkRouteCreateResponse, network_route, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.network_routes.with_streaming_response.create(
            cidr="10.20.0.0/16",
            network_id="91446ee3-5b1c-4f0e-8d2a-6c7e9b0a1f24",
            next_hop={
                "id": "62d438d2-8a51-4c5e-9d0c-1f6b2a7e4c39",
                "type": "tunnel",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network_route = response.parse()
            assert_matches_type(NetworkRouteCreateResponse, network_route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        network_route = client.network_routes.retrieve(
            "e8a2c5d0-3f7b-4a19-b6d2-9c1e0f8a7b53",
        )
        assert_matches_type(NetworkRouteRetrieveResponse, network_route, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.network_routes.with_raw_response.retrieve(
            "e8a2c5d0-3f7b-4a19-b6d2-9c1e0f8a7b53",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network_route = response.parse()
        assert_matches_type(NetworkRouteRetrieveResponse, network_route, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.network_routes.with_streaming_response.retrieve(
            "e8a2c5d0-3f7b-4a19-b6d2-9c1e0f8a7b53",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network_route = response.parse()
            assert_matches_type(NetworkRouteRetrieveResponse, network_route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.network_routes.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        network_route = client.network_routes.list(
            filter={"network_id": "91446ee3-5b1c-4f0e-8d2a-6c7e9b0a1f24"},
        )
        assert_matches_type(NetworkRouteListResponse, network_route, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        network_route = client.network_routes.list(
            filter={
                "network_id": "91446ee3-5b1c-4f0e-8d2a-6c7e9b0a1f24",
                "cidr": "10.20.0.0/16",
                "next_hop_type": "tunnel",
                "origin": "static",
                "status": "active",
            },
            page={
                "after": "after",
                "limit": 1,
            },
            sort="-created_at",
        )
        assert_matches_type(NetworkRouteListResponse, network_route, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.network_routes.with_raw_response.list(
            filter={"network_id": "91446ee3-5b1c-4f0e-8d2a-6c7e9b0a1f24"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network_route = response.parse()
        assert_matches_type(NetworkRouteListResponse, network_route, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.network_routes.with_streaming_response.list(
            filter={"network_id": "91446ee3-5b1c-4f0e-8d2a-6c7e9b0a1f24"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network_route = response.parse()
            assert_matches_type(NetworkRouteListResponse, network_route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        network_route = client.network_routes.delete(
            "e8a2c5d0-3f7b-4a19-b6d2-9c1e0f8a7b53",
        )
        assert network_route is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.network_routes.with_raw_response.delete(
            "e8a2c5d0-3f7b-4a19-b6d2-9c1e0f8a7b53",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network_route = response.parse()
        assert network_route is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.network_routes.with_streaming_response.delete(
            "e8a2c5d0-3f7b-4a19-b6d2-9c1e0f8a7b53",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network_route = response.parse()
            assert network_route is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.network_routes.with_raw_response.delete(
                "",
            )


class TestAsyncNetworkRoutes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        network_route = await async_client.network_routes.create(
            cidr="10.20.0.0/16",
            network_id="91446ee3-5b1c-4f0e-8d2a-6c7e9b0a1f24",
            next_hop={
                "id": "62d438d2-8a51-4c5e-9d0c-1f6b2a7e4c39",
                "type": "tunnel",
            },
        )
        assert_matches_type(NetworkRouteCreateResponse, network_route, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.network_routes.with_raw_response.create(
            cidr="10.20.0.0/16",
            network_id="91446ee3-5b1c-4f0e-8d2a-6c7e9b0a1f24",
            next_hop={
                "id": "62d438d2-8a51-4c5e-9d0c-1f6b2a7e4c39",
                "type": "tunnel",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network_route = await response.parse()
        assert_matches_type(NetworkRouteCreateResponse, network_route, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.network_routes.with_streaming_response.create(
            cidr="10.20.0.0/16",
            network_id="91446ee3-5b1c-4f0e-8d2a-6c7e9b0a1f24",
            next_hop={
                "id": "62d438d2-8a51-4c5e-9d0c-1f6b2a7e4c39",
                "type": "tunnel",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network_route = await response.parse()
            assert_matches_type(NetworkRouteCreateResponse, network_route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        network_route = await async_client.network_routes.retrieve(
            "e8a2c5d0-3f7b-4a19-b6d2-9c1e0f8a7b53",
        )
        assert_matches_type(NetworkRouteRetrieveResponse, network_route, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.network_routes.with_raw_response.retrieve(
            "e8a2c5d0-3f7b-4a19-b6d2-9c1e0f8a7b53",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network_route = await response.parse()
        assert_matches_type(NetworkRouteRetrieveResponse, network_route, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.network_routes.with_streaming_response.retrieve(
            "e8a2c5d0-3f7b-4a19-b6d2-9c1e0f8a7b53",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network_route = await response.parse()
            assert_matches_type(NetworkRouteRetrieveResponse, network_route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.network_routes.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        network_route = await async_client.network_routes.list(
            filter={"network_id": "91446ee3-5b1c-4f0e-8d2a-6c7e9b0a1f24"},
        )
        assert_matches_type(NetworkRouteListResponse, network_route, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        network_route = await async_client.network_routes.list(
            filter={
                "network_id": "91446ee3-5b1c-4f0e-8d2a-6c7e9b0a1f24",
                "cidr": "10.20.0.0/16",
                "next_hop_type": "tunnel",
                "origin": "static",
                "status": "active",
            },
            page={
                "after": "after",
                "limit": 1,
            },
            sort="-created_at",
        )
        assert_matches_type(NetworkRouteListResponse, network_route, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.network_routes.with_raw_response.list(
            filter={"network_id": "91446ee3-5b1c-4f0e-8d2a-6c7e9b0a1f24"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network_route = await response.parse()
        assert_matches_type(NetworkRouteListResponse, network_route, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.network_routes.with_streaming_response.list(
            filter={"network_id": "91446ee3-5b1c-4f0e-8d2a-6c7e9b0a1f24"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network_route = await response.parse()
            assert_matches_type(NetworkRouteListResponse, network_route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        network_route = await async_client.network_routes.delete(
            "e8a2c5d0-3f7b-4a19-b6d2-9c1e0f8a7b53",
        )
        assert network_route is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.network_routes.with_raw_response.delete(
            "e8a2c5d0-3f7b-4a19-b6d2-9c1e0f8a7b53",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network_route = await response.parse()
        assert network_route is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.network_routes.with_streaming_response.delete(
            "e8a2c5d0-3f7b-4a19-b6d2-9c1e0f8a7b53",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network_route = await response.parse()
            assert network_route is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.network_routes.with_raw_response.delete(
                "",
            )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    VirtualCrossConnectListResponse,
    VirtualCrossConnectCreateResponse,
    VirtualCrossConnectDeleteResponse,
    VirtualCrossConnectUpdateResponse,
    VirtualCrossConnectRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVirtualCrossConnects:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        virtual_cross_connect = client.virtual_cross_connects.create(
            bgp_asn=1234,
            cloud_provider="aws",
            cloud_provider_region="us-east-1",
            network_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            primary_cloud_account_id="123456789012",
            region_code="ashburn-va",
        )
        assert_matches_type(VirtualCrossConnectCreateResponse, virtual_cross_connect, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        virtual_cross_connect = client.virtual_cross_connects.create(
            bgp_asn=1234,
            cloud_provider="aws",
            cloud_provider_region="us-east-1",
            network_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            primary_cloud_account_id="123456789012",
            region_code="ashburn-va",
            bandwidth_mbps=50,
            name="test interface",
            primary_bgp_key="yFV4wEPtPVPfDUGLWiyQzwga",
            primary_cloud_ip="169.254.0.2",
            primary_telnyx_ip="169.254.0.1",
            secondary_bgp_key="ge1lONeK9RcA83uuWaw9DvZy",
            secondary_cloud_account_id="",
            secondary_cloud_ip="169.254.0.4",
            secondary_telnyx_ip="169.254.0.3",
        )
        assert_matches_type(VirtualCrossConnectCreateResponse, virtual_cross_connect, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.virtual_cross_connects.with_raw_response.create(
            bgp_asn=1234,
            cloud_provider="aws",
            cloud_provider_region="us-east-1",
            network_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            primary_cloud_account_id="123456789012",
            region_code="ashburn-va",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_cross_connect = response.parse()
        assert_matches_type(VirtualCrossConnectCreateResponse, virtual_cross_connect, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.virtual_cross_connects.with_streaming_response.create(
            bgp_asn=1234,
            cloud_provider="aws",
            cloud_provider_region="us-east-1",
            network_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            primary_cloud_account_id="123456789012",
            region_code="ashburn-va",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            virtual_cross_connect = response.parse()
            assert_matches_type(VirtualCrossConnectCreateResponse, virtual_cross_connect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        virtual_cross_connect = client.virtual_cross_connects.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(VirtualCrossConnectRetrieveResponse, virtual_cross_connect, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.virtual_cross_connects.with_raw_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_cross_connect = response.parse()
        assert_matches_type(VirtualCrossConnectRetrieveResponse, virtual_cross_connect, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.virtual_cross_connects.with_streaming_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            virtual_cross_connect = response.parse()
            assert_matches_type(VirtualCrossConnectRetrieveResponse, virtual_cross_connect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.virtual_cross_connects.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        virtual_cross_connect = client.virtual_cross_connects.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(VirtualCrossConnectUpdateResponse, virtual_cross_connect, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        virtual_cross_connect = client.virtual_cross_connects.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            primary_cloud_ip="169.254.0.2",
            primary_enabled=True,
            primary_routing_announcement=False,
            secondary_cloud_ip="169.254.0.4",
            secondary_enabled=True,
            secondary_routing_announcement=False,
        )
        assert_matches_type(VirtualCrossConnectUpdateResponse, virtual_cross_connect, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.virtual_cross_connects.with_raw_response.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_cross_connect = response.parse()
        assert_matches_type(VirtualCrossConnectUpdateResponse, virtual_cross_connect, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.virtual_cross_connects.with_streaming_response.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            virtual_cross_connect = response.parse()
            assert_matches_type(VirtualCrossConnectUpdateResponse, virtual_cross_connect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.virtual_cross_connects.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        virtual_cross_connect = client.virtual_cross_connects.list()
        assert_matches_type(VirtualCrossConnectListResponse, virtual_cross_connect, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        virtual_cross_connect = client.virtual_cross_connects.list(
            filter={"network_id": "6a09cdc3-8948-47f0-aa62-74ac943d6c58"},
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(VirtualCrossConnectListResponse, virtual_cross_connect, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.virtual_cross_connects.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_cross_connect = response.parse()
        assert_matches_type(VirtualCrossConnectListResponse, virtual_cross_connect, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.virtual_cross_connects.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            virtual_cross_connect = response.parse()
            assert_matches_type(VirtualCrossConnectListResponse, virtual_cross_connect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        virtual_cross_connect = client.virtual_cross_connects.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(VirtualCrossConnectDeleteResponse, virtual_cross_connect, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.virtual_cross_connects.with_raw_response.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_cross_connect = response.parse()
        assert_matches_type(VirtualCrossConnectDeleteResponse, virtual_cross_connect, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.virtual_cross_connects.with_streaming_response.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            virtual_cross_connect = response.parse()
            assert_matches_type(VirtualCrossConnectDeleteResponse, virtual_cross_connect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.virtual_cross_connects.with_raw_response.delete(
                "",
            )


class TestAsyncVirtualCrossConnects:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        virtual_cross_connect = await async_client.virtual_cross_connects.create(
            bgp_asn=1234,
            cloud_provider="aws",
            cloud_provider_region="us-east-1",
            network_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            primary_cloud_account_id="123456789012",
            region_code="ashburn-va",
        )
        assert_matches_type(VirtualCrossConnectCreateResponse, virtual_cross_connect, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        virtual_cross_connect = await async_client.virtual_cross_connects.create(
            bgp_asn=1234,
            cloud_provider="aws",
            cloud_provider_region="us-east-1",
            network_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            primary_cloud_account_id="123456789012",
            region_code="ashburn-va",
            bandwidth_mbps=50,
            name="test interface",
            primary_bgp_key="yFV4wEPtPVPfDUGLWiyQzwga",
            primary_cloud_ip="169.254.0.2",
            primary_telnyx_ip="169.254.0.1",
            secondary_bgp_key="ge1lONeK9RcA83uuWaw9DvZy",
            secondary_cloud_account_id="",
            secondary_cloud_ip="169.254.0.4",
            secondary_telnyx_ip="169.254.0.3",
        )
        assert_matches_type(VirtualCrossConnectCreateResponse, virtual_cross_connect, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.virtual_cross_connects.with_raw_response.create(
            bgp_asn=1234,
            cloud_provider="aws",
            cloud_provider_region="us-east-1",
            network_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            primary_cloud_account_id="123456789012",
            region_code="ashburn-va",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_cross_connect = await response.parse()
        assert_matches_type(VirtualCrossConnectCreateResponse, virtual_cross_connect, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.virtual_cross_connects.with_streaming_response.create(
            bgp_asn=1234,
            cloud_provider="aws",
            cloud_provider_region="us-east-1",
            network_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            primary_cloud_account_id="123456789012",
            region_code="ashburn-va",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            virtual_cross_connect = await response.parse()
            assert_matches_type(VirtualCrossConnectCreateResponse, virtual_cross_connect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        virtual_cross_connect = await async_client.virtual_cross_connects.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(VirtualCrossConnectRetrieveResponse, virtual_cross_connect, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.virtual_cross_connects.with_raw_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_cross_connect = await response.parse()
        assert_matches_type(VirtualCrossConnectRetrieveResponse, virtual_cross_connect, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.virtual_cross_connects.with_streaming_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            virtual_cross_connect = await response.parse()
            assert_matches_type(VirtualCrossConnectRetrieveResponse, virtual_cross_connect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.virtual_cross_connects.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        virtual_cross_connect = await async_client.virtual_cross_connects.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(VirtualCrossConnectUpdateResponse, virtual_cross_connect, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        virtual_cross_connect = await async_client.virtual_cross_connects.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            primary_cloud_ip="169.254.0.2",
            primary_enabled=True,
            primary_routing_announcement=False,
            secondary_cloud_ip="169.254.0.4",
            secondary_enabled=True,
            secondary_routing_announcement=False,
        )
        assert_matches_type(VirtualCrossConnectUpdateResponse, virtual_cross_connect, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.virtual_cross_connects.with_raw_response.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_cross_connect = await response.parse()
        assert_matches_type(VirtualCrossConnectUpdateResponse, virtual_cross_connect, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.virtual_cross_connects.with_streaming_response.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            virtual_cross_connect = await response.parse()
            assert_matches_type(VirtualCrossConnectUpdateResponse, virtual_cross_connect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.virtual_cross_connects.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        virtual_cross_connect = await async_client.virtual_cross_connects.list()
        assert_matches_type(VirtualCrossConnectListResponse, virtual_cross_connect, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        virtual_cross_connect = await async_client.virtual_cross_connects.list(
            filter={"network_id": "6a09cdc3-8948-47f0-aa62-74ac943d6c58"},
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(VirtualCrossConnectListResponse, virtual_cross_connect, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.virtual_cross_connects.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_cross_connect = await response.parse()
        assert_matches_type(VirtualCrossConnectListResponse, virtual_cross_connect, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.virtual_cross_connects.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            virtual_cross_connect = await response.parse()
            assert_matches_type(VirtualCrossConnectListResponse, virtual_cross_connect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        virtual_cross_connect = await async_client.virtual_cross_connects.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(VirtualCrossConnectDeleteResponse, virtual_cross_connect, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.virtual_cross_connects.with_raw_response.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_cross_connect = await response.parse()
        assert_matches_type(VirtualCrossConnectDeleteResponse, virtual_cross_connect, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.virtual_cross_connects.with_streaming_response.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            virtual_cross_connect = await response.parse()
            assert_matches_type(VirtualCrossConnectDeleteResponse, virtual_cross_connect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.virtual_cross_connects.with_raw_response.delete(
                "",
            )

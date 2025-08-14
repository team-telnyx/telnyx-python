# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    WireguardPeerListResponse,
    WireguardPeerCreateResponse,
    WireguardPeerDeleteResponse,
    WireguardPeerUpdateResponse,
    WireguardPeerRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWireguardPeers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        wireguard_peer = client.wireguard_peers.create(
            wireguard_interface_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(WireguardPeerCreateResponse, wireguard_peer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        wireguard_peer = client.wireguard_peers.create(
            wireguard_interface_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            public_key="qF4EqlZq+5JL2IKYY8ij49daYyfKVhevJrcDxdqC8GU=",
        )
        assert_matches_type(WireguardPeerCreateResponse, wireguard_peer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.wireguard_peers.with_raw_response.create(
            wireguard_interface_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wireguard_peer = response.parse()
        assert_matches_type(WireguardPeerCreateResponse, wireguard_peer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.wireguard_peers.with_streaming_response.create(
            wireguard_interface_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wireguard_peer = response.parse()
            assert_matches_type(WireguardPeerCreateResponse, wireguard_peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        wireguard_peer = client.wireguard_peers.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(WireguardPeerRetrieveResponse, wireguard_peer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.wireguard_peers.with_raw_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wireguard_peer = response.parse()
        assert_matches_type(WireguardPeerRetrieveResponse, wireguard_peer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.wireguard_peers.with_streaming_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wireguard_peer = response.parse()
            assert_matches_type(WireguardPeerRetrieveResponse, wireguard_peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.wireguard_peers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        wireguard_peer = client.wireguard_peers.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(WireguardPeerUpdateResponse, wireguard_peer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        wireguard_peer = client.wireguard_peers.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            public_key="qF4EqlZq+5JL2IKYY8ij49daYyfKVhevJrcDxdqC8GU=",
        )
        assert_matches_type(WireguardPeerUpdateResponse, wireguard_peer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.wireguard_peers.with_raw_response.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wireguard_peer = response.parse()
        assert_matches_type(WireguardPeerUpdateResponse, wireguard_peer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.wireguard_peers.with_streaming_response.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wireguard_peer = response.parse()
            assert_matches_type(WireguardPeerUpdateResponse, wireguard_peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.wireguard_peers.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        wireguard_peer = client.wireguard_peers.list()
        assert_matches_type(WireguardPeerListResponse, wireguard_peer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        wireguard_peer = client.wireguard_peers.list(
            filter={"wireguard_interface_id": "6a09cdc3-8948-47f0-aa62-74ac943d6c58"},
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(WireguardPeerListResponse, wireguard_peer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.wireguard_peers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wireguard_peer = response.parse()
        assert_matches_type(WireguardPeerListResponse, wireguard_peer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.wireguard_peers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wireguard_peer = response.parse()
            assert_matches_type(WireguardPeerListResponse, wireguard_peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        wireguard_peer = client.wireguard_peers.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(WireguardPeerDeleteResponse, wireguard_peer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.wireguard_peers.with_raw_response.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wireguard_peer = response.parse()
        assert_matches_type(WireguardPeerDeleteResponse, wireguard_peer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.wireguard_peers.with_streaming_response.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wireguard_peer = response.parse()
            assert_matches_type(WireguardPeerDeleteResponse, wireguard_peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.wireguard_peers.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_config(self, client: Telnyx) -> None:
        wireguard_peer = client.wireguard_peers.retrieve_config(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(str, wireguard_peer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_config(self, client: Telnyx) -> None:
        response = client.wireguard_peers.with_raw_response.retrieve_config(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wireguard_peer = response.parse()
        assert_matches_type(str, wireguard_peer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_config(self, client: Telnyx) -> None:
        with client.wireguard_peers.with_streaming_response.retrieve_config(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wireguard_peer = response.parse()
            assert_matches_type(str, wireguard_peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_config(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.wireguard_peers.with_raw_response.retrieve_config(
                "",
            )


class TestAsyncWireguardPeers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        wireguard_peer = await async_client.wireguard_peers.create(
            wireguard_interface_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(WireguardPeerCreateResponse, wireguard_peer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        wireguard_peer = await async_client.wireguard_peers.create(
            wireguard_interface_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            public_key="qF4EqlZq+5JL2IKYY8ij49daYyfKVhevJrcDxdqC8GU=",
        )
        assert_matches_type(WireguardPeerCreateResponse, wireguard_peer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.wireguard_peers.with_raw_response.create(
            wireguard_interface_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wireguard_peer = await response.parse()
        assert_matches_type(WireguardPeerCreateResponse, wireguard_peer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.wireguard_peers.with_streaming_response.create(
            wireguard_interface_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wireguard_peer = await response.parse()
            assert_matches_type(WireguardPeerCreateResponse, wireguard_peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        wireguard_peer = await async_client.wireguard_peers.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(WireguardPeerRetrieveResponse, wireguard_peer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.wireguard_peers.with_raw_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wireguard_peer = await response.parse()
        assert_matches_type(WireguardPeerRetrieveResponse, wireguard_peer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.wireguard_peers.with_streaming_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wireguard_peer = await response.parse()
            assert_matches_type(WireguardPeerRetrieveResponse, wireguard_peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.wireguard_peers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        wireguard_peer = await async_client.wireguard_peers.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(WireguardPeerUpdateResponse, wireguard_peer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        wireguard_peer = await async_client.wireguard_peers.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            public_key="qF4EqlZq+5JL2IKYY8ij49daYyfKVhevJrcDxdqC8GU=",
        )
        assert_matches_type(WireguardPeerUpdateResponse, wireguard_peer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.wireguard_peers.with_raw_response.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wireguard_peer = await response.parse()
        assert_matches_type(WireguardPeerUpdateResponse, wireguard_peer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.wireguard_peers.with_streaming_response.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wireguard_peer = await response.parse()
            assert_matches_type(WireguardPeerUpdateResponse, wireguard_peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.wireguard_peers.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        wireguard_peer = await async_client.wireguard_peers.list()
        assert_matches_type(WireguardPeerListResponse, wireguard_peer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        wireguard_peer = await async_client.wireguard_peers.list(
            filter={"wireguard_interface_id": "6a09cdc3-8948-47f0-aa62-74ac943d6c58"},
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(WireguardPeerListResponse, wireguard_peer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.wireguard_peers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wireguard_peer = await response.parse()
        assert_matches_type(WireguardPeerListResponse, wireguard_peer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.wireguard_peers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wireguard_peer = await response.parse()
            assert_matches_type(WireguardPeerListResponse, wireguard_peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        wireguard_peer = await async_client.wireguard_peers.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(WireguardPeerDeleteResponse, wireguard_peer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.wireguard_peers.with_raw_response.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wireguard_peer = await response.parse()
        assert_matches_type(WireguardPeerDeleteResponse, wireguard_peer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.wireguard_peers.with_streaming_response.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wireguard_peer = await response.parse()
            assert_matches_type(WireguardPeerDeleteResponse, wireguard_peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.wireguard_peers.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_config(self, async_client: AsyncTelnyx) -> None:
        wireguard_peer = await async_client.wireguard_peers.retrieve_config(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(str, wireguard_peer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_config(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.wireguard_peers.with_raw_response.retrieve_config(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wireguard_peer = await response.parse()
        assert_matches_type(str, wireguard_peer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_config(self, async_client: AsyncTelnyx) -> None:
        async with async_client.wireguard_peers.with_streaming_response.retrieve_config(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wireguard_peer = await response.parse()
            assert_matches_type(str, wireguard_peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_config(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.wireguard_peers.with_raw_response.retrieve_config(
                "",
            )

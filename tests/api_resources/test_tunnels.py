# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    TunnelListResponse,
    TunnelCreateResponse,
    TunnelRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTunnels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        tunnel = client.tunnels.create(
            name="chicago-dc",
        )
        assert_matches_type(TunnelCreateResponse, tunnel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.tunnels.with_raw_response.create(
            name="chicago-dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tunnel = response.parse()
        assert_matches_type(TunnelCreateResponse, tunnel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.tunnels.with_streaming_response.create(
            name="chicago-dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tunnel = response.parse()
            assert_matches_type(TunnelCreateResponse, tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        tunnel = client.tunnels.retrieve(
            "62d438d2-8a51-4c5e-9d0c-1f6b2a7e4c39",
        )
        assert_matches_type(TunnelRetrieveResponse, tunnel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.tunnels.with_raw_response.retrieve(
            "62d438d2-8a51-4c5e-9d0c-1f6b2a7e4c39",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tunnel = response.parse()
        assert_matches_type(TunnelRetrieveResponse, tunnel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.tunnels.with_streaming_response.retrieve(
            "62d438d2-8a51-4c5e-9d0c-1f6b2a7e4c39",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tunnel = response.parse()
            assert_matches_type(TunnelRetrieveResponse, tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tunnels.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        tunnel = client.tunnels.list()
        assert_matches_type(TunnelListResponse, tunnel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        tunnel = client.tunnels.list(
            filter={
                "name": "chicago-dc",
                "status": "healthy",
            },
            page={
                "after": "after",
                "limit": 1,
            },
            sort="-created_at",
        )
        assert_matches_type(TunnelListResponse, tunnel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.tunnels.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tunnel = response.parse()
        assert_matches_type(TunnelListResponse, tunnel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.tunnels.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tunnel = response.parse()
            assert_matches_type(TunnelListResponse, tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        tunnel = client.tunnels.delete(
            "62d438d2-8a51-4c5e-9d0c-1f6b2a7e4c39",
        )
        assert tunnel is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.tunnels.with_raw_response.delete(
            "62d438d2-8a51-4c5e-9d0c-1f6b2a7e4c39",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tunnel = response.parse()
        assert tunnel is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.tunnels.with_streaming_response.delete(
            "62d438d2-8a51-4c5e-9d0c-1f6b2a7e4c39",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tunnel = response.parse()
            assert tunnel is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tunnels.with_raw_response.delete(
                "",
            )


class TestAsyncTunnels:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        tunnel = await async_client.tunnels.create(
            name="chicago-dc",
        )
        assert_matches_type(TunnelCreateResponse, tunnel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.tunnels.with_raw_response.create(
            name="chicago-dc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tunnel = await response.parse()
        assert_matches_type(TunnelCreateResponse, tunnel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.tunnels.with_streaming_response.create(
            name="chicago-dc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tunnel = await response.parse()
            assert_matches_type(TunnelCreateResponse, tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        tunnel = await async_client.tunnels.retrieve(
            "62d438d2-8a51-4c5e-9d0c-1f6b2a7e4c39",
        )
        assert_matches_type(TunnelRetrieveResponse, tunnel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.tunnels.with_raw_response.retrieve(
            "62d438d2-8a51-4c5e-9d0c-1f6b2a7e4c39",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tunnel = await response.parse()
        assert_matches_type(TunnelRetrieveResponse, tunnel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.tunnels.with_streaming_response.retrieve(
            "62d438d2-8a51-4c5e-9d0c-1f6b2a7e4c39",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tunnel = await response.parse()
            assert_matches_type(TunnelRetrieveResponse, tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tunnels.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        tunnel = await async_client.tunnels.list()
        assert_matches_type(TunnelListResponse, tunnel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        tunnel = await async_client.tunnels.list(
            filter={
                "name": "chicago-dc",
                "status": "healthy",
            },
            page={
                "after": "after",
                "limit": 1,
            },
            sort="-created_at",
        )
        assert_matches_type(TunnelListResponse, tunnel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.tunnels.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tunnel = await response.parse()
        assert_matches_type(TunnelListResponse, tunnel, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.tunnels.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tunnel = await response.parse()
            assert_matches_type(TunnelListResponse, tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        tunnel = await async_client.tunnels.delete(
            "62d438d2-8a51-4c5e-9d0c-1f6b2a7e4c39",
        )
        assert tunnel is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.tunnels.with_raw_response.delete(
            "62d438d2-8a51-4c5e-9d0c-1f6b2a7e4c39",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tunnel = await response.parse()
        assert tunnel is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.tunnels.with_streaming_response.delete(
            "62d438d2-8a51-4c5e-9d0c-1f6b2a7e4c39",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tunnel = await response.parse()
            assert tunnel is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tunnels.with_raw_response.delete(
                "",
            )

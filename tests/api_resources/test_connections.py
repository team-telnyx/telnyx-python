# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    ConnectionListResponse,
    ConnectionRetrieveResponse,
    ConnectionListActiveCallsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConnections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        connection = client.connections.retrieve(
            "id",
        )
        assert_matches_type(ConnectionRetrieveResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.connections.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(ConnectionRetrieveResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.connections.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(ConnectionRetrieveResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.connections.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        connection = client.connections.list()
        assert_matches_type(ConnectionListResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        connection = client.connections.list(
            filter={
                "connection_name": {"contains": "contains"},
                "fqdn": "fqdn",
                "outbound_voice_profile_id": "outbound_voice_profile_id",
            },
            page={
                "number": 1,
                "size": 1,
            },
            sort="connection_name",
        )
        assert_matches_type(ConnectionListResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.connections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(ConnectionListResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.connections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(ConnectionListResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_active_calls(self, client: Telnyx) -> None:
        connection = client.connections.list_active_calls(
            connection_id="1293384261075731461",
        )
        assert_matches_type(ConnectionListActiveCallsResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_active_calls_with_all_params(self, client: Telnyx) -> None:
        connection = client.connections.list_active_calls(
            connection_id="1293384261075731461",
            page={
                "after": "after",
                "before": "before",
                "limit": 1,
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(ConnectionListActiveCallsResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_active_calls(self, client: Telnyx) -> None:
        response = client.connections.with_raw_response.list_active_calls(
            connection_id="1293384261075731461",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(ConnectionListActiveCallsResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_active_calls(self, client: Telnyx) -> None:
        with client.connections.with_streaming_response.list_active_calls(
            connection_id="1293384261075731461",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(ConnectionListActiveCallsResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_active_calls(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.connections.with_raw_response.list_active_calls(
                connection_id="",
            )


class TestAsyncConnections:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        connection = await async_client.connections.retrieve(
            "id",
        )
        assert_matches_type(ConnectionRetrieveResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.connections.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(ConnectionRetrieveResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.connections.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(ConnectionRetrieveResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.connections.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        connection = await async_client.connections.list()
        assert_matches_type(ConnectionListResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        connection = await async_client.connections.list(
            filter={
                "connection_name": {"contains": "contains"},
                "fqdn": "fqdn",
                "outbound_voice_profile_id": "outbound_voice_profile_id",
            },
            page={
                "number": 1,
                "size": 1,
            },
            sort="connection_name",
        )
        assert_matches_type(ConnectionListResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.connections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(ConnectionListResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.connections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(ConnectionListResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_active_calls(self, async_client: AsyncTelnyx) -> None:
        connection = await async_client.connections.list_active_calls(
            connection_id="1293384261075731461",
        )
        assert_matches_type(ConnectionListActiveCallsResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_active_calls_with_all_params(self, async_client: AsyncTelnyx) -> None:
        connection = await async_client.connections.list_active_calls(
            connection_id="1293384261075731461",
            page={
                "after": "after",
                "before": "before",
                "limit": 1,
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(ConnectionListActiveCallsResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_active_calls(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.connections.with_raw_response.list_active_calls(
            connection_id="1293384261075731461",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(ConnectionListActiveCallsResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_active_calls(self, async_client: AsyncTelnyx) -> None:
        async with async_client.connections.with_streaming_response.list_active_calls(
            connection_id="1293384261075731461",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(ConnectionListActiveCallsResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_active_calls(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.connections.with_raw_response.list_active_calls(
                connection_id="",
            )

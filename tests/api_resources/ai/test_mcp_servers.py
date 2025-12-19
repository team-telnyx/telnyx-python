# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx._utils import parse_datetime
from telnyx.types.ai import (
    McpServerListResponse,
    McpServerCreateResponse,
    McpServerUpdateResponse,
    McpServerRetrieveResponse,
)
from telnyx.pagination import SyncDefaultFlatPaginationTopLevelArray, AsyncDefaultFlatPaginationTopLevelArray

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMcpServers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        mcp_server = client.ai.mcp_servers.create(
            name="name",
            type="type",
            url="url",
        )
        assert_matches_type(McpServerCreateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        mcp_server = client.ai.mcp_servers.create(
            name="name",
            type="type",
            url="url",
            allowed_tools=["string"],
            api_key_ref="api_key_ref",
        )
        assert_matches_type(McpServerCreateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.ai.mcp_servers.with_raw_response.create(
            name="name",
            type="type",
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = response.parse()
        assert_matches_type(McpServerCreateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.ai.mcp_servers.with_streaming_response.create(
            name="name",
            type="type",
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = response.parse()
            assert_matches_type(McpServerCreateResponse, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        mcp_server = client.ai.mcp_servers.retrieve(
            "mcp_server_id",
        )
        assert_matches_type(McpServerRetrieveResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.ai.mcp_servers.with_raw_response.retrieve(
            "mcp_server_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = response.parse()
        assert_matches_type(McpServerRetrieveResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.ai.mcp_servers.with_streaming_response.retrieve(
            "mcp_server_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = response.parse()
            assert_matches_type(McpServerRetrieveResponse, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_id` but received ''"):
            client.ai.mcp_servers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        mcp_server = client.ai.mcp_servers.update(
            mcp_server_id="mcp_server_id",
        )
        assert_matches_type(McpServerUpdateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        mcp_server = client.ai.mcp_servers.update(
            mcp_server_id="mcp_server_id",
            id="id",
            allowed_tools=["string"],
            api_key_ref="api_key_ref",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            type="type",
            url="url",
        )
        assert_matches_type(McpServerUpdateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.ai.mcp_servers.with_raw_response.update(
            mcp_server_id="mcp_server_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = response.parse()
        assert_matches_type(McpServerUpdateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.ai.mcp_servers.with_streaming_response.update(
            mcp_server_id="mcp_server_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = response.parse()
            assert_matches_type(McpServerUpdateResponse, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_id` but received ''"):
            client.ai.mcp_servers.with_raw_response.update(
                mcp_server_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        mcp_server = client.ai.mcp_servers.list()
        assert_matches_type(
            SyncDefaultFlatPaginationTopLevelArray[McpServerListResponse], mcp_server, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        mcp_server = client.ai.mcp_servers.list(
            page_number=1,
            page_size=1,
            type="type",
            url="url",
        )
        assert_matches_type(
            SyncDefaultFlatPaginationTopLevelArray[McpServerListResponse], mcp_server, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.ai.mcp_servers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = response.parse()
        assert_matches_type(
            SyncDefaultFlatPaginationTopLevelArray[McpServerListResponse], mcp_server, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.ai.mcp_servers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = response.parse()
            assert_matches_type(
                SyncDefaultFlatPaginationTopLevelArray[McpServerListResponse], mcp_server, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        mcp_server = client.ai.mcp_servers.delete(
            "mcp_server_id",
        )
        assert mcp_server is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.ai.mcp_servers.with_raw_response.delete(
            "mcp_server_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = response.parse()
        assert mcp_server is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.ai.mcp_servers.with_streaming_response.delete(
            "mcp_server_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = response.parse()
            assert mcp_server is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_id` but received ''"):
            client.ai.mcp_servers.with_raw_response.delete(
                "",
            )


class TestAsyncMcpServers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        mcp_server = await async_client.ai.mcp_servers.create(
            name="name",
            type="type",
            url="url",
        )
        assert_matches_type(McpServerCreateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        mcp_server = await async_client.ai.mcp_servers.create(
            name="name",
            type="type",
            url="url",
            allowed_tools=["string"],
            api_key_ref="api_key_ref",
        )
        assert_matches_type(McpServerCreateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.mcp_servers.with_raw_response.create(
            name="name",
            type="type",
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = await response.parse()
        assert_matches_type(McpServerCreateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.mcp_servers.with_streaming_response.create(
            name="name",
            type="type",
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = await response.parse()
            assert_matches_type(McpServerCreateResponse, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        mcp_server = await async_client.ai.mcp_servers.retrieve(
            "mcp_server_id",
        )
        assert_matches_type(McpServerRetrieveResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.mcp_servers.with_raw_response.retrieve(
            "mcp_server_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = await response.parse()
        assert_matches_type(McpServerRetrieveResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.mcp_servers.with_streaming_response.retrieve(
            "mcp_server_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = await response.parse()
            assert_matches_type(McpServerRetrieveResponse, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_id` but received ''"):
            await async_client.ai.mcp_servers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        mcp_server = await async_client.ai.mcp_servers.update(
            mcp_server_id="mcp_server_id",
        )
        assert_matches_type(McpServerUpdateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        mcp_server = await async_client.ai.mcp_servers.update(
            mcp_server_id="mcp_server_id",
            id="id",
            allowed_tools=["string"],
            api_key_ref="api_key_ref",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            type="type",
            url="url",
        )
        assert_matches_type(McpServerUpdateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.mcp_servers.with_raw_response.update(
            mcp_server_id="mcp_server_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = await response.parse()
        assert_matches_type(McpServerUpdateResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.mcp_servers.with_streaming_response.update(
            mcp_server_id="mcp_server_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = await response.parse()
            assert_matches_type(McpServerUpdateResponse, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_id` but received ''"):
            await async_client.ai.mcp_servers.with_raw_response.update(
                mcp_server_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        mcp_server = await async_client.ai.mcp_servers.list()
        assert_matches_type(
            AsyncDefaultFlatPaginationTopLevelArray[McpServerListResponse], mcp_server, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        mcp_server = await async_client.ai.mcp_servers.list(
            page_number=1,
            page_size=1,
            type="type",
            url="url",
        )
        assert_matches_type(
            AsyncDefaultFlatPaginationTopLevelArray[McpServerListResponse], mcp_server, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.mcp_servers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = await response.parse()
        assert_matches_type(
            AsyncDefaultFlatPaginationTopLevelArray[McpServerListResponse], mcp_server, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.mcp_servers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = await response.parse()
            assert_matches_type(
                AsyncDefaultFlatPaginationTopLevelArray[McpServerListResponse], mcp_server, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        mcp_server = await async_client.ai.mcp_servers.delete(
            "mcp_server_id",
        )
        assert mcp_server is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.mcp_servers.with_raw_response.delete(
            "mcp_server_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = await response.parse()
        assert mcp_server is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.mcp_servers.with_streaming_response.delete(
            "mcp_server_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = await response.parse()
            assert mcp_server is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_id` but received ''"):
            await async_client.ai.mcp_servers.with_raw_response.delete(
                "",
            )

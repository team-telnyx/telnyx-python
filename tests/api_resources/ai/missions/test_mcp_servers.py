# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMcpServers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_mcp_server(self, client: Telnyx) -> None:
        mcp_server = client.ai.missions.mcp_servers.create_mcp_server(
            "mission_id",
        )
        assert_matches_type(object, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_mcp_server(self, client: Telnyx) -> None:
        response = client.ai.missions.mcp_servers.with_raw_response.create_mcp_server(
            "mission_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = response.parse()
        assert_matches_type(object, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_mcp_server(self, client: Telnyx) -> None:
        with client.ai.missions.mcp_servers.with_streaming_response.create_mcp_server(
            "mission_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = response.parse()
            assert_matches_type(object, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_mcp_server(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            client.ai.missions.mcp_servers.with_raw_response.create_mcp_server(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_mcp_server(self, client: Telnyx) -> None:
        mcp_server = client.ai.missions.mcp_servers.delete_mcp_server(
            mcp_server_id="mcp_server_id",
            mission_id="mission_id",
        )
        assert mcp_server is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_mcp_server(self, client: Telnyx) -> None:
        response = client.ai.missions.mcp_servers.with_raw_response.delete_mcp_server(
            mcp_server_id="mcp_server_id",
            mission_id="mission_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = response.parse()
        assert mcp_server is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_mcp_server(self, client: Telnyx) -> None:
        with client.ai.missions.mcp_servers.with_streaming_response.delete_mcp_server(
            mcp_server_id="mcp_server_id",
            mission_id="mission_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = response.parse()
            assert mcp_server is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_mcp_server(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            client.ai.missions.mcp_servers.with_raw_response.delete_mcp_server(
                mcp_server_id="mcp_server_id",
                mission_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_id` but received ''"):
            client.ai.missions.mcp_servers.with_raw_response.delete_mcp_server(
                mcp_server_id="",
                mission_id="mission_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_mcp_server(self, client: Telnyx) -> None:
        mcp_server = client.ai.missions.mcp_servers.get_mcp_server(
            mcp_server_id="mcp_server_id",
            mission_id="mission_id",
        )
        assert_matches_type(object, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_mcp_server(self, client: Telnyx) -> None:
        response = client.ai.missions.mcp_servers.with_raw_response.get_mcp_server(
            mcp_server_id="mcp_server_id",
            mission_id="mission_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = response.parse()
        assert_matches_type(object, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_mcp_server(self, client: Telnyx) -> None:
        with client.ai.missions.mcp_servers.with_streaming_response.get_mcp_server(
            mcp_server_id="mcp_server_id",
            mission_id="mission_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = response.parse()
            assert_matches_type(object, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_mcp_server(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            client.ai.missions.mcp_servers.with_raw_response.get_mcp_server(
                mcp_server_id="mcp_server_id",
                mission_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_id` but received ''"):
            client.ai.missions.mcp_servers.with_raw_response.get_mcp_server(
                mcp_server_id="",
                mission_id="mission_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_mcp_servers(self, client: Telnyx) -> None:
        mcp_server = client.ai.missions.mcp_servers.list_mcp_servers(
            "mission_id",
        )
        assert_matches_type(object, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_mcp_servers(self, client: Telnyx) -> None:
        response = client.ai.missions.mcp_servers.with_raw_response.list_mcp_servers(
            "mission_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = response.parse()
        assert_matches_type(object, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_mcp_servers(self, client: Telnyx) -> None:
        with client.ai.missions.mcp_servers.with_streaming_response.list_mcp_servers(
            "mission_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = response.parse()
            assert_matches_type(object, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_mcp_servers(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            client.ai.missions.mcp_servers.with_raw_response.list_mcp_servers(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_mcp_server(self, client: Telnyx) -> None:
        mcp_server = client.ai.missions.mcp_servers.update_mcp_server(
            mcp_server_id="mcp_server_id",
            mission_id="mission_id",
        )
        assert_matches_type(object, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_mcp_server(self, client: Telnyx) -> None:
        response = client.ai.missions.mcp_servers.with_raw_response.update_mcp_server(
            mcp_server_id="mcp_server_id",
            mission_id="mission_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = response.parse()
        assert_matches_type(object, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_mcp_server(self, client: Telnyx) -> None:
        with client.ai.missions.mcp_servers.with_streaming_response.update_mcp_server(
            mcp_server_id="mcp_server_id",
            mission_id="mission_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = response.parse()
            assert_matches_type(object, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_mcp_server(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            client.ai.missions.mcp_servers.with_raw_response.update_mcp_server(
                mcp_server_id="mcp_server_id",
                mission_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_id` but received ''"):
            client.ai.missions.mcp_servers.with_raw_response.update_mcp_server(
                mcp_server_id="",
                mission_id="mission_id",
            )


class TestAsyncMcpServers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_mcp_server(self, async_client: AsyncTelnyx) -> None:
        mcp_server = await async_client.ai.missions.mcp_servers.create_mcp_server(
            "mission_id",
        )
        assert_matches_type(object, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_mcp_server(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.missions.mcp_servers.with_raw_response.create_mcp_server(
            "mission_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = await response.parse()
        assert_matches_type(object, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_mcp_server(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.missions.mcp_servers.with_streaming_response.create_mcp_server(
            "mission_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = await response.parse()
            assert_matches_type(object, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_mcp_server(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            await async_client.ai.missions.mcp_servers.with_raw_response.create_mcp_server(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_mcp_server(self, async_client: AsyncTelnyx) -> None:
        mcp_server = await async_client.ai.missions.mcp_servers.delete_mcp_server(
            mcp_server_id="mcp_server_id",
            mission_id="mission_id",
        )
        assert mcp_server is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_mcp_server(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.missions.mcp_servers.with_raw_response.delete_mcp_server(
            mcp_server_id="mcp_server_id",
            mission_id="mission_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = await response.parse()
        assert mcp_server is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_mcp_server(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.missions.mcp_servers.with_streaming_response.delete_mcp_server(
            mcp_server_id="mcp_server_id",
            mission_id="mission_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = await response.parse()
            assert mcp_server is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_mcp_server(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            await async_client.ai.missions.mcp_servers.with_raw_response.delete_mcp_server(
                mcp_server_id="mcp_server_id",
                mission_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_id` but received ''"):
            await async_client.ai.missions.mcp_servers.with_raw_response.delete_mcp_server(
                mcp_server_id="",
                mission_id="mission_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_mcp_server(self, async_client: AsyncTelnyx) -> None:
        mcp_server = await async_client.ai.missions.mcp_servers.get_mcp_server(
            mcp_server_id="mcp_server_id",
            mission_id="mission_id",
        )
        assert_matches_type(object, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_mcp_server(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.missions.mcp_servers.with_raw_response.get_mcp_server(
            mcp_server_id="mcp_server_id",
            mission_id="mission_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = await response.parse()
        assert_matches_type(object, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_mcp_server(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.missions.mcp_servers.with_streaming_response.get_mcp_server(
            mcp_server_id="mcp_server_id",
            mission_id="mission_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = await response.parse()
            assert_matches_type(object, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_mcp_server(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            await async_client.ai.missions.mcp_servers.with_raw_response.get_mcp_server(
                mcp_server_id="mcp_server_id",
                mission_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_id` but received ''"):
            await async_client.ai.missions.mcp_servers.with_raw_response.get_mcp_server(
                mcp_server_id="",
                mission_id="mission_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_mcp_servers(self, async_client: AsyncTelnyx) -> None:
        mcp_server = await async_client.ai.missions.mcp_servers.list_mcp_servers(
            "mission_id",
        )
        assert_matches_type(object, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_mcp_servers(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.missions.mcp_servers.with_raw_response.list_mcp_servers(
            "mission_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = await response.parse()
        assert_matches_type(object, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_mcp_servers(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.missions.mcp_servers.with_streaming_response.list_mcp_servers(
            "mission_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = await response.parse()
            assert_matches_type(object, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_mcp_servers(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            await async_client.ai.missions.mcp_servers.with_raw_response.list_mcp_servers(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_mcp_server(self, async_client: AsyncTelnyx) -> None:
        mcp_server = await async_client.ai.missions.mcp_servers.update_mcp_server(
            mcp_server_id="mcp_server_id",
            mission_id="mission_id",
        )
        assert_matches_type(object, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_mcp_server(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.missions.mcp_servers.with_raw_response.update_mcp_server(
            mcp_server_id="mcp_server_id",
            mission_id="mission_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = await response.parse()
        assert_matches_type(object, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_mcp_server(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.missions.mcp_servers.with_streaming_response.update_mcp_server(
            mcp_server_id="mcp_server_id",
            mission_id="mission_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = await response.parse()
            assert_matches_type(object, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_mcp_server(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            await async_client.ai.missions.mcp_servers.with_raw_response.update_mcp_server(
                mcp_server_id="mcp_server_id",
                mission_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcp_server_id` but received ''"):
            await async_client.ai.missions.mcp_servers.with_raw_response.update_mcp_server(
                mcp_server_id="",
                mission_id="mission_id",
            )

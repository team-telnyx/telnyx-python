# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTools:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_tool(self, client: Telnyx) -> None:
        tool = client.ai.missions.tools.create_tool(
            "mission_id",
        )
        assert_matches_type(object, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_tool(self, client: Telnyx) -> None:
        response = client.ai.missions.tools.with_raw_response.create_tool(
            "mission_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(object, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_tool(self, client: Telnyx) -> None:
        with client.ai.missions.tools.with_streaming_response.create_tool(
            "mission_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(object, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_tool(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            client.ai.missions.tools.with_raw_response.create_tool(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_tool(self, client: Telnyx) -> None:
        tool = client.ai.missions.tools.delete_tool(
            tool_id="tool_id",
            mission_id="mission_id",
        )
        assert tool is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_tool(self, client: Telnyx) -> None:
        response = client.ai.missions.tools.with_raw_response.delete_tool(
            tool_id="tool_id",
            mission_id="mission_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert tool is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_tool(self, client: Telnyx) -> None:
        with client.ai.missions.tools.with_streaming_response.delete_tool(
            tool_id="tool_id",
            mission_id="mission_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert tool is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete_tool(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            client.ai.missions.tools.with_raw_response.delete_tool(
                tool_id="tool_id",
                mission_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            client.ai.missions.tools.with_raw_response.delete_tool(
                tool_id="",
                mission_id="mission_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_tool(self, client: Telnyx) -> None:
        tool = client.ai.missions.tools.get_tool(
            tool_id="tool_id",
            mission_id="mission_id",
        )
        assert_matches_type(object, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_tool(self, client: Telnyx) -> None:
        response = client.ai.missions.tools.with_raw_response.get_tool(
            tool_id="tool_id",
            mission_id="mission_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(object, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_tool(self, client: Telnyx) -> None:
        with client.ai.missions.tools.with_streaming_response.get_tool(
            tool_id="tool_id",
            mission_id="mission_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(object, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_tool(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            client.ai.missions.tools.with_raw_response.get_tool(
                tool_id="tool_id",
                mission_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            client.ai.missions.tools.with_raw_response.get_tool(
                tool_id="",
                mission_id="mission_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_tools(self, client: Telnyx) -> None:
        tool = client.ai.missions.tools.list_tools(
            "mission_id",
        )
        assert_matches_type(object, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_tools(self, client: Telnyx) -> None:
        response = client.ai.missions.tools.with_raw_response.list_tools(
            "mission_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(object, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_tools(self, client: Telnyx) -> None:
        with client.ai.missions.tools.with_streaming_response.list_tools(
            "mission_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(object, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_tools(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            client.ai.missions.tools.with_raw_response.list_tools(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_tool(self, client: Telnyx) -> None:
        tool = client.ai.missions.tools.update_tool(
            tool_id="tool_id",
            mission_id="mission_id",
        )
        assert_matches_type(object, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_tool(self, client: Telnyx) -> None:
        response = client.ai.missions.tools.with_raw_response.update_tool(
            tool_id="tool_id",
            mission_id="mission_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(object, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_tool(self, client: Telnyx) -> None:
        with client.ai.missions.tools.with_streaming_response.update_tool(
            tool_id="tool_id",
            mission_id="mission_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(object, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_tool(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            client.ai.missions.tools.with_raw_response.update_tool(
                tool_id="tool_id",
                mission_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            client.ai.missions.tools.with_raw_response.update_tool(
                tool_id="",
                mission_id="mission_id",
            )


class TestAsyncTools:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_tool(self, async_client: AsyncTelnyx) -> None:
        tool = await async_client.ai.missions.tools.create_tool(
            "mission_id",
        )
        assert_matches_type(object, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_tool(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.missions.tools.with_raw_response.create_tool(
            "mission_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(object, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_tool(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.missions.tools.with_streaming_response.create_tool(
            "mission_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(object, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_tool(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            await async_client.ai.missions.tools.with_raw_response.create_tool(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_tool(self, async_client: AsyncTelnyx) -> None:
        tool = await async_client.ai.missions.tools.delete_tool(
            tool_id="tool_id",
            mission_id="mission_id",
        )
        assert tool is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_tool(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.missions.tools.with_raw_response.delete_tool(
            tool_id="tool_id",
            mission_id="mission_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert tool is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_tool(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.missions.tools.with_streaming_response.delete_tool(
            tool_id="tool_id",
            mission_id="mission_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert tool is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete_tool(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            await async_client.ai.missions.tools.with_raw_response.delete_tool(
                tool_id="tool_id",
                mission_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            await async_client.ai.missions.tools.with_raw_response.delete_tool(
                tool_id="",
                mission_id="mission_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_tool(self, async_client: AsyncTelnyx) -> None:
        tool = await async_client.ai.missions.tools.get_tool(
            tool_id="tool_id",
            mission_id="mission_id",
        )
        assert_matches_type(object, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_tool(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.missions.tools.with_raw_response.get_tool(
            tool_id="tool_id",
            mission_id="mission_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(object, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_tool(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.missions.tools.with_streaming_response.get_tool(
            tool_id="tool_id",
            mission_id="mission_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(object, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_tool(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            await async_client.ai.missions.tools.with_raw_response.get_tool(
                tool_id="tool_id",
                mission_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            await async_client.ai.missions.tools.with_raw_response.get_tool(
                tool_id="",
                mission_id="mission_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_tools(self, async_client: AsyncTelnyx) -> None:
        tool = await async_client.ai.missions.tools.list_tools(
            "mission_id",
        )
        assert_matches_type(object, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_tools(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.missions.tools.with_raw_response.list_tools(
            "mission_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(object, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_tools(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.missions.tools.with_streaming_response.list_tools(
            "mission_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(object, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_tools(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            await async_client.ai.missions.tools.with_raw_response.list_tools(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_tool(self, async_client: AsyncTelnyx) -> None:
        tool = await async_client.ai.missions.tools.update_tool(
            tool_id="tool_id",
            mission_id="mission_id",
        )
        assert_matches_type(object, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_tool(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.missions.tools.with_raw_response.update_tool(
            tool_id="tool_id",
            mission_id="mission_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(object, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_tool(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.missions.tools.with_streaming_response.update_tool(
            tool_id="tool_id",
            mission_id="mission_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(object, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_tool(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            await async_client.ai.missions.tools.with_raw_response.update_tool(
                tool_id="tool_id",
                mission_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            await async_client.ai.missions.tools.with_raw_response.update_tool(
                tool_id="",
                mission_id="mission_id",
            )

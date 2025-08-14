# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.ai.assistants import ToolTestResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTools:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test(self, client: Telnyx) -> None:
        tool = client.ai.assistants.tools.test(
            tool_id="tool_id",
            assistant_id="assistant_id",
        )
        assert_matches_type(ToolTestResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test_with_all_params(self, client: Telnyx) -> None:
        tool = client.ai.assistants.tools.test(
            tool_id="tool_id",
            assistant_id="assistant_id",
            arguments={"foo": "bar"},
            dynamic_variables={"foo": "bar"},
        )
        assert_matches_type(ToolTestResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_test(self, client: Telnyx) -> None:
        response = client.ai.assistants.tools.with_raw_response.test(
            tool_id="tool_id",
            assistant_id="assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolTestResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_test(self, client: Telnyx) -> None:
        with client.ai.assistants.tools.with_streaming_response.test(
            tool_id="tool_id",
            assistant_id="assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolTestResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_test(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            client.ai.assistants.tools.with_raw_response.test(
                tool_id="tool_id",
                assistant_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            client.ai.assistants.tools.with_raw_response.test(
                tool_id="",
                assistant_id="assistant_id",
            )


class TestAsyncTools:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test(self, async_client: AsyncTelnyx) -> None:
        tool = await async_client.ai.assistants.tools.test(
            tool_id="tool_id",
            assistant_id="assistant_id",
        )
        assert_matches_type(ToolTestResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test_with_all_params(self, async_client: AsyncTelnyx) -> None:
        tool = await async_client.ai.assistants.tools.test(
            tool_id="tool_id",
            assistant_id="assistant_id",
            arguments={"foo": "bar"},
            dynamic_variables={"foo": "bar"},
        )
        assert_matches_type(ToolTestResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_test(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.assistants.tools.with_raw_response.test(
            tool_id="tool_id",
            assistant_id="assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolTestResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_test(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.assistants.tools.with_streaming_response.test(
            tool_id="tool_id",
            assistant_id="assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolTestResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_test(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            await async_client.ai.assistants.tools.with_raw_response.test(
                tool_id="tool_id",
                assistant_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            await async_client.ai.assistants.tools.with_raw_response.test(
                tool_id="",
                assistant_id="assistant_id",
            )

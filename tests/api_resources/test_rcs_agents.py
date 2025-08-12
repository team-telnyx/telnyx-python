# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import RcsAgentResponse, RcsAgentListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRcsAgents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        rcs_agent = client.rcs_agents.retrieve(
            "id",
        )
        assert_matches_type(RcsAgentResponse, rcs_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.rcs_agents.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rcs_agent = response.parse()
        assert_matches_type(RcsAgentResponse, rcs_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.rcs_agents.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rcs_agent = response.parse()
            assert_matches_type(RcsAgentResponse, rcs_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.rcs_agents.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        rcs_agent = client.rcs_agents.update(
            id="id",
        )
        assert_matches_type(RcsAgentResponse, rcs_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        rcs_agent = client.rcs_agents.update(
            id="id",
            profile_id="4001932a-b8a3-42fc-9389-021be6388909",
            webhook_failover_url="http://example.com",
            webhook_url="http://example.com",
        )
        assert_matches_type(RcsAgentResponse, rcs_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.rcs_agents.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rcs_agent = response.parse()
        assert_matches_type(RcsAgentResponse, rcs_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.rcs_agents.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rcs_agent = response.parse()
            assert_matches_type(RcsAgentResponse, rcs_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.rcs_agents.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        rcs_agent = client.rcs_agents.list()
        assert_matches_type(RcsAgentListResponse, rcs_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        rcs_agent = client.rcs_agents.list(
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(RcsAgentListResponse, rcs_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.rcs_agents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rcs_agent = response.parse()
        assert_matches_type(RcsAgentListResponse, rcs_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.rcs_agents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rcs_agent = response.parse()
            assert_matches_type(RcsAgentListResponse, rcs_agent, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRcsAgents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        rcs_agent = await async_client.rcs_agents.retrieve(
            "id",
        )
        assert_matches_type(RcsAgentResponse, rcs_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.rcs_agents.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rcs_agent = await response.parse()
        assert_matches_type(RcsAgentResponse, rcs_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.rcs_agents.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rcs_agent = await response.parse()
            assert_matches_type(RcsAgentResponse, rcs_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.rcs_agents.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        rcs_agent = await async_client.rcs_agents.update(
            id="id",
        )
        assert_matches_type(RcsAgentResponse, rcs_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        rcs_agent = await async_client.rcs_agents.update(
            id="id",
            profile_id="4001932a-b8a3-42fc-9389-021be6388909",
            webhook_failover_url="http://example.com",
            webhook_url="http://example.com",
        )
        assert_matches_type(RcsAgentResponse, rcs_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.rcs_agents.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rcs_agent = await response.parse()
        assert_matches_type(RcsAgentResponse, rcs_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.rcs_agents.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rcs_agent = await response.parse()
            assert_matches_type(RcsAgentResponse, rcs_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.rcs_agents.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        rcs_agent = await async_client.rcs_agents.list()
        assert_matches_type(RcsAgentListResponse, rcs_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        rcs_agent = await async_client.rcs_agents.list(
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(RcsAgentListResponse, rcs_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.rcs_agents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rcs_agent = await response.parse()
        assert_matches_type(RcsAgentListResponse, rcs_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.rcs_agents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rcs_agent = await response.parse()
            assert_matches_type(RcsAgentListResponse, rcs_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

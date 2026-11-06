# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.agent_gateways.keys import AgentGatewayToolPermissionsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestToolPermissions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        tool_permission = client.agent_gateways.teams.tool_permissions.create(
            team_id="d7b21324-a2bf-406c-ba49-c6ec4d23d476",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            servers=[{"id": "88d5a97b-4080-4855-8bac-a39811b1dc24"}],
        )
        assert_matches_type(AgentGatewayToolPermissionsResponse, tool_permission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.agent_gateways.teams.tool_permissions.with_raw_response.create(
            team_id="d7b21324-a2bf-406c-ba49-c6ec4d23d476",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            servers=[{"id": "88d5a97b-4080-4855-8bac-a39811b1dc24"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_permission = response.parse()
        assert_matches_type(AgentGatewayToolPermissionsResponse, tool_permission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.agent_gateways.teams.tool_permissions.with_streaming_response.create(
            team_id="d7b21324-a2bf-406c-ba49-c6ec4d23d476",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            servers=[{"id": "88d5a97b-4080-4855-8bac-a39811b1dc24"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_permission = response.parse()
            assert_matches_type(AgentGatewayToolPermissionsResponse, tool_permission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.agent_gateways.teams.tool_permissions.with_raw_response.create(
                team_id="d7b21324-a2bf-406c-ba49-c6ec4d23d476",
                instance_id="",
                servers=[{"id": "88d5a97b-4080-4855-8bac-a39811b1dc24"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            client.agent_gateways.teams.tool_permissions.with_raw_response.create(
                team_id="",
                instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
                servers=[{"id": "88d5a97b-4080-4855-8bac-a39811b1dc24"}],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        tool_permission = client.agent_gateways.teams.tool_permissions.list(
            team_id="d7b21324-a2bf-406c-ba49-c6ec4d23d476",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        )
        assert_matches_type(AgentGatewayToolPermissionsResponse, tool_permission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.agent_gateways.teams.tool_permissions.with_raw_response.list(
            team_id="d7b21324-a2bf-406c-ba49-c6ec4d23d476",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_permission = response.parse()
        assert_matches_type(AgentGatewayToolPermissionsResponse, tool_permission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.agent_gateways.teams.tool_permissions.with_streaming_response.list(
            team_id="d7b21324-a2bf-406c-ba49-c6ec4d23d476",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_permission = response.parse()
            assert_matches_type(AgentGatewayToolPermissionsResponse, tool_permission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.agent_gateways.teams.tool_permissions.with_raw_response.list(
                team_id="d7b21324-a2bf-406c-ba49-c6ec4d23d476",
                instance_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            client.agent_gateways.teams.tool_permissions.with_raw_response.list(
                team_id="",
                instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            )


class TestAsyncToolPermissions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        tool_permission = await async_client.agent_gateways.teams.tool_permissions.create(
            team_id="d7b21324-a2bf-406c-ba49-c6ec4d23d476",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            servers=[{"id": "88d5a97b-4080-4855-8bac-a39811b1dc24"}],
        )
        assert_matches_type(AgentGatewayToolPermissionsResponse, tool_permission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.agent_gateways.teams.tool_permissions.with_raw_response.create(
            team_id="d7b21324-a2bf-406c-ba49-c6ec4d23d476",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            servers=[{"id": "88d5a97b-4080-4855-8bac-a39811b1dc24"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_permission = await response.parse()
        assert_matches_type(AgentGatewayToolPermissionsResponse, tool_permission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.agent_gateways.teams.tool_permissions.with_streaming_response.create(
            team_id="d7b21324-a2bf-406c-ba49-c6ec4d23d476",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            servers=[{"id": "88d5a97b-4080-4855-8bac-a39811b1dc24"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_permission = await response.parse()
            assert_matches_type(AgentGatewayToolPermissionsResponse, tool_permission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.agent_gateways.teams.tool_permissions.with_raw_response.create(
                team_id="d7b21324-a2bf-406c-ba49-c6ec4d23d476",
                instance_id="",
                servers=[{"id": "88d5a97b-4080-4855-8bac-a39811b1dc24"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            await async_client.agent_gateways.teams.tool_permissions.with_raw_response.create(
                team_id="",
                instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
                servers=[{"id": "88d5a97b-4080-4855-8bac-a39811b1dc24"}],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        tool_permission = await async_client.agent_gateways.teams.tool_permissions.list(
            team_id="d7b21324-a2bf-406c-ba49-c6ec4d23d476",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        )
        assert_matches_type(AgentGatewayToolPermissionsResponse, tool_permission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.agent_gateways.teams.tool_permissions.with_raw_response.list(
            team_id="d7b21324-a2bf-406c-ba49-c6ec4d23d476",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_permission = await response.parse()
        assert_matches_type(AgentGatewayToolPermissionsResponse, tool_permission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.agent_gateways.teams.tool_permissions.with_streaming_response.list(
            team_id="d7b21324-a2bf-406c-ba49-c6ec4d23d476",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_permission = await response.parse()
            assert_matches_type(AgentGatewayToolPermissionsResponse, tool_permission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.agent_gateways.teams.tool_permissions.with_raw_response.list(
                team_id="d7b21324-a2bf-406c-ba49-c6ec4d23d476",
                instance_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            await async_client.agent_gateways.teams.tool_permissions.with_raw_response.list(
                team_id="",
                instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            )

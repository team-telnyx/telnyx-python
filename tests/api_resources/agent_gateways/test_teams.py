# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.agent_gateways import (
    TeamListResponse,
    AgentGatewayTeamResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTeams:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        team = client.agent_gateways.teams.create(
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
            name="support",
        )
        assert_matches_type(AgentGatewayTeamResponse, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        team = client.agent_gateways.teams.create(
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
            name="support",
            budget_resets_every="30d",
            max_budget=50,
            models=["GLM-5.3-Flash", "Qwen3.8-27B-nothink"],
            requests_per_minute=120,
            tokens_per_minute=1,
        )
        assert_matches_type(AgentGatewayTeamResponse, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.agent_gateways.teams.with_raw_response.create(
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
            name="support",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = response.parse()
        assert_matches_type(AgentGatewayTeamResponse, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.agent_gateways.teams.with_streaming_response.create(
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
            name="support",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = response.parse()
            assert_matches_type(AgentGatewayTeamResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.agent_gateways.teams.with_raw_response.create(
                instance_id="",
                name="support",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        team = client.agent_gateways.teams.update(
            team_id="0b6c5d4e-3f2a-4b1c-9d8e-7f6a5b4c3d2e",
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        )
        assert_matches_type(AgentGatewayTeamResponse, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        team = client.agent_gateways.teams.update(
            team_id="0b6c5d4e-3f2a-4b1c-9d8e-7f6a5b4c3d2e",
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
            blocked=True,
            budget_resets_every="30d",
            max_budget=100,
            models=["x"],
            name="x",
            requests_per_minute=1,
            tokens_per_minute=1,
        )
        assert_matches_type(AgentGatewayTeamResponse, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.agent_gateways.teams.with_raw_response.update(
            team_id="0b6c5d4e-3f2a-4b1c-9d8e-7f6a5b4c3d2e",
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = response.parse()
        assert_matches_type(AgentGatewayTeamResponse, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.agent_gateways.teams.with_streaming_response.update(
            team_id="0b6c5d4e-3f2a-4b1c-9d8e-7f6a5b4c3d2e",
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = response.parse()
            assert_matches_type(AgentGatewayTeamResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.agent_gateways.teams.with_raw_response.update(
                team_id="0b6c5d4e-3f2a-4b1c-9d8e-7f6a5b4c3d2e",
                instance_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            client.agent_gateways.teams.with_raw_response.update(
                team_id="",
                instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        team = client.agent_gateways.teams.list(
            "ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        )
        assert_matches_type(TeamListResponse, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.agent_gateways.teams.with_raw_response.list(
            "ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = response.parse()
        assert_matches_type(TeamListResponse, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.agent_gateways.teams.with_streaming_response.list(
            "ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = response.parse()
            assert_matches_type(TeamListResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.agent_gateways.teams.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        team = client.agent_gateways.teams.delete(
            team_id="0b6c5d4e-3f2a-4b1c-9d8e-7f6a5b4c3d2e",
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        )
        assert_matches_type(AgentGatewayTeamResponse, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.agent_gateways.teams.with_raw_response.delete(
            team_id="0b6c5d4e-3f2a-4b1c-9d8e-7f6a5b4c3d2e",
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = response.parse()
        assert_matches_type(AgentGatewayTeamResponse, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.agent_gateways.teams.with_streaming_response.delete(
            team_id="0b6c5d4e-3f2a-4b1c-9d8e-7f6a5b4c3d2e",
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = response.parse()
            assert_matches_type(AgentGatewayTeamResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.agent_gateways.teams.with_raw_response.delete(
                team_id="0b6c5d4e-3f2a-4b1c-9d8e-7f6a5b4c3d2e",
                instance_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            client.agent_gateways.teams.with_raw_response.delete(
                team_id="",
                instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
            )


class TestAsyncTeams:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        team = await async_client.agent_gateways.teams.create(
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
            name="support",
        )
        assert_matches_type(AgentGatewayTeamResponse, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        team = await async_client.agent_gateways.teams.create(
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
            name="support",
            budget_resets_every="30d",
            max_budget=50,
            models=["GLM-5.3-Flash", "Qwen3.8-27B-nothink"],
            requests_per_minute=120,
            tokens_per_minute=1,
        )
        assert_matches_type(AgentGatewayTeamResponse, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.agent_gateways.teams.with_raw_response.create(
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
            name="support",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = await response.parse()
        assert_matches_type(AgentGatewayTeamResponse, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.agent_gateways.teams.with_streaming_response.create(
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
            name="support",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = await response.parse()
            assert_matches_type(AgentGatewayTeamResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.agent_gateways.teams.with_raw_response.create(
                instance_id="",
                name="support",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        team = await async_client.agent_gateways.teams.update(
            team_id="0b6c5d4e-3f2a-4b1c-9d8e-7f6a5b4c3d2e",
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        )
        assert_matches_type(AgentGatewayTeamResponse, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        team = await async_client.agent_gateways.teams.update(
            team_id="0b6c5d4e-3f2a-4b1c-9d8e-7f6a5b4c3d2e",
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
            blocked=True,
            budget_resets_every="30d",
            max_budget=100,
            models=["x"],
            name="x",
            requests_per_minute=1,
            tokens_per_minute=1,
        )
        assert_matches_type(AgentGatewayTeamResponse, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.agent_gateways.teams.with_raw_response.update(
            team_id="0b6c5d4e-3f2a-4b1c-9d8e-7f6a5b4c3d2e",
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = await response.parse()
        assert_matches_type(AgentGatewayTeamResponse, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.agent_gateways.teams.with_streaming_response.update(
            team_id="0b6c5d4e-3f2a-4b1c-9d8e-7f6a5b4c3d2e",
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = await response.parse()
            assert_matches_type(AgentGatewayTeamResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.agent_gateways.teams.with_raw_response.update(
                team_id="0b6c5d4e-3f2a-4b1c-9d8e-7f6a5b4c3d2e",
                instance_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            await async_client.agent_gateways.teams.with_raw_response.update(
                team_id="",
                instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        team = await async_client.agent_gateways.teams.list(
            "ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        )
        assert_matches_type(TeamListResponse, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.agent_gateways.teams.with_raw_response.list(
            "ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = await response.parse()
        assert_matches_type(TeamListResponse, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.agent_gateways.teams.with_streaming_response.list(
            "ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = await response.parse()
            assert_matches_type(TeamListResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.agent_gateways.teams.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        team = await async_client.agent_gateways.teams.delete(
            team_id="0b6c5d4e-3f2a-4b1c-9d8e-7f6a5b4c3d2e",
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        )
        assert_matches_type(AgentGatewayTeamResponse, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.agent_gateways.teams.with_raw_response.delete(
            team_id="0b6c5d4e-3f2a-4b1c-9d8e-7f6a5b4c3d2e",
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = await response.parse()
        assert_matches_type(AgentGatewayTeamResponse, team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.agent_gateways.teams.with_streaming_response.delete(
            team_id="0b6c5d4e-3f2a-4b1c-9d8e-7f6a5b4c3d2e",
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = await response.parse()
            assert_matches_type(AgentGatewayTeamResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.agent_gateways.teams.with_raw_response.delete(
                team_id="0b6c5d4e-3f2a-4b1c-9d8e-7f6a5b4c3d2e",
                instance_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            await async_client.agent_gateways.teams.with_raw_response.delete(
                team_id="",
                instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
            )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.ai.missions.runs import TelnyxAgentLinkResponse, TelnyxAgentListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTelnyxAgents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        telnyx_agent = client.ai.missions.runs.telnyx_agents.list(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TelnyxAgentListResponse, telnyx_agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.ai.missions.runs.telnyx_agents.with_raw_response.list(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telnyx_agent = response.parse()
        assert_matches_type(TelnyxAgentListResponse, telnyx_agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.ai.missions.runs.telnyx_agents.with_streaming_response.list(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telnyx_agent = response.parse()
            assert_matches_type(TelnyxAgentListResponse, telnyx_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            client.ai.missions.runs.telnyx_agents.with_raw_response.list(
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                mission_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.ai.missions.runs.telnyx_agents.with_raw_response.list(
                run_id="",
                mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_link(self, client: Telnyx) -> None:
        telnyx_agent = client.ai.missions.runs.telnyx_agents.link(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            telnyx_agent_id="telnyx_agent_id",
        )
        assert_matches_type(TelnyxAgentLinkResponse, telnyx_agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_link(self, client: Telnyx) -> None:
        response = client.ai.missions.runs.telnyx_agents.with_raw_response.link(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            telnyx_agent_id="telnyx_agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telnyx_agent = response.parse()
        assert_matches_type(TelnyxAgentLinkResponse, telnyx_agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_link(self, client: Telnyx) -> None:
        with client.ai.missions.runs.telnyx_agents.with_streaming_response.link(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            telnyx_agent_id="telnyx_agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telnyx_agent = response.parse()
            assert_matches_type(TelnyxAgentLinkResponse, telnyx_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_link(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            client.ai.missions.runs.telnyx_agents.with_raw_response.link(
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                mission_id="",
                telnyx_agent_id="telnyx_agent_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.ai.missions.runs.telnyx_agents.with_raw_response.link(
                run_id="",
                mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                telnyx_agent_id="telnyx_agent_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unlink(self, client: Telnyx) -> None:
        telnyx_agent = client.ai.missions.runs.telnyx_agents.unlink(
            telnyx_agent_id="telnyx_agent_id",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert telnyx_agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_unlink(self, client: Telnyx) -> None:
        response = client.ai.missions.runs.telnyx_agents.with_raw_response.unlink(
            telnyx_agent_id="telnyx_agent_id",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telnyx_agent = response.parse()
        assert telnyx_agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_unlink(self, client: Telnyx) -> None:
        with client.ai.missions.runs.telnyx_agents.with_streaming_response.unlink(
            telnyx_agent_id="telnyx_agent_id",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telnyx_agent = response.parse()
            assert telnyx_agent is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_unlink(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            client.ai.missions.runs.telnyx_agents.with_raw_response.unlink(
                telnyx_agent_id="telnyx_agent_id",
                mission_id="",
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.ai.missions.runs.telnyx_agents.with_raw_response.unlink(
                telnyx_agent_id="telnyx_agent_id",
                mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                run_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `telnyx_agent_id` but received ''"):
            client.ai.missions.runs.telnyx_agents.with_raw_response.unlink(
                telnyx_agent_id="",
                mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncTelnyxAgents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        telnyx_agent = await async_client.ai.missions.runs.telnyx_agents.list(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TelnyxAgentListResponse, telnyx_agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.missions.runs.telnyx_agents.with_raw_response.list(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telnyx_agent = await response.parse()
        assert_matches_type(TelnyxAgentListResponse, telnyx_agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.missions.runs.telnyx_agents.with_streaming_response.list(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telnyx_agent = await response.parse()
            assert_matches_type(TelnyxAgentListResponse, telnyx_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            await async_client.ai.missions.runs.telnyx_agents.with_raw_response.list(
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                mission_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.ai.missions.runs.telnyx_agents.with_raw_response.list(
                run_id="",
                mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_link(self, async_client: AsyncTelnyx) -> None:
        telnyx_agent = await async_client.ai.missions.runs.telnyx_agents.link(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            telnyx_agent_id="telnyx_agent_id",
        )
        assert_matches_type(TelnyxAgentLinkResponse, telnyx_agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_link(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.missions.runs.telnyx_agents.with_raw_response.link(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            telnyx_agent_id="telnyx_agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telnyx_agent = await response.parse()
        assert_matches_type(TelnyxAgentLinkResponse, telnyx_agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_link(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.missions.runs.telnyx_agents.with_streaming_response.link(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            telnyx_agent_id="telnyx_agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telnyx_agent = await response.parse()
            assert_matches_type(TelnyxAgentLinkResponse, telnyx_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_link(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            await async_client.ai.missions.runs.telnyx_agents.with_raw_response.link(
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                mission_id="",
                telnyx_agent_id="telnyx_agent_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.ai.missions.runs.telnyx_agents.with_raw_response.link(
                run_id="",
                mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                telnyx_agent_id="telnyx_agent_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unlink(self, async_client: AsyncTelnyx) -> None:
        telnyx_agent = await async_client.ai.missions.runs.telnyx_agents.unlink(
            telnyx_agent_id="telnyx_agent_id",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert telnyx_agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_unlink(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.missions.runs.telnyx_agents.with_raw_response.unlink(
            telnyx_agent_id="telnyx_agent_id",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telnyx_agent = await response.parse()
        assert telnyx_agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_unlink(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.missions.runs.telnyx_agents.with_streaming_response.unlink(
            telnyx_agent_id="telnyx_agent_id",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telnyx_agent = await response.parse()
            assert telnyx_agent is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_unlink(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            await async_client.ai.missions.runs.telnyx_agents.with_raw_response.unlink(
                telnyx_agent_id="telnyx_agent_id",
                mission_id="",
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.ai.missions.runs.telnyx_agents.with_raw_response.unlink(
                telnyx_agent_id="telnyx_agent_id",
                mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                run_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `telnyx_agent_id` but received ''"):
            await async_client.ai.missions.runs.telnyx_agents.with_raw_response.unlink(
                telnyx_agent_id="",
                mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

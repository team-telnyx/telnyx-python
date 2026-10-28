# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from telnyx.types.ai.tests.test_framework.v1 import (
    ScenarioListResponse,
    EvaluatorScenarioDetail,
    ScenarioGenerationResponse,
    ScenarioRunScenariosResponse,
    ScenarioScenarioAgentResponse,
    ScenarioRetrieveGenerateProgressResponse,
    ScenarioRetrieveScenarioAgentProgressResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScenarios:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        scenario = client.ai.tests.test_framework.v1.scenarios.create(
            name="Refund escalation flow",
            personality=4643,
        )
        assert_matches_type(EvaluatorScenarioDetail, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        scenario = client.ai.tests.test_framework.v1.scenarios.create(
            name="Refund escalation flow",
            personality=4643,
            agent=1259,
            expected_outcome_prompt="The assistant explains the refund policy and offers escalation.",
            first_message="Hi, I want a refund.",
            folder_path="folder_path",
            instructions="Call the support line and demand a refund for a damaged product.",
            metrics=[266881],
            tags=["support"],
            test_profile=0,
        )
        assert_matches_type(EvaluatorScenarioDetail, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.ai.tests.test_framework.v1.scenarios.with_raw_response.create(
            name="Refund escalation flow",
            personality=4643,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scenario = response.parse()
        assert_matches_type(EvaluatorScenarioDetail, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.ai.tests.test_framework.v1.scenarios.with_streaming_response.create(
            name="Refund escalation flow",
            personality=4643,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scenario = response.parse()
            assert_matches_type(EvaluatorScenarioDetail, scenario, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        scenario = client.ai.tests.test_framework.v1.scenarios.retrieve(
            0,
        )
        assert_matches_type(EvaluatorScenarioDetail, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.ai.tests.test_framework.v1.scenarios.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scenario = response.parse()
        assert_matches_type(EvaluatorScenarioDetail, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.ai.tests.test_framework.v1.scenarios.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scenario = response.parse()
            assert_matches_type(EvaluatorScenarioDetail, scenario, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        scenario = client.ai.tests.test_framework.v1.scenarios.update(
            id=0,
        )
        assert_matches_type(EvaluatorScenarioDetail, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        scenario = client.ai.tests.test_framework.v1.scenarios.update(
            id=0,
            agent=0,
            expected_outcome_prompt="expected_outcome_prompt",
            first_message="first_message",
            folder_path="folder_path",
            inbound_phone_number=0,
            instructions="Call the support line, demand a refund, and mention the damaged packaging.",
            max_duration=0,
            metrics=[266881, 266882],
            name="Refund escalation flow - updated",
            personality=0,
            phone_number=0,
            scenario_language="scenario_language",
            tags=["string"],
            test_profile=0,
            tool_ids=["string"],
        )
        assert_matches_type(EvaluatorScenarioDetail, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.ai.tests.test_framework.v1.scenarios.with_raw_response.update(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scenario = response.parse()
        assert_matches_type(EvaluatorScenarioDetail, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.ai.tests.test_framework.v1.scenarios.with_streaming_response.update(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scenario = response.parse()
            assert_matches_type(EvaluatorScenarioDetail, scenario, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        scenario = client.ai.tests.test_framework.v1.scenarios.list()
        assert_matches_type(ScenarioListResponse, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        scenario = client.ai.tests.test_framework.v1.scenarios.list(
            agent_id=0,
            assistant_id="assistant_id",
            page=1,
            page_size=1,
            tags="tags",
        )
        assert_matches_type(ScenarioListResponse, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.ai.tests.test_framework.v1.scenarios.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scenario = response.parse()
        assert_matches_type(ScenarioListResponse, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.ai.tests.test_framework.v1.scenarios.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scenario = response.parse()
            assert_matches_type(ScenarioListResponse, scenario, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        scenario = client.ai.tests.test_framework.v1.scenarios.delete(
            0,
        )
        assert_matches_type(object, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.ai.tests.test_framework.v1.scenarios.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scenario = response.parse()
        assert_matches_type(object, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.ai.tests.test_framework.v1.scenarios.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scenario = response.parse()
            assert_matches_type(object, scenario, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate_bg(self, client: Telnyx) -> None:
        scenario = client.ai.tests.test_framework.v1.scenarios.generate_bg(
            num_scenarios=5,
        )
        assert_matches_type(ScenarioGenerationResponse, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate_bg_with_all_params(self, client: Telnyx) -> None:
        scenario = client.ai.tests.test_framework.v1.scenarios.generate_bg(
            num_scenarios=5,
            agent_id=1259,
            extra_instructions="Focus on angry customers asking about refunds.",
            first_message="first_message",
            folder_path="folder_path",
            generate_expected_outcomes=True,
            inbound_phone_number=0,
            personalities=[0],
            scenario_type="workflow",
            tags=["string"],
            test_profile=0,
            tool_ids=["string"],
        )
        assert_matches_type(ScenarioGenerationResponse, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_generate_bg(self, client: Telnyx) -> None:
        response = client.ai.tests.test_framework.v1.scenarios.with_raw_response.generate_bg(
            num_scenarios=5,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scenario = response.parse()
        assert_matches_type(ScenarioGenerationResponse, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_generate_bg(self, client: Telnyx) -> None:
        with client.ai.tests.test_framework.v1.scenarios.with_streaming_response.generate_bg(
            num_scenarios=5,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scenario = response.parse()
            assert_matches_type(ScenarioGenerationResponse, scenario, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve_export_scenarios(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/ai/tests/test_framework/v1/scenarios/export_scenarios").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        scenario = client.ai.tests.test_framework.v1.scenarios.retrieve_export_scenarios(
            export_type="csv",
            scenario_ids="scenario_ids",
        )
        assert scenario.is_closed
        assert scenario.json() == {"foo": "bar"}
        assert cast(Any, scenario.is_closed) is True
        assert isinstance(scenario, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve_export_scenarios_with_all_params(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/ai/tests/test_framework/v1/scenarios/export_scenarios").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        scenario = client.ai.tests.test_framework.v1.scenarios.retrieve_export_scenarios(
            export_type="csv",
            scenario_ids="scenario_ids",
            agent_id=0,
        )
        assert scenario.is_closed
        assert scenario.json() == {"foo": "bar"}
        assert cast(Any, scenario.is_closed) is True
        assert isinstance(scenario, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve_export_scenarios(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/ai/tests/test_framework/v1/scenarios/export_scenarios").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        scenario = client.ai.tests.test_framework.v1.scenarios.with_raw_response.retrieve_export_scenarios(
            export_type="csv",
            scenario_ids="scenario_ids",
        )

        assert scenario.is_closed is True
        assert scenario.http_request.headers.get("X-Stainless-Lang") == "python"
        assert scenario.json() == {"foo": "bar"}
        assert isinstance(scenario, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve_export_scenarios(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/ai/tests/test_framework/v1/scenarios/export_scenarios").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.ai.tests.test_framework.v1.scenarios.with_streaming_response.retrieve_export_scenarios(
            export_type="csv",
            scenario_ids="scenario_ids",
        ) as scenario:
            assert not scenario.is_closed
            assert scenario.http_request.headers.get("X-Stainless-Lang") == "python"

            assert scenario.json() == {"foo": "bar"}
            assert cast(Any, scenario.is_closed) is True
            assert isinstance(scenario, StreamedBinaryAPIResponse)

        assert cast(Any, scenario.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_generate_progress(self, client: Telnyx) -> None:
        scenario = client.ai.tests.test_framework.v1.scenarios.retrieve_generate_progress(
            progress_id="progress_id",
        )
        assert_matches_type(ScenarioRetrieveGenerateProgressResponse, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_generate_progress(self, client: Telnyx) -> None:
        response = client.ai.tests.test_framework.v1.scenarios.with_raw_response.retrieve_generate_progress(
            progress_id="progress_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scenario = response.parse()
        assert_matches_type(ScenarioRetrieveGenerateProgressResponse, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_generate_progress(self, client: Telnyx) -> None:
        with client.ai.tests.test_framework.v1.scenarios.with_streaming_response.retrieve_generate_progress(
            progress_id="progress_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scenario = response.parse()
            assert_matches_type(ScenarioRetrieveGenerateProgressResponse, scenario, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_scenario_agent_progress(self, client: Telnyx) -> None:
        scenario = client.ai.tests.test_framework.v1.scenarios.retrieve_scenario_agent_progress(
            progress_id="progress_id",
        )
        assert_matches_type(ScenarioRetrieveScenarioAgentProgressResponse, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_scenario_agent_progress(self, client: Telnyx) -> None:
        response = client.ai.tests.test_framework.v1.scenarios.with_raw_response.retrieve_scenario_agent_progress(
            progress_id="progress_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scenario = response.parse()
        assert_matches_type(ScenarioRetrieveScenarioAgentProgressResponse, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_scenario_agent_progress(self, client: Telnyx) -> None:
        with client.ai.tests.test_framework.v1.scenarios.with_streaming_response.retrieve_scenario_agent_progress(
            progress_id="progress_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scenario = response.parse()
            assert_matches_type(ScenarioRetrieveScenarioAgentProgressResponse, scenario, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run_scenarios(self, client: Telnyx) -> None:
        scenario = client.ai.tests.test_framework.v1.scenarios.run_scenarios()
        assert_matches_type(ScenarioRunScenariosResponse, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run_scenarios_with_all_params(self, client: Telnyx) -> None:
        scenario = client.ai.tests.test_framework.v1.scenarios.run_scenarios(
            agent_id=1259,
            agent_number="agent_number",
            assistant_id="assistant_id",
            concurrency_limit=3,
            frequency=0,
            mode="same_number",
            name="name",
            outbound_phone_number="outbound_phone_number",
            personality_ids=[0],
            scenarios=[9512],
            tags=["regression"],
            test_profile_ids=[0],
        )
        assert_matches_type(ScenarioRunScenariosResponse, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_run_scenarios(self, client: Telnyx) -> None:
        response = client.ai.tests.test_framework.v1.scenarios.with_raw_response.run_scenarios()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scenario = response.parse()
        assert_matches_type(ScenarioRunScenariosResponse, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_run_scenarios(self, client: Telnyx) -> None:
        with client.ai.tests.test_framework.v1.scenarios.with_streaming_response.run_scenarios() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scenario = response.parse()
            assert_matches_type(ScenarioRunScenariosResponse, scenario, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_scenario_agent(self, client: Telnyx) -> None:
        scenario = client.ai.tests.test_framework.v1.scenarios.scenario_agent(
            scenarios="all",
            user_message="Make the callers ask about damaged packaging too.",
        )
        assert_matches_type(ScenarioScenarioAgentResponse, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_scenario_agent_with_all_params(self, client: Telnyx) -> None:
        scenario = client.ai.tests.test_framework.v1.scenarios.scenario_agent(
            scenarios="all",
            user_message="Make the callers ask about damaged packaging too.",
            agent_id=1259,
            agent_resolution_response="agent_resolution_response",
            apply_changes=True,
            context=[
                {
                    "content": "content",
                    "role": "role",
                    "timestamp": "timestamp",
                }
            ],
            knowledge_base=[0],
            num_scenarios=0,
            pending_tool_calls=[{"foo": "bar"}],
            scenarios_needing_agent=[0],
            session_id=0,
            updated_scenarios=[{"foo": "bar"}],
        )
        assert_matches_type(ScenarioScenarioAgentResponse, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_scenario_agent(self, client: Telnyx) -> None:
        response = client.ai.tests.test_framework.v1.scenarios.with_raw_response.scenario_agent(
            scenarios="all",
            user_message="Make the callers ask about damaged packaging too.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scenario = response.parse()
        assert_matches_type(ScenarioScenarioAgentResponse, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_scenario_agent(self, client: Telnyx) -> None:
        with client.ai.tests.test_framework.v1.scenarios.with_streaming_response.scenario_agent(
            scenarios="all",
            user_message="Make the callers ask about damaged packaging too.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scenario = response.parse()
            assert_matches_type(ScenarioScenarioAgentResponse, scenario, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncScenarios:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        scenario = await async_client.ai.tests.test_framework.v1.scenarios.create(
            name="Refund escalation flow",
            personality=4643,
        )
        assert_matches_type(EvaluatorScenarioDetail, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        scenario = await async_client.ai.tests.test_framework.v1.scenarios.create(
            name="Refund escalation flow",
            personality=4643,
            agent=1259,
            expected_outcome_prompt="The assistant explains the refund policy and offers escalation.",
            first_message="Hi, I want a refund.",
            folder_path="folder_path",
            instructions="Call the support line and demand a refund for a damaged product.",
            metrics=[266881],
            tags=["support"],
            test_profile=0,
        )
        assert_matches_type(EvaluatorScenarioDetail, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.tests.test_framework.v1.scenarios.with_raw_response.create(
            name="Refund escalation flow",
            personality=4643,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scenario = await response.parse()
        assert_matches_type(EvaluatorScenarioDetail, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.tests.test_framework.v1.scenarios.with_streaming_response.create(
            name="Refund escalation flow",
            personality=4643,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scenario = await response.parse()
            assert_matches_type(EvaluatorScenarioDetail, scenario, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        scenario = await async_client.ai.tests.test_framework.v1.scenarios.retrieve(
            0,
        )
        assert_matches_type(EvaluatorScenarioDetail, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.tests.test_framework.v1.scenarios.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scenario = await response.parse()
        assert_matches_type(EvaluatorScenarioDetail, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.tests.test_framework.v1.scenarios.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scenario = await response.parse()
            assert_matches_type(EvaluatorScenarioDetail, scenario, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        scenario = await async_client.ai.tests.test_framework.v1.scenarios.update(
            id=0,
        )
        assert_matches_type(EvaluatorScenarioDetail, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        scenario = await async_client.ai.tests.test_framework.v1.scenarios.update(
            id=0,
            agent=0,
            expected_outcome_prompt="expected_outcome_prompt",
            first_message="first_message",
            folder_path="folder_path",
            inbound_phone_number=0,
            instructions="Call the support line, demand a refund, and mention the damaged packaging.",
            max_duration=0,
            metrics=[266881, 266882],
            name="Refund escalation flow - updated",
            personality=0,
            phone_number=0,
            scenario_language="scenario_language",
            tags=["string"],
            test_profile=0,
            tool_ids=["string"],
        )
        assert_matches_type(EvaluatorScenarioDetail, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.tests.test_framework.v1.scenarios.with_raw_response.update(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scenario = await response.parse()
        assert_matches_type(EvaluatorScenarioDetail, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.tests.test_framework.v1.scenarios.with_streaming_response.update(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scenario = await response.parse()
            assert_matches_type(EvaluatorScenarioDetail, scenario, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        scenario = await async_client.ai.tests.test_framework.v1.scenarios.list()
        assert_matches_type(ScenarioListResponse, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        scenario = await async_client.ai.tests.test_framework.v1.scenarios.list(
            agent_id=0,
            assistant_id="assistant_id",
            page=1,
            page_size=1,
            tags="tags",
        )
        assert_matches_type(ScenarioListResponse, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.tests.test_framework.v1.scenarios.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scenario = await response.parse()
        assert_matches_type(ScenarioListResponse, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.tests.test_framework.v1.scenarios.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scenario = await response.parse()
            assert_matches_type(ScenarioListResponse, scenario, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        scenario = await async_client.ai.tests.test_framework.v1.scenarios.delete(
            0,
        )
        assert_matches_type(object, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.tests.test_framework.v1.scenarios.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scenario = await response.parse()
        assert_matches_type(object, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.tests.test_framework.v1.scenarios.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scenario = await response.parse()
            assert_matches_type(object, scenario, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate_bg(self, async_client: AsyncTelnyx) -> None:
        scenario = await async_client.ai.tests.test_framework.v1.scenarios.generate_bg(
            num_scenarios=5,
        )
        assert_matches_type(ScenarioGenerationResponse, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate_bg_with_all_params(self, async_client: AsyncTelnyx) -> None:
        scenario = await async_client.ai.tests.test_framework.v1.scenarios.generate_bg(
            num_scenarios=5,
            agent_id=1259,
            extra_instructions="Focus on angry customers asking about refunds.",
            first_message="first_message",
            folder_path="folder_path",
            generate_expected_outcomes=True,
            inbound_phone_number=0,
            personalities=[0],
            scenario_type="workflow",
            tags=["string"],
            test_profile=0,
            tool_ids=["string"],
        )
        assert_matches_type(ScenarioGenerationResponse, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_generate_bg(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.tests.test_framework.v1.scenarios.with_raw_response.generate_bg(
            num_scenarios=5,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scenario = await response.parse()
        assert_matches_type(ScenarioGenerationResponse, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_generate_bg(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.tests.test_framework.v1.scenarios.with_streaming_response.generate_bg(
            num_scenarios=5,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scenario = await response.parse()
            assert_matches_type(ScenarioGenerationResponse, scenario, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve_export_scenarios(self, async_client: AsyncTelnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/ai/tests/test_framework/v1/scenarios/export_scenarios").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        scenario = await async_client.ai.tests.test_framework.v1.scenarios.retrieve_export_scenarios(
            export_type="csv",
            scenario_ids="scenario_ids",
        )
        assert scenario.is_closed
        assert await scenario.json() == {"foo": "bar"}
        assert cast(Any, scenario.is_closed) is True
        assert isinstance(scenario, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve_export_scenarios_with_all_params(
        self, async_client: AsyncTelnyx, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/ai/tests/test_framework/v1/scenarios/export_scenarios").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        scenario = await async_client.ai.tests.test_framework.v1.scenarios.retrieve_export_scenarios(
            export_type="csv",
            scenario_ids="scenario_ids",
            agent_id=0,
        )
        assert scenario.is_closed
        assert await scenario.json() == {"foo": "bar"}
        assert cast(Any, scenario.is_closed) is True
        assert isinstance(scenario, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve_export_scenarios(
        self, async_client: AsyncTelnyx, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/ai/tests/test_framework/v1/scenarios/export_scenarios").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        scenario = await async_client.ai.tests.test_framework.v1.scenarios.with_raw_response.retrieve_export_scenarios(
            export_type="csv",
            scenario_ids="scenario_ids",
        )

        assert scenario.is_closed is True
        assert scenario.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await scenario.json() == {"foo": "bar"}
        assert isinstance(scenario, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve_export_scenarios(
        self, async_client: AsyncTelnyx, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/ai/tests/test_framework/v1/scenarios/export_scenarios").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.ai.tests.test_framework.v1.scenarios.with_streaming_response.retrieve_export_scenarios(
            export_type="csv",
            scenario_ids="scenario_ids",
        ) as scenario:
            assert not scenario.is_closed
            assert scenario.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await scenario.json() == {"foo": "bar"}
            assert cast(Any, scenario.is_closed) is True
            assert isinstance(scenario, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, scenario.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_generate_progress(self, async_client: AsyncTelnyx) -> None:
        scenario = await async_client.ai.tests.test_framework.v1.scenarios.retrieve_generate_progress(
            progress_id="progress_id",
        )
        assert_matches_type(ScenarioRetrieveGenerateProgressResponse, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_generate_progress(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.tests.test_framework.v1.scenarios.with_raw_response.retrieve_generate_progress(
            progress_id="progress_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scenario = await response.parse()
        assert_matches_type(ScenarioRetrieveGenerateProgressResponse, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_generate_progress(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.tests.test_framework.v1.scenarios.with_streaming_response.retrieve_generate_progress(
            progress_id="progress_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scenario = await response.parse()
            assert_matches_type(ScenarioRetrieveGenerateProgressResponse, scenario, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_scenario_agent_progress(self, async_client: AsyncTelnyx) -> None:
        scenario = await async_client.ai.tests.test_framework.v1.scenarios.retrieve_scenario_agent_progress(
            progress_id="progress_id",
        )
        assert_matches_type(ScenarioRetrieveScenarioAgentProgressResponse, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_scenario_agent_progress(self, async_client: AsyncTelnyx) -> None:
        response = (
            await async_client.ai.tests.test_framework.v1.scenarios.with_raw_response.retrieve_scenario_agent_progress(
                progress_id="progress_id",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scenario = await response.parse()
        assert_matches_type(ScenarioRetrieveScenarioAgentProgressResponse, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_scenario_agent_progress(self, async_client: AsyncTelnyx) -> None:
        async with (
            async_client.ai.tests.test_framework.v1.scenarios.with_streaming_response.retrieve_scenario_agent_progress(
                progress_id="progress_id",
            )
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scenario = await response.parse()
            assert_matches_type(ScenarioRetrieveScenarioAgentProgressResponse, scenario, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run_scenarios(self, async_client: AsyncTelnyx) -> None:
        scenario = await async_client.ai.tests.test_framework.v1.scenarios.run_scenarios()
        assert_matches_type(ScenarioRunScenariosResponse, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run_scenarios_with_all_params(self, async_client: AsyncTelnyx) -> None:
        scenario = await async_client.ai.tests.test_framework.v1.scenarios.run_scenarios(
            agent_id=1259,
            agent_number="agent_number",
            assistant_id="assistant_id",
            concurrency_limit=3,
            frequency=0,
            mode="same_number",
            name="name",
            outbound_phone_number="outbound_phone_number",
            personality_ids=[0],
            scenarios=[9512],
            tags=["regression"],
            test_profile_ids=[0],
        )
        assert_matches_type(ScenarioRunScenariosResponse, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_run_scenarios(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.tests.test_framework.v1.scenarios.with_raw_response.run_scenarios()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scenario = await response.parse()
        assert_matches_type(ScenarioRunScenariosResponse, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_run_scenarios(self, async_client: AsyncTelnyx) -> None:
        async with (
            async_client.ai.tests.test_framework.v1.scenarios.with_streaming_response.run_scenarios()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scenario = await response.parse()
            assert_matches_type(ScenarioRunScenariosResponse, scenario, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_scenario_agent(self, async_client: AsyncTelnyx) -> None:
        scenario = await async_client.ai.tests.test_framework.v1.scenarios.scenario_agent(
            scenarios="all",
            user_message="Make the callers ask about damaged packaging too.",
        )
        assert_matches_type(ScenarioScenarioAgentResponse, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_scenario_agent_with_all_params(self, async_client: AsyncTelnyx) -> None:
        scenario = await async_client.ai.tests.test_framework.v1.scenarios.scenario_agent(
            scenarios="all",
            user_message="Make the callers ask about damaged packaging too.",
            agent_id=1259,
            agent_resolution_response="agent_resolution_response",
            apply_changes=True,
            context=[
                {
                    "content": "content",
                    "role": "role",
                    "timestamp": "timestamp",
                }
            ],
            knowledge_base=[0],
            num_scenarios=0,
            pending_tool_calls=[{"foo": "bar"}],
            scenarios_needing_agent=[0],
            session_id=0,
            updated_scenarios=[{"foo": "bar"}],
        )
        assert_matches_type(ScenarioScenarioAgentResponse, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_scenario_agent(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.tests.test_framework.v1.scenarios.with_raw_response.scenario_agent(
            scenarios="all",
            user_message="Make the callers ask about damaged packaging too.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scenario = await response.parse()
        assert_matches_type(ScenarioScenarioAgentResponse, scenario, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_scenario_agent(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.tests.test_framework.v1.scenarios.with_streaming_response.scenario_agent(
            scenarios="all",
            user_message="Make the callers ask about damaged packaging too.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scenario = await response.parse()
            assert_matches_type(ScenarioScenarioAgentResponse, scenario, path=["response"])

        assert cast(Any, response.is_closed) is True

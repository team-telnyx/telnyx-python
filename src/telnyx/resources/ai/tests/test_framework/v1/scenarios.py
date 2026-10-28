# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal

import httpx

from ......_types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ......_utils import path_template, maybe_transform, async_maybe_transform
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ......_base_client import make_request_options
from ......types.ai.tests.test_framework.v1 import (
    scenario_list_params,
    scenario_create_params,
    scenario_update_params,
    scenario_generate_bg_params,
    scenario_run_scenarios_params,
    scenario_scenario_agent_params,
    scenario_retrieve_export_scenarios_params,
    scenario_retrieve_generate_progress_params,
    scenario_retrieve_scenario_agent_progress_params,
)
from ......types.ai.tests.test_framework.v1.scenario_list_response import ScenarioListResponse
from ......types.ai.tests.test_framework.v1.evaluator_scenario_detail import EvaluatorScenarioDetail
from ......types.ai.tests.test_framework.v1.scenario_generation_response import ScenarioGenerationResponse
from ......types.ai.tests.test_framework.v1.scenario_run_scenarios_response import ScenarioRunScenariosResponse
from ......types.ai.tests.test_framework.v1.scenario_scenario_agent_response import ScenarioScenarioAgentResponse
from ......types.ai.tests.test_framework.v1.scenario_retrieve_generate_progress_response import (
    ScenarioRetrieveGenerateProgressResponse,
)
from ......types.ai.tests.test_framework.v1.scenario_retrieve_scenario_agent_progress_response import (
    ScenarioRetrieveScenarioAgentProgressResponse,
)

__all__ = ["ScenariosResource", "AsyncScenariosResource"]


class ScenariosResource(SyncAPIResource):
    """
    Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
    """

    @cached_property
    def with_raw_response(self) -> ScenariosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ScenariosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScenariosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ScenariosResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        personality: int,
        agent: Optional[int] | Omit = omit,
        expected_outcome_prompt: str | Omit = omit,
        first_message: str | Omit = omit,
        folder_path: Optional[str] | Omit = omit,
        instructions: str | Omit = omit,
        metrics: Iterable[int] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        test_profile: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluatorScenarioDetail:
        """
        Creates an evaluator scenario in your organization.

        Args:
          personality: ID of the personality the caller simulates.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/tests/test_framework/v1/scenarios",
            body=maybe_transform(
                {
                    "name": name,
                    "personality": personality,
                    "agent": agent,
                    "expected_outcome_prompt": expected_outcome_prompt,
                    "first_message": first_message,
                    "folder_path": folder_path,
                    "instructions": instructions,
                    "metrics": metrics,
                    "tags": tags,
                    "test_profile": test_profile,
                },
                scenario_create_params.ScenarioCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluatorScenarioDetail,
        )

    def retrieve(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluatorScenarioDetail:
        """
        Returns the specified evaluator scenario with full detail.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/ai/tests/test_framework/v1/scenarios/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluatorScenarioDetail,
        )

    def update(
        self,
        id: int,
        *,
        agent: Optional[int] | Omit = omit,
        expected_outcome_prompt: str | Omit = omit,
        first_message: str | Omit = omit,
        folder_path: Optional[str] | Omit = omit,
        inbound_phone_number: int | Omit = omit,
        instructions: str | Omit = omit,
        max_duration: Optional[int] | Omit = omit,
        metrics: Iterable[int] | Omit = omit,
        name: str | Omit = omit,
        personality: int | Omit = omit,
        phone_number: int | Omit = omit,
        scenario_language: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        test_profile: int | Omit = omit,
        tool_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluatorScenarioDetail:
        """
        Updates the specified evaluator scenario.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            path_template("/ai/tests/test_framework/v1/scenarios/{id}", id=id),
            body=maybe_transform(
                {
                    "agent": agent,
                    "expected_outcome_prompt": expected_outcome_prompt,
                    "first_message": first_message,
                    "folder_path": folder_path,
                    "inbound_phone_number": inbound_phone_number,
                    "instructions": instructions,
                    "max_duration": max_duration,
                    "metrics": metrics,
                    "name": name,
                    "personality": personality,
                    "phone_number": phone_number,
                    "scenario_language": scenario_language,
                    "tags": tags,
                    "test_profile": test_profile,
                    "tool_ids": tool_ids,
                },
                scenario_update_params.ScenarioUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluatorScenarioDetail,
        )

    def list(
        self,
        *,
        agent_id: int | Omit = omit,
        assistant_id: str | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        tags: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScenarioListResponse:
        """
        Returns a paginated list of evaluator scenarios in your organization, optionally
        filtered by test agent or tags.

        Args:
          agent_id: Filter scenarios belonging to the specified test agent.

          assistant_id: Filter scenarios belonging to the specified Telnyx assistant.

          page: Page number (1-based).

          page_size: Number of results per page.

          tags: Filter scenarios by a comma-separated list of tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/ai/tests/test_framework/v1/scenarios",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agent_id": agent_id,
                        "assistant_id": assistant_id,
                        "page": page,
                        "page_size": page_size,
                        "tags": tags,
                    },
                    scenario_list_params.ScenarioListParams,
                ),
            ),
            cast_to=ScenarioListResponse,
        )

    def delete(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes the specified evaluator scenario.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            path_template("/ai/tests/test_framework/v1/scenarios/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def generate_bg(
        self,
        *,
        num_scenarios: int,
        agent_id: int | Omit = omit,
        extra_instructions: str | Omit = omit,
        first_message: str | Omit = omit,
        folder_path: Optional[str] | Omit = omit,
        generate_expected_outcomes: bool | Omit = omit,
        inbound_phone_number: Optional[int] | Omit = omit,
        personalities: Iterable[int] | Omit = omit,
        scenario_type: Literal["workflow", "red_teaming_voice", "red_teaming_text"] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        test_profile: int | Omit = omit,
        tool_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScenarioGenerationResponse:
        """Starts background generation of evaluator scenarios for a test agent.

        Returns a
        progress ID to poll with the generate-scenarios-progress endpoint.

        Args:
          num_scenarios: How many scenarios to generate.

          extra_instructions: Optional guidance steering scenario generation.

          generate_expected_outcomes: Whether to generate expected-outcome prompts for the scenarios.

          scenario_type: Type of scenario to generate.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/tests/test_framework/v1/scenarios/generate-bg",
            body=maybe_transform(
                {
                    "num_scenarios": num_scenarios,
                    "agent_id": agent_id,
                    "extra_instructions": extra_instructions,
                    "first_message": first_message,
                    "folder_path": folder_path,
                    "generate_expected_outcomes": generate_expected_outcomes,
                    "inbound_phone_number": inbound_phone_number,
                    "personalities": personalities,
                    "scenario_type": scenario_type,
                    "tags": tags,
                    "test_profile": test_profile,
                    "tool_ids": tool_ids,
                },
                scenario_generate_bg_params.ScenarioGenerateBgParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScenarioGenerationResponse,
        )

    def retrieve_export_scenarios(
        self,
        *,
        export_type: Literal["csv", "xlsx"],
        scenario_ids: str,
        agent_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Exports the selected evaluator scenarios as a CSV or XLSX file download.

        Args:
          export_type: File format of the export.

          scenario_ids: Comma-separated scenario IDs to export.

          agent_id: Export scenarios belonging to the specified test agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            "Accept": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            **(extra_headers or {}),
        }
        return self._get(
            "/ai/tests/test_framework/v1/scenarios/export_scenarios",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "export_type": export_type,
                        "scenario_ids": scenario_ids,
                        "agent_id": agent_id,
                    },
                    scenario_retrieve_export_scenarios_params.ScenarioRetrieveExportScenariosParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )

    def retrieve_generate_progress(
        self,
        *,
        progress_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScenarioRetrieveGenerateProgressResponse:
        """
        Returns the status of a background scenario-generation job started with the
        generate-evaluator-scenarios endpoint.

        Args:
          progress_id: Progress ID returned by the generate-evaluator-scenarios endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/ai/tests/test_framework/v1/scenarios/generate-progress",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"progress_id": progress_id},
                    scenario_retrieve_generate_progress_params.ScenarioRetrieveGenerateProgressParams,
                ),
            ),
            cast_to=ScenarioRetrieveGenerateProgressResponse,
        )

    def retrieve_scenario_agent_progress(
        self,
        *,
        progress_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScenarioRetrieveScenarioAgentProgressResponse:
        """
        Returns the status of an improve-scenarios session started with the
        improve-evaluator-scenarios endpoint.

        Args:
          progress_id: Progress ID returned by the improve-evaluator-scenarios endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/ai/tests/test_framework/v1/scenarios/scenario-agent-progress",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"progress_id": progress_id},
                    scenario_retrieve_scenario_agent_progress_params.ScenarioRetrieveScenarioAgentProgressParams,
                ),
            ),
            cast_to=ScenarioRetrieveScenarioAgentProgressResponse,
        )

    def run_scenarios(
        self,
        *,
        agent_id: int | Omit = omit,
        agent_number: str | Omit = omit,
        assistant_id: str | Omit = omit,
        concurrency_limit: int | Omit = omit,
        frequency: int | Omit = omit,
        mode: Literal["same_number", "different_numbers"] | Omit = omit,
        name: str | Omit = omit,
        outbound_phone_number: str | Omit = omit,
        personality_ids: Iterable[int] | Omit = omit,
        scenarios: Union[Iterable[object], str] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        test_profile_ids: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScenarioRunScenariosResponse:
        """
        Runs the selected evaluator scenarios against their test agents and creates a
        run batch. Returns the ID of the created batch, whose results can be listed with
        the test-run-results endpoints.

        Args:
          concurrency_limit: Maximum number of concurrent simulated calls.

          scenarios: Scenario IDs to run, or the literal string 'all'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/tests/test_framework/v1/scenarios/run_scenarios",
            body=maybe_transform(
                {
                    "agent_id": agent_id,
                    "agent_number": agent_number,
                    "assistant_id": assistant_id,
                    "concurrency_limit": concurrency_limit,
                    "frequency": frequency,
                    "mode": mode,
                    "name": name,
                    "outbound_phone_number": outbound_phone_number,
                    "personality_ids": personality_ids,
                    "scenarios": scenarios,
                    "tags": tags,
                    "test_profile_ids": test_profile_ids,
                },
                scenario_run_scenarios_params.ScenarioRunScenariosParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScenarioRunScenariosResponse,
        )

    def scenario_agent(
        self,
        *,
        scenarios: Union[Iterable[object], str],
        user_message: str,
        agent_id: Optional[int] | Omit = omit,
        agent_resolution_response: str | Omit = omit,
        apply_changes: bool | Omit = omit,
        context: Optional[Iterable[scenario_scenario_agent_params.Context]] | Omit = omit,
        knowledge_base: Iterable[int] | Omit = omit,
        num_scenarios: int | Omit = omit,
        pending_tool_calls: Optional[Iterable[Dict[str, object]]] | Omit = omit,
        scenarios_needing_agent: Iterable[int] | Omit = omit,
        session_id: Optional[int] | Omit = omit,
        updated_scenarios: Iterable[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScenarioScenarioAgentResponse:
        """
        Starts an interactive session that improves selected evaluator scenarios from a
        natural-language instruction. Returns a progress ID to poll with the
        improve-scenarios-progress endpoint.

        Args:
          scenarios: Scenario IDs to improve, or the literal string 'all'.

          user_message: What the assistant should improve about the selected scenarios.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/tests/test_framework/v1/scenarios/scenario-agent",
            body=maybe_transform(
                {
                    "scenarios": scenarios,
                    "user_message": user_message,
                    "agent_id": agent_id,
                    "agent_resolution_response": agent_resolution_response,
                    "apply_changes": apply_changes,
                    "context": context,
                    "knowledge_base": knowledge_base,
                    "num_scenarios": num_scenarios,
                    "pending_tool_calls": pending_tool_calls,
                    "scenarios_needing_agent": scenarios_needing_agent,
                    "session_id": session_id,
                    "updated_scenarios": updated_scenarios,
                },
                scenario_scenario_agent_params.ScenarioScenarioAgentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScenarioScenarioAgentResponse,
        )


class AsyncScenariosResource(AsyncAPIResource):
    """
    Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
    """

    @cached_property
    def with_raw_response(self) -> AsyncScenariosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScenariosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScenariosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncScenariosResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        personality: int,
        agent: Optional[int] | Omit = omit,
        expected_outcome_prompt: str | Omit = omit,
        first_message: str | Omit = omit,
        folder_path: Optional[str] | Omit = omit,
        instructions: str | Omit = omit,
        metrics: Iterable[int] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        test_profile: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluatorScenarioDetail:
        """
        Creates an evaluator scenario in your organization.

        Args:
          personality: ID of the personality the caller simulates.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/tests/test_framework/v1/scenarios",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "personality": personality,
                    "agent": agent,
                    "expected_outcome_prompt": expected_outcome_prompt,
                    "first_message": first_message,
                    "folder_path": folder_path,
                    "instructions": instructions,
                    "metrics": metrics,
                    "tags": tags,
                    "test_profile": test_profile,
                },
                scenario_create_params.ScenarioCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluatorScenarioDetail,
        )

    async def retrieve(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluatorScenarioDetail:
        """
        Returns the specified evaluator scenario with full detail.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/ai/tests/test_framework/v1/scenarios/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluatorScenarioDetail,
        )

    async def update(
        self,
        id: int,
        *,
        agent: Optional[int] | Omit = omit,
        expected_outcome_prompt: str | Omit = omit,
        first_message: str | Omit = omit,
        folder_path: Optional[str] | Omit = omit,
        inbound_phone_number: int | Omit = omit,
        instructions: str | Omit = omit,
        max_duration: Optional[int] | Omit = omit,
        metrics: Iterable[int] | Omit = omit,
        name: str | Omit = omit,
        personality: int | Omit = omit,
        phone_number: int | Omit = omit,
        scenario_language: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        test_profile: int | Omit = omit,
        tool_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EvaluatorScenarioDetail:
        """
        Updates the specified evaluator scenario.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            path_template("/ai/tests/test_framework/v1/scenarios/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "agent": agent,
                    "expected_outcome_prompt": expected_outcome_prompt,
                    "first_message": first_message,
                    "folder_path": folder_path,
                    "inbound_phone_number": inbound_phone_number,
                    "instructions": instructions,
                    "max_duration": max_duration,
                    "metrics": metrics,
                    "name": name,
                    "personality": personality,
                    "phone_number": phone_number,
                    "scenario_language": scenario_language,
                    "tags": tags,
                    "test_profile": test_profile,
                    "tool_ids": tool_ids,
                },
                scenario_update_params.ScenarioUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluatorScenarioDetail,
        )

    async def list(
        self,
        *,
        agent_id: int | Omit = omit,
        assistant_id: str | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        tags: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScenarioListResponse:
        """
        Returns a paginated list of evaluator scenarios in your organization, optionally
        filtered by test agent or tags.

        Args:
          agent_id: Filter scenarios belonging to the specified test agent.

          assistant_id: Filter scenarios belonging to the specified Telnyx assistant.

          page: Page number (1-based).

          page_size: Number of results per page.

          tags: Filter scenarios by a comma-separated list of tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/ai/tests/test_framework/v1/scenarios",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agent_id": agent_id,
                        "assistant_id": assistant_id,
                        "page": page,
                        "page_size": page_size,
                        "tags": tags,
                    },
                    scenario_list_params.ScenarioListParams,
                ),
            ),
            cast_to=ScenarioListResponse,
        )

    async def delete(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes the specified evaluator scenario.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            path_template("/ai/tests/test_framework/v1/scenarios/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def generate_bg(
        self,
        *,
        num_scenarios: int,
        agent_id: int | Omit = omit,
        extra_instructions: str | Omit = omit,
        first_message: str | Omit = omit,
        folder_path: Optional[str] | Omit = omit,
        generate_expected_outcomes: bool | Omit = omit,
        inbound_phone_number: Optional[int] | Omit = omit,
        personalities: Iterable[int] | Omit = omit,
        scenario_type: Literal["workflow", "red_teaming_voice", "red_teaming_text"] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        test_profile: int | Omit = omit,
        tool_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScenarioGenerationResponse:
        """Starts background generation of evaluator scenarios for a test agent.

        Returns a
        progress ID to poll with the generate-scenarios-progress endpoint.

        Args:
          num_scenarios: How many scenarios to generate.

          extra_instructions: Optional guidance steering scenario generation.

          generate_expected_outcomes: Whether to generate expected-outcome prompts for the scenarios.

          scenario_type: Type of scenario to generate.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/tests/test_framework/v1/scenarios/generate-bg",
            body=await async_maybe_transform(
                {
                    "num_scenarios": num_scenarios,
                    "agent_id": agent_id,
                    "extra_instructions": extra_instructions,
                    "first_message": first_message,
                    "folder_path": folder_path,
                    "generate_expected_outcomes": generate_expected_outcomes,
                    "inbound_phone_number": inbound_phone_number,
                    "personalities": personalities,
                    "scenario_type": scenario_type,
                    "tags": tags,
                    "test_profile": test_profile,
                    "tool_ids": tool_ids,
                },
                scenario_generate_bg_params.ScenarioGenerateBgParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScenarioGenerationResponse,
        )

    async def retrieve_export_scenarios(
        self,
        *,
        export_type: Literal["csv", "xlsx"],
        scenario_ids: str,
        agent_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Exports the selected evaluator scenarios as a CSV or XLSX file download.

        Args:
          export_type: File format of the export.

          scenario_ids: Comma-separated scenario IDs to export.

          agent_id: Export scenarios belonging to the specified test agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            "Accept": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            **(extra_headers or {}),
        }
        return await self._get(
            "/ai/tests/test_framework/v1/scenarios/export_scenarios",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "export_type": export_type,
                        "scenario_ids": scenario_ids,
                        "agent_id": agent_id,
                    },
                    scenario_retrieve_export_scenarios_params.ScenarioRetrieveExportScenariosParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def retrieve_generate_progress(
        self,
        *,
        progress_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScenarioRetrieveGenerateProgressResponse:
        """
        Returns the status of a background scenario-generation job started with the
        generate-evaluator-scenarios endpoint.

        Args:
          progress_id: Progress ID returned by the generate-evaluator-scenarios endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/ai/tests/test_framework/v1/scenarios/generate-progress",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"progress_id": progress_id},
                    scenario_retrieve_generate_progress_params.ScenarioRetrieveGenerateProgressParams,
                ),
            ),
            cast_to=ScenarioRetrieveGenerateProgressResponse,
        )

    async def retrieve_scenario_agent_progress(
        self,
        *,
        progress_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScenarioRetrieveScenarioAgentProgressResponse:
        """
        Returns the status of an improve-scenarios session started with the
        improve-evaluator-scenarios endpoint.

        Args:
          progress_id: Progress ID returned by the improve-evaluator-scenarios endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/ai/tests/test_framework/v1/scenarios/scenario-agent-progress",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"progress_id": progress_id},
                    scenario_retrieve_scenario_agent_progress_params.ScenarioRetrieveScenarioAgentProgressParams,
                ),
            ),
            cast_to=ScenarioRetrieveScenarioAgentProgressResponse,
        )

    async def run_scenarios(
        self,
        *,
        agent_id: int | Omit = omit,
        agent_number: str | Omit = omit,
        assistant_id: str | Omit = omit,
        concurrency_limit: int | Omit = omit,
        frequency: int | Omit = omit,
        mode: Literal["same_number", "different_numbers"] | Omit = omit,
        name: str | Omit = omit,
        outbound_phone_number: str | Omit = omit,
        personality_ids: Iterable[int] | Omit = omit,
        scenarios: Union[Iterable[object], str] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        test_profile_ids: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScenarioRunScenariosResponse:
        """
        Runs the selected evaluator scenarios against their test agents and creates a
        run batch. Returns the ID of the created batch, whose results can be listed with
        the test-run-results endpoints.

        Args:
          concurrency_limit: Maximum number of concurrent simulated calls.

          scenarios: Scenario IDs to run, or the literal string 'all'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/tests/test_framework/v1/scenarios/run_scenarios",
            body=await async_maybe_transform(
                {
                    "agent_id": agent_id,
                    "agent_number": agent_number,
                    "assistant_id": assistant_id,
                    "concurrency_limit": concurrency_limit,
                    "frequency": frequency,
                    "mode": mode,
                    "name": name,
                    "outbound_phone_number": outbound_phone_number,
                    "personality_ids": personality_ids,
                    "scenarios": scenarios,
                    "tags": tags,
                    "test_profile_ids": test_profile_ids,
                },
                scenario_run_scenarios_params.ScenarioRunScenariosParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScenarioRunScenariosResponse,
        )

    async def scenario_agent(
        self,
        *,
        scenarios: Union[Iterable[object], str],
        user_message: str,
        agent_id: Optional[int] | Omit = omit,
        agent_resolution_response: str | Omit = omit,
        apply_changes: bool | Omit = omit,
        context: Optional[Iterable[scenario_scenario_agent_params.Context]] | Omit = omit,
        knowledge_base: Iterable[int] | Omit = omit,
        num_scenarios: int | Omit = omit,
        pending_tool_calls: Optional[Iterable[Dict[str, object]]] | Omit = omit,
        scenarios_needing_agent: Iterable[int] | Omit = omit,
        session_id: Optional[int] | Omit = omit,
        updated_scenarios: Iterable[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScenarioScenarioAgentResponse:
        """
        Starts an interactive session that improves selected evaluator scenarios from a
        natural-language instruction. Returns a progress ID to poll with the
        improve-scenarios-progress endpoint.

        Args:
          scenarios: Scenario IDs to improve, or the literal string 'all'.

          user_message: What the assistant should improve about the selected scenarios.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/tests/test_framework/v1/scenarios/scenario-agent",
            body=await async_maybe_transform(
                {
                    "scenarios": scenarios,
                    "user_message": user_message,
                    "agent_id": agent_id,
                    "agent_resolution_response": agent_resolution_response,
                    "apply_changes": apply_changes,
                    "context": context,
                    "knowledge_base": knowledge_base,
                    "num_scenarios": num_scenarios,
                    "pending_tool_calls": pending_tool_calls,
                    "scenarios_needing_agent": scenarios_needing_agent,
                    "session_id": session_id,
                    "updated_scenarios": updated_scenarios,
                },
                scenario_scenario_agent_params.ScenarioScenarioAgentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScenarioScenarioAgentResponse,
        )


class ScenariosResourceWithRawResponse:
    def __init__(self, scenarios: ScenariosResource) -> None:
        self._scenarios = scenarios

        self.create = to_raw_response_wrapper(
            scenarios.create,
        )
        self.retrieve = to_raw_response_wrapper(
            scenarios.retrieve,
        )
        self.update = to_raw_response_wrapper(
            scenarios.update,
        )
        self.list = to_raw_response_wrapper(
            scenarios.list,
        )
        self.delete = to_raw_response_wrapper(
            scenarios.delete,
        )
        self.generate_bg = to_raw_response_wrapper(
            scenarios.generate_bg,
        )
        self.retrieve_export_scenarios = to_custom_raw_response_wrapper(
            scenarios.retrieve_export_scenarios,
            BinaryAPIResponse,
        )
        self.retrieve_generate_progress = to_raw_response_wrapper(
            scenarios.retrieve_generate_progress,
        )
        self.retrieve_scenario_agent_progress = to_raw_response_wrapper(
            scenarios.retrieve_scenario_agent_progress,
        )
        self.run_scenarios = to_raw_response_wrapper(
            scenarios.run_scenarios,
        )
        self.scenario_agent = to_raw_response_wrapper(
            scenarios.scenario_agent,
        )


class AsyncScenariosResourceWithRawResponse:
    def __init__(self, scenarios: AsyncScenariosResource) -> None:
        self._scenarios = scenarios

        self.create = async_to_raw_response_wrapper(
            scenarios.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            scenarios.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            scenarios.update,
        )
        self.list = async_to_raw_response_wrapper(
            scenarios.list,
        )
        self.delete = async_to_raw_response_wrapper(
            scenarios.delete,
        )
        self.generate_bg = async_to_raw_response_wrapper(
            scenarios.generate_bg,
        )
        self.retrieve_export_scenarios = async_to_custom_raw_response_wrapper(
            scenarios.retrieve_export_scenarios,
            AsyncBinaryAPIResponse,
        )
        self.retrieve_generate_progress = async_to_raw_response_wrapper(
            scenarios.retrieve_generate_progress,
        )
        self.retrieve_scenario_agent_progress = async_to_raw_response_wrapper(
            scenarios.retrieve_scenario_agent_progress,
        )
        self.run_scenarios = async_to_raw_response_wrapper(
            scenarios.run_scenarios,
        )
        self.scenario_agent = async_to_raw_response_wrapper(
            scenarios.scenario_agent,
        )


class ScenariosResourceWithStreamingResponse:
    def __init__(self, scenarios: ScenariosResource) -> None:
        self._scenarios = scenarios

        self.create = to_streamed_response_wrapper(
            scenarios.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            scenarios.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            scenarios.update,
        )
        self.list = to_streamed_response_wrapper(
            scenarios.list,
        )
        self.delete = to_streamed_response_wrapper(
            scenarios.delete,
        )
        self.generate_bg = to_streamed_response_wrapper(
            scenarios.generate_bg,
        )
        self.retrieve_export_scenarios = to_custom_streamed_response_wrapper(
            scenarios.retrieve_export_scenarios,
            StreamedBinaryAPIResponse,
        )
        self.retrieve_generate_progress = to_streamed_response_wrapper(
            scenarios.retrieve_generate_progress,
        )
        self.retrieve_scenario_agent_progress = to_streamed_response_wrapper(
            scenarios.retrieve_scenario_agent_progress,
        )
        self.run_scenarios = to_streamed_response_wrapper(
            scenarios.run_scenarios,
        )
        self.scenario_agent = to_streamed_response_wrapper(
            scenarios.scenario_agent,
        )


class AsyncScenariosResourceWithStreamingResponse:
    def __init__(self, scenarios: AsyncScenariosResource) -> None:
        self._scenarios = scenarios

        self.create = async_to_streamed_response_wrapper(
            scenarios.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            scenarios.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            scenarios.update,
        )
        self.list = async_to_streamed_response_wrapper(
            scenarios.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            scenarios.delete,
        )
        self.generate_bg = async_to_streamed_response_wrapper(
            scenarios.generate_bg,
        )
        self.retrieve_export_scenarios = async_to_custom_streamed_response_wrapper(
            scenarios.retrieve_export_scenarios,
            AsyncStreamedBinaryAPIResponse,
        )
        self.retrieve_generate_progress = async_to_streamed_response_wrapper(
            scenarios.retrieve_generate_progress,
        )
        self.retrieve_scenario_agent_progress = async_to_streamed_response_wrapper(
            scenarios.retrieve_scenario_agent_progress,
        )
        self.run_scenarios = async_to_streamed_response_wrapper(
            scenarios.run_scenarios,
        )
        self.scenario_agent = async_to_streamed_response_wrapper(
            scenarios.scenario_agent,
        )

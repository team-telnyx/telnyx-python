# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ......_types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ......_utils import path_template, maybe_transform, async_maybe_transform
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_base_client import make_request_options
from ......types.ai.tests.test_framework.v1 import (
    metric_list_params,
    metric_create_params,
    metric_update_params,
    metric_generate_metrics_params,
    metric_retrieve_generate_metrics_progress_params,
)
from ......types.ai.tests.test_framework.v1.ai_test_metric import AITestMetric
from ......types.ai.tests.test_framework.v1.metric_list_response import MetricListResponse
from ......types.ai.tests.test_framework.v1.metric_bulk_create_response import MetricBulkCreateResponse
from ......types.ai.tests.test_framework.v1.scenario_generation_response import ScenarioGenerationResponse
from ......types.ai.tests.test_framework.v1.create_ai_test_metric_request_param import CreateAITestMetricRequestParam
from ......types.ai.tests.test_framework.v1.metric_retrieve_generate_metrics_progress_response import (
    MetricRetrieveGenerateMetricsProgressResponse,
)

__all__ = ["MetricsResource", "AsyncMetricsResource"]


class MetricsResource(SyncAPIResource):
    """
    Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
    """

    @cached_property
    def with_raw_response(self) -> MetricsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return MetricsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetricsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return MetricsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        add_to_new_agents: Optional[bool] | Omit = omit,
        agents: Iterable[int] | Omit = omit,
        assistant_id: str | Omit = omit,
        audio_enabled: bool | Omit = omit,
        description: str | Omit = omit,
        display_order: int | Omit = omit,
        enum_values: SequenceNotStr[str] | Omit = omit,
        eval_type: str | Omit = omit,
        observability_enabled: bool | Omit = omit,
        prompt: str | Omit = omit,
        sampling_enabled: bool | Omit = omit,
        simulation_enabled: bool | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AITestMetric:
        """
        Creates a metric in your organization.

        Args:
          eval_type: What the metric scores: numeric, continuous_qualitative, or
              binary_workflow_adherence.

          prompt: Judge prompt used by llm_judge metrics.

          type: How the metric is evaluated: custom_code or llm_judge.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/tests/test_framework/v1/metrics",
            body=maybe_transform(
                {
                    "name": name,
                    "add_to_new_agents": add_to_new_agents,
                    "agents": agents,
                    "assistant_id": assistant_id,
                    "audio_enabled": audio_enabled,
                    "description": description,
                    "display_order": display_order,
                    "enum_values": enum_values,
                    "eval_type": eval_type,
                    "observability_enabled": observability_enabled,
                    "prompt": prompt,
                    "sampling_enabled": sampling_enabled,
                    "simulation_enabled": simulation_enabled,
                    "type": type,
                },
                metric_create_params.MetricCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AITestMetric,
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
    ) -> AITestMetric:
        """
        Returns the specified metric.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/ai/tests/test_framework/v1/metrics/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AITestMetric,
        )

    def update(
        self,
        id: int,
        *,
        add_to_new_agents: Optional[bool] | Omit = omit,
        agents: Iterable[int] | Omit = omit,
        audio_enabled: bool | Omit = omit,
        description: str | Omit = omit,
        display_order: int | Omit = omit,
        enum_values: SequenceNotStr[str] | Omit = omit,
        eval_type: str | Omit = omit,
        name: str | Omit = omit,
        observability_enabled: bool | Omit = omit,
        prompt: str | Omit = omit,
        sampling_enabled: bool | Omit = omit,
        simulation_enabled: bool | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AITestMetric:
        """
        Updates the specified metric.

        Args:
          eval_type: What the metric scores: numeric, continuous_qualitative, or
              binary_workflow_adherence.

          prompt: Judge prompt used by llm_judge metrics.

          type: How the metric is evaluated: custom_code or llm_judge.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            path_template("/ai/tests/test_framework/v1/metrics/{id}", id=id),
            body=maybe_transform(
                {
                    "add_to_new_agents": add_to_new_agents,
                    "agents": agents,
                    "audio_enabled": audio_enabled,
                    "description": description,
                    "display_order": display_order,
                    "enum_values": enum_values,
                    "eval_type": eval_type,
                    "name": name,
                    "observability_enabled": observability_enabled,
                    "prompt": prompt,
                    "sampling_enabled": sampling_enabled,
                    "simulation_enabled": simulation_enabled,
                    "type": type,
                },
                metric_update_params.MetricUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AITestMetric,
        )

    def list(
        self,
        *,
        agent_id: int | Omit = omit,
        assistant_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricListResponse:
        """
        Returns the metrics available in your organization, optionally filtered by test
        agent. Each metric scores one aspect of a conversation or scenario run.

        Args:
          agent_id: Filter metrics attached to the specified test agent.

          assistant_id: Filter metrics attached to the specified Telnyx assistant.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/ai/tests/test_framework/v1/metrics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agent_id": agent_id,
                        "assistant_id": assistant_id,
                    },
                    metric_list_params.MetricListParams,
                ),
            ),
            cast_to=MetricListResponse,
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
        Deletes the specified metric.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            path_template("/ai/tests/test_framework/v1/metrics/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def bulk_create(
        self,
        *,
        body: Iterable[CreateAITestMetricRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricBulkCreateResponse:
        """Creates several metrics in one request.

        Accepts an array of metric objects and
        returns the created metrics.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/tests/test_framework/v1/metrics/bulk_create",
            body=maybe_transform(body, Iterable[CreateAITestMetricRequestParam]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricBulkCreateResponse,
        )

    def generate_metrics(
        self,
        *,
        agent_id: int,
        num_metrics: int,
        scenarios: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScenarioGenerationResponse:
        """Starts background generation of suggested metrics for a test agent.

        Returns a
        progress ID to poll with the get-test-metric-generation-progress endpoint.

        Args:
          agent_id: Test agent to suggest metrics for.

          num_metrics: How many metrics to suggest.

          scenarios: Scenario IDs to base the suggestions on.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/tests/test_framework/v1/metrics/generate_metrics",
            body=maybe_transform(
                {
                    "agent_id": agent_id,
                    "num_metrics": num_metrics,
                    "scenarios": scenarios,
                },
                metric_generate_metrics_params.MetricGenerateMetricsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScenarioGenerationResponse,
        )

    def retrieve_generate_metrics_progress(
        self,
        *,
        progress_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricRetrieveGenerateMetricsProgressResponse:
        """
        Returns the status of a background metric-generation job started with the
        generate-test-metrics endpoint.

        Args:
          progress_id: Progress ID returned by the generate-test-metrics endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/ai/tests/test_framework/v1/metrics/generate_metrics_progress",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"progress_id": progress_id},
                    metric_retrieve_generate_metrics_progress_params.MetricRetrieveGenerateMetricsProgressParams,
                ),
            ),
            cast_to=MetricRetrieveGenerateMetricsProgressResponse,
        )


class AsyncMetricsResource(AsyncAPIResource):
    """
    Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
    """

    @cached_property
    def with_raw_response(self) -> AsyncMetricsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMetricsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetricsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncMetricsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        add_to_new_agents: Optional[bool] | Omit = omit,
        agents: Iterable[int] | Omit = omit,
        assistant_id: str | Omit = omit,
        audio_enabled: bool | Omit = omit,
        description: str | Omit = omit,
        display_order: int | Omit = omit,
        enum_values: SequenceNotStr[str] | Omit = omit,
        eval_type: str | Omit = omit,
        observability_enabled: bool | Omit = omit,
        prompt: str | Omit = omit,
        sampling_enabled: bool | Omit = omit,
        simulation_enabled: bool | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AITestMetric:
        """
        Creates a metric in your organization.

        Args:
          eval_type: What the metric scores: numeric, continuous_qualitative, or
              binary_workflow_adherence.

          prompt: Judge prompt used by llm_judge metrics.

          type: How the metric is evaluated: custom_code or llm_judge.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/tests/test_framework/v1/metrics",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "add_to_new_agents": add_to_new_agents,
                    "agents": agents,
                    "assistant_id": assistant_id,
                    "audio_enabled": audio_enabled,
                    "description": description,
                    "display_order": display_order,
                    "enum_values": enum_values,
                    "eval_type": eval_type,
                    "observability_enabled": observability_enabled,
                    "prompt": prompt,
                    "sampling_enabled": sampling_enabled,
                    "simulation_enabled": simulation_enabled,
                    "type": type,
                },
                metric_create_params.MetricCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AITestMetric,
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
    ) -> AITestMetric:
        """
        Returns the specified metric.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/ai/tests/test_framework/v1/metrics/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AITestMetric,
        )

    async def update(
        self,
        id: int,
        *,
        add_to_new_agents: Optional[bool] | Omit = omit,
        agents: Iterable[int] | Omit = omit,
        audio_enabled: bool | Omit = omit,
        description: str | Omit = omit,
        display_order: int | Omit = omit,
        enum_values: SequenceNotStr[str] | Omit = omit,
        eval_type: str | Omit = omit,
        name: str | Omit = omit,
        observability_enabled: bool | Omit = omit,
        prompt: str | Omit = omit,
        sampling_enabled: bool | Omit = omit,
        simulation_enabled: bool | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AITestMetric:
        """
        Updates the specified metric.

        Args:
          eval_type: What the metric scores: numeric, continuous_qualitative, or
              binary_workflow_adherence.

          prompt: Judge prompt used by llm_judge metrics.

          type: How the metric is evaluated: custom_code or llm_judge.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            path_template("/ai/tests/test_framework/v1/metrics/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "add_to_new_agents": add_to_new_agents,
                    "agents": agents,
                    "audio_enabled": audio_enabled,
                    "description": description,
                    "display_order": display_order,
                    "enum_values": enum_values,
                    "eval_type": eval_type,
                    "name": name,
                    "observability_enabled": observability_enabled,
                    "prompt": prompt,
                    "sampling_enabled": sampling_enabled,
                    "simulation_enabled": simulation_enabled,
                    "type": type,
                },
                metric_update_params.MetricUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AITestMetric,
        )

    async def list(
        self,
        *,
        agent_id: int | Omit = omit,
        assistant_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricListResponse:
        """
        Returns the metrics available in your organization, optionally filtered by test
        agent. Each metric scores one aspect of a conversation or scenario run.

        Args:
          agent_id: Filter metrics attached to the specified test agent.

          assistant_id: Filter metrics attached to the specified Telnyx assistant.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/ai/tests/test_framework/v1/metrics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agent_id": agent_id,
                        "assistant_id": assistant_id,
                    },
                    metric_list_params.MetricListParams,
                ),
            ),
            cast_to=MetricListResponse,
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
        Deletes the specified metric.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            path_template("/ai/tests/test_framework/v1/metrics/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def bulk_create(
        self,
        *,
        body: Iterable[CreateAITestMetricRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricBulkCreateResponse:
        """Creates several metrics in one request.

        Accepts an array of metric objects and
        returns the created metrics.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/tests/test_framework/v1/metrics/bulk_create",
            body=await async_maybe_transform(body, Iterable[CreateAITestMetricRequestParam]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricBulkCreateResponse,
        )

    async def generate_metrics(
        self,
        *,
        agent_id: int,
        num_metrics: int,
        scenarios: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScenarioGenerationResponse:
        """Starts background generation of suggested metrics for a test agent.

        Returns a
        progress ID to poll with the get-test-metric-generation-progress endpoint.

        Args:
          agent_id: Test agent to suggest metrics for.

          num_metrics: How many metrics to suggest.

          scenarios: Scenario IDs to base the suggestions on.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/tests/test_framework/v1/metrics/generate_metrics",
            body=await async_maybe_transform(
                {
                    "agent_id": agent_id,
                    "num_metrics": num_metrics,
                    "scenarios": scenarios,
                },
                metric_generate_metrics_params.MetricGenerateMetricsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScenarioGenerationResponse,
        )

    async def retrieve_generate_metrics_progress(
        self,
        *,
        progress_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricRetrieveGenerateMetricsProgressResponse:
        """
        Returns the status of a background metric-generation job started with the
        generate-test-metrics endpoint.

        Args:
          progress_id: Progress ID returned by the generate-test-metrics endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/ai/tests/test_framework/v1/metrics/generate_metrics_progress",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"progress_id": progress_id},
                    metric_retrieve_generate_metrics_progress_params.MetricRetrieveGenerateMetricsProgressParams,
                ),
            ),
            cast_to=MetricRetrieveGenerateMetricsProgressResponse,
        )


class MetricsResourceWithRawResponse:
    def __init__(self, metrics: MetricsResource) -> None:
        self._metrics = metrics

        self.create = to_raw_response_wrapper(
            metrics.create,
        )
        self.retrieve = to_raw_response_wrapper(
            metrics.retrieve,
        )
        self.update = to_raw_response_wrapper(
            metrics.update,
        )
        self.list = to_raw_response_wrapper(
            metrics.list,
        )
        self.delete = to_raw_response_wrapper(
            metrics.delete,
        )
        self.bulk_create = to_raw_response_wrapper(
            metrics.bulk_create,
        )
        self.generate_metrics = to_raw_response_wrapper(
            metrics.generate_metrics,
        )
        self.retrieve_generate_metrics_progress = to_raw_response_wrapper(
            metrics.retrieve_generate_metrics_progress,
        )


class AsyncMetricsResourceWithRawResponse:
    def __init__(self, metrics: AsyncMetricsResource) -> None:
        self._metrics = metrics

        self.create = async_to_raw_response_wrapper(
            metrics.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            metrics.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            metrics.update,
        )
        self.list = async_to_raw_response_wrapper(
            metrics.list,
        )
        self.delete = async_to_raw_response_wrapper(
            metrics.delete,
        )
        self.bulk_create = async_to_raw_response_wrapper(
            metrics.bulk_create,
        )
        self.generate_metrics = async_to_raw_response_wrapper(
            metrics.generate_metrics,
        )
        self.retrieve_generate_metrics_progress = async_to_raw_response_wrapper(
            metrics.retrieve_generate_metrics_progress,
        )


class MetricsResourceWithStreamingResponse:
    def __init__(self, metrics: MetricsResource) -> None:
        self._metrics = metrics

        self.create = to_streamed_response_wrapper(
            metrics.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            metrics.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            metrics.update,
        )
        self.list = to_streamed_response_wrapper(
            metrics.list,
        )
        self.delete = to_streamed_response_wrapper(
            metrics.delete,
        )
        self.bulk_create = to_streamed_response_wrapper(
            metrics.bulk_create,
        )
        self.generate_metrics = to_streamed_response_wrapper(
            metrics.generate_metrics,
        )
        self.retrieve_generate_metrics_progress = to_streamed_response_wrapper(
            metrics.retrieve_generate_metrics_progress,
        )


class AsyncMetricsResourceWithStreamingResponse:
    def __init__(self, metrics: AsyncMetricsResource) -> None:
        self._metrics = metrics

        self.create = async_to_streamed_response_wrapper(
            metrics.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            metrics.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            metrics.update,
        )
        self.list = async_to_streamed_response_wrapper(
            metrics.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            metrics.delete,
        )
        self.bulk_create = async_to_streamed_response_wrapper(
            metrics.bulk_create,
        )
        self.generate_metrics = async_to_streamed_response_wrapper(
            metrics.generate_metrics,
        )
        self.retrieve_generate_metrics_progress = async_to_streamed_response_wrapper(
            metrics.retrieve_generate_metrics_progress,
        )

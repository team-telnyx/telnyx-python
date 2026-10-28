# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .metrics import (
    MetricsResource,
    AsyncMetricsResource,
    MetricsResourceWithRawResponse,
    AsyncMetricsResourceWithRawResponse,
    MetricsResourceWithStreamingResponse,
    AsyncMetricsResourceWithStreamingResponse,
)
from .results import (
    ResultsResource,
    AsyncResultsResource,
    ResultsResourceWithRawResponse,
    AsyncResultsResourceWithRawResponse,
    ResultsResourceWithStreamingResponse,
    AsyncResultsResourceWithStreamingResponse,
)
from .aiagents import (
    AiagentsResource,
    AsyncAiagentsResource,
    AiagentsResourceWithRawResponse,
    AsyncAiagentsResourceWithRawResponse,
    AiagentsResourceWithStreamingResponse,
    AsyncAiagentsResourceWithStreamingResponse,
)
from .scenarios import (
    ScenariosResource,
    AsyncScenariosResource,
    ScenariosResourceWithRawResponse,
    AsyncScenariosResourceWithRawResponse,
    ScenariosResourceWithStreamingResponse,
    AsyncScenariosResourceWithStreamingResponse,
)
from ......_types import Body, Query, Headers, NotGiven, not_given
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_base_client import make_request_options
from ......types.ai.tests.test_framework.v1_retrieve_personalities_response import V1RetrievePersonalitiesResponse

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    """
    Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
    """

    @cached_property
    def aiagents(self) -> AiagentsResource:
        """
        Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
        """
        return AiagentsResource(self._client)

    @cached_property
    def metrics(self) -> MetricsResource:
        """
        Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
        """
        return MetricsResource(self._client)

    @cached_property
    def results(self) -> ResultsResource:
        """
        Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
        """
        return ResultsResource(self._client)

    @cached_property
    def scenarios(self) -> ScenariosResource:
        """
        Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
        """
        return ScenariosResource(self._client)

    @cached_property
    def with_raw_response(self) -> V1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return V1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return V1ResourceWithStreamingResponse(self)

    def retrieve_personalities(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1RetrievePersonalitiesResponse:
        """Returns the catalogue of test personalities available to your organization.

        A
        personality describes how a simulated caller speaks: prompt, language, accent,
        voice, interruption level, and call-behaviour settings.
        """
        return self._get(
            "/ai/tests/test_framework/v1/personalities",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1RetrievePersonalitiesResponse,
        )


class AsyncV1Resource(AsyncAPIResource):
    """
    Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
    """

    @cached_property
    def aiagents(self) -> AsyncAiagentsResource:
        """
        Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
        """
        return AsyncAiagentsResource(self._client)

    @cached_property
    def metrics(self) -> AsyncMetricsResource:
        """
        Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
        """
        return AsyncMetricsResource(self._client)

    @cached_property
    def results(self) -> AsyncResultsResource:
        """
        Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
        """
        return AsyncResultsResource(self._client)

    @cached_property
    def scenarios(self) -> AsyncScenariosResource:
        """
        Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
        """
        return AsyncScenariosResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncV1ResourceWithStreamingResponse(self)

    async def retrieve_personalities(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V1RetrievePersonalitiesResponse:
        """Returns the catalogue of test personalities available to your organization.

        A
        personality describes how a simulated caller speaks: prompt, language, accent,
        voice, interruption level, and call-behaviour settings.
        """
        return await self._get(
            "/ai/tests/test_framework/v1/personalities",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1RetrievePersonalitiesResponse,
        )


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.retrieve_personalities = to_raw_response_wrapper(
            v1.retrieve_personalities,
        )

    @cached_property
    def aiagents(self) -> AiagentsResourceWithRawResponse:
        """
        Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
        """
        return AiagentsResourceWithRawResponse(self._v1.aiagents)

    @cached_property
    def metrics(self) -> MetricsResourceWithRawResponse:
        """
        Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
        """
        return MetricsResourceWithRawResponse(self._v1.metrics)

    @cached_property
    def results(self) -> ResultsResourceWithRawResponse:
        """
        Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
        """
        return ResultsResourceWithRawResponse(self._v1.results)

    @cached_property
    def scenarios(self) -> ScenariosResourceWithRawResponse:
        """
        Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
        """
        return ScenariosResourceWithRawResponse(self._v1.scenarios)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.retrieve_personalities = async_to_raw_response_wrapper(
            v1.retrieve_personalities,
        )

    @cached_property
    def aiagents(self) -> AsyncAiagentsResourceWithRawResponse:
        """
        Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
        """
        return AsyncAiagentsResourceWithRawResponse(self._v1.aiagents)

    @cached_property
    def metrics(self) -> AsyncMetricsResourceWithRawResponse:
        """
        Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
        """
        return AsyncMetricsResourceWithRawResponse(self._v1.metrics)

    @cached_property
    def results(self) -> AsyncResultsResourceWithRawResponse:
        """
        Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
        """
        return AsyncResultsResourceWithRawResponse(self._v1.results)

    @cached_property
    def scenarios(self) -> AsyncScenariosResourceWithRawResponse:
        """
        Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
        """
        return AsyncScenariosResourceWithRawResponse(self._v1.scenarios)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.retrieve_personalities = to_streamed_response_wrapper(
            v1.retrieve_personalities,
        )

    @cached_property
    def aiagents(self) -> AiagentsResourceWithStreamingResponse:
        """
        Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
        """
        return AiagentsResourceWithStreamingResponse(self._v1.aiagents)

    @cached_property
    def metrics(self) -> MetricsResourceWithStreamingResponse:
        """
        Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
        """
        return MetricsResourceWithStreamingResponse(self._v1.metrics)

    @cached_property
    def results(self) -> ResultsResourceWithStreamingResponse:
        """
        Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
        """
        return ResultsResourceWithStreamingResponse(self._v1.results)

    @cached_property
    def scenarios(self) -> ScenariosResourceWithStreamingResponse:
        """
        Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
        """
        return ScenariosResourceWithStreamingResponse(self._v1.scenarios)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.retrieve_personalities = async_to_streamed_response_wrapper(
            v1.retrieve_personalities,
        )

    @cached_property
    def aiagents(self) -> AsyncAiagentsResourceWithStreamingResponse:
        """
        Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
        """
        return AsyncAiagentsResourceWithStreamingResponse(self._v1.aiagents)

    @cached_property
    def metrics(self) -> AsyncMetricsResourceWithStreamingResponse:
        """
        Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
        """
        return AsyncMetricsResourceWithStreamingResponse(self._v1.metrics)

    @cached_property
    def results(self) -> AsyncResultsResourceWithStreamingResponse:
        """
        Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
        """
        return AsyncResultsResourceWithStreamingResponse(self._v1.results)

    @cached_property
    def scenarios(self) -> AsyncScenariosResourceWithStreamingResponse:
        """
        Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
        """
        return AsyncScenariosResourceWithStreamingResponse(self._v1.scenarios)

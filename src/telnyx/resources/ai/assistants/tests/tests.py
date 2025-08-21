# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from .runs import (
    RunsResource,
    AsyncRunsResource,
    RunsResourceWithRawResponse,
    AsyncRunsResourceWithRawResponse,
    RunsResourceWithStreamingResponse,
    AsyncRunsResourceWithStreamingResponse,
)
from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.ai.assistants import TelnyxConversationChannel, test_list_params, test_create_params, test_update_params
from .test_suites.test_suites import (
    TestSuitesResource,
    AsyncTestSuitesResource,
    TestSuitesResourceWithRawResponse,
    AsyncTestSuitesResourceWithRawResponse,
    TestSuitesResourceWithStreamingResponse,
    AsyncTestSuitesResourceWithStreamingResponse,
)
from .....types.ai.assistants.assistant_test import AssistantTest
from .....types.ai.assistants.test_list_response import TestListResponse
from .....types.ai.assistants.telnyx_conversation_channel import TelnyxConversationChannel

__all__ = ["TestsResource", "AsyncTestsResource"]


class TestsResource(SyncAPIResource):
    __test__ = False

    @cached_property
    def test_suites(self) -> TestSuitesResource:
        return TestSuitesResource(self._client)

    @cached_property
    def runs(self) -> RunsResource:
        return RunsResource(self._client)

    @cached_property
    def with_raw_response(self) -> TestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return TestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return TestsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        destination: str,
        instructions: str,
        name: str,
        rubric: Iterable[test_create_params.Rubric],
        description: str | NotGiven = NOT_GIVEN,
        max_duration_seconds: int | NotGiven = NOT_GIVEN,
        telnyx_conversation_channel: TelnyxConversationChannel | NotGiven = NOT_GIVEN,
        test_suite: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssistantTest:
        """
        Creates a comprehensive test configuration for evaluating AI assistant
        performance

        Args:
          destination:
              The target destination for the test conversation. Format depends on the channel:
              phone number for SMS/voice, webhook URL for web chat, etc.

          instructions: Detailed instructions that define the test scenario and what the assistant
              should accomplish. This guides the test execution and evaluation.

          name: A descriptive name for the assistant test. This will be used to identify the
              test in the UI and reports.

          rubric: Evaluation criteria used to assess the assistant's performance. Each rubric item
              contains a name and specific criteria for evaluation.

          description: Optional detailed description of what this test evaluates and its purpose. Helps
              team members understand the test's objectives.

          max_duration_seconds: Maximum duration in seconds that the test conversation should run before timing
              out. If not specified, uses system default timeout.

          telnyx_conversation_channel: The communication channel through which the test will be conducted. Determines
              how the assistant will receive and respond to test messages.

          test_suite: Optional test suite name to group related tests together. Useful for organizing
              tests by feature, team, or release cycle.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/assistants/tests",
            body=maybe_transform(
                {
                    "destination": destination,
                    "instructions": instructions,
                    "name": name,
                    "rubric": rubric,
                    "description": description,
                    "max_duration_seconds": max_duration_seconds,
                    "telnyx_conversation_channel": telnyx_conversation_channel,
                    "test_suite": test_suite,
                },
                test_create_params.TestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssistantTest,
        )

    def retrieve(
        self,
        test_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssistantTest:
        """
        Retrieves detailed information about a specific assistant test

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not test_id:
            raise ValueError(f"Expected a non-empty value for `test_id` but received {test_id!r}")
        return self._get(
            f"/ai/assistants/tests/{test_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssistantTest,
        )

    def update(
        self,
        test_id: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        destination: str | NotGiven = NOT_GIVEN,
        instructions: str | NotGiven = NOT_GIVEN,
        max_duration_seconds: int | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        rubric: Iterable[test_update_params.Rubric] | NotGiven = NOT_GIVEN,
        telnyx_conversation_channel: TelnyxConversationChannel | NotGiven = NOT_GIVEN,
        test_suite: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssistantTest:
        """
        Updates an existing assistant test configuration with new settings

        Args:
          description: Updated description of the test's purpose and evaluation criteria.

          destination: Updated target destination for test conversations.

          instructions: Updated test scenario instructions and objectives.

          max_duration_seconds: Updated maximum test duration in seconds.

          name: Updated name for the assistant test. Must be unique and descriptive.

          rubric: Updated evaluation criteria for assessing assistant performance.

          telnyx_conversation_channel: Updated communication channel for the test execution.

          test_suite: Updated test suite assignment for better organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not test_id:
            raise ValueError(f"Expected a non-empty value for `test_id` but received {test_id!r}")
        return self._put(
            f"/ai/assistants/tests/{test_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "destination": destination,
                    "instructions": instructions,
                    "max_duration_seconds": max_duration_seconds,
                    "name": name,
                    "rubric": rubric,
                    "telnyx_conversation_channel": telnyx_conversation_channel,
                    "test_suite": test_suite,
                },
                test_update_params.TestUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssistantTest,
        )

    def list(
        self,
        *,
        destination: str | NotGiven = NOT_GIVEN,
        page: test_list_params.Page | NotGiven = NOT_GIVEN,
        telnyx_conversation_channel: str | NotGiven = NOT_GIVEN,
        test_suite: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestListResponse:
        """
        Retrieves a paginated list of assistant tests with optional filtering
        capabilities

        Args:
          destination: Filter tests by destination (phone number, webhook URL, etc.)

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          telnyx_conversation_channel: Filter tests by communication channel (e.g., 'web_chat', 'sms')

          test_suite: Filter tests by test suite name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/ai/assistants/tests",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "destination": destination,
                        "page": page,
                        "telnyx_conversation_channel": telnyx_conversation_channel,
                        "test_suite": test_suite,
                    },
                    test_list_params.TestListParams,
                ),
            ),
            cast_to=TestListResponse,
        )

    def delete(
        self,
        test_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Permanently removes an assistant test and all associated data

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not test_id:
            raise ValueError(f"Expected a non-empty value for `test_id` but received {test_id!r}")
        return self._delete(
            f"/ai/assistants/tests/{test_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncTestsResource(AsyncAPIResource):
    @cached_property
    def test_suites(self) -> AsyncTestSuitesResource:
        return AsyncTestSuitesResource(self._client)

    @cached_property
    def runs(self) -> AsyncRunsResource:
        return AsyncRunsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncTestsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        destination: str,
        instructions: str,
        name: str,
        rubric: Iterable[test_create_params.Rubric],
        description: str | NotGiven = NOT_GIVEN,
        max_duration_seconds: int | NotGiven = NOT_GIVEN,
        telnyx_conversation_channel: TelnyxConversationChannel | NotGiven = NOT_GIVEN,
        test_suite: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssistantTest:
        """
        Creates a comprehensive test configuration for evaluating AI assistant
        performance

        Args:
          destination:
              The target destination for the test conversation. Format depends on the channel:
              phone number for SMS/voice, webhook URL for web chat, etc.

          instructions: Detailed instructions that define the test scenario and what the assistant
              should accomplish. This guides the test execution and evaluation.

          name: A descriptive name for the assistant test. This will be used to identify the
              test in the UI and reports.

          rubric: Evaluation criteria used to assess the assistant's performance. Each rubric item
              contains a name and specific criteria for evaluation.

          description: Optional detailed description of what this test evaluates and its purpose. Helps
              team members understand the test's objectives.

          max_duration_seconds: Maximum duration in seconds that the test conversation should run before timing
              out. If not specified, uses system default timeout.

          telnyx_conversation_channel: The communication channel through which the test will be conducted. Determines
              how the assistant will receive and respond to test messages.

          test_suite: Optional test suite name to group related tests together. Useful for organizing
              tests by feature, team, or release cycle.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/assistants/tests",
            body=await async_maybe_transform(
                {
                    "destination": destination,
                    "instructions": instructions,
                    "name": name,
                    "rubric": rubric,
                    "description": description,
                    "max_duration_seconds": max_duration_seconds,
                    "telnyx_conversation_channel": telnyx_conversation_channel,
                    "test_suite": test_suite,
                },
                test_create_params.TestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssistantTest,
        )

    async def retrieve(
        self,
        test_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssistantTest:
        """
        Retrieves detailed information about a specific assistant test

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not test_id:
            raise ValueError(f"Expected a non-empty value for `test_id` but received {test_id!r}")
        return await self._get(
            f"/ai/assistants/tests/{test_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssistantTest,
        )

    async def update(
        self,
        test_id: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        destination: str | NotGiven = NOT_GIVEN,
        instructions: str | NotGiven = NOT_GIVEN,
        max_duration_seconds: int | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        rubric: Iterable[test_update_params.Rubric] | NotGiven = NOT_GIVEN,
        telnyx_conversation_channel: TelnyxConversationChannel | NotGiven = NOT_GIVEN,
        test_suite: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssistantTest:
        """
        Updates an existing assistant test configuration with new settings

        Args:
          description: Updated description of the test's purpose and evaluation criteria.

          destination: Updated target destination for test conversations.

          instructions: Updated test scenario instructions and objectives.

          max_duration_seconds: Updated maximum test duration in seconds.

          name: Updated name for the assistant test. Must be unique and descriptive.

          rubric: Updated evaluation criteria for assessing assistant performance.

          telnyx_conversation_channel: Updated communication channel for the test execution.

          test_suite: Updated test suite assignment for better organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not test_id:
            raise ValueError(f"Expected a non-empty value for `test_id` but received {test_id!r}")
        return await self._put(
            f"/ai/assistants/tests/{test_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "destination": destination,
                    "instructions": instructions,
                    "max_duration_seconds": max_duration_seconds,
                    "name": name,
                    "rubric": rubric,
                    "telnyx_conversation_channel": telnyx_conversation_channel,
                    "test_suite": test_suite,
                },
                test_update_params.TestUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssistantTest,
        )

    async def list(
        self,
        *,
        destination: str | NotGiven = NOT_GIVEN,
        page: test_list_params.Page | NotGiven = NOT_GIVEN,
        telnyx_conversation_channel: str | NotGiven = NOT_GIVEN,
        test_suite: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestListResponse:
        """
        Retrieves a paginated list of assistant tests with optional filtering
        capabilities

        Args:
          destination: Filter tests by destination (phone number, webhook URL, etc.)

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          telnyx_conversation_channel: Filter tests by communication channel (e.g., 'web_chat', 'sms')

          test_suite: Filter tests by test suite name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/ai/assistants/tests",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "destination": destination,
                        "page": page,
                        "telnyx_conversation_channel": telnyx_conversation_channel,
                        "test_suite": test_suite,
                    },
                    test_list_params.TestListParams,
                ),
            ),
            cast_to=TestListResponse,
        )

    async def delete(
        self,
        test_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Permanently removes an assistant test and all associated data

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not test_id:
            raise ValueError(f"Expected a non-empty value for `test_id` but received {test_id!r}")
        return await self._delete(
            f"/ai/assistants/tests/{test_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class TestsResourceWithRawResponse:
    __test__ = False

    def __init__(self, tests: TestsResource) -> None:
        self._tests = tests

        self.create = to_raw_response_wrapper(
            tests.create,
        )
        self.retrieve = to_raw_response_wrapper(
            tests.retrieve,
        )
        self.update = to_raw_response_wrapper(
            tests.update,
        )
        self.list = to_raw_response_wrapper(
            tests.list,
        )
        self.delete = to_raw_response_wrapper(
            tests.delete,
        )

    @cached_property
    def test_suites(self) -> TestSuitesResourceWithRawResponse:
        return TestSuitesResourceWithRawResponse(self._tests.test_suites)

    @cached_property
    def runs(self) -> RunsResourceWithRawResponse:
        return RunsResourceWithRawResponse(self._tests.runs)


class AsyncTestsResourceWithRawResponse:
    def __init__(self, tests: AsyncTestsResource) -> None:
        self._tests = tests

        self.create = async_to_raw_response_wrapper(
            tests.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            tests.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            tests.update,
        )
        self.list = async_to_raw_response_wrapper(
            tests.list,
        )
        self.delete = async_to_raw_response_wrapper(
            tests.delete,
        )

    @cached_property
    def test_suites(self) -> AsyncTestSuitesResourceWithRawResponse:
        return AsyncTestSuitesResourceWithRawResponse(self._tests.test_suites)

    @cached_property
    def runs(self) -> AsyncRunsResourceWithRawResponse:
        return AsyncRunsResourceWithRawResponse(self._tests.runs)


class TestsResourceWithStreamingResponse:
    __test__ = False

    def __init__(self, tests: TestsResource) -> None:
        self._tests = tests

        self.create = to_streamed_response_wrapper(
            tests.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            tests.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            tests.update,
        )
        self.list = to_streamed_response_wrapper(
            tests.list,
        )
        self.delete = to_streamed_response_wrapper(
            tests.delete,
        )

    @cached_property
    def test_suites(self) -> TestSuitesResourceWithStreamingResponse:
        return TestSuitesResourceWithStreamingResponse(self._tests.test_suites)

    @cached_property
    def runs(self) -> RunsResourceWithStreamingResponse:
        return RunsResourceWithStreamingResponse(self._tests.runs)


class AsyncTestsResourceWithStreamingResponse:
    def __init__(self, tests: AsyncTestsResource) -> None:
        self._tests = tests

        self.create = async_to_streamed_response_wrapper(
            tests.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            tests.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            tests.update,
        )
        self.list = async_to_streamed_response_wrapper(
            tests.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            tests.delete,
        )

    @cached_property
    def test_suites(self) -> AsyncTestSuitesResourceWithStreamingResponse:
        return AsyncTestSuitesResourceWithStreamingResponse(self._tests.test_suites)

    @cached_property
    def runs(self) -> AsyncRunsResourceWithStreamingResponse:
        return AsyncRunsResourceWithStreamingResponse(self._tests.runs)

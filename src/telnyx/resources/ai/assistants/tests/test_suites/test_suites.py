# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .runs import (
    RunsResource,
    AsyncRunsResource,
    RunsResourceWithRawResponse,
    AsyncRunsResourceWithRawResponse,
    RunsResourceWithStreamingResponse,
    AsyncRunsResourceWithStreamingResponse,
)
from ......_types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_base_client import make_request_options
from ......types.ai.assistants.tests.test_suite_list_response import TestSuiteListResponse

__all__ = ["TestSuitesResource", "AsyncTestSuitesResource"]


class TestSuitesResource(SyncAPIResource):
    __test__ = False

    @cached_property
    def runs(self) -> RunsResource:
        return RunsResource(self._client)

    @cached_property
    def with_raw_response(self) -> TestSuitesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return TestSuitesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TestSuitesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return TestSuitesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestSuiteListResponse:
        """Retrieves a list of all distinct test suite names available to the current user"""
        return self._get(
            "/ai/assistants/tests/test-suites",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestSuiteListResponse,
        )


class AsyncTestSuitesResource(AsyncAPIResource):
    @cached_property
    def runs(self) -> AsyncRunsResource:
        return AsyncRunsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTestSuitesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTestSuitesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTestSuitesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncTestSuitesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TestSuiteListResponse:
        """Retrieves a list of all distinct test suite names available to the current user"""
        return await self._get(
            "/ai/assistants/tests/test-suites",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestSuiteListResponse,
        )


class TestSuitesResourceWithRawResponse:
    __test__ = False

    def __init__(self, test_suites: TestSuitesResource) -> None:
        self._test_suites = test_suites

        self.list = to_raw_response_wrapper(
            test_suites.list,
        )

    @cached_property
    def runs(self) -> RunsResourceWithRawResponse:
        return RunsResourceWithRawResponse(self._test_suites.runs)


class AsyncTestSuitesResourceWithRawResponse:
    def __init__(self, test_suites: AsyncTestSuitesResource) -> None:
        self._test_suites = test_suites

        self.list = async_to_raw_response_wrapper(
            test_suites.list,
        )

    @cached_property
    def runs(self) -> AsyncRunsResourceWithRawResponse:
        return AsyncRunsResourceWithRawResponse(self._test_suites.runs)


class TestSuitesResourceWithStreamingResponse:
    __test__ = False

    def __init__(self, test_suites: TestSuitesResource) -> None:
        self._test_suites = test_suites

        self.list = to_streamed_response_wrapper(
            test_suites.list,
        )

    @cached_property
    def runs(self) -> RunsResourceWithStreamingResponse:
        return RunsResourceWithStreamingResponse(self._test_suites.runs)


class AsyncTestSuitesResourceWithStreamingResponse:
    def __init__(self, test_suites: AsyncTestSuitesResource) -> None:
        self._test_suites = test_suites

        self.list = async_to_streamed_response_wrapper(
            test_suites.list,
        )

    @cached_property
    def runs(self) -> AsyncRunsResourceWithStreamingResponse:
        return AsyncRunsResourceWithStreamingResponse(self._test_suites.runs)

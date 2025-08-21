# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ......_types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ......_utils import maybe_transform, async_maybe_transform
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_base_client import make_request_options
from ......types.ai.assistants.tests.test_suites import run_list_params, run_trigger_params
from ......types.ai.assistants.tests.test_suites.run_trigger_response import RunTriggerResponse
from ......types.ai.assistants.tests.test_suites.paginated_test_run_list import PaginatedTestRunList

__all__ = ["RunsResource", "AsyncRunsResource"]


class RunsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return RunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return RunsResourceWithStreamingResponse(self)

    def list(
        self,
        suite_name: str,
        *,
        page: run_list_params.Page | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        test_suite_run_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaginatedTestRunList:
        """
        Retrieves paginated history of test runs for a specific test suite with
        filtering options

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          status: Filter runs by execution status (pending, running, completed, failed, timeout)

          test_suite_run_id: Filter runs by specific suite execution batch ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not suite_name:
            raise ValueError(f"Expected a non-empty value for `suite_name` but received {suite_name!r}")
        return self._get(
            f"/ai/assistants/tests/test-suites/{suite_name}/runs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "status": status,
                        "test_suite_run_id": test_suite_run_id,
                    },
                    run_list_params.RunListParams,
                ),
            ),
            cast_to=PaginatedTestRunList,
        )

    def trigger(
        self,
        suite_name: str,
        *,
        destination_version_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunTriggerResponse:
        """
        Executes all tests within a specific test suite as a batch operation

        Args:
          destination_version_id: Optional assistant version ID to use for all test runs in this suite. If
              provided, the version must exist or a 400 error will be returned. If not
              provided, test will run on main version

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not suite_name:
            raise ValueError(f"Expected a non-empty value for `suite_name` but received {suite_name!r}")
        return self._post(
            f"/ai/assistants/tests/test-suites/{suite_name}/runs",
            body=maybe_transform(
                {"destination_version_id": destination_version_id}, run_trigger_params.RunTriggerParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunTriggerResponse,
        )


class AsyncRunsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncRunsResourceWithStreamingResponse(self)

    async def list(
        self,
        suite_name: str,
        *,
        page: run_list_params.Page | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        test_suite_run_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaginatedTestRunList:
        """
        Retrieves paginated history of test runs for a specific test suite with
        filtering options

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          status: Filter runs by execution status (pending, running, completed, failed, timeout)

          test_suite_run_id: Filter runs by specific suite execution batch ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not suite_name:
            raise ValueError(f"Expected a non-empty value for `suite_name` but received {suite_name!r}")
        return await self._get(
            f"/ai/assistants/tests/test-suites/{suite_name}/runs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "status": status,
                        "test_suite_run_id": test_suite_run_id,
                    },
                    run_list_params.RunListParams,
                ),
            ),
            cast_to=PaginatedTestRunList,
        )

    async def trigger(
        self,
        suite_name: str,
        *,
        destination_version_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunTriggerResponse:
        """
        Executes all tests within a specific test suite as a batch operation

        Args:
          destination_version_id: Optional assistant version ID to use for all test runs in this suite. If
              provided, the version must exist or a 400 error will be returned. If not
              provided, test will run on main version

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not suite_name:
            raise ValueError(f"Expected a non-empty value for `suite_name` but received {suite_name!r}")
        return await self._post(
            f"/ai/assistants/tests/test-suites/{suite_name}/runs",
            body=await async_maybe_transform(
                {"destination_version_id": destination_version_id}, run_trigger_params.RunTriggerParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunTriggerResponse,
        )


class RunsResourceWithRawResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.list = to_raw_response_wrapper(
            runs.list,
        )
        self.trigger = to_raw_response_wrapper(
            runs.trigger,
        )


class AsyncRunsResourceWithRawResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.list = async_to_raw_response_wrapper(
            runs.list,
        )
        self.trigger = async_to_raw_response_wrapper(
            runs.trigger,
        )


class RunsResourceWithStreamingResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.list = to_streamed_response_wrapper(
            runs.list,
        )
        self.trigger = to_streamed_response_wrapper(
            runs.trigger,
        )


class AsyncRunsResourceWithStreamingResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.list = async_to_streamed_response_wrapper(
            runs.list,
        )
        self.trigger = async_to_streamed_response_wrapper(
            runs.trigger,
        )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

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
from ......types.ai.tests.schedules.v1 import (
    cron_job_update_params,
    cron_job_cron_jobs_params,
    cron_job_retrieve_cron_jobs_params,
)
from ......types.ai.tests.schedules.v1.scheduled_test_job import ScheduledTestJob
from ......types.ai.tests.schedules.v1.cron_job_retrieve_cron_jobs_response import CronJobRetrieveCronJobsResponse

__all__ = ["CronJobsResource", "AsyncCronJobsResource"]


class CronJobsResource(SyncAPIResource):
    """
    Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
    """

    @cached_property
    def with_raw_response(self) -> CronJobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return CronJobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CronJobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return CronJobsResourceWithStreamingResponse(self)

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
    ) -> ScheduledTestJob:
        """
        Returns the specified scheduled test job.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/ai/tests/schedules/v1/cron-jobs/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduledTestJob,
        )

    def update(
        self,
        id: int,
        *,
        agent: Optional[int] | Omit = omit,
        crontab_expression: str | Omit = omit,
        execution_mode: str | Omit = omit,
        frequency: int | Omit = omit,
        is_active: bool | Omit = omit,
        name: str | Omit = omit,
        notify_on: Literal["never", "success", "failure", "both"] | Omit = omit,
        personalities: Iterable[int] | Omit = omit,
        run_as_text: bool | Omit = omit,
        scenarios: Iterable[int] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduledTestJob:
        """
        Updates the specified scheduled test job.

        Args:
          crontab_expression: Cron expression controlling when the job runs.

          execution_mode: Execution mode for the test runs, such as voice, text, or sip.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            path_template("/ai/tests/schedules/v1/cron-jobs/{id}", id=id),
            body=maybe_transform(
                {
                    "agent": agent,
                    "crontab_expression": crontab_expression,
                    "execution_mode": execution_mode,
                    "frequency": frequency,
                    "is_active": is_active,
                    "name": name,
                    "notify_on": notify_on,
                    "personalities": personalities,
                    "run_as_text": run_as_text,
                    "scenarios": scenarios,
                    "tags": tags,
                    "timezone": timezone,
                },
                cron_job_update_params.CronJobUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduledTestJob,
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
        Deletes the specified scheduled test job.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            path_template("/ai/tests/schedules/v1/cron-jobs/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def cron_jobs(
        self,
        *,
        crontab_expression: str,
        agent: int | Omit = omit,
        execution_mode: str | Omit = omit,
        frequency: int | Omit = omit,
        is_active: bool | Omit = omit,
        name: str | Omit = omit,
        notify_on: Literal["never", "success", "failure", "both"] | Omit = omit,
        personalities: Iterable[int] | Omit = omit,
        run_as_text: bool | Omit = omit,
        scenarios: Iterable[int] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduledTestJob:
        """
        Creates a scheduled test job that runs the selected scenarios on a cron
        expression.

        Args:
          crontab_expression: Cron expression controlling when the job runs.

          execution_mode: Execution mode for the test runs, such as voice, text, or sip.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/tests/schedules/v1/cron-jobs",
            body=maybe_transform(
                {
                    "crontab_expression": crontab_expression,
                    "agent": agent,
                    "execution_mode": execution_mode,
                    "frequency": frequency,
                    "is_active": is_active,
                    "name": name,
                    "notify_on": notify_on,
                    "personalities": personalities,
                    "run_as_text": run_as_text,
                    "scenarios": scenarios,
                    "tags": tags,
                    "timezone": timezone,
                },
                cron_job_cron_jobs_params.CronJobCronJobsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduledTestJob,
        )

    def retrieve_cron_jobs(
        self,
        *,
        agent_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CronJobRetrieveCronJobsResponse:
        """
        Returns the scheduled test jobs in your organization, optionally filtered by
        test agent. A scheduled job runs selected scenarios on a cron expression.

        Args:
          agent_id: Filter jobs belonging to the specified test agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/ai/tests/schedules/v1/cron-jobs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"agent_id": agent_id}, cron_job_retrieve_cron_jobs_params.CronJobRetrieveCronJobsParams
                ),
            ),
            cast_to=CronJobRetrieveCronJobsResponse,
        )


class AsyncCronJobsResource(AsyncAPIResource):
    """
    Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
    """

    @cached_property
    def with_raw_response(self) -> AsyncCronJobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCronJobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCronJobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncCronJobsResourceWithStreamingResponse(self)

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
    ) -> ScheduledTestJob:
        """
        Returns the specified scheduled test job.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/ai/tests/schedules/v1/cron-jobs/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduledTestJob,
        )

    async def update(
        self,
        id: int,
        *,
        agent: Optional[int] | Omit = omit,
        crontab_expression: str | Omit = omit,
        execution_mode: str | Omit = omit,
        frequency: int | Omit = omit,
        is_active: bool | Omit = omit,
        name: str | Omit = omit,
        notify_on: Literal["never", "success", "failure", "both"] | Omit = omit,
        personalities: Iterable[int] | Omit = omit,
        run_as_text: bool | Omit = omit,
        scenarios: Iterable[int] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduledTestJob:
        """
        Updates the specified scheduled test job.

        Args:
          crontab_expression: Cron expression controlling when the job runs.

          execution_mode: Execution mode for the test runs, such as voice, text, or sip.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            path_template("/ai/tests/schedules/v1/cron-jobs/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "agent": agent,
                    "crontab_expression": crontab_expression,
                    "execution_mode": execution_mode,
                    "frequency": frequency,
                    "is_active": is_active,
                    "name": name,
                    "notify_on": notify_on,
                    "personalities": personalities,
                    "run_as_text": run_as_text,
                    "scenarios": scenarios,
                    "tags": tags,
                    "timezone": timezone,
                },
                cron_job_update_params.CronJobUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduledTestJob,
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
        Deletes the specified scheduled test job.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            path_template("/ai/tests/schedules/v1/cron-jobs/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def cron_jobs(
        self,
        *,
        crontab_expression: str,
        agent: int | Omit = omit,
        execution_mode: str | Omit = omit,
        frequency: int | Omit = omit,
        is_active: bool | Omit = omit,
        name: str | Omit = omit,
        notify_on: Literal["never", "success", "failure", "both"] | Omit = omit,
        personalities: Iterable[int] | Omit = omit,
        run_as_text: bool | Omit = omit,
        scenarios: Iterable[int] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduledTestJob:
        """
        Creates a scheduled test job that runs the selected scenarios on a cron
        expression.

        Args:
          crontab_expression: Cron expression controlling when the job runs.

          execution_mode: Execution mode for the test runs, such as voice, text, or sip.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/tests/schedules/v1/cron-jobs",
            body=await async_maybe_transform(
                {
                    "crontab_expression": crontab_expression,
                    "agent": agent,
                    "execution_mode": execution_mode,
                    "frequency": frequency,
                    "is_active": is_active,
                    "name": name,
                    "notify_on": notify_on,
                    "personalities": personalities,
                    "run_as_text": run_as_text,
                    "scenarios": scenarios,
                    "tags": tags,
                    "timezone": timezone,
                },
                cron_job_cron_jobs_params.CronJobCronJobsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduledTestJob,
        )

    async def retrieve_cron_jobs(
        self,
        *,
        agent_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CronJobRetrieveCronJobsResponse:
        """
        Returns the scheduled test jobs in your organization, optionally filtered by
        test agent. A scheduled job runs selected scenarios on a cron expression.

        Args:
          agent_id: Filter jobs belonging to the specified test agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/ai/tests/schedules/v1/cron-jobs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"agent_id": agent_id}, cron_job_retrieve_cron_jobs_params.CronJobRetrieveCronJobsParams
                ),
            ),
            cast_to=CronJobRetrieveCronJobsResponse,
        )


class CronJobsResourceWithRawResponse:
    def __init__(self, cron_jobs: CronJobsResource) -> None:
        self._cron_jobs = cron_jobs

        self.retrieve = to_raw_response_wrapper(
            cron_jobs.retrieve,
        )
        self.update = to_raw_response_wrapper(
            cron_jobs.update,
        )
        self.delete = to_raw_response_wrapper(
            cron_jobs.delete,
        )
        self.cron_jobs = to_raw_response_wrapper(
            cron_jobs.cron_jobs,
        )
        self.retrieve_cron_jobs = to_raw_response_wrapper(
            cron_jobs.retrieve_cron_jobs,
        )


class AsyncCronJobsResourceWithRawResponse:
    def __init__(self, cron_jobs: AsyncCronJobsResource) -> None:
        self._cron_jobs = cron_jobs

        self.retrieve = async_to_raw_response_wrapper(
            cron_jobs.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            cron_jobs.update,
        )
        self.delete = async_to_raw_response_wrapper(
            cron_jobs.delete,
        )
        self.cron_jobs = async_to_raw_response_wrapper(
            cron_jobs.cron_jobs,
        )
        self.retrieve_cron_jobs = async_to_raw_response_wrapper(
            cron_jobs.retrieve_cron_jobs,
        )


class CronJobsResourceWithStreamingResponse:
    def __init__(self, cron_jobs: CronJobsResource) -> None:
        self._cron_jobs = cron_jobs

        self.retrieve = to_streamed_response_wrapper(
            cron_jobs.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            cron_jobs.update,
        )
        self.delete = to_streamed_response_wrapper(
            cron_jobs.delete,
        )
        self.cron_jobs = to_streamed_response_wrapper(
            cron_jobs.cron_jobs,
        )
        self.retrieve_cron_jobs = to_streamed_response_wrapper(
            cron_jobs.retrieve_cron_jobs,
        )


class AsyncCronJobsResourceWithStreamingResponse:
    def __init__(self, cron_jobs: AsyncCronJobsResource) -> None:
        self._cron_jobs = cron_jobs

        self.retrieve = async_to_streamed_response_wrapper(
            cron_jobs.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            cron_jobs.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            cron_jobs.delete,
        )
        self.cron_jobs = async_to_streamed_response_wrapper(
            cron_jobs.cron_jobs,
        )
        self.retrieve_cron_jobs = async_to_streamed_response_wrapper(
            cron_jobs.retrieve_cron_jobs,
        )

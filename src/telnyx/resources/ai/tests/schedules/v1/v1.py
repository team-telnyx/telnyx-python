# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .cron_jobs import (
    CronJobsResource,
    AsyncCronJobsResource,
    CronJobsResourceWithRawResponse,
    AsyncCronJobsResourceWithRawResponse,
    CronJobsResourceWithStreamingResponse,
    AsyncCronJobsResourceWithStreamingResponse,
)
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def cron_jobs(self) -> CronJobsResource:
        """
        Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
        """
        return CronJobsResource(self._client)

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


class AsyncV1Resource(AsyncAPIResource):
    @cached_property
    def cron_jobs(self) -> AsyncCronJobsResource:
        """
        Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
        """
        return AsyncCronJobsResource(self._client)

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


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

    @cached_property
    def cron_jobs(self) -> CronJobsResourceWithRawResponse:
        """
        Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
        """
        return CronJobsResourceWithRawResponse(self._v1.cron_jobs)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def cron_jobs(self) -> AsyncCronJobsResourceWithRawResponse:
        """
        Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
        """
        return AsyncCronJobsResourceWithRawResponse(self._v1.cron_jobs)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

    @cached_property
    def cron_jobs(self) -> CronJobsResourceWithStreamingResponse:
        """
        Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
        """
        return CronJobsResourceWithStreamingResponse(self._v1.cron_jobs)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def cron_jobs(self) -> AsyncCronJobsResourceWithStreamingResponse:
        """
        Test agents, evaluator scenarios, metrics, and run results for the AI test framework.
        """
        return AsyncCronJobsResourceWithStreamingResponse(self._v1.cron_jobs)

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .jobs import (
    JobsResource,
    AsyncJobsResource,
    JobsResourceWithRawResponse,
    AsyncJobsResourceWithRawResponse,
    JobsResourceWithStreamingResponse,
    AsyncJobsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["FineTuningResource", "AsyncFineTuningResource"]


class FineTuningResource(SyncAPIResource):
    @cached_property
    def jobs(self) -> JobsResource:
        return JobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> FineTuningResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return FineTuningResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FineTuningResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return FineTuningResourceWithStreamingResponse(self)


class AsyncFineTuningResource(AsyncAPIResource):
    @cached_property
    def jobs(self) -> AsyncJobsResource:
        return AsyncJobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFineTuningResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFineTuningResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFineTuningResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncFineTuningResourceWithStreamingResponse(self)


class FineTuningResourceWithRawResponse:
    def __init__(self, fine_tuning: FineTuningResource) -> None:
        self._fine_tuning = fine_tuning

    @cached_property
    def jobs(self) -> JobsResourceWithRawResponse:
        return JobsResourceWithRawResponse(self._fine_tuning.jobs)


class AsyncFineTuningResourceWithRawResponse:
    def __init__(self, fine_tuning: AsyncFineTuningResource) -> None:
        self._fine_tuning = fine_tuning

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithRawResponse:
        return AsyncJobsResourceWithRawResponse(self._fine_tuning.jobs)


class FineTuningResourceWithStreamingResponse:
    def __init__(self, fine_tuning: FineTuningResource) -> None:
        self._fine_tuning = fine_tuning

    @cached_property
    def jobs(self) -> JobsResourceWithStreamingResponse:
        return JobsResourceWithStreamingResponse(self._fine_tuning.jobs)


class AsyncFineTuningResourceWithStreamingResponse:
    def __init__(self, fine_tuning: AsyncFineTuningResource) -> None:
        self._fine_tuning = fine_tuning

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithStreamingResponse:
        return AsyncJobsResourceWithStreamingResponse(self._fine_tuning.jobs)

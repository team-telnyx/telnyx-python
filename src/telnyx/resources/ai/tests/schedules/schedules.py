# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .v1.v1 import (
    V1Resource,
    AsyncV1Resource,
    V1ResourceWithRawResponse,
    AsyncV1ResourceWithRawResponse,
    V1ResourceWithStreamingResponse,
    AsyncV1ResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["SchedulesResource", "AsyncSchedulesResource"]


class SchedulesResource(SyncAPIResource):
    @cached_property
    def v1(self) -> V1Resource:
        return V1Resource(self._client)

    @cached_property
    def with_raw_response(self) -> SchedulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return SchedulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SchedulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return SchedulesResourceWithStreamingResponse(self)


class AsyncSchedulesResource(AsyncAPIResource):
    @cached_property
    def v1(self) -> AsyncV1Resource:
        return AsyncV1Resource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSchedulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSchedulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSchedulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncSchedulesResourceWithStreamingResponse(self)


class SchedulesResourceWithRawResponse:
    def __init__(self, schedules: SchedulesResource) -> None:
        self._schedules = schedules

    @cached_property
    def v1(self) -> V1ResourceWithRawResponse:
        return V1ResourceWithRawResponse(self._schedules.v1)


class AsyncSchedulesResourceWithRawResponse:
    def __init__(self, schedules: AsyncSchedulesResource) -> None:
        self._schedules = schedules

    @cached_property
    def v1(self) -> AsyncV1ResourceWithRawResponse:
        return AsyncV1ResourceWithRawResponse(self._schedules.v1)


class SchedulesResourceWithStreamingResponse:
    def __init__(self, schedules: SchedulesResource) -> None:
        self._schedules = schedules

    @cached_property
    def v1(self) -> V1ResourceWithStreamingResponse:
        return V1ResourceWithStreamingResponse(self._schedules.v1)


class AsyncSchedulesResourceWithStreamingResponse:
    def __init__(self, schedules: AsyncSchedulesResource) -> None:
        self._schedules = schedules

    @cached_property
    def v1(self) -> AsyncV1ResourceWithStreamingResponse:
        return AsyncV1ResourceWithStreamingResponse(self._schedules.v1)

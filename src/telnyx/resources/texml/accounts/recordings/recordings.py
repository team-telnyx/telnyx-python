# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .json import (
    JsonResource,
    AsyncJsonResource,
    JsonResourceWithRawResponse,
    AsyncJsonResourceWithRawResponse,
    JsonResourceWithStreamingResponse,
    AsyncJsonResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["RecordingsResource", "AsyncRecordingsResource"]


class RecordingsResource(SyncAPIResource):
    @cached_property
    def json(self) -> JsonResource:
        return JsonResource(self._client)

    @cached_property
    def with_raw_response(self) -> RecordingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return RecordingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RecordingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return RecordingsResourceWithStreamingResponse(self)


class AsyncRecordingsResource(AsyncAPIResource):
    @cached_property
    def json(self) -> AsyncJsonResource:
        return AsyncJsonResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRecordingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRecordingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRecordingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncRecordingsResourceWithStreamingResponse(self)


class RecordingsResourceWithRawResponse:
    def __init__(self, recordings: RecordingsResource) -> None:
        self._recordings = recordings

    @cached_property
    def json(self) -> JsonResourceWithRawResponse:
        return JsonResourceWithRawResponse(self._recordings.json)


class AsyncRecordingsResourceWithRawResponse:
    def __init__(self, recordings: AsyncRecordingsResource) -> None:
        self._recordings = recordings

    @cached_property
    def json(self) -> AsyncJsonResourceWithRawResponse:
        return AsyncJsonResourceWithRawResponse(self._recordings.json)


class RecordingsResourceWithStreamingResponse:
    def __init__(self, recordings: RecordingsResource) -> None:
        self._recordings = recordings

    @cached_property
    def json(self) -> JsonResourceWithStreamingResponse:
        return JsonResourceWithStreamingResponse(self._recordings.json)


class AsyncRecordingsResourceWithStreamingResponse:
    def __init__(self, recordings: AsyncRecordingsResource) -> None:
        self._recordings = recordings

    @cached_property
    def json(self) -> AsyncJsonResourceWithStreamingResponse:
        return AsyncJsonResourceWithStreamingResponse(self._recordings.json)

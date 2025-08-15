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

__all__ = ["TranscriptionsResource", "AsyncTranscriptionsResource"]


class TranscriptionsResource(SyncAPIResource):
    @cached_property
    def json(self) -> JsonResource:
        return JsonResource(self._client)

    @cached_property
    def with_raw_response(self) -> TranscriptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return TranscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TranscriptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return TranscriptionsResourceWithStreamingResponse(self)


class AsyncTranscriptionsResource(AsyncAPIResource):
    @cached_property
    def json(self) -> AsyncJsonResource:
        return AsyncJsonResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTranscriptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTranscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTranscriptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncTranscriptionsResourceWithStreamingResponse(self)


class TranscriptionsResourceWithRawResponse:
    def __init__(self, transcriptions: TranscriptionsResource) -> None:
        self._transcriptions = transcriptions

    @cached_property
    def json(self) -> JsonResourceWithRawResponse:
        return JsonResourceWithRawResponse(self._transcriptions.json)


class AsyncTranscriptionsResourceWithRawResponse:
    def __init__(self, transcriptions: AsyncTranscriptionsResource) -> None:
        self._transcriptions = transcriptions

    @cached_property
    def json(self) -> AsyncJsonResourceWithRawResponse:
        return AsyncJsonResourceWithRawResponse(self._transcriptions.json)


class TranscriptionsResourceWithStreamingResponse:
    def __init__(self, transcriptions: TranscriptionsResource) -> None:
        self._transcriptions = transcriptions

    @cached_property
    def json(self) -> JsonResourceWithStreamingResponse:
        return JsonResourceWithStreamingResponse(self._transcriptions.json)


class AsyncTranscriptionsResourceWithStreamingResponse:
    def __init__(self, transcriptions: AsyncTranscriptionsResource) -> None:
        self._transcriptions = transcriptions

    @cached_property
    def json(self) -> AsyncJsonResourceWithStreamingResponse:
        return AsyncJsonResourceWithStreamingResponse(self._transcriptions.json)

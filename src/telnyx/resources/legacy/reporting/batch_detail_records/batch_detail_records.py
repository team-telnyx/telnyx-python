# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .voice import (
    VoiceResource,
    AsyncVoiceResource,
    VoiceResourceWithRawResponse,
    AsyncVoiceResourceWithRawResponse,
    VoiceResourceWithStreamingResponse,
    AsyncVoiceResourceWithStreamingResponse,
)
from .messaging import (
    MessagingResource,
    AsyncMessagingResource,
    MessagingResourceWithRawResponse,
    AsyncMessagingResourceWithRawResponse,
    MessagingResourceWithStreamingResponse,
    AsyncMessagingResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from .speech_to_text import (
    SpeechToTextResource,
    AsyncSpeechToTextResource,
    SpeechToTextResourceWithRawResponse,
    AsyncSpeechToTextResourceWithRawResponse,
    SpeechToTextResourceWithStreamingResponse,
    AsyncSpeechToTextResourceWithStreamingResponse,
)

__all__ = ["BatchDetailRecordsResource", "AsyncBatchDetailRecordsResource"]


class BatchDetailRecordsResource(SyncAPIResource):
    @cached_property
    def messaging(self) -> MessagingResource:
        return MessagingResource(self._client)

    @cached_property
    def speech_to_text(self) -> SpeechToTextResource:
        return SpeechToTextResource(self._client)

    @cached_property
    def voice(self) -> VoiceResource:
        return VoiceResource(self._client)

    @cached_property
    def with_raw_response(self) -> BatchDetailRecordsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return BatchDetailRecordsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatchDetailRecordsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return BatchDetailRecordsResourceWithStreamingResponse(self)


class AsyncBatchDetailRecordsResource(AsyncAPIResource):
    @cached_property
    def messaging(self) -> AsyncMessagingResource:
        return AsyncMessagingResource(self._client)

    @cached_property
    def speech_to_text(self) -> AsyncSpeechToTextResource:
        return AsyncSpeechToTextResource(self._client)

    @cached_property
    def voice(self) -> AsyncVoiceResource:
        return AsyncVoiceResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBatchDetailRecordsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBatchDetailRecordsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatchDetailRecordsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncBatchDetailRecordsResourceWithStreamingResponse(self)


class BatchDetailRecordsResourceWithRawResponse:
    def __init__(self, batch_detail_records: BatchDetailRecordsResource) -> None:
        self._batch_detail_records = batch_detail_records

    @cached_property
    def messaging(self) -> MessagingResourceWithRawResponse:
        return MessagingResourceWithRawResponse(self._batch_detail_records.messaging)

    @cached_property
    def speech_to_text(self) -> SpeechToTextResourceWithRawResponse:
        return SpeechToTextResourceWithRawResponse(self._batch_detail_records.speech_to_text)

    @cached_property
    def voice(self) -> VoiceResourceWithRawResponse:
        return VoiceResourceWithRawResponse(self._batch_detail_records.voice)


class AsyncBatchDetailRecordsResourceWithRawResponse:
    def __init__(self, batch_detail_records: AsyncBatchDetailRecordsResource) -> None:
        self._batch_detail_records = batch_detail_records

    @cached_property
    def messaging(self) -> AsyncMessagingResourceWithRawResponse:
        return AsyncMessagingResourceWithRawResponse(self._batch_detail_records.messaging)

    @cached_property
    def speech_to_text(self) -> AsyncSpeechToTextResourceWithRawResponse:
        return AsyncSpeechToTextResourceWithRawResponse(self._batch_detail_records.speech_to_text)

    @cached_property
    def voice(self) -> AsyncVoiceResourceWithRawResponse:
        return AsyncVoiceResourceWithRawResponse(self._batch_detail_records.voice)


class BatchDetailRecordsResourceWithStreamingResponse:
    def __init__(self, batch_detail_records: BatchDetailRecordsResource) -> None:
        self._batch_detail_records = batch_detail_records

    @cached_property
    def messaging(self) -> MessagingResourceWithStreamingResponse:
        return MessagingResourceWithStreamingResponse(self._batch_detail_records.messaging)

    @cached_property
    def speech_to_text(self) -> SpeechToTextResourceWithStreamingResponse:
        return SpeechToTextResourceWithStreamingResponse(self._batch_detail_records.speech_to_text)

    @cached_property
    def voice(self) -> VoiceResourceWithStreamingResponse:
        return VoiceResourceWithStreamingResponse(self._batch_detail_records.voice)


class AsyncBatchDetailRecordsResourceWithStreamingResponse:
    def __init__(self, batch_detail_records: AsyncBatchDetailRecordsResource) -> None:
        self._batch_detail_records = batch_detail_records

    @cached_property
    def messaging(self) -> AsyncMessagingResourceWithStreamingResponse:
        return AsyncMessagingResourceWithStreamingResponse(self._batch_detail_records.messaging)

    @cached_property
    def speech_to_text(self) -> AsyncSpeechToTextResourceWithStreamingResponse:
        return AsyncSpeechToTextResourceWithStreamingResponse(self._batch_detail_records.speech_to_text)

    @cached_property
    def voice(self) -> AsyncVoiceResourceWithStreamingResponse:
        return AsyncVoiceResourceWithStreamingResponse(self._batch_detail_records.voice)

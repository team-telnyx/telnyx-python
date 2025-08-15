# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.recording_transcription_list_response import RecordingTranscriptionListResponse
from ..types.recording_transcription_delete_response import RecordingTranscriptionDeleteResponse
from ..types.recording_transcription_retrieve_response import RecordingTranscriptionRetrieveResponse

__all__ = ["RecordingTranscriptionsResource", "AsyncRecordingTranscriptionsResource"]


class RecordingTranscriptionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RecordingTranscriptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return RecordingTranscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RecordingTranscriptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return RecordingTranscriptionsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        recording_transcription_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RecordingTranscriptionRetrieveResponse:
        """
        Retrieves the details of an existing recording transcription.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not recording_transcription_id:
            raise ValueError(
                f"Expected a non-empty value for `recording_transcription_id` but received {recording_transcription_id!r}"
            )
        return self._get(
            f"/recording_transcriptions/{recording_transcription_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingTranscriptionRetrieveResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RecordingTranscriptionListResponse:
        """Returns a list of your recording transcriptions."""
        return self._get(
            "/recording_transcriptions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingTranscriptionListResponse,
        )

    def delete(
        self,
        recording_transcription_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RecordingTranscriptionDeleteResponse:
        """
        Permanently deletes a recording transcription.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not recording_transcription_id:
            raise ValueError(
                f"Expected a non-empty value for `recording_transcription_id` but received {recording_transcription_id!r}"
            )
        return self._delete(
            f"/recording_transcriptions/{recording_transcription_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingTranscriptionDeleteResponse,
        )


class AsyncRecordingTranscriptionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRecordingTranscriptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRecordingTranscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRecordingTranscriptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncRecordingTranscriptionsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        recording_transcription_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RecordingTranscriptionRetrieveResponse:
        """
        Retrieves the details of an existing recording transcription.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not recording_transcription_id:
            raise ValueError(
                f"Expected a non-empty value for `recording_transcription_id` but received {recording_transcription_id!r}"
            )
        return await self._get(
            f"/recording_transcriptions/{recording_transcription_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingTranscriptionRetrieveResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RecordingTranscriptionListResponse:
        """Returns a list of your recording transcriptions."""
        return await self._get(
            "/recording_transcriptions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingTranscriptionListResponse,
        )

    async def delete(
        self,
        recording_transcription_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RecordingTranscriptionDeleteResponse:
        """
        Permanently deletes a recording transcription.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not recording_transcription_id:
            raise ValueError(
                f"Expected a non-empty value for `recording_transcription_id` but received {recording_transcription_id!r}"
            )
        return await self._delete(
            f"/recording_transcriptions/{recording_transcription_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingTranscriptionDeleteResponse,
        )


class RecordingTranscriptionsResourceWithRawResponse:
    def __init__(self, recording_transcriptions: RecordingTranscriptionsResource) -> None:
        self._recording_transcriptions = recording_transcriptions

        self.retrieve = to_raw_response_wrapper(
            recording_transcriptions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            recording_transcriptions.list,
        )
        self.delete = to_raw_response_wrapper(
            recording_transcriptions.delete,
        )


class AsyncRecordingTranscriptionsResourceWithRawResponse:
    def __init__(self, recording_transcriptions: AsyncRecordingTranscriptionsResource) -> None:
        self._recording_transcriptions = recording_transcriptions

        self.retrieve = async_to_raw_response_wrapper(
            recording_transcriptions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            recording_transcriptions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            recording_transcriptions.delete,
        )


class RecordingTranscriptionsResourceWithStreamingResponse:
    def __init__(self, recording_transcriptions: RecordingTranscriptionsResource) -> None:
        self._recording_transcriptions = recording_transcriptions

        self.retrieve = to_streamed_response_wrapper(
            recording_transcriptions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            recording_transcriptions.list,
        )
        self.delete = to_streamed_response_wrapper(
            recording_transcriptions.delete,
        )


class AsyncRecordingTranscriptionsResourceWithStreamingResponse:
    def __init__(self, recording_transcriptions: AsyncRecordingTranscriptionsResource) -> None:
        self._recording_transcriptions = recording_transcriptions

        self.retrieve = async_to_streamed_response_wrapper(
            recording_transcriptions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            recording_transcriptions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            recording_transcriptions.delete,
        )

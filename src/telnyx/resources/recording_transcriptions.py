# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import recording_transcription_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from .._base_client import AsyncPaginator, make_request_options
from ..types.recording_transcription import RecordingTranscription
from ..types.recording_transcription_delete_response import RecordingTranscriptionDeleteResponse
from ..types.recording_transcription_retrieve_response import RecordingTranscriptionRetrieveResponse

__all__ = ["RecordingTranscriptionsResource", "AsyncRecordingTranscriptionsResource"]


class RecordingTranscriptionsResource(SyncAPIResource):
    """Call Recordings operations."""

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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        filter: recording_transcription_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[RecordingTranscription]:
        """
        Returns a list of your recording transcriptions.

        Args:
          filter: Filter recording transcriptions by various attributes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/recording_transcriptions",
            page=SyncDefaultFlatPagination[RecordingTranscription],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    recording_transcription_list_params.RecordingTranscriptionListParams,
                ),
            ),
            model=RecordingTranscription,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
    """Call Recordings operations."""

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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    def list(
        self,
        *,
        filter: recording_transcription_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[RecordingTranscription, AsyncDefaultFlatPagination[RecordingTranscription]]:
        """
        Returns a list of your recording transcriptions.

        Args:
          filter: Filter recording transcriptions by various attributes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/recording_transcriptions",
            page=AsyncDefaultFlatPagination[RecordingTranscription],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    recording_transcription_list_params.RecordingTranscriptionListParams,
                ),
            ),
            model=RecordingTranscription,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.texml.accounts.transcriptions.json_retrieve_recording_transcription_sid_json_response import (
    JsonRetrieveRecordingTranscriptionSidJsonResponse,
)

__all__ = ["JsonResource", "AsyncJsonResource"]


class JsonResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> JsonResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return JsonResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JsonResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return JsonResourceWithStreamingResponse(self)

    def delete_recording_transcription_sid_json(
        self,
        recording_transcription_sid: str,
        *,
        account_sid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Permanently deletes a recording transcription.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        if not recording_transcription_sid:
            raise ValueError(
                f"Expected a non-empty value for `recording_transcription_sid` but received {recording_transcription_sid!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/texml/Accounts/{account_sid}/Transcriptions/{recording_transcription_sid}.json",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve_recording_transcription_sid_json(
        self,
        recording_transcription_sid: str,
        *,
        account_sid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JsonRetrieveRecordingTranscriptionSidJsonResponse:
        """
        Returns the recording transcription resource identified by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        if not recording_transcription_sid:
            raise ValueError(
                f"Expected a non-empty value for `recording_transcription_sid` but received {recording_transcription_sid!r}"
            )
        return self._get(
            f"/texml/Accounts/{account_sid}/Transcriptions/{recording_transcription_sid}.json",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JsonRetrieveRecordingTranscriptionSidJsonResponse,
        )


class AsyncJsonResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncJsonResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncJsonResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJsonResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncJsonResourceWithStreamingResponse(self)

    async def delete_recording_transcription_sid_json(
        self,
        recording_transcription_sid: str,
        *,
        account_sid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Permanently deletes a recording transcription.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        if not recording_transcription_sid:
            raise ValueError(
                f"Expected a non-empty value for `recording_transcription_sid` but received {recording_transcription_sid!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/texml/Accounts/{account_sid}/Transcriptions/{recording_transcription_sid}.json",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve_recording_transcription_sid_json(
        self,
        recording_transcription_sid: str,
        *,
        account_sid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JsonRetrieveRecordingTranscriptionSidJsonResponse:
        """
        Returns the recording transcription resource identified by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        if not recording_transcription_sid:
            raise ValueError(
                f"Expected a non-empty value for `recording_transcription_sid` but received {recording_transcription_sid!r}"
            )
        return await self._get(
            f"/texml/Accounts/{account_sid}/Transcriptions/{recording_transcription_sid}.json",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JsonRetrieveRecordingTranscriptionSidJsonResponse,
        )


class JsonResourceWithRawResponse:
    def __init__(self, json: JsonResource) -> None:
        self._json = json

        self.delete_recording_transcription_sid_json = to_raw_response_wrapper(
            json.delete_recording_transcription_sid_json,
        )
        self.retrieve_recording_transcription_sid_json = to_raw_response_wrapper(
            json.retrieve_recording_transcription_sid_json,
        )


class AsyncJsonResourceWithRawResponse:
    def __init__(self, json: AsyncJsonResource) -> None:
        self._json = json

        self.delete_recording_transcription_sid_json = async_to_raw_response_wrapper(
            json.delete_recording_transcription_sid_json,
        )
        self.retrieve_recording_transcription_sid_json = async_to_raw_response_wrapper(
            json.retrieve_recording_transcription_sid_json,
        )


class JsonResourceWithStreamingResponse:
    def __init__(self, json: JsonResource) -> None:
        self._json = json

        self.delete_recording_transcription_sid_json = to_streamed_response_wrapper(
            json.delete_recording_transcription_sid_json,
        )
        self.retrieve_recording_transcription_sid_json = to_streamed_response_wrapper(
            json.retrieve_recording_transcription_sid_json,
        )


class AsyncJsonResourceWithStreamingResponse:
    def __init__(self, json: AsyncJsonResource) -> None:
        self._json = json

        self.delete_recording_transcription_sid_json = async_to_streamed_response_wrapper(
            json.delete_recording_transcription_sid_json,
        )
        self.retrieve_recording_transcription_sid_json = async_to_streamed_response_wrapper(
            json.retrieve_recording_transcription_sid_json,
        )

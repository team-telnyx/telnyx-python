# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.texml.accounts.calls import recordings_json_recordings_json_params
from .....types.texml.accounts.calls.recordings_json_recordings_json_response import (
    RecordingsJsonRecordingsJsonResponse,
)
from .....types.texml.accounts.calls.recordings_json_retrieve_recordings_json_response import (
    RecordingsJsonRetrieveRecordingsJsonResponse,
)

__all__ = ["RecordingsJsonResource", "AsyncRecordingsJsonResource"]


class RecordingsJsonResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RecordingsJsonResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return RecordingsJsonResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RecordingsJsonResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return RecordingsJsonResourceWithStreamingResponse(self)

    def recordings_json(
        self,
        call_sid: str,
        *,
        account_sid: str,
        play_beep: bool | NotGiven = NOT_GIVEN,
        recording_channels: Literal["single", "dual"] | NotGiven = NOT_GIVEN,
        recording_status_callback: str | NotGiven = NOT_GIVEN,
        recording_status_callback_event: str | NotGiven = NOT_GIVEN,
        recording_status_callback_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        recording_track: Literal["inbound", "outbound", "both"] | NotGiven = NOT_GIVEN,
        send_recording_url: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RecordingsJsonRecordingsJsonResponse:
        """
        Starts recording with specified parameters for call idientified by call_sid.

        Args:
          play_beep: Whether to play a beep when recording is started.

          recording_channels: When `dual`, final audio file has the first leg on channel A, and the rest on
              channel B. `single` mixes both tracks into a single channel.

          recording_status_callback: Url where status callbacks will be sent.

          recording_status_callback_event: The changes to the recording's state that should generate a call to
              `RecoridngStatusCallback`. Can be: `in-progress`, `completed` and `absent`.
              Separate multiple values with a space. Defaults to `completed`.

          recording_status_callback_method: HTTP method used to send status callbacks.

          recording_track: The audio track to record for the call. The default is `both`.

          send_recording_url: Whether to send RecordingUrl in webhooks.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        if not call_sid:
            raise ValueError(f"Expected a non-empty value for `call_sid` but received {call_sid!r}")
        return self._post(
            f"/texml/Accounts/{account_sid}/Calls/{call_sid}/Recordings.json",
            body=maybe_transform(
                {
                    "play_beep": play_beep,
                    "recording_channels": recording_channels,
                    "recording_status_callback": recording_status_callback,
                    "recording_status_callback_event": recording_status_callback_event,
                    "recording_status_callback_method": recording_status_callback_method,
                    "recording_track": recording_track,
                    "send_recording_url": send_recording_url,
                },
                recordings_json_recordings_json_params.RecordingsJsonRecordingsJsonParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingsJsonRecordingsJsonResponse,
        )

    def retrieve_recordings_json(
        self,
        call_sid: str,
        *,
        account_sid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RecordingsJsonRetrieveRecordingsJsonResponse:
        """
        Returns recordings for a call identified by call_sid.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        if not call_sid:
            raise ValueError(f"Expected a non-empty value for `call_sid` but received {call_sid!r}")
        return self._get(
            f"/texml/Accounts/{account_sid}/Calls/{call_sid}/Recordings.json",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingsJsonRetrieveRecordingsJsonResponse,
        )


class AsyncRecordingsJsonResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRecordingsJsonResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRecordingsJsonResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRecordingsJsonResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncRecordingsJsonResourceWithStreamingResponse(self)

    async def recordings_json(
        self,
        call_sid: str,
        *,
        account_sid: str,
        play_beep: bool | NotGiven = NOT_GIVEN,
        recording_channels: Literal["single", "dual"] | NotGiven = NOT_GIVEN,
        recording_status_callback: str | NotGiven = NOT_GIVEN,
        recording_status_callback_event: str | NotGiven = NOT_GIVEN,
        recording_status_callback_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        recording_track: Literal["inbound", "outbound", "both"] | NotGiven = NOT_GIVEN,
        send_recording_url: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RecordingsJsonRecordingsJsonResponse:
        """
        Starts recording with specified parameters for call idientified by call_sid.

        Args:
          play_beep: Whether to play a beep when recording is started.

          recording_channels: When `dual`, final audio file has the first leg on channel A, and the rest on
              channel B. `single` mixes both tracks into a single channel.

          recording_status_callback: Url where status callbacks will be sent.

          recording_status_callback_event: The changes to the recording's state that should generate a call to
              `RecoridngStatusCallback`. Can be: `in-progress`, `completed` and `absent`.
              Separate multiple values with a space. Defaults to `completed`.

          recording_status_callback_method: HTTP method used to send status callbacks.

          recording_track: The audio track to record for the call. The default is `both`.

          send_recording_url: Whether to send RecordingUrl in webhooks.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        if not call_sid:
            raise ValueError(f"Expected a non-empty value for `call_sid` but received {call_sid!r}")
        return await self._post(
            f"/texml/Accounts/{account_sid}/Calls/{call_sid}/Recordings.json",
            body=await async_maybe_transform(
                {
                    "play_beep": play_beep,
                    "recording_channels": recording_channels,
                    "recording_status_callback": recording_status_callback,
                    "recording_status_callback_event": recording_status_callback_event,
                    "recording_status_callback_method": recording_status_callback_method,
                    "recording_track": recording_track,
                    "send_recording_url": send_recording_url,
                },
                recordings_json_recordings_json_params.RecordingsJsonRecordingsJsonParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingsJsonRecordingsJsonResponse,
        )

    async def retrieve_recordings_json(
        self,
        call_sid: str,
        *,
        account_sid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RecordingsJsonRetrieveRecordingsJsonResponse:
        """
        Returns recordings for a call identified by call_sid.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        if not call_sid:
            raise ValueError(f"Expected a non-empty value for `call_sid` but received {call_sid!r}")
        return await self._get(
            f"/texml/Accounts/{account_sid}/Calls/{call_sid}/Recordings.json",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingsJsonRetrieveRecordingsJsonResponse,
        )


class RecordingsJsonResourceWithRawResponse:
    def __init__(self, recordings_json: RecordingsJsonResource) -> None:
        self._recordings_json = recordings_json

        self.recordings_json = to_raw_response_wrapper(
            recordings_json.recordings_json,
        )
        self.retrieve_recordings_json = to_raw_response_wrapper(
            recordings_json.retrieve_recordings_json,
        )


class AsyncRecordingsJsonResourceWithRawResponse:
    def __init__(self, recordings_json: AsyncRecordingsJsonResource) -> None:
        self._recordings_json = recordings_json

        self.recordings_json = async_to_raw_response_wrapper(
            recordings_json.recordings_json,
        )
        self.retrieve_recordings_json = async_to_raw_response_wrapper(
            recordings_json.retrieve_recordings_json,
        )


class RecordingsJsonResourceWithStreamingResponse:
    def __init__(self, recordings_json: RecordingsJsonResource) -> None:
        self._recordings_json = recordings_json

        self.recordings_json = to_streamed_response_wrapper(
            recordings_json.recordings_json,
        )
        self.retrieve_recordings_json = to_streamed_response_wrapper(
            recordings_json.retrieve_recordings_json,
        )


class AsyncRecordingsJsonResourceWithStreamingResponse:
    def __init__(self, recordings_json: AsyncRecordingsJsonResource) -> None:
        self._recordings_json = recordings_json

        self.recordings_json = async_to_streamed_response_wrapper(
            recordings_json.recordings_json,
        )
        self.retrieve_recordings_json = async_to_streamed_response_wrapper(
            recordings_json.retrieve_recordings_json,
        )

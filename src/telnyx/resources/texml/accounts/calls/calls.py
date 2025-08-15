# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .siprec import (
    SiprecResource,
    AsyncSiprecResource,
    SiprecResourceWithRawResponse,
    AsyncSiprecResourceWithRawResponse,
    SiprecResourceWithStreamingResponse,
    AsyncSiprecResourceWithStreamingResponse,
)
from .streams import (
    StreamsResource,
    AsyncStreamsResource,
    StreamsResourceWithRawResponse,
    AsyncStreamsResourceWithRawResponse,
    StreamsResourceWithStreamingResponse,
    AsyncStreamsResourceWithStreamingResponse,
)
from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform, async_maybe_transform
from .recordings import (
    RecordingsResource,
    AsyncRecordingsResource,
    RecordingsResourceWithRawResponse,
    AsyncRecordingsResourceWithRawResponse,
    RecordingsResourceWithStreamingResponse,
    AsyncRecordingsResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .recordings_json import (
    RecordingsJsonResource,
    AsyncRecordingsJsonResource,
    RecordingsJsonResourceWithRawResponse,
    AsyncRecordingsJsonResourceWithRawResponse,
    RecordingsJsonResourceWithStreamingResponse,
    AsyncRecordingsJsonResourceWithStreamingResponse,
)
from ....._base_client import make_request_options
from .....types.texml.accounts import (
    call_calls_params,
    call_update_params,
    call_siprec_json_params,
    call_streams_json_params,
    call_retrieve_calls_params,
)
from .....types.texml.accounts.call_calls_response import CallCallsResponse
from .....types.texml.accounts.call_update_response import CallUpdateResponse
from .....types.texml.accounts.call_retrieve_response import CallRetrieveResponse
from .....types.texml.accounts.call_siprec_json_response import CallSiprecJsonResponse
from .....types.texml.accounts.call_streams_json_response import CallStreamsJsonResponse
from .....types.texml.accounts.call_retrieve_calls_response import CallRetrieveCallsResponse

__all__ = ["CallsResource", "AsyncCallsResource"]


class CallsResource(SyncAPIResource):
    @cached_property
    def recordings_json(self) -> RecordingsJsonResource:
        return RecordingsJsonResource(self._client)

    @cached_property
    def recordings(self) -> RecordingsResource:
        return RecordingsResource(self._client)

    @cached_property
    def siprec(self) -> SiprecResource:
        return SiprecResource(self._client)

    @cached_property
    def streams(self) -> StreamsResource:
        return StreamsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CallsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return CallsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CallsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return CallsResourceWithStreamingResponse(self)

    def retrieve(
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
    ) -> CallRetrieveResponse:
        """Returns an individual call identified by its CallSid.

        This endpoint is
        eventually consistent.

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
            f"/texml/Accounts/{account_sid}/Calls/{call_sid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallRetrieveResponse,
        )

    def update(
        self,
        call_sid: str,
        *,
        account_sid: str,
        fallback_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        fallback_url: str | NotGiven = NOT_GIVEN,
        method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        status_callback: str | NotGiven = NOT_GIVEN,
        status_callback_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        texml: str | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallUpdateResponse:
        """Update TeXML call.

        Please note that the keys present in the payload MUST BE
        formatted in CamelCase as specified in the example.

        Args:
          fallback_method: HTTP request type used for `FallbackUrl`.

          fallback_url: A failover URL for which Telnyx will retrieve the TeXML call instructions if the
              Url is not responding.

          method: HTTP request type used for `Url`.

          status: The value to set the call status to. Setting the status to completed ends the
              call.

          status_callback: URL destination for Telnyx to send status callback events to for the call.

          status_callback_method: HTTP request type used for `StatusCallback`.

          texml: TeXML to replace the current one with.

          url: The URL where TeXML will make a request to retrieve a new set of TeXML
              instructions to continue the call flow.

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
            f"/texml/Accounts/{account_sid}/Calls/{call_sid}",
            body=maybe_transform(
                {
                    "fallback_method": fallback_method,
                    "fallback_url": fallback_url,
                    "method": method,
                    "status": status,
                    "status_callback": status_callback,
                    "status_callback_method": status_callback_method,
                    "texml": texml,
                    "url": url,
                },
                call_update_params.CallUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallUpdateResponse,
        )

    def calls(
        self,
        account_sid: str,
        *,
        application_sid: str,
        from_: str,
        to: str,
        async_amd: bool | NotGiven = NOT_GIVEN,
        async_amd_status_callback: str | NotGiven = NOT_GIVEN,
        async_amd_status_callback_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        caller_id: str | NotGiven = NOT_GIVEN,
        cancel_playback_on_detect_message_end: bool | NotGiven = NOT_GIVEN,
        cancel_playback_on_machine_detection: bool | NotGiven = NOT_GIVEN,
        detection_mode: Literal["Premium", "Regular"] | NotGiven = NOT_GIVEN,
        fallback_url: str | NotGiven = NOT_GIVEN,
        machine_detection: Literal["Enable", "Disable", "DetectMessageEnd"] | NotGiven = NOT_GIVEN,
        machine_detection_silence_timeout: int | NotGiven = NOT_GIVEN,
        machine_detection_speech_end_threshold: int | NotGiven = NOT_GIVEN,
        machine_detection_speech_threshold: int | NotGiven = NOT_GIVEN,
        machine_detection_timeout: int | NotGiven = NOT_GIVEN,
        preferred_codecs: str | NotGiven = NOT_GIVEN,
        record: bool | NotGiven = NOT_GIVEN,
        recording_channels: Literal["mono", "dual"] | NotGiven = NOT_GIVEN,
        recording_status_callback: str | NotGiven = NOT_GIVEN,
        recording_status_callback_event: str | NotGiven = NOT_GIVEN,
        recording_status_callback_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        recording_timeout: int | NotGiven = NOT_GIVEN,
        recording_track: Literal["inbound", "outbound", "both"] | NotGiven = NOT_GIVEN,
        send_recording_url: bool | NotGiven = NOT_GIVEN,
        sip_auth_password: str | NotGiven = NOT_GIVEN,
        sip_auth_username: str | NotGiven = NOT_GIVEN,
        status_callback: str | NotGiven = NOT_GIVEN,
        status_callback_event: Literal["initiated", "ringing", "answered", "completed"] | NotGiven = NOT_GIVEN,
        status_callback_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        trim: Literal["trim-silence", "do-not-trim"] | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        url_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallCallsResponse:
        """Initiate an outbound TeXML call.

        Telnyx will request TeXML from the XML Request
        URL configured for the connection in the Mission Control Portal.

        Args:
          application_sid: The ID of the TeXML Application.

          from_: The phone number of the party that initiated the call. Phone numbers are
              formatted with a `+` and country code.

          to: The phone number of the called party. Phone numbers are formatted with a `+` and
              country code.

          async_amd: Select whether to perform answering machine detection in the background. By
              default execution is blocked until Answering Machine Detection is completed.

          async_amd_status_callback: URL destination for Telnyx to send AMD callback events to for the call.

          async_amd_status_callback_method: HTTP request type used for `AsyncAmdStatusCallback`. The default value is
              inherited from TeXML Application setting.

          caller_id: To be used as the caller id name (SIP From Display Name) presented to the
              destination (`To` number). The string should have a maximum of 128 characters,
              containing only letters, numbers, spaces, and `-_~!.+` special characters. If
              ommited, the display name will be the same as the number in the `From` field.

          cancel_playback_on_detect_message_end: Whether to cancel ongoing playback on `greeting ended` detection. Defaults to
              `true`.

          cancel_playback_on_machine_detection: Whether to cancel ongoing playback on `machine` detection. Defaults to `true`.

          detection_mode: Allows you to chose between Premium and Standard detections.

          fallback_url: A failover URL for which Telnyx will retrieve the TeXML call instructions if the
              `Url` is not responding.

          machine_detection: Enables Answering Machine Detection.

          machine_detection_silence_timeout: If initial silence duration is greater than this value, consider it a machine.
              Ignored when `premium` detection is used.

          machine_detection_speech_end_threshold: Silence duration threshold after a greeting message or voice for it be
              considered human. Ignored when `premium` detection is used.

          machine_detection_speech_threshold: Maximum threshold of a human greeting. If greeting longer than this value,
              considered machine. Ignored when `premium` detection is used.

          machine_detection_timeout: Maximum timeout threshold in milliseconds for overall detection.

          preferred_codecs: The list of comma-separated codecs to be offered on a call.

          record: Whether to record the entire participant's call leg. Defaults to `false`.

          recording_channels: The number of channels in the final recording. Defaults to `mono`.

          recording_status_callback: The URL the recording callbacks will be sent to.

          recording_status_callback_event: The changes to the recording's state that should generate a call to
              `RecoridngStatusCallback`. Can be: `in-progress`, `completed` and `absent`.
              Separate multiple values with a space. Defaults to `completed`.

          recording_status_callback_method: HTTP request type used for `RecordingStatusCallback`. Defaults to `POST`.

          recording_timeout: The number of seconds that Telnyx will wait for the recording to be stopped if
              silence is detected. The timer only starts when the speech is detected. Please
              note that the transcription is used to detect silence and the related charge
              will be applied. The minimum value is 0. The default value is 0 (infinite)

          recording_track: The audio track to record for the call. The default is `both`.

          send_recording_url: Whether to send RecordingUrl in webhooks.

          sip_auth_password: The password to use for SIP authentication.

          sip_auth_username: The username to use for SIP authentication.

          status_callback: URL destination for Telnyx to send status callback events to for the call.

          status_callback_event: The call events for which Telnyx should send a webhook. Multiple events can be
              defined when separated by a space.

          status_callback_method: HTTP request type used for `StatusCallback`.

          trim: Whether to trim any leading and trailing silence from the recording. Defaults to
              `trim-silence`.

          url: The URL from which Telnyx will retrieve the TeXML call instructions.

          url_method: HTTP request type used for `Url`. The default value is inherited from TeXML
              Application setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        return self._post(
            f"/texml/Accounts/{account_sid}/Calls",
            body=maybe_transform(
                {
                    "application_sid": application_sid,
                    "from_": from_,
                    "to": to,
                    "async_amd": async_amd,
                    "async_amd_status_callback": async_amd_status_callback,
                    "async_amd_status_callback_method": async_amd_status_callback_method,
                    "caller_id": caller_id,
                    "cancel_playback_on_detect_message_end": cancel_playback_on_detect_message_end,
                    "cancel_playback_on_machine_detection": cancel_playback_on_machine_detection,
                    "detection_mode": detection_mode,
                    "fallback_url": fallback_url,
                    "machine_detection": machine_detection,
                    "machine_detection_silence_timeout": machine_detection_silence_timeout,
                    "machine_detection_speech_end_threshold": machine_detection_speech_end_threshold,
                    "machine_detection_speech_threshold": machine_detection_speech_threshold,
                    "machine_detection_timeout": machine_detection_timeout,
                    "preferred_codecs": preferred_codecs,
                    "record": record,
                    "recording_channels": recording_channels,
                    "recording_status_callback": recording_status_callback,
                    "recording_status_callback_event": recording_status_callback_event,
                    "recording_status_callback_method": recording_status_callback_method,
                    "recording_timeout": recording_timeout,
                    "recording_track": recording_track,
                    "send_recording_url": send_recording_url,
                    "sip_auth_password": sip_auth_password,
                    "sip_auth_username": sip_auth_username,
                    "status_callback": status_callback,
                    "status_callback_event": status_callback_event,
                    "status_callback_method": status_callback_method,
                    "trim": trim,
                    "url": url,
                    "url_method": url_method,
                },
                call_calls_params.CallCallsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallCallsResponse,
        )

    def retrieve_calls(
        self,
        account_sid: str,
        *,
        end_time: str | NotGiven = NOT_GIVEN,
        end_time_gt: str | NotGiven = NOT_GIVEN,
        end_time_lt: str | NotGiven = NOT_GIVEN,
        from_: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        page_token: str | NotGiven = NOT_GIVEN,
        start_time: str | NotGiven = NOT_GIVEN,
        start_time_gt: str | NotGiven = NOT_GIVEN,
        start_time_lt: str | NotGiven = NOT_GIVEN,
        status: Literal["canceled", "completed", "failed", "busy", "no-answer"] | NotGiven = NOT_GIVEN,
        to: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallRetrieveCallsResponse:
        """Returns multiple call resouces for an account.

        This endpoint is eventually
        consistent.

        Args:
          end_time: Filters calls by their end date. Expected format is YYYY-MM-DD

          end_time_gt: Filters calls by their end date (after). Expected format is YYYY-MM-DD

          end_time_lt: Filters calls by their end date (before). Expected format is YYYY-MM-DD

          from_: Filters calls by the from number.

          page: The number of the page to be displayed, zero-indexed, should be used in
              conjuction with PageToken.

          page_size: The number of records to be displayed on a page

          page_token: Used to request the next page of results.

          start_time: Filters calls by their start date. Expected format is YYYY-MM-DD.

          start_time_gt: Filters calls by their start date (after). Expected format is YYYY-MM-DD

          start_time_lt: Filters calls by their start date (before). Expected format is YYYY-MM-DD

          status: Filters calls by status.

          to: Filters calls by the to number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        return self._get(
            f"/texml/Accounts/{account_sid}/Calls",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_time": end_time,
                        "end_time_gt": end_time_gt,
                        "end_time_lt": end_time_lt,
                        "from_": from_,
                        "page": page,
                        "page_size": page_size,
                        "page_token": page_token,
                        "start_time": start_time,
                        "start_time_gt": start_time_gt,
                        "start_time_lt": start_time_lt,
                        "status": status,
                        "to": to,
                    },
                    call_retrieve_calls_params.CallRetrieveCallsParams,
                ),
            ),
            cast_to=CallRetrieveCallsResponse,
        )

    def siprec_json(
        self,
        call_sid: str,
        *,
        account_sid: str,
        connector_name: str | NotGiven = NOT_GIVEN,
        include_metadata_custom_headers: Literal[True, False] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        secure: Literal[True, False] | NotGiven = NOT_GIVEN,
        session_timeout_secs: int | NotGiven = NOT_GIVEN,
        sip_transport: Literal["udp", "tcp", "tls"] | NotGiven = NOT_GIVEN,
        status_callback: str | NotGiven = NOT_GIVEN,
        status_callback_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        track: Literal["both_tracks", "inbound_track", "outbound_track"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallSiprecJsonResponse:
        """
        Starts siprec session with specified parameters for call idientified by
        call_sid.

        Args:
          connector_name: The name of the connector to use for the SIPREC session.

          include_metadata_custom_headers: When set, custom parameters will be added as metadata
              (recording.session.ExtensionParameters). Otherwise, they’ll be added to sip
              headers.

          name: Name of the SIPREC session. May be used to stop the SIPREC session from TeXML
              instruction.

          secure: Controls whether to encrypt media sent to your SRS using SRTP and TLS. When set
              you need to configure SRS port in your connector to 5061.

          session_timeout_secs: Sets `Session-Expires` header to the INVITE. A reinvite is sent every half the
              value set. Usefull for session keep alive. Minimum value is 90, set to 0 to
              disable.

          sip_transport: Specifies SIP transport protocol.

          status_callback: URL destination for Telnyx to send status callback events to for the siprec
              session.

          status_callback_method: HTTP request type used for `StatusCallback`.

          track: The track to be used for siprec session. Can be `both_tracks`, `inbound_track`
              or `outbound_track`. Defaults to `both_tracks`.

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
            f"/texml/Accounts/{account_sid}/Calls/{call_sid}/Siprec.json",
            body=maybe_transform(
                {
                    "connector_name": connector_name,
                    "include_metadata_custom_headers": include_metadata_custom_headers,
                    "name": name,
                    "secure": secure,
                    "session_timeout_secs": session_timeout_secs,
                    "sip_transport": sip_transport,
                    "status_callback": status_callback,
                    "status_callback_method": status_callback_method,
                    "track": track,
                },
                call_siprec_json_params.CallSiprecJsonParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallSiprecJsonResponse,
        )

    def streams_json(
        self,
        call_sid: str,
        *,
        account_sid: str,
        bidirectional_codec: Literal["PCMU", "PCMA", "G722"] | NotGiven = NOT_GIVEN,
        bidirectional_mode: Literal["mp3", "rtp"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        status_callback: str | NotGiven = NOT_GIVEN,
        status_callback_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        track: Literal["inbound_track", "outbound_track", "both_tracks"] | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallStreamsJsonResponse:
        """
        Starts streaming media from a call to a specific WebSocket address.

        Args:
          bidirectional_codec: Indicates codec for bidirectional streaming RTP payloads. Used only with
              stream_bidirectional_mode=rtp. Case sensitive.

          bidirectional_mode: Configures method of bidirectional streaming (mp3, rtp).

          name: The user specified name of Stream.

          status_callback: Url where status callbacks will be sent.

          status_callback_method: HTTP method used to send status callbacks.

          track: Tracks to be included in the stream

          url: The destination WebSocket address where the stream is going to be delivered.

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
            f"/texml/Accounts/{account_sid}/Calls/{call_sid}/Streams.json",
            body=maybe_transform(
                {
                    "bidirectional_codec": bidirectional_codec,
                    "bidirectional_mode": bidirectional_mode,
                    "name": name,
                    "status_callback": status_callback,
                    "status_callback_method": status_callback_method,
                    "track": track,
                    "url": url,
                },
                call_streams_json_params.CallStreamsJsonParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallStreamsJsonResponse,
        )


class AsyncCallsResource(AsyncAPIResource):
    @cached_property
    def recordings_json(self) -> AsyncRecordingsJsonResource:
        return AsyncRecordingsJsonResource(self._client)

    @cached_property
    def recordings(self) -> AsyncRecordingsResource:
        return AsyncRecordingsResource(self._client)

    @cached_property
    def siprec(self) -> AsyncSiprecResource:
        return AsyncSiprecResource(self._client)

    @cached_property
    def streams(self) -> AsyncStreamsResource:
        return AsyncStreamsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCallsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCallsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCallsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncCallsResourceWithStreamingResponse(self)

    async def retrieve(
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
    ) -> CallRetrieveResponse:
        """Returns an individual call identified by its CallSid.

        This endpoint is
        eventually consistent.

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
            f"/texml/Accounts/{account_sid}/Calls/{call_sid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallRetrieveResponse,
        )

    async def update(
        self,
        call_sid: str,
        *,
        account_sid: str,
        fallback_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        fallback_url: str | NotGiven = NOT_GIVEN,
        method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        status_callback: str | NotGiven = NOT_GIVEN,
        status_callback_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        texml: str | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallUpdateResponse:
        """Update TeXML call.

        Please note that the keys present in the payload MUST BE
        formatted in CamelCase as specified in the example.

        Args:
          fallback_method: HTTP request type used for `FallbackUrl`.

          fallback_url: A failover URL for which Telnyx will retrieve the TeXML call instructions if the
              Url is not responding.

          method: HTTP request type used for `Url`.

          status: The value to set the call status to. Setting the status to completed ends the
              call.

          status_callback: URL destination for Telnyx to send status callback events to for the call.

          status_callback_method: HTTP request type used for `StatusCallback`.

          texml: TeXML to replace the current one with.

          url: The URL where TeXML will make a request to retrieve a new set of TeXML
              instructions to continue the call flow.

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
            f"/texml/Accounts/{account_sid}/Calls/{call_sid}",
            body=await async_maybe_transform(
                {
                    "fallback_method": fallback_method,
                    "fallback_url": fallback_url,
                    "method": method,
                    "status": status,
                    "status_callback": status_callback,
                    "status_callback_method": status_callback_method,
                    "texml": texml,
                    "url": url,
                },
                call_update_params.CallUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallUpdateResponse,
        )

    async def calls(
        self,
        account_sid: str,
        *,
        application_sid: str,
        from_: str,
        to: str,
        async_amd: bool | NotGiven = NOT_GIVEN,
        async_amd_status_callback: str | NotGiven = NOT_GIVEN,
        async_amd_status_callback_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        caller_id: str | NotGiven = NOT_GIVEN,
        cancel_playback_on_detect_message_end: bool | NotGiven = NOT_GIVEN,
        cancel_playback_on_machine_detection: bool | NotGiven = NOT_GIVEN,
        detection_mode: Literal["Premium", "Regular"] | NotGiven = NOT_GIVEN,
        fallback_url: str | NotGiven = NOT_GIVEN,
        machine_detection: Literal["Enable", "Disable", "DetectMessageEnd"] | NotGiven = NOT_GIVEN,
        machine_detection_silence_timeout: int | NotGiven = NOT_GIVEN,
        machine_detection_speech_end_threshold: int | NotGiven = NOT_GIVEN,
        machine_detection_speech_threshold: int | NotGiven = NOT_GIVEN,
        machine_detection_timeout: int | NotGiven = NOT_GIVEN,
        preferred_codecs: str | NotGiven = NOT_GIVEN,
        record: bool | NotGiven = NOT_GIVEN,
        recording_channels: Literal["mono", "dual"] | NotGiven = NOT_GIVEN,
        recording_status_callback: str | NotGiven = NOT_GIVEN,
        recording_status_callback_event: str | NotGiven = NOT_GIVEN,
        recording_status_callback_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        recording_timeout: int | NotGiven = NOT_GIVEN,
        recording_track: Literal["inbound", "outbound", "both"] | NotGiven = NOT_GIVEN,
        send_recording_url: bool | NotGiven = NOT_GIVEN,
        sip_auth_password: str | NotGiven = NOT_GIVEN,
        sip_auth_username: str | NotGiven = NOT_GIVEN,
        status_callback: str | NotGiven = NOT_GIVEN,
        status_callback_event: Literal["initiated", "ringing", "answered", "completed"] | NotGiven = NOT_GIVEN,
        status_callback_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        trim: Literal["trim-silence", "do-not-trim"] | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        url_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallCallsResponse:
        """Initiate an outbound TeXML call.

        Telnyx will request TeXML from the XML Request
        URL configured for the connection in the Mission Control Portal.

        Args:
          application_sid: The ID of the TeXML Application.

          from_: The phone number of the party that initiated the call. Phone numbers are
              formatted with a `+` and country code.

          to: The phone number of the called party. Phone numbers are formatted with a `+` and
              country code.

          async_amd: Select whether to perform answering machine detection in the background. By
              default execution is blocked until Answering Machine Detection is completed.

          async_amd_status_callback: URL destination for Telnyx to send AMD callback events to for the call.

          async_amd_status_callback_method: HTTP request type used for `AsyncAmdStatusCallback`. The default value is
              inherited from TeXML Application setting.

          caller_id: To be used as the caller id name (SIP From Display Name) presented to the
              destination (`To` number). The string should have a maximum of 128 characters,
              containing only letters, numbers, spaces, and `-_~!.+` special characters. If
              ommited, the display name will be the same as the number in the `From` field.

          cancel_playback_on_detect_message_end: Whether to cancel ongoing playback on `greeting ended` detection. Defaults to
              `true`.

          cancel_playback_on_machine_detection: Whether to cancel ongoing playback on `machine` detection. Defaults to `true`.

          detection_mode: Allows you to chose between Premium and Standard detections.

          fallback_url: A failover URL for which Telnyx will retrieve the TeXML call instructions if the
              `Url` is not responding.

          machine_detection: Enables Answering Machine Detection.

          machine_detection_silence_timeout: If initial silence duration is greater than this value, consider it a machine.
              Ignored when `premium` detection is used.

          machine_detection_speech_end_threshold: Silence duration threshold after a greeting message or voice for it be
              considered human. Ignored when `premium` detection is used.

          machine_detection_speech_threshold: Maximum threshold of a human greeting. If greeting longer than this value,
              considered machine. Ignored when `premium` detection is used.

          machine_detection_timeout: Maximum timeout threshold in milliseconds for overall detection.

          preferred_codecs: The list of comma-separated codecs to be offered on a call.

          record: Whether to record the entire participant's call leg. Defaults to `false`.

          recording_channels: The number of channels in the final recording. Defaults to `mono`.

          recording_status_callback: The URL the recording callbacks will be sent to.

          recording_status_callback_event: The changes to the recording's state that should generate a call to
              `RecoridngStatusCallback`. Can be: `in-progress`, `completed` and `absent`.
              Separate multiple values with a space. Defaults to `completed`.

          recording_status_callback_method: HTTP request type used for `RecordingStatusCallback`. Defaults to `POST`.

          recording_timeout: The number of seconds that Telnyx will wait for the recording to be stopped if
              silence is detected. The timer only starts when the speech is detected. Please
              note that the transcription is used to detect silence and the related charge
              will be applied. The minimum value is 0. The default value is 0 (infinite)

          recording_track: The audio track to record for the call. The default is `both`.

          send_recording_url: Whether to send RecordingUrl in webhooks.

          sip_auth_password: The password to use for SIP authentication.

          sip_auth_username: The username to use for SIP authentication.

          status_callback: URL destination for Telnyx to send status callback events to for the call.

          status_callback_event: The call events for which Telnyx should send a webhook. Multiple events can be
              defined when separated by a space.

          status_callback_method: HTTP request type used for `StatusCallback`.

          trim: Whether to trim any leading and trailing silence from the recording. Defaults to
              `trim-silence`.

          url: The URL from which Telnyx will retrieve the TeXML call instructions.

          url_method: HTTP request type used for `Url`. The default value is inherited from TeXML
              Application setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        return await self._post(
            f"/texml/Accounts/{account_sid}/Calls",
            body=await async_maybe_transform(
                {
                    "application_sid": application_sid,
                    "from_": from_,
                    "to": to,
                    "async_amd": async_amd,
                    "async_amd_status_callback": async_amd_status_callback,
                    "async_amd_status_callback_method": async_amd_status_callback_method,
                    "caller_id": caller_id,
                    "cancel_playback_on_detect_message_end": cancel_playback_on_detect_message_end,
                    "cancel_playback_on_machine_detection": cancel_playback_on_machine_detection,
                    "detection_mode": detection_mode,
                    "fallback_url": fallback_url,
                    "machine_detection": machine_detection,
                    "machine_detection_silence_timeout": machine_detection_silence_timeout,
                    "machine_detection_speech_end_threshold": machine_detection_speech_end_threshold,
                    "machine_detection_speech_threshold": machine_detection_speech_threshold,
                    "machine_detection_timeout": machine_detection_timeout,
                    "preferred_codecs": preferred_codecs,
                    "record": record,
                    "recording_channels": recording_channels,
                    "recording_status_callback": recording_status_callback,
                    "recording_status_callback_event": recording_status_callback_event,
                    "recording_status_callback_method": recording_status_callback_method,
                    "recording_timeout": recording_timeout,
                    "recording_track": recording_track,
                    "send_recording_url": send_recording_url,
                    "sip_auth_password": sip_auth_password,
                    "sip_auth_username": sip_auth_username,
                    "status_callback": status_callback,
                    "status_callback_event": status_callback_event,
                    "status_callback_method": status_callback_method,
                    "trim": trim,
                    "url": url,
                    "url_method": url_method,
                },
                call_calls_params.CallCallsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallCallsResponse,
        )

    async def retrieve_calls(
        self,
        account_sid: str,
        *,
        end_time: str | NotGiven = NOT_GIVEN,
        end_time_gt: str | NotGiven = NOT_GIVEN,
        end_time_lt: str | NotGiven = NOT_GIVEN,
        from_: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        page_token: str | NotGiven = NOT_GIVEN,
        start_time: str | NotGiven = NOT_GIVEN,
        start_time_gt: str | NotGiven = NOT_GIVEN,
        start_time_lt: str | NotGiven = NOT_GIVEN,
        status: Literal["canceled", "completed", "failed", "busy", "no-answer"] | NotGiven = NOT_GIVEN,
        to: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallRetrieveCallsResponse:
        """Returns multiple call resouces for an account.

        This endpoint is eventually
        consistent.

        Args:
          end_time: Filters calls by their end date. Expected format is YYYY-MM-DD

          end_time_gt: Filters calls by their end date (after). Expected format is YYYY-MM-DD

          end_time_lt: Filters calls by their end date (before). Expected format is YYYY-MM-DD

          from_: Filters calls by the from number.

          page: The number of the page to be displayed, zero-indexed, should be used in
              conjuction with PageToken.

          page_size: The number of records to be displayed on a page

          page_token: Used to request the next page of results.

          start_time: Filters calls by their start date. Expected format is YYYY-MM-DD.

          start_time_gt: Filters calls by their start date (after). Expected format is YYYY-MM-DD

          start_time_lt: Filters calls by their start date (before). Expected format is YYYY-MM-DD

          status: Filters calls by status.

          to: Filters calls by the to number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        return await self._get(
            f"/texml/Accounts/{account_sid}/Calls",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_time": end_time,
                        "end_time_gt": end_time_gt,
                        "end_time_lt": end_time_lt,
                        "from_": from_,
                        "page": page,
                        "page_size": page_size,
                        "page_token": page_token,
                        "start_time": start_time,
                        "start_time_gt": start_time_gt,
                        "start_time_lt": start_time_lt,
                        "status": status,
                        "to": to,
                    },
                    call_retrieve_calls_params.CallRetrieveCallsParams,
                ),
            ),
            cast_to=CallRetrieveCallsResponse,
        )

    async def siprec_json(
        self,
        call_sid: str,
        *,
        account_sid: str,
        connector_name: str | NotGiven = NOT_GIVEN,
        include_metadata_custom_headers: Literal[True, False] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        secure: Literal[True, False] | NotGiven = NOT_GIVEN,
        session_timeout_secs: int | NotGiven = NOT_GIVEN,
        sip_transport: Literal["udp", "tcp", "tls"] | NotGiven = NOT_GIVEN,
        status_callback: str | NotGiven = NOT_GIVEN,
        status_callback_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        track: Literal["both_tracks", "inbound_track", "outbound_track"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallSiprecJsonResponse:
        """
        Starts siprec session with specified parameters for call idientified by
        call_sid.

        Args:
          connector_name: The name of the connector to use for the SIPREC session.

          include_metadata_custom_headers: When set, custom parameters will be added as metadata
              (recording.session.ExtensionParameters). Otherwise, they’ll be added to sip
              headers.

          name: Name of the SIPREC session. May be used to stop the SIPREC session from TeXML
              instruction.

          secure: Controls whether to encrypt media sent to your SRS using SRTP and TLS. When set
              you need to configure SRS port in your connector to 5061.

          session_timeout_secs: Sets `Session-Expires` header to the INVITE. A reinvite is sent every half the
              value set. Usefull for session keep alive. Minimum value is 90, set to 0 to
              disable.

          sip_transport: Specifies SIP transport protocol.

          status_callback: URL destination for Telnyx to send status callback events to for the siprec
              session.

          status_callback_method: HTTP request type used for `StatusCallback`.

          track: The track to be used for siprec session. Can be `both_tracks`, `inbound_track`
              or `outbound_track`. Defaults to `both_tracks`.

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
            f"/texml/Accounts/{account_sid}/Calls/{call_sid}/Siprec.json",
            body=await async_maybe_transform(
                {
                    "connector_name": connector_name,
                    "include_metadata_custom_headers": include_metadata_custom_headers,
                    "name": name,
                    "secure": secure,
                    "session_timeout_secs": session_timeout_secs,
                    "sip_transport": sip_transport,
                    "status_callback": status_callback,
                    "status_callback_method": status_callback_method,
                    "track": track,
                },
                call_siprec_json_params.CallSiprecJsonParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallSiprecJsonResponse,
        )

    async def streams_json(
        self,
        call_sid: str,
        *,
        account_sid: str,
        bidirectional_codec: Literal["PCMU", "PCMA", "G722"] | NotGiven = NOT_GIVEN,
        bidirectional_mode: Literal["mp3", "rtp"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        status_callback: str | NotGiven = NOT_GIVEN,
        status_callback_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        track: Literal["inbound_track", "outbound_track", "both_tracks"] | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallStreamsJsonResponse:
        """
        Starts streaming media from a call to a specific WebSocket address.

        Args:
          bidirectional_codec: Indicates codec for bidirectional streaming RTP payloads. Used only with
              stream_bidirectional_mode=rtp. Case sensitive.

          bidirectional_mode: Configures method of bidirectional streaming (mp3, rtp).

          name: The user specified name of Stream.

          status_callback: Url where status callbacks will be sent.

          status_callback_method: HTTP method used to send status callbacks.

          track: Tracks to be included in the stream

          url: The destination WebSocket address where the stream is going to be delivered.

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
            f"/texml/Accounts/{account_sid}/Calls/{call_sid}/Streams.json",
            body=await async_maybe_transform(
                {
                    "bidirectional_codec": bidirectional_codec,
                    "bidirectional_mode": bidirectional_mode,
                    "name": name,
                    "status_callback": status_callback,
                    "status_callback_method": status_callback_method,
                    "track": track,
                    "url": url,
                },
                call_streams_json_params.CallStreamsJsonParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallStreamsJsonResponse,
        )


class CallsResourceWithRawResponse:
    def __init__(self, calls: CallsResource) -> None:
        self._calls = calls

        self.retrieve = to_raw_response_wrapper(
            calls.retrieve,
        )
        self.update = to_raw_response_wrapper(
            calls.update,
        )
        self.calls = to_raw_response_wrapper(
            calls.calls,
        )
        self.retrieve_calls = to_raw_response_wrapper(
            calls.retrieve_calls,
        )
        self.siprec_json = to_raw_response_wrapper(
            calls.siprec_json,
        )
        self.streams_json = to_raw_response_wrapper(
            calls.streams_json,
        )

    @cached_property
    def recordings_json(self) -> RecordingsJsonResourceWithRawResponse:
        return RecordingsJsonResourceWithRawResponse(self._calls.recordings_json)

    @cached_property
    def recordings(self) -> RecordingsResourceWithRawResponse:
        return RecordingsResourceWithRawResponse(self._calls.recordings)

    @cached_property
    def siprec(self) -> SiprecResourceWithRawResponse:
        return SiprecResourceWithRawResponse(self._calls.siprec)

    @cached_property
    def streams(self) -> StreamsResourceWithRawResponse:
        return StreamsResourceWithRawResponse(self._calls.streams)


class AsyncCallsResourceWithRawResponse:
    def __init__(self, calls: AsyncCallsResource) -> None:
        self._calls = calls

        self.retrieve = async_to_raw_response_wrapper(
            calls.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            calls.update,
        )
        self.calls = async_to_raw_response_wrapper(
            calls.calls,
        )
        self.retrieve_calls = async_to_raw_response_wrapper(
            calls.retrieve_calls,
        )
        self.siprec_json = async_to_raw_response_wrapper(
            calls.siprec_json,
        )
        self.streams_json = async_to_raw_response_wrapper(
            calls.streams_json,
        )

    @cached_property
    def recordings_json(self) -> AsyncRecordingsJsonResourceWithRawResponse:
        return AsyncRecordingsJsonResourceWithRawResponse(self._calls.recordings_json)

    @cached_property
    def recordings(self) -> AsyncRecordingsResourceWithRawResponse:
        return AsyncRecordingsResourceWithRawResponse(self._calls.recordings)

    @cached_property
    def siprec(self) -> AsyncSiprecResourceWithRawResponse:
        return AsyncSiprecResourceWithRawResponse(self._calls.siprec)

    @cached_property
    def streams(self) -> AsyncStreamsResourceWithRawResponse:
        return AsyncStreamsResourceWithRawResponse(self._calls.streams)


class CallsResourceWithStreamingResponse:
    def __init__(self, calls: CallsResource) -> None:
        self._calls = calls

        self.retrieve = to_streamed_response_wrapper(
            calls.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            calls.update,
        )
        self.calls = to_streamed_response_wrapper(
            calls.calls,
        )
        self.retrieve_calls = to_streamed_response_wrapper(
            calls.retrieve_calls,
        )
        self.siprec_json = to_streamed_response_wrapper(
            calls.siprec_json,
        )
        self.streams_json = to_streamed_response_wrapper(
            calls.streams_json,
        )

    @cached_property
    def recordings_json(self) -> RecordingsJsonResourceWithStreamingResponse:
        return RecordingsJsonResourceWithStreamingResponse(self._calls.recordings_json)

    @cached_property
    def recordings(self) -> RecordingsResourceWithStreamingResponse:
        return RecordingsResourceWithStreamingResponse(self._calls.recordings)

    @cached_property
    def siprec(self) -> SiprecResourceWithStreamingResponse:
        return SiprecResourceWithStreamingResponse(self._calls.siprec)

    @cached_property
    def streams(self) -> StreamsResourceWithStreamingResponse:
        return StreamsResourceWithStreamingResponse(self._calls.streams)


class AsyncCallsResourceWithStreamingResponse:
    def __init__(self, calls: AsyncCallsResource) -> None:
        self._calls = calls

        self.retrieve = async_to_streamed_response_wrapper(
            calls.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            calls.update,
        )
        self.calls = async_to_streamed_response_wrapper(
            calls.calls,
        )
        self.retrieve_calls = async_to_streamed_response_wrapper(
            calls.retrieve_calls,
        )
        self.siprec_json = async_to_streamed_response_wrapper(
            calls.siprec_json,
        )
        self.streams_json = async_to_streamed_response_wrapper(
            calls.streams_json,
        )

    @cached_property
    def recordings_json(self) -> AsyncRecordingsJsonResourceWithStreamingResponse:
        return AsyncRecordingsJsonResourceWithStreamingResponse(self._calls.recordings_json)

    @cached_property
    def recordings(self) -> AsyncRecordingsResourceWithStreamingResponse:
        return AsyncRecordingsResourceWithStreamingResponse(self._calls.recordings)

    @cached_property
    def siprec(self) -> AsyncSiprecResourceWithStreamingResponse:
        return AsyncSiprecResourceWithStreamingResponse(self._calls.siprec)

    @cached_property
    def streams(self) -> AsyncStreamsResourceWithStreamingResponse:
        return AsyncStreamsResourceWithStreamingResponse(self._calls.streams)

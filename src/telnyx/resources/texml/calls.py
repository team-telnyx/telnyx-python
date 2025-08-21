# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.texml import call_update_params, call_initiate_params
from ..._base_client import make_request_options
from ...types.texml.call_update_response import CallUpdateResponse
from ...types.texml.call_initiate_response import CallInitiateResponse

__all__ = ["CallsResource", "AsyncCallsResource"]


class CallsResource(SyncAPIResource):
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

    def update(
        self,
        call_sid: str,
        *,
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
        if not call_sid:
            raise ValueError(f"Expected a non-empty value for `call_sid` but received {call_sid!r}")
        return self._post(
            f"/texml/calls/{call_sid}/update",
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

    def initiate(
        self,
        application_id: str,
        *,
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
    ) -> CallInitiateResponse:
        """Initiate an outbound TeXML call.

        Telnyx will request TeXML from the XML Request
        URL configured for the connection in the Mission Control Portal.

        Args:
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
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return self._post(
            f"/texml/calls/{application_id}",
            body=maybe_transform(
                {
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
                    "sip_auth_password": sip_auth_password,
                    "sip_auth_username": sip_auth_username,
                    "status_callback": status_callback,
                    "status_callback_event": status_callback_event,
                    "status_callback_method": status_callback_method,
                    "trim": trim,
                    "url": url,
                    "url_method": url_method,
                },
                call_initiate_params.CallInitiateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallInitiateResponse,
        )


class AsyncCallsResource(AsyncAPIResource):
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

    async def update(
        self,
        call_sid: str,
        *,
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
        if not call_sid:
            raise ValueError(f"Expected a non-empty value for `call_sid` but received {call_sid!r}")
        return await self._post(
            f"/texml/calls/{call_sid}/update",
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

    async def initiate(
        self,
        application_id: str,
        *,
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
    ) -> CallInitiateResponse:
        """Initiate an outbound TeXML call.

        Telnyx will request TeXML from the XML Request
        URL configured for the connection in the Mission Control Portal.

        Args:
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
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return await self._post(
            f"/texml/calls/{application_id}",
            body=await async_maybe_transform(
                {
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
                    "sip_auth_password": sip_auth_password,
                    "sip_auth_username": sip_auth_username,
                    "status_callback": status_callback,
                    "status_callback_event": status_callback_event,
                    "status_callback_method": status_callback_method,
                    "trim": trim,
                    "url": url,
                    "url_method": url_method,
                },
                call_initiate_params.CallInitiateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallInitiateResponse,
        )


class CallsResourceWithRawResponse:
    def __init__(self, calls: CallsResource) -> None:
        self._calls = calls

        self.update = to_raw_response_wrapper(
            calls.update,
        )
        self.initiate = to_raw_response_wrapper(
            calls.initiate,
        )


class AsyncCallsResourceWithRawResponse:
    def __init__(self, calls: AsyncCallsResource) -> None:
        self._calls = calls

        self.update = async_to_raw_response_wrapper(
            calls.update,
        )
        self.initiate = async_to_raw_response_wrapper(
            calls.initiate,
        )


class CallsResourceWithStreamingResponse:
    def __init__(self, calls: CallsResource) -> None:
        self._calls = calls

        self.update = to_streamed_response_wrapper(
            calls.update,
        )
        self.initiate = to_streamed_response_wrapper(
            calls.initiate,
        )


class AsyncCallsResourceWithStreamingResponse:
    def __init__(self, calls: AsyncCallsResource) -> None:
        self._calls = calls

        self.update = async_to_streamed_response_wrapper(
            calls.update,
        )
        self.initiate = async_to_streamed_response_wrapper(
            calls.initiate,
        )

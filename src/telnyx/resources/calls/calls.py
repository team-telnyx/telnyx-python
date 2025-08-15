# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal

import httpx

from ...types import (
    StreamCodec,
    StreamBidirectionalMode,
    StreamBidirectionalCodec,
    StreamBidirectionalTargetLegs,
    call_dial_params,
)
from .actions import (
    ActionsResource,
    AsyncActionsResource,
    ActionsResourceWithRawResponse,
    AsyncActionsResourceWithRawResponse,
    ActionsResourceWithStreamingResponse,
    AsyncActionsResourceWithStreamingResponse,
)
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
from ..._base_client import make_request_options
from ...types.stream_codec import StreamCodec
from ...types.sip_header_param import SipHeaderParam
from ...types.call_dial_response import CallDialResponse
from ...types.custom_sip_header_param import CustomSipHeaderParam
from ...types.dialogflow_config_param import DialogflowConfigParam
from ...types.sound_modifications_param import SoundModificationsParam
from ...types.stream_bidirectional_mode import StreamBidirectionalMode
from ...types.stream_bidirectional_codec import StreamBidirectionalCodec
from ...types.call_retrieve_status_response import CallRetrieveStatusResponse
from ...types.stream_bidirectional_target_legs import StreamBidirectionalTargetLegs
from ...types.calls.transcription_start_request_param import TranscriptionStartRequestParam

__all__ = ["CallsResource", "AsyncCallsResource"]


class CallsResource(SyncAPIResource):
    @cached_property
    def actions(self) -> ActionsResource:
        return ActionsResource(self._client)

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

    def dial(
        self,
        *,
        connection_id: str,
        from_: str,
        to: Union[str, List[str]],
        answering_machine_detection: Literal[
            "premium", "detect", "detect_beep", "detect_words", "greeting_end", "disabled"
        ]
        | NotGiven = NOT_GIVEN,
        answering_machine_detection_config: call_dial_params.AnsweringMachineDetectionConfig | NotGiven = NOT_GIVEN,
        audio_url: str | NotGiven = NOT_GIVEN,
        billing_group_id: str | NotGiven = NOT_GIVEN,
        bridge_intent: bool | NotGiven = NOT_GIVEN,
        bridge_on_answer: bool | NotGiven = NOT_GIVEN,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        conference_config: call_dial_params.ConferenceConfig | NotGiven = NOT_GIVEN,
        custom_headers: Iterable[CustomSipHeaderParam] | NotGiven = NOT_GIVEN,
        dialogflow_config: DialogflowConfigParam | NotGiven = NOT_GIVEN,
        enable_dialogflow: bool | NotGiven = NOT_GIVEN,
        from_display_name: str | NotGiven = NOT_GIVEN,
        link_to: str | NotGiven = NOT_GIVEN,
        media_encryption: Literal["disabled", "SRTP", "DTLS"] | NotGiven = NOT_GIVEN,
        media_name: str | NotGiven = NOT_GIVEN,
        preferred_codecs: str | NotGiven = NOT_GIVEN,
        record: Literal["record-from-answer"] | NotGiven = NOT_GIVEN,
        record_channels: Literal["single", "dual"] | NotGiven = NOT_GIVEN,
        record_custom_file_name: str | NotGiven = NOT_GIVEN,
        record_format: Literal["wav", "mp3"] | NotGiven = NOT_GIVEN,
        record_max_length: int | NotGiven = NOT_GIVEN,
        record_timeout_secs: int | NotGiven = NOT_GIVEN,
        record_track: Literal["both", "inbound", "outbound"] | NotGiven = NOT_GIVEN,
        record_trim: Literal["trim-silence"] | NotGiven = NOT_GIVEN,
        send_silence_when_idle: bool | NotGiven = NOT_GIVEN,
        sip_auth_password: str | NotGiven = NOT_GIVEN,
        sip_auth_username: str | NotGiven = NOT_GIVEN,
        sip_headers: Iterable[SipHeaderParam] | NotGiven = NOT_GIVEN,
        sip_transport_protocol: Literal["UDP", "TCP", "TLS"] | NotGiven = NOT_GIVEN,
        sound_modifications: SoundModificationsParam | NotGiven = NOT_GIVEN,
        stream_bidirectional_codec: StreamBidirectionalCodec | NotGiven = NOT_GIVEN,
        stream_bidirectional_mode: StreamBidirectionalMode | NotGiven = NOT_GIVEN,
        stream_bidirectional_sampling_rate: Literal[8000, 16000, 48000] | NotGiven = NOT_GIVEN,
        stream_bidirectional_target_legs: StreamBidirectionalTargetLegs | NotGiven = NOT_GIVEN,
        stream_codec: StreamCodec | NotGiven = NOT_GIVEN,
        stream_establish_before_call_originate: bool | NotGiven = NOT_GIVEN,
        stream_track: Literal["inbound_track", "outbound_track", "both_tracks"] | NotGiven = NOT_GIVEN,
        stream_url: str | NotGiven = NOT_GIVEN,
        supervise_call_control_id: str | NotGiven = NOT_GIVEN,
        supervisor_role: Literal["barge", "whisper", "monitor"] | NotGiven = NOT_GIVEN,
        time_limit_secs: int | NotGiven = NOT_GIVEN,
        timeout_secs: int | NotGiven = NOT_GIVEN,
        transcription: bool | NotGiven = NOT_GIVEN,
        transcription_config: TranscriptionStartRequestParam | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        webhook_url_method: Literal["POST", "GET"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallDialResponse:
        """Dial a number or SIP URI from a given connection.

        A successful response will
        include a `call_leg_id` which can be used to correlate the command with
        subsequent webhooks.

        **Expected Webhooks (see
        [schema](https://developers.telnyx.com/api/call-control/dial-call#callbacks)
        below):**

        - `call.initiated`
        - `call.answered` or `call.hangup`
        - `call.machine.detection.ended` if `answering_machine_detection` was requested
        - `call.machine.greeting.ended` if `answering_machine_detection` was requested
          to detect the end of machine greeting
        - `call.machine.premium.detection.ended` if
          `answering_machine_detection=premium` was requested
        - `call.machine.premium.greeting.ended` if `answering_machine_detection=premium`
          was requested and a beep was detected
        - `streaming.started`, `streaming.stopped` or `streaming.failed` if `stream_url`
          was set

        When the `record` parameter is set to `record-from-answer`, the response will
        include a `recording_id` field.

        Args:
          connection_id: The ID of the Call Control App (formerly ID of the connection) to be used when
              dialing the destination.

          from_: The `from` number to be used as the caller id presented to the destination (`to`
              number). The number should be in +E164 format.

          to: The DID or SIP URI to dial out to. Multiple DID or SIP URIs can be provided
              using an array of strings

          answering_machine_detection: Enables Answering Machine Detection. Telnyx offers Premium and Standard
              detections. With Premium detection, when a call is answered, Telnyx runs
              real-time detection and sends a `call.machine.premium.detection.ended` webhook
              with one of the following results: `human_residence`, `human_business`,
              `machine`, `silence` or `fax_detected`. If we detect a beep, we also send a
              `call.machine.premium.greeting.ended` webhook with the result of
              `beep_detected`. If we detect a beep before
              `call.machine.premium.detection.ended` we only send
              `call.machine.premium.greeting.ended`, and if we detect a beep after
              `call.machine.premium.detection.ended`, we send both webhooks. With Standard
              detection, when a call is answered, Telnyx runs real-time detection to determine
              if it was picked up by a human or a machine and sends an
              `call.machine.detection.ended` webhook with the analysis result. If
              `greeting_end` or `detect_words` is used and a `machine` is detected, you will
              receive another `call.machine.greeting.ended` webhook when the answering machine
              greeting ends with a beep or silence. If `detect_beep` is used, you will only
              receive `call.machine.greeting.ended` if a beep is detected.

          answering_machine_detection_config: Optional configuration parameters to modify 'answering_machine_detection'
              performance.

          audio_url: The URL of a file to be played back to the callee when the call is answered. The
              URL can point to either a WAV or MP3 file. media_name and audio_url cannot be
              used together in one request.

          billing_group_id: Use this field to set the Billing Group ID for the call. Must be a valid and
              existing Billing Group ID.

          bridge_intent: Indicates the intent to bridge this call with the call specified in link_to.
              When bridge_intent is true, link_to becomes required and the from number will be
              overwritten by the from number from the linked call.

          bridge_on_answer: Whether to automatically bridge answered call to the call specified in link_to.
              When bridge_on_answer is true, link_to becomes required.

          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore others Dial
              commands with the same `command_id`.

          conference_config: Optional configuration parameters to dial new participant into a conference.

          custom_headers: Custom headers to be added to the SIP INVITE.

          enable_dialogflow: Enables Dialogflow for the current call. The default value is false.

          from_display_name: The `from_display_name` string to be used as the caller id name (SIP From
              Display Name) presented to the destination (`to` number). The string should have
              a maximum of 128 characters, containing only letters, numbers, spaces, and
              -\\__~!.+ special characters. If ommited, the display name will be the same as the
              number in the `from` field.

          link_to: Use another call's control id for sharing the same call session id

          media_encryption: Defines whether media should be encrypted on the call.

          media_name: The media_name of a file to be played back to the callee when the call is
              answered. The media_name must point to a file previously uploaded to
              api.telnyx.com/v2/media by the same user/organization. The file must either be a
              WAV or MP3 file.

          preferred_codecs: The list of comma-separated codecs in a preferred order for the forked media to
              be received.

          record: Start recording automatically after an event. Disabled by default.

          record_channels: Defines which channel should be recorded ('single' or 'dual') when `record` is
              specified.

          record_custom_file_name: The custom recording file name to be used instead of the default `call_leg_id`.
              Telnyx will still add a Unix timestamp suffix.

          record_format: Defines the format of the recording ('wav' or 'mp3') when `record` is specified.

          record_max_length: Defines the maximum length for the recording in seconds when `record` is
              specified. The minimum value is 0. The maximum value is 43200. The default value
              is 0 (infinite).

          record_timeout_secs: The number of seconds that Telnyx will wait for the recording to be stopped if
              silence is detected when `record` is specified. The timer only starts when the
              speech is detected. Please note that call transcription is used to detect
              silence and the related charge will be applied. The minimum value is 0. The
              default value is 0 (infinite).

          record_track: The audio track to be recorded. Can be either `both`, `inbound` or `outbound`.
              If only single track is specified (`inbound`, `outbound`), `channels`
              configuration is ignored and it will be recorded as mono (single channel).

          record_trim: When set to `trim-silence`, silence will be removed from the beginning and end
              of the recording.

          send_silence_when_idle: Generate silence RTP packets when no transmission available.

          sip_auth_password: SIP Authentication password used for SIP challenges.

          sip_auth_username: SIP Authentication username used for SIP challenges.

          sip_headers: SIP headers to be added to the SIP INVITE request. Currently only User-to-User
              header is supported.

          sip_transport_protocol: Defines SIP transport protocol to be used on the call.

          sound_modifications: Use this field to modify sound effects, for example adjust the pitch.

          stream_bidirectional_codec: Indicates codec for bidirectional streaming RTP payloads. Used only with
              stream_bidirectional_mode=rtp. Case sensitive.

          stream_bidirectional_mode: Configures method of bidirectional streaming (mp3, rtp).

          stream_bidirectional_sampling_rate: Audio sampling rate.

          stream_bidirectional_target_legs: Specifies which call legs should receive the bidirectional stream audio.

          stream_codec: Specifies the codec to be used for the streamed audio. When set to 'default' or
              when transcoding is not possible, the codec from the call will be used.
              Currently, transcoding is only supported between PCMU and PCMA codecs.

          stream_establish_before_call_originate: Establish websocket connection before dialing the destination. This is useful
              for cases where the websocket connection takes a long time to establish.

          stream_track: Specifies which track should be streamed.

          stream_url: The destination WebSocket address where the stream is going to be delivered.

          supervise_call_control_id: The call leg which will be supervised by the new call.

          supervisor_role: The role of the supervisor call. 'barge' means that supervisor call hears and is
              being heard by both ends of the call (caller & callee). 'whisper' means that
              only supervised_call_control_id hears supervisor but supervisor can hear
              everything. 'monitor' means that nobody can hear supervisor call, but supervisor
              can hear everything on the call.

          time_limit_secs: Sets the maximum duration of a Call Control Leg in seconds. If the time limit is
              reached, the call will hangup and a `call.hangup` webhook with a `hangup_cause`
              of `time_limit` will be sent. For example, by setting a time limit of 120
              seconds, a Call Leg will be automatically terminated two minutes after being
              answered. The default time limit is 14400 seconds or 4 hours and this is also
              the maximum allowed call length.

          timeout_secs: The number of seconds that Telnyx will wait for the call to be answered by the
              destination to which it is being called. If the timeout is reached before an
              answer is received, the call will hangup and a `call.hangup` webhook with a
              `hangup_cause` of `timeout` will be sent. Minimum value is 5 seconds. Maximum
              value is 600 seconds.

          transcription: Enable transcription upon call answer. The default value is false.

          webhook_url: Use this field to override the URL for which Telnyx will send subsequent
              webhooks to for this call.

          webhook_url_method: HTTP request type used for `webhook_url`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/calls",
            body=maybe_transform(
                {
                    "connection_id": connection_id,
                    "from_": from_,
                    "to": to,
                    "answering_machine_detection": answering_machine_detection,
                    "answering_machine_detection_config": answering_machine_detection_config,
                    "audio_url": audio_url,
                    "billing_group_id": billing_group_id,
                    "bridge_intent": bridge_intent,
                    "bridge_on_answer": bridge_on_answer,
                    "client_state": client_state,
                    "command_id": command_id,
                    "conference_config": conference_config,
                    "custom_headers": custom_headers,
                    "dialogflow_config": dialogflow_config,
                    "enable_dialogflow": enable_dialogflow,
                    "from_display_name": from_display_name,
                    "link_to": link_to,
                    "media_encryption": media_encryption,
                    "media_name": media_name,
                    "preferred_codecs": preferred_codecs,
                    "record": record,
                    "record_channels": record_channels,
                    "record_custom_file_name": record_custom_file_name,
                    "record_format": record_format,
                    "record_max_length": record_max_length,
                    "record_timeout_secs": record_timeout_secs,
                    "record_track": record_track,
                    "record_trim": record_trim,
                    "send_silence_when_idle": send_silence_when_idle,
                    "sip_auth_password": sip_auth_password,
                    "sip_auth_username": sip_auth_username,
                    "sip_headers": sip_headers,
                    "sip_transport_protocol": sip_transport_protocol,
                    "sound_modifications": sound_modifications,
                    "stream_bidirectional_codec": stream_bidirectional_codec,
                    "stream_bidirectional_mode": stream_bidirectional_mode,
                    "stream_bidirectional_sampling_rate": stream_bidirectional_sampling_rate,
                    "stream_bidirectional_target_legs": stream_bidirectional_target_legs,
                    "stream_codec": stream_codec,
                    "stream_establish_before_call_originate": stream_establish_before_call_originate,
                    "stream_track": stream_track,
                    "stream_url": stream_url,
                    "supervise_call_control_id": supervise_call_control_id,
                    "supervisor_role": supervisor_role,
                    "time_limit_secs": time_limit_secs,
                    "timeout_secs": timeout_secs,
                    "transcription": transcription,
                    "transcription_config": transcription_config,
                    "webhook_url": webhook_url,
                    "webhook_url_method": webhook_url_method,
                },
                call_dial_params.CallDialParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallDialResponse,
        )

    def retrieve_status(
        self,
        call_control_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallRetrieveStatusResponse:
        """
        Returns the status of a call (data is available 10 minutes after call ended).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return self._get(
            f"/calls/{call_control_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallRetrieveStatusResponse,
        )


class AsyncCallsResource(AsyncAPIResource):
    @cached_property
    def actions(self) -> AsyncActionsResource:
        return AsyncActionsResource(self._client)

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

    async def dial(
        self,
        *,
        connection_id: str,
        from_: str,
        to: Union[str, List[str]],
        answering_machine_detection: Literal[
            "premium", "detect", "detect_beep", "detect_words", "greeting_end", "disabled"
        ]
        | NotGiven = NOT_GIVEN,
        answering_machine_detection_config: call_dial_params.AnsweringMachineDetectionConfig | NotGiven = NOT_GIVEN,
        audio_url: str | NotGiven = NOT_GIVEN,
        billing_group_id: str | NotGiven = NOT_GIVEN,
        bridge_intent: bool | NotGiven = NOT_GIVEN,
        bridge_on_answer: bool | NotGiven = NOT_GIVEN,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        conference_config: call_dial_params.ConferenceConfig | NotGiven = NOT_GIVEN,
        custom_headers: Iterable[CustomSipHeaderParam] | NotGiven = NOT_GIVEN,
        dialogflow_config: DialogflowConfigParam | NotGiven = NOT_GIVEN,
        enable_dialogflow: bool | NotGiven = NOT_GIVEN,
        from_display_name: str | NotGiven = NOT_GIVEN,
        link_to: str | NotGiven = NOT_GIVEN,
        media_encryption: Literal["disabled", "SRTP", "DTLS"] | NotGiven = NOT_GIVEN,
        media_name: str | NotGiven = NOT_GIVEN,
        preferred_codecs: str | NotGiven = NOT_GIVEN,
        record: Literal["record-from-answer"] | NotGiven = NOT_GIVEN,
        record_channels: Literal["single", "dual"] | NotGiven = NOT_GIVEN,
        record_custom_file_name: str | NotGiven = NOT_GIVEN,
        record_format: Literal["wav", "mp3"] | NotGiven = NOT_GIVEN,
        record_max_length: int | NotGiven = NOT_GIVEN,
        record_timeout_secs: int | NotGiven = NOT_GIVEN,
        record_track: Literal["both", "inbound", "outbound"] | NotGiven = NOT_GIVEN,
        record_trim: Literal["trim-silence"] | NotGiven = NOT_GIVEN,
        send_silence_when_idle: bool | NotGiven = NOT_GIVEN,
        sip_auth_password: str | NotGiven = NOT_GIVEN,
        sip_auth_username: str | NotGiven = NOT_GIVEN,
        sip_headers: Iterable[SipHeaderParam] | NotGiven = NOT_GIVEN,
        sip_transport_protocol: Literal["UDP", "TCP", "TLS"] | NotGiven = NOT_GIVEN,
        sound_modifications: SoundModificationsParam | NotGiven = NOT_GIVEN,
        stream_bidirectional_codec: StreamBidirectionalCodec | NotGiven = NOT_GIVEN,
        stream_bidirectional_mode: StreamBidirectionalMode | NotGiven = NOT_GIVEN,
        stream_bidirectional_sampling_rate: Literal[8000, 16000, 48000] | NotGiven = NOT_GIVEN,
        stream_bidirectional_target_legs: StreamBidirectionalTargetLegs | NotGiven = NOT_GIVEN,
        stream_codec: StreamCodec | NotGiven = NOT_GIVEN,
        stream_establish_before_call_originate: bool | NotGiven = NOT_GIVEN,
        stream_track: Literal["inbound_track", "outbound_track", "both_tracks"] | NotGiven = NOT_GIVEN,
        stream_url: str | NotGiven = NOT_GIVEN,
        supervise_call_control_id: str | NotGiven = NOT_GIVEN,
        supervisor_role: Literal["barge", "whisper", "monitor"] | NotGiven = NOT_GIVEN,
        time_limit_secs: int | NotGiven = NOT_GIVEN,
        timeout_secs: int | NotGiven = NOT_GIVEN,
        transcription: bool | NotGiven = NOT_GIVEN,
        transcription_config: TranscriptionStartRequestParam | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        webhook_url_method: Literal["POST", "GET"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallDialResponse:
        """Dial a number or SIP URI from a given connection.

        A successful response will
        include a `call_leg_id` which can be used to correlate the command with
        subsequent webhooks.

        **Expected Webhooks (see
        [schema](https://developers.telnyx.com/api/call-control/dial-call#callbacks)
        below):**

        - `call.initiated`
        - `call.answered` or `call.hangup`
        - `call.machine.detection.ended` if `answering_machine_detection` was requested
        - `call.machine.greeting.ended` if `answering_machine_detection` was requested
          to detect the end of machine greeting
        - `call.machine.premium.detection.ended` if
          `answering_machine_detection=premium` was requested
        - `call.machine.premium.greeting.ended` if `answering_machine_detection=premium`
          was requested and a beep was detected
        - `streaming.started`, `streaming.stopped` or `streaming.failed` if `stream_url`
          was set

        When the `record` parameter is set to `record-from-answer`, the response will
        include a `recording_id` field.

        Args:
          connection_id: The ID of the Call Control App (formerly ID of the connection) to be used when
              dialing the destination.

          from_: The `from` number to be used as the caller id presented to the destination (`to`
              number). The number should be in +E164 format.

          to: The DID or SIP URI to dial out to. Multiple DID or SIP URIs can be provided
              using an array of strings

          answering_machine_detection: Enables Answering Machine Detection. Telnyx offers Premium and Standard
              detections. With Premium detection, when a call is answered, Telnyx runs
              real-time detection and sends a `call.machine.premium.detection.ended` webhook
              with one of the following results: `human_residence`, `human_business`,
              `machine`, `silence` or `fax_detected`. If we detect a beep, we also send a
              `call.machine.premium.greeting.ended` webhook with the result of
              `beep_detected`. If we detect a beep before
              `call.machine.premium.detection.ended` we only send
              `call.machine.premium.greeting.ended`, and if we detect a beep after
              `call.machine.premium.detection.ended`, we send both webhooks. With Standard
              detection, when a call is answered, Telnyx runs real-time detection to determine
              if it was picked up by a human or a machine and sends an
              `call.machine.detection.ended` webhook with the analysis result. If
              `greeting_end` or `detect_words` is used and a `machine` is detected, you will
              receive another `call.machine.greeting.ended` webhook when the answering machine
              greeting ends with a beep or silence. If `detect_beep` is used, you will only
              receive `call.machine.greeting.ended` if a beep is detected.

          answering_machine_detection_config: Optional configuration parameters to modify 'answering_machine_detection'
              performance.

          audio_url: The URL of a file to be played back to the callee when the call is answered. The
              URL can point to either a WAV or MP3 file. media_name and audio_url cannot be
              used together in one request.

          billing_group_id: Use this field to set the Billing Group ID for the call. Must be a valid and
              existing Billing Group ID.

          bridge_intent: Indicates the intent to bridge this call with the call specified in link_to.
              When bridge_intent is true, link_to becomes required and the from number will be
              overwritten by the from number from the linked call.

          bridge_on_answer: Whether to automatically bridge answered call to the call specified in link_to.
              When bridge_on_answer is true, link_to becomes required.

          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore others Dial
              commands with the same `command_id`.

          conference_config: Optional configuration parameters to dial new participant into a conference.

          custom_headers: Custom headers to be added to the SIP INVITE.

          enable_dialogflow: Enables Dialogflow for the current call. The default value is false.

          from_display_name: The `from_display_name` string to be used as the caller id name (SIP From
              Display Name) presented to the destination (`to` number). The string should have
              a maximum of 128 characters, containing only letters, numbers, spaces, and
              -\\__~!.+ special characters. If ommited, the display name will be the same as the
              number in the `from` field.

          link_to: Use another call's control id for sharing the same call session id

          media_encryption: Defines whether media should be encrypted on the call.

          media_name: The media_name of a file to be played back to the callee when the call is
              answered. The media_name must point to a file previously uploaded to
              api.telnyx.com/v2/media by the same user/organization. The file must either be a
              WAV or MP3 file.

          preferred_codecs: The list of comma-separated codecs in a preferred order for the forked media to
              be received.

          record: Start recording automatically after an event. Disabled by default.

          record_channels: Defines which channel should be recorded ('single' or 'dual') when `record` is
              specified.

          record_custom_file_name: The custom recording file name to be used instead of the default `call_leg_id`.
              Telnyx will still add a Unix timestamp suffix.

          record_format: Defines the format of the recording ('wav' or 'mp3') when `record` is specified.

          record_max_length: Defines the maximum length for the recording in seconds when `record` is
              specified. The minimum value is 0. The maximum value is 43200. The default value
              is 0 (infinite).

          record_timeout_secs: The number of seconds that Telnyx will wait for the recording to be stopped if
              silence is detected when `record` is specified. The timer only starts when the
              speech is detected. Please note that call transcription is used to detect
              silence and the related charge will be applied. The minimum value is 0. The
              default value is 0 (infinite).

          record_track: The audio track to be recorded. Can be either `both`, `inbound` or `outbound`.
              If only single track is specified (`inbound`, `outbound`), `channels`
              configuration is ignored and it will be recorded as mono (single channel).

          record_trim: When set to `trim-silence`, silence will be removed from the beginning and end
              of the recording.

          send_silence_when_idle: Generate silence RTP packets when no transmission available.

          sip_auth_password: SIP Authentication password used for SIP challenges.

          sip_auth_username: SIP Authentication username used for SIP challenges.

          sip_headers: SIP headers to be added to the SIP INVITE request. Currently only User-to-User
              header is supported.

          sip_transport_protocol: Defines SIP transport protocol to be used on the call.

          sound_modifications: Use this field to modify sound effects, for example adjust the pitch.

          stream_bidirectional_codec: Indicates codec for bidirectional streaming RTP payloads. Used only with
              stream_bidirectional_mode=rtp. Case sensitive.

          stream_bidirectional_mode: Configures method of bidirectional streaming (mp3, rtp).

          stream_bidirectional_sampling_rate: Audio sampling rate.

          stream_bidirectional_target_legs: Specifies which call legs should receive the bidirectional stream audio.

          stream_codec: Specifies the codec to be used for the streamed audio. When set to 'default' or
              when transcoding is not possible, the codec from the call will be used.
              Currently, transcoding is only supported between PCMU and PCMA codecs.

          stream_establish_before_call_originate: Establish websocket connection before dialing the destination. This is useful
              for cases where the websocket connection takes a long time to establish.

          stream_track: Specifies which track should be streamed.

          stream_url: The destination WebSocket address where the stream is going to be delivered.

          supervise_call_control_id: The call leg which will be supervised by the new call.

          supervisor_role: The role of the supervisor call. 'barge' means that supervisor call hears and is
              being heard by both ends of the call (caller & callee). 'whisper' means that
              only supervised_call_control_id hears supervisor but supervisor can hear
              everything. 'monitor' means that nobody can hear supervisor call, but supervisor
              can hear everything on the call.

          time_limit_secs: Sets the maximum duration of a Call Control Leg in seconds. If the time limit is
              reached, the call will hangup and a `call.hangup` webhook with a `hangup_cause`
              of `time_limit` will be sent. For example, by setting a time limit of 120
              seconds, a Call Leg will be automatically terminated two minutes after being
              answered. The default time limit is 14400 seconds or 4 hours and this is also
              the maximum allowed call length.

          timeout_secs: The number of seconds that Telnyx will wait for the call to be answered by the
              destination to which it is being called. If the timeout is reached before an
              answer is received, the call will hangup and a `call.hangup` webhook with a
              `hangup_cause` of `timeout` will be sent. Minimum value is 5 seconds. Maximum
              value is 600 seconds.

          transcription: Enable transcription upon call answer. The default value is false.

          webhook_url: Use this field to override the URL for which Telnyx will send subsequent
              webhooks to for this call.

          webhook_url_method: HTTP request type used for `webhook_url`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/calls",
            body=await async_maybe_transform(
                {
                    "connection_id": connection_id,
                    "from_": from_,
                    "to": to,
                    "answering_machine_detection": answering_machine_detection,
                    "answering_machine_detection_config": answering_machine_detection_config,
                    "audio_url": audio_url,
                    "billing_group_id": billing_group_id,
                    "bridge_intent": bridge_intent,
                    "bridge_on_answer": bridge_on_answer,
                    "client_state": client_state,
                    "command_id": command_id,
                    "conference_config": conference_config,
                    "custom_headers": custom_headers,
                    "dialogflow_config": dialogflow_config,
                    "enable_dialogflow": enable_dialogflow,
                    "from_display_name": from_display_name,
                    "link_to": link_to,
                    "media_encryption": media_encryption,
                    "media_name": media_name,
                    "preferred_codecs": preferred_codecs,
                    "record": record,
                    "record_channels": record_channels,
                    "record_custom_file_name": record_custom_file_name,
                    "record_format": record_format,
                    "record_max_length": record_max_length,
                    "record_timeout_secs": record_timeout_secs,
                    "record_track": record_track,
                    "record_trim": record_trim,
                    "send_silence_when_idle": send_silence_when_idle,
                    "sip_auth_password": sip_auth_password,
                    "sip_auth_username": sip_auth_username,
                    "sip_headers": sip_headers,
                    "sip_transport_protocol": sip_transport_protocol,
                    "sound_modifications": sound_modifications,
                    "stream_bidirectional_codec": stream_bidirectional_codec,
                    "stream_bidirectional_mode": stream_bidirectional_mode,
                    "stream_bidirectional_sampling_rate": stream_bidirectional_sampling_rate,
                    "stream_bidirectional_target_legs": stream_bidirectional_target_legs,
                    "stream_codec": stream_codec,
                    "stream_establish_before_call_originate": stream_establish_before_call_originate,
                    "stream_track": stream_track,
                    "stream_url": stream_url,
                    "supervise_call_control_id": supervise_call_control_id,
                    "supervisor_role": supervisor_role,
                    "time_limit_secs": time_limit_secs,
                    "timeout_secs": timeout_secs,
                    "transcription": transcription,
                    "transcription_config": transcription_config,
                    "webhook_url": webhook_url,
                    "webhook_url_method": webhook_url_method,
                },
                call_dial_params.CallDialParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallDialResponse,
        )

    async def retrieve_status(
        self,
        call_control_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallRetrieveStatusResponse:
        """
        Returns the status of a call (data is available 10 minutes after call ended).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return await self._get(
            f"/calls/{call_control_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallRetrieveStatusResponse,
        )


class CallsResourceWithRawResponse:
    def __init__(self, calls: CallsResource) -> None:
        self._calls = calls

        self.dial = to_raw_response_wrapper(
            calls.dial,
        )
        self.retrieve_status = to_raw_response_wrapper(
            calls.retrieve_status,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        return ActionsResourceWithRawResponse(self._calls.actions)


class AsyncCallsResourceWithRawResponse:
    def __init__(self, calls: AsyncCallsResource) -> None:
        self._calls = calls

        self.dial = async_to_raw_response_wrapper(
            calls.dial,
        )
        self.retrieve_status = async_to_raw_response_wrapper(
            calls.retrieve_status,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        return AsyncActionsResourceWithRawResponse(self._calls.actions)


class CallsResourceWithStreamingResponse:
    def __init__(self, calls: CallsResource) -> None:
        self._calls = calls

        self.dial = to_streamed_response_wrapper(
            calls.dial,
        )
        self.retrieve_status = to_streamed_response_wrapper(
            calls.retrieve_status,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        return ActionsResourceWithStreamingResponse(self._calls.actions)


class AsyncCallsResourceWithStreamingResponse:
    def __init__(self, calls: AsyncCallsResource) -> None:
        self._calls = calls

        self.dial = async_to_streamed_response_wrapper(
            calls.dial,
        )
        self.retrieve_status = async_to_streamed_response_wrapper(
            calls.retrieve_status,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        return AsyncActionsResourceWithStreamingResponse(self._calls.actions)

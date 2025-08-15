# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ...types import (
    StreamCodec,
    StreamBidirectionalMode,
    StreamBidirectionalCodec,
    StreamBidirectionalTargetLegs,
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
from ...types.calls import (
    GoogleTranscriptionLanguage,
    action_refer_params,
    action_speak_params,
    action_answer_params,
    action_bridge_params,
    action_gather_params,
    action_hangup_params,
    action_reject_params,
    action_enqueue_params,
    action_transfer_params,
    action_send_dtmf_params,
    action_leave_queue_params,
    action_stop_gather_params,
    action_stop_siprec_params,
    action_start_siprec_params,
    action_stop_forking_params,
    action_send_sip_info_params,
    action_start_forking_params,
    action_stop_playback_params,
    action_start_playback_params,
    action_stop_recording_params,
    action_stop_streaming_params,
    action_gather_using_ai_params,
    action_pause_recording_params,
    action_start_recording_params,
    action_start_streaming_params,
    action_resume_recording_params,
    action_stop_ai_assistant_params,
    action_gather_using_audio_params,
    action_gather_using_speak_params,
    action_start_ai_assistant_params,
    action_stop_transcription_params,
    action_start_transcription_params,
    action_update_client_state_params,
    action_stop_noise_suppression_params,
    action_switch_supervisor_role_params,
    action_start_noise_suppression_params,
)
from ..._base_client import make_request_options
from ...types.stream_codec import StreamCodec
from ...types.sip_header_param import SipHeaderParam
from ...types.ai.assistant_param import AssistantParam
from ...types.calls.loopcount_param import LoopcountParam
from ...types.custom_sip_header_param import CustomSipHeaderParam
from ...types.dialogflow_config_param import DialogflowConfigParam
from ...types.sound_modifications_param import SoundModificationsParam
from ...types.stream_bidirectional_mode import StreamBidirectionalMode
from ...types.stream_bidirectional_codec import StreamBidirectionalCodec
from ...types.calls.action_refer_response import ActionReferResponse
from ...types.calls.action_speak_response import ActionSpeakResponse
from ...types.calls.action_answer_response import ActionAnswerResponse
from ...types.calls.action_bridge_response import ActionBridgeResponse
from ...types.calls.action_gather_response import ActionGatherResponse
from ...types.calls.action_hangup_response import ActionHangupResponse
from ...types.calls.action_reject_response import ActionRejectResponse
from ...types.calls.action_enqueue_response import ActionEnqueueResponse
from ...types.calls.action_transfer_response import ActionTransferResponse
from ...types.calls.action_send_dtmf_response import ActionSendDtmfResponse
from ...types.calls.transcription_config_param import TranscriptionConfigParam
from ...types.stream_bidirectional_target_legs import StreamBidirectionalTargetLegs
from ...types.calls.action_leave_queue_response import ActionLeaveQueueResponse
from ...types.calls.action_stop_gather_response import ActionStopGatherResponse
from ...types.calls.action_stop_siprec_response import ActionStopSiprecResponse
from ...types.calls.interruption_settings_param import InterruptionSettingsParam
from ...types.calls.action_start_siprec_response import ActionStartSiprecResponse
from ...types.calls.action_stop_forking_response import ActionStopForkingResponse
from ...types.calls.action_send_sip_info_response import ActionSendSipInfoResponse
from ...types.calls.action_start_forking_response import ActionStartForkingResponse
from ...types.calls.action_stop_playback_response import ActionStopPlaybackResponse
from ...types.calls.google_transcription_language import GoogleTranscriptionLanguage
from ...types.calls.action_start_playback_response import ActionStartPlaybackResponse
from ...types.calls.action_stop_recording_response import ActionStopRecordingResponse
from ...types.calls.action_stop_streaming_response import ActionStopStreamingResponse
from ...types.calls.action_gather_using_ai_response import ActionGatherUsingAIResponse
from ...types.calls.action_pause_recording_response import ActionPauseRecordingResponse
from ...types.calls.action_start_recording_response import ActionStartRecordingResponse
from ...types.calls.action_start_streaming_response import ActionStartStreamingResponse
from ...types.calls.action_resume_recording_response import ActionResumeRecordingResponse
from ...types.calls.action_stop_ai_assistant_response import ActionStopAIAssistantResponse
from ...types.calls.transcription_start_request_param import TranscriptionStartRequestParam
from ...types.calls.action_gather_using_audio_response import ActionGatherUsingAudioResponse
from ...types.calls.action_gather_using_speak_response import ActionGatherUsingSpeakResponse
from ...types.calls.action_start_ai_assistant_response import ActionStartAIAssistantResponse
from ...types.calls.action_stop_transcription_response import ActionStopTranscriptionResponse
from ...types.calls.action_start_transcription_response import ActionStartTranscriptionResponse
from ...types.calls.action_update_client_state_response import ActionUpdateClientStateResponse
from ...types.calls.action_stop_noise_suppression_response import ActionStopNoiseSuppressionResponse
from ...types.calls.action_switch_supervisor_role_response import ActionSwitchSupervisorRoleResponse
from ...types.calls.action_start_noise_suppression_response import ActionStartNoiseSuppressionResponse

__all__ = ["ActionsResource", "AsyncActionsResource"]


class ActionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ActionsResourceWithStreamingResponse(self)

    def answer(
        self,
        call_control_id: str,
        *,
        billing_group_id: str | NotGiven = NOT_GIVEN,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        custom_headers: Iterable[CustomSipHeaderParam] | NotGiven = NOT_GIVEN,
        preferred_codecs: Literal["G722,PCMU,PCMA,G729,OPUS,VP8,H264"] | NotGiven = NOT_GIVEN,
        record: Literal["record-from-answer"] | NotGiven = NOT_GIVEN,
        record_channels: Literal["single", "dual"] | NotGiven = NOT_GIVEN,
        record_custom_file_name: str | NotGiven = NOT_GIVEN,
        record_format: Literal["wav", "mp3"] | NotGiven = NOT_GIVEN,
        record_max_length: int | NotGiven = NOT_GIVEN,
        record_timeout_secs: int | NotGiven = NOT_GIVEN,
        record_track: Literal["both", "inbound", "outbound"] | NotGiven = NOT_GIVEN,
        record_trim: Literal["trim-silence"] | NotGiven = NOT_GIVEN,
        send_silence_when_idle: bool | NotGiven = NOT_GIVEN,
        sip_headers: Iterable[SipHeaderParam] | NotGiven = NOT_GIVEN,
        sound_modifications: SoundModificationsParam | NotGiven = NOT_GIVEN,
        stream_bidirectional_codec: StreamBidirectionalCodec | NotGiven = NOT_GIVEN,
        stream_bidirectional_mode: StreamBidirectionalMode | NotGiven = NOT_GIVEN,
        stream_bidirectional_target_legs: StreamBidirectionalTargetLegs | NotGiven = NOT_GIVEN,
        stream_codec: StreamCodec | NotGiven = NOT_GIVEN,
        stream_track: Literal["inbound_track", "outbound_track", "both_tracks"] | NotGiven = NOT_GIVEN,
        stream_url: str | NotGiven = NOT_GIVEN,
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
    ) -> ActionAnswerResponse:
        """Answer an incoming call.

        You must issue this command before executing subsequent
        commands on an incoming call.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/answer-call#callbacks)
        below):**

        - `call.answered`
        - `streaming.started`, `streaming.stopped` or `streaming.failed` if `stream_url`
          was set

        When the `record` parameter is set to `record-from-answer`, the response will
        include a `recording_id` field.

        Args:
          billing_group_id: Use this field to set the Billing Group ID for the call. Must be a valid and
              existing Billing Group ID.

          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          custom_headers: Custom headers to be added to the SIP INVITE response.

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

          sip_headers: SIP headers to be added to the SIP INVITE response. Currently only User-to-User
              header is supported.

          sound_modifications: Use this field to modify sound effects, for example adjust the pitch.

          stream_bidirectional_codec: Indicates codec for bidirectional streaming RTP payloads. Used only with
              stream_bidirectional_mode=rtp. Case sensitive.

          stream_bidirectional_mode: Configures method of bidirectional streaming (mp3, rtp).

          stream_bidirectional_target_legs: Specifies which call legs should receive the bidirectional stream audio.

          stream_codec: Specifies the codec to be used for the streamed audio. When set to 'default' or
              when transcoding is not possible, the codec from the call will be used.
              Currently, transcoding is only supported between PCMU and PCMA codecs.

          stream_track: Specifies which track should be streamed.

          stream_url: The destination WebSocket address where the stream is going to be delivered.

          transcription: Enable transcription upon call answer. The default value is false.

          webhook_url: Use this field to override the URL for which Telnyx will send subsequent
              webhooks to for this call.

          webhook_url_method: HTTP request type used for `webhook_url`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return self._post(
            f"/calls/{call_control_id}/actions/answer",
            body=maybe_transform(
                {
                    "billing_group_id": billing_group_id,
                    "client_state": client_state,
                    "command_id": command_id,
                    "custom_headers": custom_headers,
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
                    "sip_headers": sip_headers,
                    "sound_modifications": sound_modifications,
                    "stream_bidirectional_codec": stream_bidirectional_codec,
                    "stream_bidirectional_mode": stream_bidirectional_mode,
                    "stream_bidirectional_target_legs": stream_bidirectional_target_legs,
                    "stream_codec": stream_codec,
                    "stream_track": stream_track,
                    "stream_url": stream_url,
                    "transcription": transcription,
                    "transcription_config": transcription_config,
                    "webhook_url": webhook_url,
                    "webhook_url_method": webhook_url_method,
                },
                action_answer_params.ActionAnswerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionAnswerResponse,
        )

    def bridge(
        self,
        path_call_control_id: str,
        *,
        body_call_control_id: str,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        mute_dtmf: Literal["none", "both", "self", "opposite"] | NotGiven = NOT_GIVEN,
        park_after_unbridge: str | NotGiven = NOT_GIVEN,
        play_ringtone: bool | NotGiven = NOT_GIVEN,
        queue: str | NotGiven = NOT_GIVEN,
        record: Literal["record-from-answer"] | NotGiven = NOT_GIVEN,
        record_channels: Literal["single", "dual"] | NotGiven = NOT_GIVEN,
        record_custom_file_name: str | NotGiven = NOT_GIVEN,
        record_format: Literal["wav", "mp3"] | NotGiven = NOT_GIVEN,
        record_max_length: int | NotGiven = NOT_GIVEN,
        record_timeout_secs: int | NotGiven = NOT_GIVEN,
        record_track: Literal["both", "inbound", "outbound"] | NotGiven = NOT_GIVEN,
        record_trim: Literal["trim-silence"] | NotGiven = NOT_GIVEN,
        ringtone: Literal[
            "at",
            "au",
            "be",
            "bg",
            "br",
            "ch",
            "cl",
            "cn",
            "cz",
            "de",
            "dk",
            "ee",
            "es",
            "fi",
            "fr",
            "gr",
            "hu",
            "il",
            "in",
            "it",
            "jp",
            "lt",
            "mx",
            "my",
            "nl",
            "no",
            "nz",
            "ph",
            "pl",
            "pt",
            "ru",
            "se",
            "sg",
            "th",
            "tw",
            "uk",
            "us-old",
            "us",
            "ve",
            "za",
        ]
        | NotGiven = NOT_GIVEN,
        video_room_context: str | NotGiven = NOT_GIVEN,
        video_room_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionBridgeResponse:
        """
        Bridge two call control calls.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/bridge-call#callbacks)
        below):**

        - `call.bridged` for Leg A
        - `call.bridged` for Leg B

        Args:
          body_call_control_id: The Call Control ID of the call you want to bridge with, can't be used together
              with queue parameter or video_room_id parameter.

          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          mute_dtmf: When enabled, DTMF tones are not passed to the call participant. The webhooks
              containing the DTMF information will be sent.

          park_after_unbridge: Specifies behavior after the bridge ends (i.e. the opposite leg either hangs up
              or is transferred). If supplied with the value `self`, the current leg will be
              parked after unbridge. If not set, the default behavior is to hang up the leg.

          play_ringtone: Specifies whether to play a ringtone if the call you want to bridge with has not
              yet been answered.

          queue: The name of the queue you want to bridge with, can't be used together with
              call_control_id parameter or video_room_id parameter. Bridging with a queue
              means bridging with the first call in the queue. The call will always be removed
              from the queue regardless of whether bridging succeeds. Returns an error when
              the queue is empty.

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

          ringtone: Specifies which country ringtone to play when `play_ringtone` is set to `true`.
              If not set, the US ringtone will be played.

          video_room_context: The additional parameter that will be passed to the video conference. It is a
              text field and the user can decide how to use it. For example, you can set the
              participant name or pass JSON text. It can be used only with video_room_id
              parameter.

          video_room_id: The ID of the video room you want to bridge with, can't be used together with
              call_control_id parameter or queue parameter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_call_control_id:
            raise ValueError(
                f"Expected a non-empty value for `path_call_control_id` but received {path_call_control_id!r}"
            )
        return self._post(
            f"/calls/{path_call_control_id}/actions/bridge",
            body=maybe_transform(
                {
                    "body_call_control_id": body_call_control_id,
                    "client_state": client_state,
                    "command_id": command_id,
                    "mute_dtmf": mute_dtmf,
                    "park_after_unbridge": park_after_unbridge,
                    "play_ringtone": play_ringtone,
                    "queue": queue,
                    "record": record,
                    "record_channels": record_channels,
                    "record_custom_file_name": record_custom_file_name,
                    "record_format": record_format,
                    "record_max_length": record_max_length,
                    "record_timeout_secs": record_timeout_secs,
                    "record_track": record_track,
                    "record_trim": record_trim,
                    "ringtone": ringtone,
                    "video_room_context": video_room_context,
                    "video_room_id": video_room_id,
                },
                action_bridge_params.ActionBridgeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionBridgeResponse,
        )

    def enqueue(
        self,
        call_control_id: str,
        *,
        queue_name: str,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        max_size: int | NotGiven = NOT_GIVEN,
        max_wait_time_secs: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionEnqueueResponse:
        """
        Put the call in a queue.

        Args:
          queue_name: The name of the queue the call should be put in. If a queue with a given name
              doesn't exist yet it will be created.

          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          max_size: The maximum number of calls allowed in the queue at a given time. Can't be
              modified for an existing queue.

          max_wait_time_secs: The number of seconds after which the call will be removed from the queue.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return self._post(
            f"/calls/{call_control_id}/actions/enqueue",
            body=maybe_transform(
                {
                    "queue_name": queue_name,
                    "client_state": client_state,
                    "command_id": command_id,
                    "max_size": max_size,
                    "max_wait_time_secs": max_wait_time_secs,
                },
                action_enqueue_params.ActionEnqueueParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionEnqueueResponse,
        )

    def gather(
        self,
        call_control_id: str,
        *,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        gather_id: str | NotGiven = NOT_GIVEN,
        initial_timeout_millis: int | NotGiven = NOT_GIVEN,
        inter_digit_timeout_millis: int | NotGiven = NOT_GIVEN,
        maximum_digits: int | NotGiven = NOT_GIVEN,
        minimum_digits: int | NotGiven = NOT_GIVEN,
        terminating_digit: str | NotGiven = NOT_GIVEN,
        timeout_millis: int | NotGiven = NOT_GIVEN,
        valid_digits: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionGatherResponse:
        """
        Gather DTMF signals to build interactive menus.

        You can pass a list of valid digits. The `Answer` command must be issued before
        the `gather` command.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/gather-call#callbacks)
        below):**

        - `call.dtmf.received` (you may receive many of these webhooks)
        - `call.gather.ended`

        Args:
          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          gather_id: An id that will be sent back in the corresponding `call.gather.ended` webhook.
              Will be randomly generated if not specified.

          initial_timeout_millis: The number of milliseconds to wait for the first DTMF.

          inter_digit_timeout_millis: The number of milliseconds to wait for input between digits.

          maximum_digits: The maximum number of digits to fetch. This parameter has a maximum value
              of 128.

          minimum_digits: The minimum number of digits to fetch. This parameter has a minimum value of 1.

          terminating_digit: The digit used to terminate input if fewer than `maximum_digits` digits have
              been gathered.

          timeout_millis: The number of milliseconds to wait to complete the request.

          valid_digits: A list of all digits accepted as valid.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return self._post(
            f"/calls/{call_control_id}/actions/gather",
            body=maybe_transform(
                {
                    "client_state": client_state,
                    "command_id": command_id,
                    "gather_id": gather_id,
                    "initial_timeout_millis": initial_timeout_millis,
                    "inter_digit_timeout_millis": inter_digit_timeout_millis,
                    "maximum_digits": maximum_digits,
                    "minimum_digits": minimum_digits,
                    "terminating_digit": terminating_digit,
                    "timeout_millis": timeout_millis,
                    "valid_digits": valid_digits,
                },
                action_gather_params.ActionGatherParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionGatherResponse,
        )

    def gather_using_ai(
        self,
        call_control_id: str,
        *,
        parameters: object,
        assistant: AssistantParam | NotGiven = NOT_GIVEN,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        greeting: str | NotGiven = NOT_GIVEN,
        interruption_settings: InterruptionSettingsParam | NotGiven = NOT_GIVEN,
        language: GoogleTranscriptionLanguage | NotGiven = NOT_GIVEN,
        message_history: Iterable[action_gather_using_ai_params.MessageHistory] | NotGiven = NOT_GIVEN,
        send_message_history_updates: bool | NotGiven = NOT_GIVEN,
        send_partial_results: bool | NotGiven = NOT_GIVEN,
        transcription: TranscriptionConfigParam | NotGiven = NOT_GIVEN,
        user_response_timeout_ms: int | NotGiven = NOT_GIVEN,
        voice: str | NotGiven = NOT_GIVEN,
        voice_settings: action_gather_using_ai_params.VoiceSettings | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionGatherUsingAIResponse:
        """
        Gather parameters defined in the request payload using a voice assistant.

        You can pass parameters described as a JSON Schema object and the voice
        assistant will attempt to gather these informations.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/call-gather-using-ai#callbacks)
        below):**

        - `call.ai_gather.ended`
        - `call.conversation.ended`
        - `call.ai_gather.partial_results` (if `send_partial_results` is set to `true`)
        - `call.ai_gather.message_history_updated` (if `send_message_history_updates` is
          set to `true`)

        Args:
          parameters: The parameters described as a JSON Schema object that needs to be gathered by
              the voice assistant. See the
              [JSON Schema reference](https://json-schema.org/understanding-json-schema) for
              documentation about the format

          assistant: Assistant configuration including choice of LLM, custom instructions, and tools.

          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          greeting: Text that will be played when the gathering starts, if none then nothing will be
              played when the gathering starts. The greeting can be text for any voice or SSML
              for `AWS.Polly.<voice_id>` voices. There is a 3,000 character limit.

          interruption_settings: Settings for handling user interruptions during assistant speech

          language: Language to use for speech recognition

          message_history: The message history you want the voice assistant to be aware of, this can be
              useful to keep the context of the conversation, or to pass additional
              information to the voice assistant.

          send_message_history_updates: Default is `false`. If set to `true`, the voice assistant will send updates to
              the message history via the `call.ai_gather.message_history_updated`
              [callback](https://developers.telnyx.com/api/call-control/call-gather-using-ai#callbacks)
              in real time as the message history is updated.

          send_partial_results: Default is `false`. If set to `true`, the voice assistant will send partial
              results via the `call.ai_gather.partial_results`
              [callback](https://developers.telnyx.com/api/call-control/call-gather-using-ai#callbacks)
              in real time as individual fields are gathered. If set to `false`, the voice
              assistant will only send the final result via the `call.ai_gather.ended`
              callback.

          transcription: The settings associated with speech to text for the voice assistant. This is
              only relevant if the assistant uses a text-to-text language model. Any assistant
              using a model with native audio support (e.g. `fixie-ai/ultravox-v0_4`) will
              ignore this field.

          user_response_timeout_ms: The number of milliseconds to wait for a user response before the voice
              assistant times out and check if the user is still there.

          voice: The voice to be used by the voice assistant. Currently we support ElevenLabs,
              Telnyx and AWS voices.

              **Supported Providers:**

              - **AWS:** Use `AWS.Polly.<VoiceId>` (e.g., `AWS.Polly.Joanna`). For neural
                voices, which provide more realistic, human-like speech, append `-Neural` to
                the `VoiceId` (e.g., `AWS.Polly.Joanna-Neural`). Check the
                [available voices](https://docs.aws.amazon.com/polly/latest/dg/available-voices.html)
                for compatibility.
              - **Azure:** Use `Azure.<VoiceId>. (e.g. Azure.en-CA-ClaraNeural,
                Azure.en-CA-LiamNeural, Azure.en-US-BrianMultilingualNeural,
                Azure.en-US-Ava:DragonHDLatestNeural. For a complete list of voices, go to
                [Azure Voice Gallery](https://speech.microsoft.com/portal/voicegallery).)
              - **ElevenLabs:** Use `ElevenLabs.<ModelId>.<VoiceId>` (e.g.,
                `ElevenLabs.BaseModel.John`). The `ModelId` part is optional. To use
                ElevenLabs, you must provide your ElevenLabs API key as an integration secret
                under `"voice_settings": {"api_key_ref": "<secret_id>"}`. See
                [integration secrets documentation](https://developers.telnyx.com/api/secrets-manager/integration-secrets/create-integration-secret)
                for details. Check
                [available voices](https://elevenlabs.io/docs/api-reference/get-voices).
              - **Telnyx:** Use `Telnyx.<model_id>.<voice_id>`

          voice_settings: The settings associated with the voice selected

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return self._post(
            f"/calls/{call_control_id}/actions/gather_using_ai",
            body=maybe_transform(
                {
                    "parameters": parameters,
                    "assistant": assistant,
                    "client_state": client_state,
                    "command_id": command_id,
                    "greeting": greeting,
                    "interruption_settings": interruption_settings,
                    "language": language,
                    "message_history": message_history,
                    "send_message_history_updates": send_message_history_updates,
                    "send_partial_results": send_partial_results,
                    "transcription": transcription,
                    "user_response_timeout_ms": user_response_timeout_ms,
                    "voice": voice,
                    "voice_settings": voice_settings,
                },
                action_gather_using_ai_params.ActionGatherUsingAIParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionGatherUsingAIResponse,
        )

    def gather_using_audio(
        self,
        call_control_id: str,
        *,
        audio_url: str | NotGiven = NOT_GIVEN,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        inter_digit_timeout_millis: int | NotGiven = NOT_GIVEN,
        invalid_audio_url: str | NotGiven = NOT_GIVEN,
        invalid_media_name: str | NotGiven = NOT_GIVEN,
        maximum_digits: int | NotGiven = NOT_GIVEN,
        maximum_tries: int | NotGiven = NOT_GIVEN,
        media_name: str | NotGiven = NOT_GIVEN,
        minimum_digits: int | NotGiven = NOT_GIVEN,
        terminating_digit: str | NotGiven = NOT_GIVEN,
        timeout_millis: int | NotGiven = NOT_GIVEN,
        valid_digits: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionGatherUsingAudioResponse:
        """
        Play an audio file on the call until the required DTMF signals are gathered to
        build interactive menus.

        You can pass a list of valid digits along with an 'invalid_audio_url', which
        will be played back at the beginning of each prompt. Playback will be
        interrupted when a DTMF signal is received. The
        `Answer command must be issued before the `gather_using_audio` command.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/gather-using-audio#callbacks)
        below):**

        - `call.playback.started`
        - `call.playback.ended`
        - `call.dtmf.received` (you may receive many of these webhooks)
        - `call.gather.ended`

        Args:
          audio_url: The URL of a file to be played back at the beginning of each prompt. The URL can
              point to either a WAV or MP3 file. media_name and audio_url cannot be used
              together in one request.

          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          inter_digit_timeout_millis: The number of milliseconds to wait for input between digits.

          invalid_audio_url: The URL of a file to play when digits don't match the `valid_digits` parameter
              or the number of digits is not between `min` and `max`. The URL can point to
              either a WAV or MP3 file. invalid_media_name and invalid_audio_url cannot be
              used together in one request.

          invalid_media_name: The media_name of a file to be played back when digits don't match the
              `valid_digits` parameter or the number of digits is not between `min` and `max`.
              The media_name must point to a file previously uploaded to
              api.telnyx.com/v2/media by the same user/organization. The file must either be a
              WAV or MP3 file.

          maximum_digits: The maximum number of digits to fetch. This parameter has a maximum value
              of 128.

          maximum_tries: The maximum number of times the file should be played if there is no input from
              the user on the call.

          media_name: The media_name of a file to be played back at the beginning of each prompt. The
              media_name must point to a file previously uploaded to api.telnyx.com/v2/media
              by the same user/organization. The file must either be a WAV or MP3 file.

          minimum_digits: The minimum number of digits to fetch. This parameter has a minimum value of 1.

          terminating_digit: The digit used to terminate input if fewer than `maximum_digits` digits have
              been gathered.

          timeout_millis: The number of milliseconds to wait for a DTMF response after file playback ends
              before a replaying the sound file.

          valid_digits: A list of all digits accepted as valid.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return self._post(
            f"/calls/{call_control_id}/actions/gather_using_audio",
            body=maybe_transform(
                {
                    "audio_url": audio_url,
                    "client_state": client_state,
                    "command_id": command_id,
                    "inter_digit_timeout_millis": inter_digit_timeout_millis,
                    "invalid_audio_url": invalid_audio_url,
                    "invalid_media_name": invalid_media_name,
                    "maximum_digits": maximum_digits,
                    "maximum_tries": maximum_tries,
                    "media_name": media_name,
                    "minimum_digits": minimum_digits,
                    "terminating_digit": terminating_digit,
                    "timeout_millis": timeout_millis,
                    "valid_digits": valid_digits,
                },
                action_gather_using_audio_params.ActionGatherUsingAudioParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionGatherUsingAudioResponse,
        )

    def gather_using_speak(
        self,
        call_control_id: str,
        *,
        payload: str,
        voice: str,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        inter_digit_timeout_millis: int | NotGiven = NOT_GIVEN,
        invalid_payload: str | NotGiven = NOT_GIVEN,
        language: Literal[
            "arb",
            "cmn-CN",
            "cy-GB",
            "da-DK",
            "de-DE",
            "en-AU",
            "en-GB",
            "en-GB-WLS",
            "en-IN",
            "en-US",
            "es-ES",
            "es-MX",
            "es-US",
            "fr-CA",
            "fr-FR",
            "hi-IN",
            "is-IS",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "nb-NO",
            "nl-NL",
            "pl-PL",
            "pt-BR",
            "pt-PT",
            "ro-RO",
            "ru-RU",
            "sv-SE",
            "tr-TR",
        ]
        | NotGiven = NOT_GIVEN,
        maximum_digits: int | NotGiven = NOT_GIVEN,
        maximum_tries: int | NotGiven = NOT_GIVEN,
        minimum_digits: int | NotGiven = NOT_GIVEN,
        payload_type: Literal["text", "ssml"] | NotGiven = NOT_GIVEN,
        service_level: Literal["basic", "premium"] | NotGiven = NOT_GIVEN,
        terminating_digit: str | NotGiven = NOT_GIVEN,
        timeout_millis: int | NotGiven = NOT_GIVEN,
        valid_digits: str | NotGiven = NOT_GIVEN,
        voice_settings: action_gather_using_speak_params.VoiceSettings | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionGatherUsingSpeakResponse:
        """
        Convert text to speech and play it on the call until the required DTMF signals
        are gathered to build interactive menus.

        You can pass a list of valid digits along with an 'invalid_payload', which will
        be played back at the beginning of each prompt. Speech will be interrupted when
        a DTMF signal is received. The `Answer` command must be issued before the
        `gather_using_speak` command.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/gather-using-speak#callbacks)
        below):**

        - `call.dtmf.received` (you may receive many of these webhooks)
        - `call.gather.ended`

        Args:
          payload: The text or SSML to be converted into speech. There is a 3,000 character limit.

          voice: Specifies the voice used in speech synthesis.

              - Define voices using the format `<Provider>.<Model>.<VoiceId>`. Specifying only
                the provider will give default values for voice_id and model_id.

                **Supported Providers:**

              - **AWS:** Use `AWS.Polly.<VoiceId>` (e.g., `AWS.Polly.Joanna`). For neural
                voices, which provide more realistic, human-like speech, append `-Neural` to
                the `VoiceId` (e.g., `AWS.Polly.Joanna-Neural`). Check the
                [available voices](https://docs.aws.amazon.com/polly/latest/dg/available-voices.html)
                for compatibility.
              - **Azure:** Use `Azure.<VoiceId>. (e.g. Azure.en-CA-ClaraNeural,
                Azure.en-CA-LiamNeural, Azure.en-US-BrianMultilingualNeural,
                Azure.en-US-Ava:DragonHDLatestNeural. For a complete list of voices, go to
                [Azure Voice Gallery](https://speech.microsoft.com/portal/voicegallery).)
              - **ElevenLabs:** Use `ElevenLabs.<ModelId>.<VoiceId>` (e.g.,
                `ElevenLabs.eleven_multilingual_v2.21m00Tcm4TlvDq8ikWAM`). The `ModelId` part
                is optional. To use ElevenLabs, you must provide your ElevenLabs API key as an
                integration identifier secret in
                `"voice_settings": {"api_key_ref": "<secret_identifier>"}`. See
                [integration secrets documentation](https://developers.telnyx.com/api/secrets-manager/integration-secrets/create-integration-secret)
                for details. Check
                [available voices](https://elevenlabs.io/docs/api-reference/get-voices).
              - **Telnyx:** Use `Telnyx.<model_id>.<voice_id>`

              For service_level basic, you may define the gender of the speaker (male or
              female).

          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          inter_digit_timeout_millis: The number of milliseconds to wait for input between digits.

          invalid_payload: The text or SSML to be converted into speech when digits don't match the
              `valid_digits` parameter or the number of digits is not between `min` and `max`.
              There is a 3,000 character limit.

          language: The language you want spoken. This parameter is ignored when a `Polly.*` voice
              is specified.

          maximum_digits: The maximum number of digits to fetch. This parameter has a maximum value
              of 128.

          maximum_tries: The maximum number of times that a file should be played back if there is no
              input from the user on the call.

          minimum_digits: The minimum number of digits to fetch. This parameter has a minimum value of 1.

          payload_type: The type of the provided payload. The payload can either be plain text, or
              Speech Synthesis Markup Language (SSML).

          service_level: This parameter impacts speech quality, language options and payload types. When
              using `basic`, only the `en-US` language and payload type `text` are allowed.

          terminating_digit: The digit used to terminate input if fewer than `maximum_digits` digits have
              been gathered.

          timeout_millis: The number of milliseconds to wait for a DTMF response after speak ends before a
              replaying the sound file.

          valid_digits: A list of all digits accepted as valid.

          voice_settings: The settings associated with the voice selected

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return self._post(
            f"/calls/{call_control_id}/actions/gather_using_speak",
            body=maybe_transform(
                {
                    "payload": payload,
                    "voice": voice,
                    "client_state": client_state,
                    "command_id": command_id,
                    "inter_digit_timeout_millis": inter_digit_timeout_millis,
                    "invalid_payload": invalid_payload,
                    "language": language,
                    "maximum_digits": maximum_digits,
                    "maximum_tries": maximum_tries,
                    "minimum_digits": minimum_digits,
                    "payload_type": payload_type,
                    "service_level": service_level,
                    "terminating_digit": terminating_digit,
                    "timeout_millis": timeout_millis,
                    "valid_digits": valid_digits,
                    "voice_settings": voice_settings,
                },
                action_gather_using_speak_params.ActionGatherUsingSpeakParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionGatherUsingSpeakResponse,
        )

    def hangup(
        self,
        call_control_id: str,
        *,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionHangupResponse:
        """
        Hang up the call.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/hangup-call#callbacks)
        below):**

        - `call.hangup`
        - `call.recording.saved`

        Args:
          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return self._post(
            f"/calls/{call_control_id}/actions/hangup",
            body=maybe_transform(
                {
                    "client_state": client_state,
                    "command_id": command_id,
                },
                action_hangup_params.ActionHangupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionHangupResponse,
        )

    def leave_queue(
        self,
        call_control_id: str,
        *,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionLeaveQueueResponse:
        """
        Removes the call from a queue.

        Args:
          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return self._post(
            f"/calls/{call_control_id}/actions/leave_queue",
            body=maybe_transform(
                {
                    "client_state": client_state,
                    "command_id": command_id,
                },
                action_leave_queue_params.ActionLeaveQueueParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionLeaveQueueResponse,
        )

    def pause_recording(
        self,
        call_control_id: str,
        *,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        recording_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionPauseRecordingResponse:
        """Pause recording the call.

        Recording can be resumed via Resume recording command.

        **Expected Webhooks:**

        There are no webhooks associated with this command.

        Args:
          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          recording_id: Uniquely identifies the resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return self._post(
            f"/calls/{call_control_id}/actions/record_pause",
            body=maybe_transform(
                {
                    "client_state": client_state,
                    "command_id": command_id,
                    "recording_id": recording_id,
                },
                action_pause_recording_params.ActionPauseRecordingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionPauseRecordingResponse,
        )

    def refer(
        self,
        call_control_id: str,
        *,
        sip_address: str,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        custom_headers: Iterable[CustomSipHeaderParam] | NotGiven = NOT_GIVEN,
        sip_auth_password: str | NotGiven = NOT_GIVEN,
        sip_auth_username: str | NotGiven = NOT_GIVEN,
        sip_headers: Iterable[SipHeaderParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionReferResponse:
        """Initiate a SIP Refer on a Call Control call.

        You can initiate a SIP Refer at any
        point in the duration of a call.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/refer-call#callbacks)
        below):**

        - `call.refer.started`
        - `call.refer.completed`
        - `call.refer.failed`

        Args:
          sip_address: The SIP URI to which the call will be referred to.

          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid execution of duplicate commands. Telnyx will ignore
              subsequent commands with the same `command_id` as one that has already been
              executed.

          custom_headers: Custom headers to be added to the SIP INVITE.

          sip_auth_password: SIP Authentication password used for SIP challenges.

          sip_auth_username: SIP Authentication username used for SIP challenges.

          sip_headers: SIP headers to be added to the request. Currently only User-to-User header is
              supported.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return self._post(
            f"/calls/{call_control_id}/actions/refer",
            body=maybe_transform(
                {
                    "sip_address": sip_address,
                    "client_state": client_state,
                    "command_id": command_id,
                    "custom_headers": custom_headers,
                    "sip_auth_password": sip_auth_password,
                    "sip_auth_username": sip_auth_username,
                    "sip_headers": sip_headers,
                },
                action_refer_params.ActionReferParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionReferResponse,
        )

    def reject(
        self,
        call_control_id: str,
        *,
        cause: Literal["CALL_REJECTED", "USER_BUSY"],
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionRejectResponse:
        """
        Reject an incoming call.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/reject-call#callbacks)
        below):**

        - `call.hangup`

        Args:
          cause: Cause for call rejection.

          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return self._post(
            f"/calls/{call_control_id}/actions/reject",
            body=maybe_transform(
                {
                    "cause": cause,
                    "client_state": client_state,
                    "command_id": command_id,
                },
                action_reject_params.ActionRejectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRejectResponse,
        )

    def resume_recording(
        self,
        call_control_id: str,
        *,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        recording_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionResumeRecordingResponse:
        """
        Resume recording the call.

        **Expected Webhooks:**

        There are no webhooks associated with this command.

        Args:
          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          recording_id: Uniquely identifies the resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return self._post(
            f"/calls/{call_control_id}/actions/record_resume",
            body=maybe_transform(
                {
                    "client_state": client_state,
                    "command_id": command_id,
                    "recording_id": recording_id,
                },
                action_resume_recording_params.ActionResumeRecordingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionResumeRecordingResponse,
        )

    def send_dtmf(
        self,
        call_control_id: str,
        *,
        digits: str,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        duration_millis: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionSendDtmfResponse:
        """Sends DTMF tones from this leg.

        DTMF tones will be heard by the other end of the
        call.

        **Expected Webhooks:**

        There are no webhooks associated with this command.

        Args:
          digits: DTMF digits to send. Valid digits are 0-9, A-D, \\**, and #. Pauses can be added
              using w (0.5s) and W (1s).

          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          duration_millis: Specifies for how many milliseconds each digit will be played in the audio
              stream. Ranges from 100 to 500ms

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return self._post(
            f"/calls/{call_control_id}/actions/send_dtmf",
            body=maybe_transform(
                {
                    "digits": digits,
                    "client_state": client_state,
                    "command_id": command_id,
                    "duration_millis": duration_millis,
                },
                action_send_dtmf_params.ActionSendDtmfParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionSendDtmfResponse,
        )

    def send_sip_info(
        self,
        call_control_id: str,
        *,
        body: str,
        content_type: str,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionSendSipInfoResponse:
        """
        Sends SIP info from this leg.

        **Expected Webhooks:**

        - `call.sip_info.received` (to be received on the target call leg)

        Args:
          body: Content of the SIP INFO

          content_type: Content type of the INFO body. Must be MIME type compliant. There is a 1,400
              bytes limit

          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return self._post(
            f"/calls/{call_control_id}/actions/send_sip_info",
            body=maybe_transform(
                {
                    "body": body,
                    "content_type": content_type,
                    "client_state": client_state,
                    "command_id": command_id,
                },
                action_send_sip_info_params.ActionSendSipInfoParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionSendSipInfoResponse,
        )

    def speak(
        self,
        call_control_id: str,
        *,
        payload: str,
        voice: str,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        language: Literal[
            "arb",
            "cmn-CN",
            "cy-GB",
            "da-DK",
            "de-DE",
            "en-AU",
            "en-GB",
            "en-GB-WLS",
            "en-IN",
            "en-US",
            "es-ES",
            "es-MX",
            "es-US",
            "fr-CA",
            "fr-FR",
            "hi-IN",
            "is-IS",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "nb-NO",
            "nl-NL",
            "pl-PL",
            "pt-BR",
            "pt-PT",
            "ro-RO",
            "ru-RU",
            "sv-SE",
            "tr-TR",
        ]
        | NotGiven = NOT_GIVEN,
        payload_type: Literal["text", "ssml"] | NotGiven = NOT_GIVEN,
        service_level: Literal["basic", "premium"] | NotGiven = NOT_GIVEN,
        stop: str | NotGiven = NOT_GIVEN,
        voice_settings: action_speak_params.VoiceSettings | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionSpeakResponse:
        """Convert text to speech and play it back on the call.

        If multiple speak text
        commands are issued consecutively, the audio files will be placed in a queue
        awaiting playback.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/speak-call#callbacks)
        below):**

        - `call.speak.started`
        - `call.speak.ended`

        Args:
          payload: The text or SSML to be converted into speech. There is a 3,000 character limit.

          voice: Specifies the voice used in speech synthesis.

              - Define voices using the format `<Provider>.<Model>.<VoiceId>`. Specifying only
                the provider will give default values for voice_id and model_id.

                **Supported Providers:**

              - **AWS:** Use `AWS.Polly.<VoiceId>` (e.g., `AWS.Polly.Joanna`). For neural
                voices, which provide more realistic, human-like speech, append `-Neural` to
                the `VoiceId` (e.g., `AWS.Polly.Joanna-Neural`). Check the
                [available voices](https://docs.aws.amazon.com/polly/latest/dg/available-voices.html)
                for compatibility.
              - **Azure:** Use `Azure.<VoiceId>. (e.g. Azure.en-CA-ClaraNeural,
                Azure.en-CA-LiamNeural, Azure.en-US-BrianMultilingualNeural,
                Azure.en-US-Ava:DragonHDLatestNeural. For a complete list of voices, go to
                [Azure Voice Gallery](https://speech.microsoft.com/portal/voicegallery).)
              - **ElevenLabs:** Use `ElevenLabs.<ModelId>.<VoiceId>` (e.g.,
                `ElevenLabs.eleven_multilingual_v2.21m00Tcm4TlvDq8ikWAM`). The `ModelId` part
                is optional. To use ElevenLabs, you must provide your ElevenLabs API key as an
                integration identifier secret in
                `"voice_settings": {"api_key_ref": "<secret_identifier>"}`. See
                [integration secrets documentation](https://developers.telnyx.com/api/secrets-manager/integration-secrets/create-integration-secret)
                for details. Check
                [available voices](https://elevenlabs.io/docs/api-reference/get-voices).
              - **Telnyx:** Use `Telnyx.<model_id>.<voice_id>`

              For service_level basic, you may define the gender of the speaker (male or
              female).

          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          language: The language you want spoken. This parameter is ignored when a `Polly.*` voice
              is specified.

          payload_type: The type of the provided payload. The payload can either be plain text, or
              Speech Synthesis Markup Language (SSML).

          service_level: This parameter impacts speech quality, language options and payload types. When
              using `basic`, only the `en-US` language and payload type `text` are allowed.

          stop: When specified, it stops the current audio being played. Specify `current` to
              stop the current audio being played, and to play the next file in the queue.
              Specify `all` to stop the current audio file being played and to also clear all
              audio files from the queue.

          voice_settings: The settings associated with the voice selected

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return self._post(
            f"/calls/{call_control_id}/actions/speak",
            body=maybe_transform(
                {
                    "payload": payload,
                    "voice": voice,
                    "client_state": client_state,
                    "command_id": command_id,
                    "language": language,
                    "payload_type": payload_type,
                    "service_level": service_level,
                    "stop": stop,
                    "voice_settings": voice_settings,
                },
                action_speak_params.ActionSpeakParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionSpeakResponse,
        )

    def start_ai_assistant(
        self,
        call_control_id: str,
        *,
        assistant: action_start_ai_assistant_params.Assistant | NotGiven = NOT_GIVEN,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        greeting: str | NotGiven = NOT_GIVEN,
        interruption_settings: InterruptionSettingsParam | NotGiven = NOT_GIVEN,
        transcription: TranscriptionConfigParam | NotGiven = NOT_GIVEN,
        voice: str | NotGiven = NOT_GIVEN,
        voice_settings: action_start_ai_assistant_params.VoiceSettings | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionStartAIAssistantResponse:
        """
        Start an AI assistant on the call.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/call-start-ai-assistant#callbacks)
        below):**

        - `call.conversation.ended`
        - `call.conversation_insights.generated`

        Args:
          assistant: AI Assistant configuration

          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          greeting: Text that will be played when the assistant starts, if none then nothing will be
              played when the assistant starts. The greeting can be text for any voice or SSML
              for `AWS.Polly.<voice_id>` voices. There is a 3,000 character limit.

          interruption_settings: Settings for handling user interruptions during assistant speech

          transcription: The settings associated with speech to text for the voice assistant. This is
              only relevant if the assistant uses a text-to-text language model. Any assistant
              using a model with native audio support (e.g. `fixie-ai/ultravox-v0_4`) will
              ignore this field.

          voice: The voice to be used by the voice assistant. Currently we support ElevenLabs,
              Telnyx and AWS voices.

              **Supported Providers:**

              - **AWS:** Use `AWS.Polly.<VoiceId>` (e.g., `AWS.Polly.Joanna`). For neural
                voices, which provide more realistic, human-like speech, append `-Neural` to
                the `VoiceId` (e.g., `AWS.Polly.Joanna-Neural`). Check the
                [available voices](https://docs.aws.amazon.com/polly/latest/dg/available-voices.html)
                for compatibility.
              - **Azure:** Use `Azure.<VoiceId>. (e.g. Azure.en-CA-ClaraNeural,
                Azure.en-CA-LiamNeural, Azure.en-US-BrianMultilingualNeural,
                Azure.en-US-Ava:DragonHDLatestNeural. For a complete list of voices, go to
                [Azure Voice Gallery](https://speech.microsoft.com/portal/voicegallery).)
              - **ElevenLabs:** Use `ElevenLabs.<ModelId>.<VoiceId>` (e.g.,
                `ElevenLabs.BaseModel.John`). The `ModelId` part is optional. To use
                ElevenLabs, you must provide your ElevenLabs API key as an integration secret
                under `"voice_settings": {"api_key_ref": "<secret_id>"}`. See
                [integration secrets documentation](https://developers.telnyx.com/api/secrets-manager/integration-secrets/create-integration-secret)
                for details. Check
                [available voices](https://elevenlabs.io/docs/api-reference/get-voices).
              - **Telnyx:** Use `Telnyx.<model_id>.<voice_id>`

          voice_settings: The settings associated with the voice selected

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return self._post(
            f"/calls/{call_control_id}/actions/ai_assistant_start",
            body=maybe_transform(
                {
                    "assistant": assistant,
                    "client_state": client_state,
                    "command_id": command_id,
                    "greeting": greeting,
                    "interruption_settings": interruption_settings,
                    "transcription": transcription,
                    "voice": voice,
                    "voice_settings": voice_settings,
                },
                action_start_ai_assistant_params.ActionStartAIAssistantParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionStartAIAssistantResponse,
        )

    def start_forking(
        self,
        call_control_id: str,
        *,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        rx: str | NotGiven = NOT_GIVEN,
        stream_type: Literal["decrypted"] | NotGiven = NOT_GIVEN,
        tx: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionStartForkingResponse:
        """
        Call forking allows you to stream the media from a call to a specific target in
        realtime. This stream can be used to enable realtime audio analysis to support a
        variety of use cases, including fraud detection, or the creation of AI-generated
        audio responses. Requests must specify either the `target` attribute or the `rx`
        and `tx` attributes.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/start-call-fork#callbacks)
        below):**

        - `call.fork.started`
        - `call.fork.stopped`

        Args:
          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          rx: The network target, <udp:ip_address:port>, where the call's incoming RTP media
              packets should be forwarded.

          stream_type: Optionally specify a media type to stream. If `decrypted` selected, Telnyx will
              decrypt incoming SIP media before forking to the target. `rx` and `tx` are
              required fields if `decrypted` selected.

          tx: The network target, <udp:ip_address:port>, where the call's outgoing RTP media
              packets should be forwarded.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return self._post(
            f"/calls/{call_control_id}/actions/fork_start",
            body=maybe_transform(
                {
                    "client_state": client_state,
                    "command_id": command_id,
                    "rx": rx,
                    "stream_type": stream_type,
                    "tx": tx,
                },
                action_start_forking_params.ActionStartForkingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionStartForkingResponse,
        )

    def start_noise_suppression(
        self,
        call_control_id: str,
        *,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        direction: Literal["inbound", "outbound", "both"] | NotGiven = NOT_GIVEN,
        noise_suppression_engine: Literal["A", "B"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionStartNoiseSuppressionResponse:
        """
        Noise Suppression Start (BETA)

        Args:
          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          direction: The direction of the audio stream to be noise suppressed.

          noise_suppression_engine: The engine to use for noise suppression. A - rnnoise engine B - deepfilter
              engine.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return self._post(
            f"/calls/{call_control_id}/actions/suppression_start",
            body=maybe_transform(
                {
                    "client_state": client_state,
                    "command_id": command_id,
                    "direction": direction,
                    "noise_suppression_engine": noise_suppression_engine,
                },
                action_start_noise_suppression_params.ActionStartNoiseSuppressionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionStartNoiseSuppressionResponse,
        )

    def start_playback(
        self,
        call_control_id: str,
        *,
        audio_type: Literal["mp3", "wav"] | NotGiven = NOT_GIVEN,
        audio_url: str | NotGiven = NOT_GIVEN,
        cache_audio: bool | NotGiven = NOT_GIVEN,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        loop: LoopcountParam | NotGiven = NOT_GIVEN,
        media_name: str | NotGiven = NOT_GIVEN,
        overlay: bool | NotGiven = NOT_GIVEN,
        playback_content: str | NotGiven = NOT_GIVEN,
        stop: str | NotGiven = NOT_GIVEN,
        target_legs: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionStartPlaybackResponse:
        """Play an audio file on the call.

        If multiple play audio commands are issued
        consecutively, the audio files will be placed in a queue awaiting playback.

        _Notes:_

        - When `overlay` is enabled, `target_legs` is limited to `self`.
        - A customer cannot Play Audio with `overlay=true` unless there is a Play Audio
          with `overlay=false` actively playing.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/start-call-playback#callbacks)
        below):**

        - `call.playback.started`
        - `call.playback.ended`

        Args:
          audio_type: Specifies the type of audio provided in `audio_url` or `playback_content`.

          audio_url: The URL of a file to be played back on the call. The URL can point to either a
              WAV or MP3 file. media_name and audio_url cannot be used together in one
              request.

          cache_audio: Caches the audio file. Useful when playing the same audio file multiple times
              during the call.

          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          loop: The number of times the audio file should be played. If supplied, the value must
              be an integer between 1 and 100, or the special string `infinity` for an endless
              loop.

          media_name: The media_name of a file to be played back on the call. The media_name must
              point to a file previously uploaded to api.telnyx.com/v2/media by the same
              user/organization. The file must either be a WAV or MP3 file.

          overlay: When enabled, audio will be mixed on top of any other audio that is actively
              being played back. Note that `overlay: true` will only work if there is another
              audio file already being played on the call.

          playback_content: Allows a user to provide base64 encoded mp3 or wav. Note: when using this
              parameter, `media_url` and `media_name` in the `playback_started` and
              `playback_ended` webhooks will be empty

          stop: When specified, it stops the current audio being played. Specify `current` to
              stop the current audio being played, and to play the next file in the queue.
              Specify `all` to stop the current audio file being played and to also clear all
              audio files from the queue.

          target_legs: Specifies the leg or legs on which audio will be played. If supplied, the value
              must be either `self`, `opposite` or `both`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return self._post(
            f"/calls/{call_control_id}/actions/playback_start",
            body=maybe_transform(
                {
                    "audio_type": audio_type,
                    "audio_url": audio_url,
                    "cache_audio": cache_audio,
                    "client_state": client_state,
                    "command_id": command_id,
                    "loop": loop,
                    "media_name": media_name,
                    "overlay": overlay,
                    "playback_content": playback_content,
                    "stop": stop,
                    "target_legs": target_legs,
                },
                action_start_playback_params.ActionStartPlaybackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionStartPlaybackResponse,
        )

    def start_recording(
        self,
        call_control_id: str,
        *,
        channels: Literal["single", "dual"],
        format: Literal["wav", "mp3"],
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        custom_file_name: str | NotGiven = NOT_GIVEN,
        max_length: int | NotGiven = NOT_GIVEN,
        play_beep: bool | NotGiven = NOT_GIVEN,
        recording_track: Literal["both", "inbound", "outbound"] | NotGiven = NOT_GIVEN,
        timeout_secs: int | NotGiven = NOT_GIVEN,
        transcription: bool | NotGiven = NOT_GIVEN,
        transcription_engine: str | NotGiven = NOT_GIVEN,
        transcription_language: Literal[
            "af-ZA",
            "am-ET",
            "ar-AE",
            "ar-BH",
            "ar-DZ",
            "ar-EG",
            "ar-IL",
            "ar-IQ",
            "ar-JO",
            "ar-KW",
            "ar-LB",
            "ar-MA",
            "ar-MR",
            "ar-OM",
            "ar-PS",
            "ar-QA",
            "ar-SA",
            "ar-TN",
            "ar-YE",
            "az-AZ",
            "bg-BG",
            "bn-BD",
            "bn-IN",
            "bs-BA",
            "ca-ES",
            "cs-CZ",
            "da-DK",
            "de-AT",
            "de-CH",
            "de-DE",
            "el-GR",
            "en-AU",
            "en-CA",
            "en-GB",
            "en-GH",
            "en-HK",
            "en-IE",
            "en-IN",
            "en-KE",
            "en-NG",
            "en-NZ",
            "en-PH",
            "en-PK",
            "en-SG",
            "en-TZ",
            "en-US",
            "en-ZA",
            "es-AR",
            "es-BO",
            "es-CL",
            "es-CO",
            "es-CR",
            "es-DO",
            "es-EC",
            "es-ES",
            "es-GT",
            "es-HN",
            "es-MX",
            "es-NI",
            "es-PA",
            "es-PE",
            "es-PR",
            "es-PY",
            "es-SV",
            "es-US",
            "es-UY",
            "es-VE",
            "et-EE",
            "eu-ES",
            "fa-IR",
            "fi-FI",
            "fil-PH",
            "fr-BE",
            "fr-CA",
            "fr-CH",
            "fr-FR",
            "gl-ES",
            "gu-IN",
            "hi-IN",
            "hr-HR",
            "hu-HU",
            "hy-AM",
            "id-ID",
            "is-IS",
            "it-CH",
            "it-IT",
            "iw-IL",
            "ja-JP",
            "jv-ID",
            "ka-GE",
            "kk-KZ",
            "km-KH",
            "kn-IN",
            "ko-KR",
            "lo-LA",
            "lt-LT",
            "lv-LV",
            "mk-MK",
            "ml-IN",
            "mn-MN",
            "mr-IN",
            "ms-MY",
            "my-MM",
            "ne-NP",
            "nl-BE",
            "nl-NL",
            "no-NO",
            "pa-Guru-IN",
            "pl-PL",
            "pt-BR",
            "pt-PT",
            "ro-RO",
            "ru-RU",
            "rw-RW",
            "si-LK",
            "sk-SK",
            "sl-SI",
            "sq-AL",
            "sr-RS",
            "ss-latn-za",
            "st-ZA",
            "su-ID",
            "sv-SE",
            "sw-KE",
            "sw-TZ",
            "ta-IN",
            "ta-LK",
            "ta-MY",
            "ta-SG",
            "te-IN",
            "th-TH",
            "tn-latn-za",
            "tr-TR",
            "ts-ZA",
            "uk-UA",
            "ur-IN",
            "ur-PK",
            "uz-UZ",
            "ve-ZA",
            "vi-VN",
            "xh-ZA",
            "yue-Hant-HK",
            "zh",
            "zh-TW",
            "zu-ZA",
        ]
        | NotGiven = NOT_GIVEN,
        transcription_max_speaker_count: int | NotGiven = NOT_GIVEN,
        transcription_min_speaker_count: int | NotGiven = NOT_GIVEN,
        transcription_profanity_filter: bool | NotGiven = NOT_GIVEN,
        transcription_speaker_diarization: bool | NotGiven = NOT_GIVEN,
        trim: Literal["trim-silence"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionStartRecordingResponse:
        """Start recording the call.

        Recording will stop on call hang-up, or can be
        initiated via the Stop Recording command.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/start-call-record#callbacks)
        below):**

        - `call.recording.saved`
        - `call.recording.transcription.saved`
        - `call.recording.error`

        Args:
          channels: When `dual`, final audio file will be stereo recorded with the first leg on
              channel A, and the rest on channel B.

          format: The audio file format used when storing the call recording. Can be either `mp3`
              or `wav`.

          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          custom_file_name: The custom recording file name to be used instead of the default `call_leg_id`.
              Telnyx will still add a Unix timestamp suffix.

          max_length: Defines the maximum length for the recording in seconds. The minimum value is 0.
              The maximum value is 14400. The default value is 0 (infinite)

          play_beep: If enabled, a beep sound will be played at the start of a recording.

          recording_track: The audio track to be recorded. Can be either `both`, `inbound` or `outbound`.
              If only single track is specified (`inbound`, `outbound`), `channels`
              configuration is ignored and it will be recorded as mono (single channel).

          timeout_secs: The number of seconds that Telnyx will wait for the recording to be stopped if
              silence is detected. The timer only starts when the speech is detected. Please
              note that call transcription is used to detect silence and the related charge
              will be applied. The minimum value is 0. The default value is 0 (infinite)

          transcription: Enable post recording transcription. The default value is false.

          transcription_engine: Engine to use for speech recognition. `A` - `Google`

          transcription_language: Language to use for speech recognition

          transcription_max_speaker_count: Defines maximum number of speakers in the conversation. Applies to `google`
              engine only.

          transcription_min_speaker_count: Defines minimum number of speakers in the conversation. Applies to `google`
              engine only.

          transcription_profanity_filter: Enables profanity_filter. Applies to `google` engine only.

          transcription_speaker_diarization: Enables speaker diarization. Applies to `google` engine only.

          trim: When set to `trim-silence`, silence will be removed from the beginning and end
              of the recording.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return self._post(
            f"/calls/{call_control_id}/actions/record_start",
            body=maybe_transform(
                {
                    "channels": channels,
                    "format": format,
                    "client_state": client_state,
                    "command_id": command_id,
                    "custom_file_name": custom_file_name,
                    "max_length": max_length,
                    "play_beep": play_beep,
                    "recording_track": recording_track,
                    "timeout_secs": timeout_secs,
                    "transcription": transcription,
                    "transcription_engine": transcription_engine,
                    "transcription_language": transcription_language,
                    "transcription_max_speaker_count": transcription_max_speaker_count,
                    "transcription_min_speaker_count": transcription_min_speaker_count,
                    "transcription_profanity_filter": transcription_profanity_filter,
                    "transcription_speaker_diarization": transcription_speaker_diarization,
                    "trim": trim,
                },
                action_start_recording_params.ActionStartRecordingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionStartRecordingResponse,
        )

    def start_siprec(
        self,
        call_control_id: str,
        *,
        client_state: str | NotGiven = NOT_GIVEN,
        connector_name: str | NotGiven = NOT_GIVEN,
        include_metadata_custom_headers: Literal[True, False] | NotGiven = NOT_GIVEN,
        secure: Literal[True, False] | NotGiven = NOT_GIVEN,
        session_timeout_secs: int | NotGiven = NOT_GIVEN,
        sip_transport: Literal["udp", "tcp", "tls"] | NotGiven = NOT_GIVEN,
        siprec_track: Literal["inbound_track", "outbound_track", "both_tracks"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionStartSiprecResponse:
        """
        Start siprec session to configured in SIPREC connector SRS.

        **Expected Webhooks:**

        - `siprec.started`
        - `siprec.stopped`
        - `siprec.failed`

        Args:
          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          connector_name: Name of configured SIPREC connector to be used.

          include_metadata_custom_headers: When set, custom parameters will be added as metadata
              (recording.session.ExtensionParameters). Otherwise, they’ll be added to sip
              headers.

          secure: Controls whether to encrypt media sent to your SRS using SRTP and TLS. When set
              you need to configure SRS port in your connector to 5061.

          session_timeout_secs: Sets `Session-Expires` header to the INVITE. A reinvite is sent every half the
              value set. Usefull for session keep alive. Minimum value is 90, set to 0 to
              disable.

          sip_transport: Specifies SIP transport protocol.

          siprec_track: Specifies which track should be sent on siprec session.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return self._post(
            f"/calls/{call_control_id}/actions/siprec_start",
            body=maybe_transform(
                {
                    "client_state": client_state,
                    "connector_name": connector_name,
                    "include_metadata_custom_headers": include_metadata_custom_headers,
                    "secure": secure,
                    "session_timeout_secs": session_timeout_secs,
                    "sip_transport": sip_transport,
                    "siprec_track": siprec_track,
                },
                action_start_siprec_params.ActionStartSiprecParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionStartSiprecResponse,
        )

    def start_streaming(
        self,
        call_control_id: str,
        *,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        dialogflow_config: DialogflowConfigParam | NotGiven = NOT_GIVEN,
        enable_dialogflow: bool | NotGiven = NOT_GIVEN,
        stream_bidirectional_codec: StreamBidirectionalCodec | NotGiven = NOT_GIVEN,
        stream_bidirectional_mode: StreamBidirectionalMode | NotGiven = NOT_GIVEN,
        stream_bidirectional_target_legs: StreamBidirectionalTargetLegs | NotGiven = NOT_GIVEN,
        stream_codec: StreamCodec | NotGiven = NOT_GIVEN,
        stream_track: Literal["inbound_track", "outbound_track", "both_tracks"] | NotGiven = NOT_GIVEN,
        stream_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionStartStreamingResponse:
        """
        Start streaming the media from a call to a specific WebSocket address or
        Dialogflow connection in near-realtime. Audio will be delivered as
        base64-encoded RTP payload (raw audio), wrapped in JSON payloads.

        Please find more details about media streaming messages specification under the
        [link](https://developers.telnyx.com/docs/voice/programmable-voice/media-streaming).

        Args:
          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          enable_dialogflow: Enables Dialogflow for the current call. The default value is false.

          stream_bidirectional_codec: Indicates codec for bidirectional streaming RTP payloads. Used only with
              stream_bidirectional_mode=rtp. Case sensitive.

          stream_bidirectional_mode: Configures method of bidirectional streaming (mp3, rtp).

          stream_bidirectional_target_legs: Specifies which call legs should receive the bidirectional stream audio.

          stream_codec: Specifies the codec to be used for the streamed audio. When set to 'default' or
              when transcoding is not possible, the codec from the call will be used.
              Currently, transcoding is only supported between PCMU and PCMA codecs.

          stream_track: Specifies which track should be streamed.

          stream_url: The destination WebSocket address where the stream is going to be delivered.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return self._post(
            f"/calls/{call_control_id}/actions/streaming_start",
            body=maybe_transform(
                {
                    "client_state": client_state,
                    "command_id": command_id,
                    "dialogflow_config": dialogflow_config,
                    "enable_dialogflow": enable_dialogflow,
                    "stream_bidirectional_codec": stream_bidirectional_codec,
                    "stream_bidirectional_mode": stream_bidirectional_mode,
                    "stream_bidirectional_target_legs": stream_bidirectional_target_legs,
                    "stream_codec": stream_codec,
                    "stream_track": stream_track,
                    "stream_url": stream_url,
                },
                action_start_streaming_params.ActionStartStreamingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionStartStreamingResponse,
        )

    def start_transcription(
        self,
        call_control_id: str,
        *,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        transcription_engine: Literal["A", "B"] | NotGiven = NOT_GIVEN,
        transcription_engine_config: action_start_transcription_params.TranscriptionEngineConfig | NotGiven = NOT_GIVEN,
        transcription_tracks: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionStartTranscriptionResponse:
        """Start real-time transcription.

        Transcription will stop on call hang-up, or can
        be initiated via the Transcription stop command.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/start-call-transcription#callbacks)
        below):**

        - `call.transcription`

        Args:
          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          transcription_engine: Engine to use for speech recognition. `A` - `Google`, `B` - `Telnyx`.

          transcription_tracks: Indicates which leg of the call will be transcribed. Use `inbound` for the leg
              that requested the transcription, `outbound` for the other leg, and `both` for
              both legs of the call. Will default to `inbound`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return self._post(
            f"/calls/{call_control_id}/actions/transcription_start",
            body=maybe_transform(
                {
                    "client_state": client_state,
                    "command_id": command_id,
                    "transcription_engine": transcription_engine,
                    "transcription_engine_config": transcription_engine_config,
                    "transcription_tracks": transcription_tracks,
                },
                action_start_transcription_params.ActionStartTranscriptionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionStartTranscriptionResponse,
        )

    def stop_ai_assistant(
        self,
        call_control_id: str,
        *,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionStopAIAssistantResponse:
        """
        Stop an AI assistant on the call.

        Args:
          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return self._post(
            f"/calls/{call_control_id}/actions/ai_assistant_stop",
            body=maybe_transform(
                {
                    "client_state": client_state,
                    "command_id": command_id,
                },
                action_stop_ai_assistant_params.ActionStopAIAssistantParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionStopAIAssistantResponse,
        )

    def stop_forking(
        self,
        call_control_id: str,
        *,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        stream_type: Literal["raw", "decrypted"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionStopForkingResponse:
        """
        Stop forking a call.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/stop-call-fork#callbacks)
        below):**

        - `call.fork.stopped`

        Args:
          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          stream_type: Optionally specify a `stream_type`. This should match the `stream_type` that was
              used in `fork_start` command to properly stop the fork.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return self._post(
            f"/calls/{call_control_id}/actions/fork_stop",
            body=maybe_transform(
                {
                    "client_state": client_state,
                    "command_id": command_id,
                    "stream_type": stream_type,
                },
                action_stop_forking_params.ActionStopForkingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionStopForkingResponse,
        )

    def stop_gather(
        self,
        call_control_id: str,
        *,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionStopGatherResponse:
        """
        Stop current gather.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/stop-call-gather#callbacks)
        below):**

        - `call.gather.ended`

        Args:
          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return self._post(
            f"/calls/{call_control_id}/actions/gather_stop",
            body=maybe_transform(
                {
                    "client_state": client_state,
                    "command_id": command_id,
                },
                action_stop_gather_params.ActionStopGatherParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionStopGatherResponse,
        )

    def stop_noise_suppression(
        self,
        call_control_id: str,
        *,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionStopNoiseSuppressionResponse:
        """
        Noise Suppression Stop (BETA)

        Args:
          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return self._post(
            f"/calls/{call_control_id}/actions/suppression_stop",
            body=maybe_transform(
                {
                    "client_state": client_state,
                    "command_id": command_id,
                },
                action_stop_noise_suppression_params.ActionStopNoiseSuppressionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionStopNoiseSuppressionResponse,
        )

    def stop_playback(
        self,
        call_control_id: str,
        *,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        overlay: bool | NotGiven = NOT_GIVEN,
        stop: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionStopPlaybackResponse:
        """
        Stop audio being played on the call.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/stop-call-playback#callbacks)
        below):**

        - `call.playback.ended` or `call.speak.ended`

        Args:
          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          overlay: When enabled, it stops the audio being played in the overlay queue.

          stop: Use `current` to stop the current audio being played. Use `all` to stop the
              current audio file being played and clear all audio files from the queue.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return self._post(
            f"/calls/{call_control_id}/actions/playback_stop",
            body=maybe_transform(
                {
                    "client_state": client_state,
                    "command_id": command_id,
                    "overlay": overlay,
                    "stop": stop,
                },
                action_stop_playback_params.ActionStopPlaybackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionStopPlaybackResponse,
        )

    def stop_recording(
        self,
        call_control_id: str,
        *,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        recording_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionStopRecordingResponse:
        """
        Stop recording the call.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/stop-call-recording#callbacks)
        below):**

        - `call.recording.saved`

        Args:
          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          recording_id: Uniquely identifies the resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return self._post(
            f"/calls/{call_control_id}/actions/record_stop",
            body=maybe_transform(
                {
                    "client_state": client_state,
                    "command_id": command_id,
                    "recording_id": recording_id,
                },
                action_stop_recording_params.ActionStopRecordingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionStopRecordingResponse,
        )

    def stop_siprec(
        self,
        call_control_id: str,
        *,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionStopSiprecResponse:
        """
        Stop SIPREC session.

        **Expected Webhooks:**

        - `siprec.stopped`

        Args:
          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return self._post(
            f"/calls/{call_control_id}/actions/siprec_stop",
            body=maybe_transform(
                {
                    "client_state": client_state,
                    "command_id": command_id,
                },
                action_stop_siprec_params.ActionStopSiprecParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionStopSiprecResponse,
        )

    def stop_streaming(
        self,
        call_control_id: str,
        *,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        stream_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionStopStreamingResponse:
        """
        Stop streaming a call to a WebSocket.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/stop-call-streaming#callbacks)
        below):**

        - `streaming.stopped`

        Args:
          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          stream_id: Identifies the stream. If the `stream_id` is not provided the command stops all
              streams associated with a given `call_control_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return self._post(
            f"/calls/{call_control_id}/actions/streaming_stop",
            body=maybe_transform(
                {
                    "client_state": client_state,
                    "command_id": command_id,
                    "stream_id": stream_id,
                },
                action_stop_streaming_params.ActionStopStreamingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionStopStreamingResponse,
        )

    def stop_transcription(
        self,
        call_control_id: str,
        *,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionStopTranscriptionResponse:
        """
        Stop real-time transcription.

        Args:
          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return self._post(
            f"/calls/{call_control_id}/actions/transcription_stop",
            body=maybe_transform(
                {
                    "client_state": client_state,
                    "command_id": command_id,
                },
                action_stop_transcription_params.ActionStopTranscriptionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionStopTranscriptionResponse,
        )

    def switch_supervisor_role(
        self,
        call_control_id: str,
        *,
        role: Literal["barge", "whisper", "monitor"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionSwitchSupervisorRoleResponse:
        """Switch the supervisor role for a bridged call.

        This allows switching between
        different supervisor modes during an active call

        Args:
          role: The supervisor role to switch to. 'barge' allows speaking to both parties,
              'whisper' allows speaking to caller only, 'monitor' allows listening only.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return self._post(
            f"/calls/{call_control_id}/actions/switch_supervisor_role",
            body=maybe_transform({"role": role}, action_switch_supervisor_role_params.ActionSwitchSupervisorRoleParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionSwitchSupervisorRoleResponse,
        )

    def transfer(
        self,
        call_control_id: str,
        *,
        to: str,
        answering_machine_detection: Literal[
            "premium", "detect", "detect_beep", "detect_words", "greeting_end", "disabled"
        ]
        | NotGiven = NOT_GIVEN,
        answering_machine_detection_config: action_transfer_params.AnsweringMachineDetectionConfig
        | NotGiven = NOT_GIVEN,
        audio_url: str | NotGiven = NOT_GIVEN,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        custom_headers: Iterable[CustomSipHeaderParam] | NotGiven = NOT_GIVEN,
        early_media: bool | NotGiven = NOT_GIVEN,
        from_: str | NotGiven = NOT_GIVEN,
        from_display_name: str | NotGiven = NOT_GIVEN,
        media_encryption: Literal["disabled", "SRTP", "DTLS"] | NotGiven = NOT_GIVEN,
        media_name: str | NotGiven = NOT_GIVEN,
        mute_dtmf: Literal["none", "both", "self", "opposite"] | NotGiven = NOT_GIVEN,
        park_after_unbridge: str | NotGiven = NOT_GIVEN,
        sip_auth_password: str | NotGiven = NOT_GIVEN,
        sip_auth_username: str | NotGiven = NOT_GIVEN,
        sip_headers: Iterable[SipHeaderParam] | NotGiven = NOT_GIVEN,
        sip_transport_protocol: Literal["UDP", "TCP", "TLS"] | NotGiven = NOT_GIVEN,
        sound_modifications: SoundModificationsParam | NotGiven = NOT_GIVEN,
        target_leg_client_state: str | NotGiven = NOT_GIVEN,
        time_limit_secs: int | NotGiven = NOT_GIVEN,
        timeout_secs: int | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        webhook_url_method: Literal["POST", "GET"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionTransferResponse:
        """Transfer a call to a new destination.

        If the transfer is unsuccessful, a
        `call.hangup` webhook for the other call (Leg B) will be sent indicating that
        the transfer could not be completed. The original call will remain active and
        may be issued additional commands, potentially transfering the call to an
        alternate destination.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/transfer-call#callbacks)
        below):**

        - `call.initiated`
        - `call.bridged` to Leg B
        - `call.answered` or `call.hangup`
        - `call.machine.detection.ended` if `answering_machine_detection` was requested
        - `call.machine.greeting.ended` if `answering_machine_detection` was requested
          to detect the end of machine greeting
        - `call.machine.premium.detection.ended` if
          `answering_machine_detection=premium` was requested
        - `call.machine.premium.greeting.ended` if `answering_machine_detection=premium`
          was requested and a beep was detected

        Args:
          to: The DID or SIP URI to dial out to.

          answering_machine_detection: Enables Answering Machine Detection. When a call is answered, Telnyx runs
              real-time detection to determine if it was picked up by a human or a machine and
              sends an `call.machine.detection.ended` webhook with the analysis result. If
              'greeting_end' or 'detect_words' is used and a 'machine' is detected, you will
              receive another 'call.machine.greeting.ended' webhook when the answering machine
              greeting ends with a beep or silence. If `detect_beep` is used, you will only
              receive 'call.machine.greeting.ended' if a beep is detected.

          answering_machine_detection_config: Optional configuration parameters to modify 'answering_machine_detection'
              performance.

          audio_url: The URL of a file to be played back when the transfer destination answers before
              bridging the call. The URL can point to either a WAV or MP3 file. media_name and
              audio_url cannot be used together in one request.

          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          custom_headers: Custom headers to be added to the SIP INVITE.

          early_media: If set to false, early media will not be passed to the originating leg.

          from_: The `from` number to be used as the caller id presented to the destination (`to`
              number). The number should be in +E164 format. This attribute will default to
              the `to` number of the original call if omitted.

          from_display_name: The `from_display_name` string to be used as the caller id name (SIP From
              Display Name) presented to the destination (`to` number). The string should have
              a maximum of 128 characters, containing only letters, numbers, spaces, and
              -\\__~!.+ special characters. If ommited, the display name will be the same as the
              number in the `from` field.

          media_encryption: Defines whether media should be encrypted on the new call leg.

          media_name: The media_name of a file to be played back when the transfer destination answers
              before bridging the call. The media_name must point to a file previously
              uploaded to api.telnyx.com/v2/media by the same user/organization. The file must
              either be a WAV or MP3 file.

          mute_dtmf: When enabled, DTMF tones are not passed to the call participant. The webhooks
              containing the DTMF information will be sent.

          park_after_unbridge: Specifies behavior after the bridge ends (i.e. the opposite leg either hangs up
              or is transferred). If supplied with the value `self`, the current leg will be
              parked after unbridge. If not set, the default behavior is to hang up the leg.

          sip_auth_password: SIP Authentication password used for SIP challenges.

          sip_auth_username: SIP Authentication username used for SIP challenges.

          sip_headers: SIP headers to be added to the SIP INVITE. Currently only User-to-User header is
              supported.

          sip_transport_protocol: Defines SIP transport protocol to be used on the call.

          sound_modifications: Use this field to modify sound effects, for example adjust the pitch.

          target_leg_client_state: Use this field to add state to every subsequent webhook for the new leg. It must
              be a valid Base-64 encoded string.

          time_limit_secs: Sets the maximum duration of a Call Control Leg in seconds. If the time limit is
              reached, the call will hangup and a `call.hangup` webhook with a `hangup_cause`
              of `time_limit` will be sent. For example, by setting a time limit of 120
              seconds, a Call Leg will be automatically terminated two minutes after being
              answered. The default time limit is 14400 seconds or 4 hours and this is also
              the maximum allowed call length.

          timeout_secs: The number of seconds that Telnyx will wait for the call to be answered by the
              destination to which it is being transferred. If the timeout is reached before
              an answer is received, the call will hangup and a `call.hangup` webhook with a
              `hangup_cause` of `timeout` will be sent. Minimum value is 5 seconds. Maximum
              value is 600 seconds.

          webhook_url: Use this field to override the URL for which Telnyx will send subsequent
              webhooks to for this call.

          webhook_url_method: HTTP request type used for `webhook_url`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return self._post(
            f"/calls/{call_control_id}/actions/transfer",
            body=maybe_transform(
                {
                    "to": to,
                    "answering_machine_detection": answering_machine_detection,
                    "answering_machine_detection_config": answering_machine_detection_config,
                    "audio_url": audio_url,
                    "client_state": client_state,
                    "command_id": command_id,
                    "custom_headers": custom_headers,
                    "early_media": early_media,
                    "from_": from_,
                    "from_display_name": from_display_name,
                    "media_encryption": media_encryption,
                    "media_name": media_name,
                    "mute_dtmf": mute_dtmf,
                    "park_after_unbridge": park_after_unbridge,
                    "sip_auth_password": sip_auth_password,
                    "sip_auth_username": sip_auth_username,
                    "sip_headers": sip_headers,
                    "sip_transport_protocol": sip_transport_protocol,
                    "sound_modifications": sound_modifications,
                    "target_leg_client_state": target_leg_client_state,
                    "time_limit_secs": time_limit_secs,
                    "timeout_secs": timeout_secs,
                    "webhook_url": webhook_url,
                    "webhook_url_method": webhook_url_method,
                },
                action_transfer_params.ActionTransferParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionTransferResponse,
        )

    def update_client_state(
        self,
        call_control_id: str,
        *,
        client_state: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionUpdateClientStateResponse:
        """
        Updates client state

        Args:
          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return self._put(
            f"/calls/{call_control_id}/actions/client_state_update",
            body=maybe_transform(
                {"client_state": client_state}, action_update_client_state_params.ActionUpdateClientStateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionUpdateClientStateResponse,
        )


class AsyncActionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncActionsResourceWithStreamingResponse(self)

    async def answer(
        self,
        call_control_id: str,
        *,
        billing_group_id: str | NotGiven = NOT_GIVEN,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        custom_headers: Iterable[CustomSipHeaderParam] | NotGiven = NOT_GIVEN,
        preferred_codecs: Literal["G722,PCMU,PCMA,G729,OPUS,VP8,H264"] | NotGiven = NOT_GIVEN,
        record: Literal["record-from-answer"] | NotGiven = NOT_GIVEN,
        record_channels: Literal["single", "dual"] | NotGiven = NOT_GIVEN,
        record_custom_file_name: str | NotGiven = NOT_GIVEN,
        record_format: Literal["wav", "mp3"] | NotGiven = NOT_GIVEN,
        record_max_length: int | NotGiven = NOT_GIVEN,
        record_timeout_secs: int | NotGiven = NOT_GIVEN,
        record_track: Literal["both", "inbound", "outbound"] | NotGiven = NOT_GIVEN,
        record_trim: Literal["trim-silence"] | NotGiven = NOT_GIVEN,
        send_silence_when_idle: bool | NotGiven = NOT_GIVEN,
        sip_headers: Iterable[SipHeaderParam] | NotGiven = NOT_GIVEN,
        sound_modifications: SoundModificationsParam | NotGiven = NOT_GIVEN,
        stream_bidirectional_codec: StreamBidirectionalCodec | NotGiven = NOT_GIVEN,
        stream_bidirectional_mode: StreamBidirectionalMode | NotGiven = NOT_GIVEN,
        stream_bidirectional_target_legs: StreamBidirectionalTargetLegs | NotGiven = NOT_GIVEN,
        stream_codec: StreamCodec | NotGiven = NOT_GIVEN,
        stream_track: Literal["inbound_track", "outbound_track", "both_tracks"] | NotGiven = NOT_GIVEN,
        stream_url: str | NotGiven = NOT_GIVEN,
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
    ) -> ActionAnswerResponse:
        """Answer an incoming call.

        You must issue this command before executing subsequent
        commands on an incoming call.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/answer-call#callbacks)
        below):**

        - `call.answered`
        - `streaming.started`, `streaming.stopped` or `streaming.failed` if `stream_url`
          was set

        When the `record` parameter is set to `record-from-answer`, the response will
        include a `recording_id` field.

        Args:
          billing_group_id: Use this field to set the Billing Group ID for the call. Must be a valid and
              existing Billing Group ID.

          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          custom_headers: Custom headers to be added to the SIP INVITE response.

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

          sip_headers: SIP headers to be added to the SIP INVITE response. Currently only User-to-User
              header is supported.

          sound_modifications: Use this field to modify sound effects, for example adjust the pitch.

          stream_bidirectional_codec: Indicates codec for bidirectional streaming RTP payloads. Used only with
              stream_bidirectional_mode=rtp. Case sensitive.

          stream_bidirectional_mode: Configures method of bidirectional streaming (mp3, rtp).

          stream_bidirectional_target_legs: Specifies which call legs should receive the bidirectional stream audio.

          stream_codec: Specifies the codec to be used for the streamed audio. When set to 'default' or
              when transcoding is not possible, the codec from the call will be used.
              Currently, transcoding is only supported between PCMU and PCMA codecs.

          stream_track: Specifies which track should be streamed.

          stream_url: The destination WebSocket address where the stream is going to be delivered.

          transcription: Enable transcription upon call answer. The default value is false.

          webhook_url: Use this field to override the URL for which Telnyx will send subsequent
              webhooks to for this call.

          webhook_url_method: HTTP request type used for `webhook_url`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return await self._post(
            f"/calls/{call_control_id}/actions/answer",
            body=await async_maybe_transform(
                {
                    "billing_group_id": billing_group_id,
                    "client_state": client_state,
                    "command_id": command_id,
                    "custom_headers": custom_headers,
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
                    "sip_headers": sip_headers,
                    "sound_modifications": sound_modifications,
                    "stream_bidirectional_codec": stream_bidirectional_codec,
                    "stream_bidirectional_mode": stream_bidirectional_mode,
                    "stream_bidirectional_target_legs": stream_bidirectional_target_legs,
                    "stream_codec": stream_codec,
                    "stream_track": stream_track,
                    "stream_url": stream_url,
                    "transcription": transcription,
                    "transcription_config": transcription_config,
                    "webhook_url": webhook_url,
                    "webhook_url_method": webhook_url_method,
                },
                action_answer_params.ActionAnswerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionAnswerResponse,
        )

    async def bridge(
        self,
        path_call_control_id: str,
        *,
        body_call_control_id: str,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        mute_dtmf: Literal["none", "both", "self", "opposite"] | NotGiven = NOT_GIVEN,
        park_after_unbridge: str | NotGiven = NOT_GIVEN,
        play_ringtone: bool | NotGiven = NOT_GIVEN,
        queue: str | NotGiven = NOT_GIVEN,
        record: Literal["record-from-answer"] | NotGiven = NOT_GIVEN,
        record_channels: Literal["single", "dual"] | NotGiven = NOT_GIVEN,
        record_custom_file_name: str | NotGiven = NOT_GIVEN,
        record_format: Literal["wav", "mp3"] | NotGiven = NOT_GIVEN,
        record_max_length: int | NotGiven = NOT_GIVEN,
        record_timeout_secs: int | NotGiven = NOT_GIVEN,
        record_track: Literal["both", "inbound", "outbound"] | NotGiven = NOT_GIVEN,
        record_trim: Literal["trim-silence"] | NotGiven = NOT_GIVEN,
        ringtone: Literal[
            "at",
            "au",
            "be",
            "bg",
            "br",
            "ch",
            "cl",
            "cn",
            "cz",
            "de",
            "dk",
            "ee",
            "es",
            "fi",
            "fr",
            "gr",
            "hu",
            "il",
            "in",
            "it",
            "jp",
            "lt",
            "mx",
            "my",
            "nl",
            "no",
            "nz",
            "ph",
            "pl",
            "pt",
            "ru",
            "se",
            "sg",
            "th",
            "tw",
            "uk",
            "us-old",
            "us",
            "ve",
            "za",
        ]
        | NotGiven = NOT_GIVEN,
        video_room_context: str | NotGiven = NOT_GIVEN,
        video_room_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionBridgeResponse:
        """
        Bridge two call control calls.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/bridge-call#callbacks)
        below):**

        - `call.bridged` for Leg A
        - `call.bridged` for Leg B

        Args:
          body_call_control_id: The Call Control ID of the call you want to bridge with, can't be used together
              with queue parameter or video_room_id parameter.

          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          mute_dtmf: When enabled, DTMF tones are not passed to the call participant. The webhooks
              containing the DTMF information will be sent.

          park_after_unbridge: Specifies behavior after the bridge ends (i.e. the opposite leg either hangs up
              or is transferred). If supplied with the value `self`, the current leg will be
              parked after unbridge. If not set, the default behavior is to hang up the leg.

          play_ringtone: Specifies whether to play a ringtone if the call you want to bridge with has not
              yet been answered.

          queue: The name of the queue you want to bridge with, can't be used together with
              call_control_id parameter or video_room_id parameter. Bridging with a queue
              means bridging with the first call in the queue. The call will always be removed
              from the queue regardless of whether bridging succeeds. Returns an error when
              the queue is empty.

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

          ringtone: Specifies which country ringtone to play when `play_ringtone` is set to `true`.
              If not set, the US ringtone will be played.

          video_room_context: The additional parameter that will be passed to the video conference. It is a
              text field and the user can decide how to use it. For example, you can set the
              participant name or pass JSON text. It can be used only with video_room_id
              parameter.

          video_room_id: The ID of the video room you want to bridge with, can't be used together with
              call_control_id parameter or queue parameter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_call_control_id:
            raise ValueError(
                f"Expected a non-empty value for `path_call_control_id` but received {path_call_control_id!r}"
            )
        return await self._post(
            f"/calls/{path_call_control_id}/actions/bridge",
            body=await async_maybe_transform(
                {
                    "body_call_control_id": body_call_control_id,
                    "client_state": client_state,
                    "command_id": command_id,
                    "mute_dtmf": mute_dtmf,
                    "park_after_unbridge": park_after_unbridge,
                    "play_ringtone": play_ringtone,
                    "queue": queue,
                    "record": record,
                    "record_channels": record_channels,
                    "record_custom_file_name": record_custom_file_name,
                    "record_format": record_format,
                    "record_max_length": record_max_length,
                    "record_timeout_secs": record_timeout_secs,
                    "record_track": record_track,
                    "record_trim": record_trim,
                    "ringtone": ringtone,
                    "video_room_context": video_room_context,
                    "video_room_id": video_room_id,
                },
                action_bridge_params.ActionBridgeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionBridgeResponse,
        )

    async def enqueue(
        self,
        call_control_id: str,
        *,
        queue_name: str,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        max_size: int | NotGiven = NOT_GIVEN,
        max_wait_time_secs: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionEnqueueResponse:
        """
        Put the call in a queue.

        Args:
          queue_name: The name of the queue the call should be put in. If a queue with a given name
              doesn't exist yet it will be created.

          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          max_size: The maximum number of calls allowed in the queue at a given time. Can't be
              modified for an existing queue.

          max_wait_time_secs: The number of seconds after which the call will be removed from the queue.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return await self._post(
            f"/calls/{call_control_id}/actions/enqueue",
            body=await async_maybe_transform(
                {
                    "queue_name": queue_name,
                    "client_state": client_state,
                    "command_id": command_id,
                    "max_size": max_size,
                    "max_wait_time_secs": max_wait_time_secs,
                },
                action_enqueue_params.ActionEnqueueParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionEnqueueResponse,
        )

    async def gather(
        self,
        call_control_id: str,
        *,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        gather_id: str | NotGiven = NOT_GIVEN,
        initial_timeout_millis: int | NotGiven = NOT_GIVEN,
        inter_digit_timeout_millis: int | NotGiven = NOT_GIVEN,
        maximum_digits: int | NotGiven = NOT_GIVEN,
        minimum_digits: int | NotGiven = NOT_GIVEN,
        terminating_digit: str | NotGiven = NOT_GIVEN,
        timeout_millis: int | NotGiven = NOT_GIVEN,
        valid_digits: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionGatherResponse:
        """
        Gather DTMF signals to build interactive menus.

        You can pass a list of valid digits. The `Answer` command must be issued before
        the `gather` command.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/gather-call#callbacks)
        below):**

        - `call.dtmf.received` (you may receive many of these webhooks)
        - `call.gather.ended`

        Args:
          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          gather_id: An id that will be sent back in the corresponding `call.gather.ended` webhook.
              Will be randomly generated if not specified.

          initial_timeout_millis: The number of milliseconds to wait for the first DTMF.

          inter_digit_timeout_millis: The number of milliseconds to wait for input between digits.

          maximum_digits: The maximum number of digits to fetch. This parameter has a maximum value
              of 128.

          minimum_digits: The minimum number of digits to fetch. This parameter has a minimum value of 1.

          terminating_digit: The digit used to terminate input if fewer than `maximum_digits` digits have
              been gathered.

          timeout_millis: The number of milliseconds to wait to complete the request.

          valid_digits: A list of all digits accepted as valid.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return await self._post(
            f"/calls/{call_control_id}/actions/gather",
            body=await async_maybe_transform(
                {
                    "client_state": client_state,
                    "command_id": command_id,
                    "gather_id": gather_id,
                    "initial_timeout_millis": initial_timeout_millis,
                    "inter_digit_timeout_millis": inter_digit_timeout_millis,
                    "maximum_digits": maximum_digits,
                    "minimum_digits": minimum_digits,
                    "terminating_digit": terminating_digit,
                    "timeout_millis": timeout_millis,
                    "valid_digits": valid_digits,
                },
                action_gather_params.ActionGatherParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionGatherResponse,
        )

    async def gather_using_ai(
        self,
        call_control_id: str,
        *,
        parameters: object,
        assistant: AssistantParam | NotGiven = NOT_GIVEN,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        greeting: str | NotGiven = NOT_GIVEN,
        interruption_settings: InterruptionSettingsParam | NotGiven = NOT_GIVEN,
        language: GoogleTranscriptionLanguage | NotGiven = NOT_GIVEN,
        message_history: Iterable[action_gather_using_ai_params.MessageHistory] | NotGiven = NOT_GIVEN,
        send_message_history_updates: bool | NotGiven = NOT_GIVEN,
        send_partial_results: bool | NotGiven = NOT_GIVEN,
        transcription: TranscriptionConfigParam | NotGiven = NOT_GIVEN,
        user_response_timeout_ms: int | NotGiven = NOT_GIVEN,
        voice: str | NotGiven = NOT_GIVEN,
        voice_settings: action_gather_using_ai_params.VoiceSettings | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionGatherUsingAIResponse:
        """
        Gather parameters defined in the request payload using a voice assistant.

        You can pass parameters described as a JSON Schema object and the voice
        assistant will attempt to gather these informations.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/call-gather-using-ai#callbacks)
        below):**

        - `call.ai_gather.ended`
        - `call.conversation.ended`
        - `call.ai_gather.partial_results` (if `send_partial_results` is set to `true`)
        - `call.ai_gather.message_history_updated` (if `send_message_history_updates` is
          set to `true`)

        Args:
          parameters: The parameters described as a JSON Schema object that needs to be gathered by
              the voice assistant. See the
              [JSON Schema reference](https://json-schema.org/understanding-json-schema) for
              documentation about the format

          assistant: Assistant configuration including choice of LLM, custom instructions, and tools.

          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          greeting: Text that will be played when the gathering starts, if none then nothing will be
              played when the gathering starts. The greeting can be text for any voice or SSML
              for `AWS.Polly.<voice_id>` voices. There is a 3,000 character limit.

          interruption_settings: Settings for handling user interruptions during assistant speech

          language: Language to use for speech recognition

          message_history: The message history you want the voice assistant to be aware of, this can be
              useful to keep the context of the conversation, or to pass additional
              information to the voice assistant.

          send_message_history_updates: Default is `false`. If set to `true`, the voice assistant will send updates to
              the message history via the `call.ai_gather.message_history_updated`
              [callback](https://developers.telnyx.com/api/call-control/call-gather-using-ai#callbacks)
              in real time as the message history is updated.

          send_partial_results: Default is `false`. If set to `true`, the voice assistant will send partial
              results via the `call.ai_gather.partial_results`
              [callback](https://developers.telnyx.com/api/call-control/call-gather-using-ai#callbacks)
              in real time as individual fields are gathered. If set to `false`, the voice
              assistant will only send the final result via the `call.ai_gather.ended`
              callback.

          transcription: The settings associated with speech to text for the voice assistant. This is
              only relevant if the assistant uses a text-to-text language model. Any assistant
              using a model with native audio support (e.g. `fixie-ai/ultravox-v0_4`) will
              ignore this field.

          user_response_timeout_ms: The number of milliseconds to wait for a user response before the voice
              assistant times out and check if the user is still there.

          voice: The voice to be used by the voice assistant. Currently we support ElevenLabs,
              Telnyx and AWS voices.

              **Supported Providers:**

              - **AWS:** Use `AWS.Polly.<VoiceId>` (e.g., `AWS.Polly.Joanna`). For neural
                voices, which provide more realistic, human-like speech, append `-Neural` to
                the `VoiceId` (e.g., `AWS.Polly.Joanna-Neural`). Check the
                [available voices](https://docs.aws.amazon.com/polly/latest/dg/available-voices.html)
                for compatibility.
              - **Azure:** Use `Azure.<VoiceId>. (e.g. Azure.en-CA-ClaraNeural,
                Azure.en-CA-LiamNeural, Azure.en-US-BrianMultilingualNeural,
                Azure.en-US-Ava:DragonHDLatestNeural. For a complete list of voices, go to
                [Azure Voice Gallery](https://speech.microsoft.com/portal/voicegallery).)
              - **ElevenLabs:** Use `ElevenLabs.<ModelId>.<VoiceId>` (e.g.,
                `ElevenLabs.BaseModel.John`). The `ModelId` part is optional. To use
                ElevenLabs, you must provide your ElevenLabs API key as an integration secret
                under `"voice_settings": {"api_key_ref": "<secret_id>"}`. See
                [integration secrets documentation](https://developers.telnyx.com/api/secrets-manager/integration-secrets/create-integration-secret)
                for details. Check
                [available voices](https://elevenlabs.io/docs/api-reference/get-voices).
              - **Telnyx:** Use `Telnyx.<model_id>.<voice_id>`

          voice_settings: The settings associated with the voice selected

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return await self._post(
            f"/calls/{call_control_id}/actions/gather_using_ai",
            body=await async_maybe_transform(
                {
                    "parameters": parameters,
                    "assistant": assistant,
                    "client_state": client_state,
                    "command_id": command_id,
                    "greeting": greeting,
                    "interruption_settings": interruption_settings,
                    "language": language,
                    "message_history": message_history,
                    "send_message_history_updates": send_message_history_updates,
                    "send_partial_results": send_partial_results,
                    "transcription": transcription,
                    "user_response_timeout_ms": user_response_timeout_ms,
                    "voice": voice,
                    "voice_settings": voice_settings,
                },
                action_gather_using_ai_params.ActionGatherUsingAIParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionGatherUsingAIResponse,
        )

    async def gather_using_audio(
        self,
        call_control_id: str,
        *,
        audio_url: str | NotGiven = NOT_GIVEN,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        inter_digit_timeout_millis: int | NotGiven = NOT_GIVEN,
        invalid_audio_url: str | NotGiven = NOT_GIVEN,
        invalid_media_name: str | NotGiven = NOT_GIVEN,
        maximum_digits: int | NotGiven = NOT_GIVEN,
        maximum_tries: int | NotGiven = NOT_GIVEN,
        media_name: str | NotGiven = NOT_GIVEN,
        minimum_digits: int | NotGiven = NOT_GIVEN,
        terminating_digit: str | NotGiven = NOT_GIVEN,
        timeout_millis: int | NotGiven = NOT_GIVEN,
        valid_digits: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionGatherUsingAudioResponse:
        """
        Play an audio file on the call until the required DTMF signals are gathered to
        build interactive menus.

        You can pass a list of valid digits along with an 'invalid_audio_url', which
        will be played back at the beginning of each prompt. Playback will be
        interrupted when a DTMF signal is received. The
        `Answer command must be issued before the `gather_using_audio` command.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/gather-using-audio#callbacks)
        below):**

        - `call.playback.started`
        - `call.playback.ended`
        - `call.dtmf.received` (you may receive many of these webhooks)
        - `call.gather.ended`

        Args:
          audio_url: The URL of a file to be played back at the beginning of each prompt. The URL can
              point to either a WAV or MP3 file. media_name and audio_url cannot be used
              together in one request.

          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          inter_digit_timeout_millis: The number of milliseconds to wait for input between digits.

          invalid_audio_url: The URL of a file to play when digits don't match the `valid_digits` parameter
              or the number of digits is not between `min` and `max`. The URL can point to
              either a WAV or MP3 file. invalid_media_name and invalid_audio_url cannot be
              used together in one request.

          invalid_media_name: The media_name of a file to be played back when digits don't match the
              `valid_digits` parameter or the number of digits is not between `min` and `max`.
              The media_name must point to a file previously uploaded to
              api.telnyx.com/v2/media by the same user/organization. The file must either be a
              WAV or MP3 file.

          maximum_digits: The maximum number of digits to fetch. This parameter has a maximum value
              of 128.

          maximum_tries: The maximum number of times the file should be played if there is no input from
              the user on the call.

          media_name: The media_name of a file to be played back at the beginning of each prompt. The
              media_name must point to a file previously uploaded to api.telnyx.com/v2/media
              by the same user/organization. The file must either be a WAV or MP3 file.

          minimum_digits: The minimum number of digits to fetch. This parameter has a minimum value of 1.

          terminating_digit: The digit used to terminate input if fewer than `maximum_digits` digits have
              been gathered.

          timeout_millis: The number of milliseconds to wait for a DTMF response after file playback ends
              before a replaying the sound file.

          valid_digits: A list of all digits accepted as valid.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return await self._post(
            f"/calls/{call_control_id}/actions/gather_using_audio",
            body=await async_maybe_transform(
                {
                    "audio_url": audio_url,
                    "client_state": client_state,
                    "command_id": command_id,
                    "inter_digit_timeout_millis": inter_digit_timeout_millis,
                    "invalid_audio_url": invalid_audio_url,
                    "invalid_media_name": invalid_media_name,
                    "maximum_digits": maximum_digits,
                    "maximum_tries": maximum_tries,
                    "media_name": media_name,
                    "minimum_digits": minimum_digits,
                    "terminating_digit": terminating_digit,
                    "timeout_millis": timeout_millis,
                    "valid_digits": valid_digits,
                },
                action_gather_using_audio_params.ActionGatherUsingAudioParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionGatherUsingAudioResponse,
        )

    async def gather_using_speak(
        self,
        call_control_id: str,
        *,
        payload: str,
        voice: str,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        inter_digit_timeout_millis: int | NotGiven = NOT_GIVEN,
        invalid_payload: str | NotGiven = NOT_GIVEN,
        language: Literal[
            "arb",
            "cmn-CN",
            "cy-GB",
            "da-DK",
            "de-DE",
            "en-AU",
            "en-GB",
            "en-GB-WLS",
            "en-IN",
            "en-US",
            "es-ES",
            "es-MX",
            "es-US",
            "fr-CA",
            "fr-FR",
            "hi-IN",
            "is-IS",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "nb-NO",
            "nl-NL",
            "pl-PL",
            "pt-BR",
            "pt-PT",
            "ro-RO",
            "ru-RU",
            "sv-SE",
            "tr-TR",
        ]
        | NotGiven = NOT_GIVEN,
        maximum_digits: int | NotGiven = NOT_GIVEN,
        maximum_tries: int | NotGiven = NOT_GIVEN,
        minimum_digits: int | NotGiven = NOT_GIVEN,
        payload_type: Literal["text", "ssml"] | NotGiven = NOT_GIVEN,
        service_level: Literal["basic", "premium"] | NotGiven = NOT_GIVEN,
        terminating_digit: str | NotGiven = NOT_GIVEN,
        timeout_millis: int | NotGiven = NOT_GIVEN,
        valid_digits: str | NotGiven = NOT_GIVEN,
        voice_settings: action_gather_using_speak_params.VoiceSettings | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionGatherUsingSpeakResponse:
        """
        Convert text to speech and play it on the call until the required DTMF signals
        are gathered to build interactive menus.

        You can pass a list of valid digits along with an 'invalid_payload', which will
        be played back at the beginning of each prompt. Speech will be interrupted when
        a DTMF signal is received. The `Answer` command must be issued before the
        `gather_using_speak` command.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/gather-using-speak#callbacks)
        below):**

        - `call.dtmf.received` (you may receive many of these webhooks)
        - `call.gather.ended`

        Args:
          payload: The text or SSML to be converted into speech. There is a 3,000 character limit.

          voice: Specifies the voice used in speech synthesis.

              - Define voices using the format `<Provider>.<Model>.<VoiceId>`. Specifying only
                the provider will give default values for voice_id and model_id.

                **Supported Providers:**

              - **AWS:** Use `AWS.Polly.<VoiceId>` (e.g., `AWS.Polly.Joanna`). For neural
                voices, which provide more realistic, human-like speech, append `-Neural` to
                the `VoiceId` (e.g., `AWS.Polly.Joanna-Neural`). Check the
                [available voices](https://docs.aws.amazon.com/polly/latest/dg/available-voices.html)
                for compatibility.
              - **Azure:** Use `Azure.<VoiceId>. (e.g. Azure.en-CA-ClaraNeural,
                Azure.en-CA-LiamNeural, Azure.en-US-BrianMultilingualNeural,
                Azure.en-US-Ava:DragonHDLatestNeural. For a complete list of voices, go to
                [Azure Voice Gallery](https://speech.microsoft.com/portal/voicegallery).)
              - **ElevenLabs:** Use `ElevenLabs.<ModelId>.<VoiceId>` (e.g.,
                `ElevenLabs.eleven_multilingual_v2.21m00Tcm4TlvDq8ikWAM`). The `ModelId` part
                is optional. To use ElevenLabs, you must provide your ElevenLabs API key as an
                integration identifier secret in
                `"voice_settings": {"api_key_ref": "<secret_identifier>"}`. See
                [integration secrets documentation](https://developers.telnyx.com/api/secrets-manager/integration-secrets/create-integration-secret)
                for details. Check
                [available voices](https://elevenlabs.io/docs/api-reference/get-voices).
              - **Telnyx:** Use `Telnyx.<model_id>.<voice_id>`

              For service_level basic, you may define the gender of the speaker (male or
              female).

          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          inter_digit_timeout_millis: The number of milliseconds to wait for input between digits.

          invalid_payload: The text or SSML to be converted into speech when digits don't match the
              `valid_digits` parameter or the number of digits is not between `min` and `max`.
              There is a 3,000 character limit.

          language: The language you want spoken. This parameter is ignored when a `Polly.*` voice
              is specified.

          maximum_digits: The maximum number of digits to fetch. This parameter has a maximum value
              of 128.

          maximum_tries: The maximum number of times that a file should be played back if there is no
              input from the user on the call.

          minimum_digits: The minimum number of digits to fetch. This parameter has a minimum value of 1.

          payload_type: The type of the provided payload. The payload can either be plain text, or
              Speech Synthesis Markup Language (SSML).

          service_level: This parameter impacts speech quality, language options and payload types. When
              using `basic`, only the `en-US` language and payload type `text` are allowed.

          terminating_digit: The digit used to terminate input if fewer than `maximum_digits` digits have
              been gathered.

          timeout_millis: The number of milliseconds to wait for a DTMF response after speak ends before a
              replaying the sound file.

          valid_digits: A list of all digits accepted as valid.

          voice_settings: The settings associated with the voice selected

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return await self._post(
            f"/calls/{call_control_id}/actions/gather_using_speak",
            body=await async_maybe_transform(
                {
                    "payload": payload,
                    "voice": voice,
                    "client_state": client_state,
                    "command_id": command_id,
                    "inter_digit_timeout_millis": inter_digit_timeout_millis,
                    "invalid_payload": invalid_payload,
                    "language": language,
                    "maximum_digits": maximum_digits,
                    "maximum_tries": maximum_tries,
                    "minimum_digits": minimum_digits,
                    "payload_type": payload_type,
                    "service_level": service_level,
                    "terminating_digit": terminating_digit,
                    "timeout_millis": timeout_millis,
                    "valid_digits": valid_digits,
                    "voice_settings": voice_settings,
                },
                action_gather_using_speak_params.ActionGatherUsingSpeakParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionGatherUsingSpeakResponse,
        )

    async def hangup(
        self,
        call_control_id: str,
        *,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionHangupResponse:
        """
        Hang up the call.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/hangup-call#callbacks)
        below):**

        - `call.hangup`
        - `call.recording.saved`

        Args:
          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return await self._post(
            f"/calls/{call_control_id}/actions/hangup",
            body=await async_maybe_transform(
                {
                    "client_state": client_state,
                    "command_id": command_id,
                },
                action_hangup_params.ActionHangupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionHangupResponse,
        )

    async def leave_queue(
        self,
        call_control_id: str,
        *,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionLeaveQueueResponse:
        """
        Removes the call from a queue.

        Args:
          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return await self._post(
            f"/calls/{call_control_id}/actions/leave_queue",
            body=await async_maybe_transform(
                {
                    "client_state": client_state,
                    "command_id": command_id,
                },
                action_leave_queue_params.ActionLeaveQueueParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionLeaveQueueResponse,
        )

    async def pause_recording(
        self,
        call_control_id: str,
        *,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        recording_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionPauseRecordingResponse:
        """Pause recording the call.

        Recording can be resumed via Resume recording command.

        **Expected Webhooks:**

        There are no webhooks associated with this command.

        Args:
          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          recording_id: Uniquely identifies the resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return await self._post(
            f"/calls/{call_control_id}/actions/record_pause",
            body=await async_maybe_transform(
                {
                    "client_state": client_state,
                    "command_id": command_id,
                    "recording_id": recording_id,
                },
                action_pause_recording_params.ActionPauseRecordingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionPauseRecordingResponse,
        )

    async def refer(
        self,
        call_control_id: str,
        *,
        sip_address: str,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        custom_headers: Iterable[CustomSipHeaderParam] | NotGiven = NOT_GIVEN,
        sip_auth_password: str | NotGiven = NOT_GIVEN,
        sip_auth_username: str | NotGiven = NOT_GIVEN,
        sip_headers: Iterable[SipHeaderParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionReferResponse:
        """Initiate a SIP Refer on a Call Control call.

        You can initiate a SIP Refer at any
        point in the duration of a call.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/refer-call#callbacks)
        below):**

        - `call.refer.started`
        - `call.refer.completed`
        - `call.refer.failed`

        Args:
          sip_address: The SIP URI to which the call will be referred to.

          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid execution of duplicate commands. Telnyx will ignore
              subsequent commands with the same `command_id` as one that has already been
              executed.

          custom_headers: Custom headers to be added to the SIP INVITE.

          sip_auth_password: SIP Authentication password used for SIP challenges.

          sip_auth_username: SIP Authentication username used for SIP challenges.

          sip_headers: SIP headers to be added to the request. Currently only User-to-User header is
              supported.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return await self._post(
            f"/calls/{call_control_id}/actions/refer",
            body=await async_maybe_transform(
                {
                    "sip_address": sip_address,
                    "client_state": client_state,
                    "command_id": command_id,
                    "custom_headers": custom_headers,
                    "sip_auth_password": sip_auth_password,
                    "sip_auth_username": sip_auth_username,
                    "sip_headers": sip_headers,
                },
                action_refer_params.ActionReferParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionReferResponse,
        )

    async def reject(
        self,
        call_control_id: str,
        *,
        cause: Literal["CALL_REJECTED", "USER_BUSY"],
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionRejectResponse:
        """
        Reject an incoming call.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/reject-call#callbacks)
        below):**

        - `call.hangup`

        Args:
          cause: Cause for call rejection.

          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return await self._post(
            f"/calls/{call_control_id}/actions/reject",
            body=await async_maybe_transform(
                {
                    "cause": cause,
                    "client_state": client_state,
                    "command_id": command_id,
                },
                action_reject_params.ActionRejectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRejectResponse,
        )

    async def resume_recording(
        self,
        call_control_id: str,
        *,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        recording_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionResumeRecordingResponse:
        """
        Resume recording the call.

        **Expected Webhooks:**

        There are no webhooks associated with this command.

        Args:
          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          recording_id: Uniquely identifies the resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return await self._post(
            f"/calls/{call_control_id}/actions/record_resume",
            body=await async_maybe_transform(
                {
                    "client_state": client_state,
                    "command_id": command_id,
                    "recording_id": recording_id,
                },
                action_resume_recording_params.ActionResumeRecordingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionResumeRecordingResponse,
        )

    async def send_dtmf(
        self,
        call_control_id: str,
        *,
        digits: str,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        duration_millis: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionSendDtmfResponse:
        """Sends DTMF tones from this leg.

        DTMF tones will be heard by the other end of the
        call.

        **Expected Webhooks:**

        There are no webhooks associated with this command.

        Args:
          digits: DTMF digits to send. Valid digits are 0-9, A-D, \\**, and #. Pauses can be added
              using w (0.5s) and W (1s).

          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          duration_millis: Specifies for how many milliseconds each digit will be played in the audio
              stream. Ranges from 100 to 500ms

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return await self._post(
            f"/calls/{call_control_id}/actions/send_dtmf",
            body=await async_maybe_transform(
                {
                    "digits": digits,
                    "client_state": client_state,
                    "command_id": command_id,
                    "duration_millis": duration_millis,
                },
                action_send_dtmf_params.ActionSendDtmfParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionSendDtmfResponse,
        )

    async def send_sip_info(
        self,
        call_control_id: str,
        *,
        body: str,
        content_type: str,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionSendSipInfoResponse:
        """
        Sends SIP info from this leg.

        **Expected Webhooks:**

        - `call.sip_info.received` (to be received on the target call leg)

        Args:
          body: Content of the SIP INFO

          content_type: Content type of the INFO body. Must be MIME type compliant. There is a 1,400
              bytes limit

          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return await self._post(
            f"/calls/{call_control_id}/actions/send_sip_info",
            body=await async_maybe_transform(
                {
                    "body": body,
                    "content_type": content_type,
                    "client_state": client_state,
                    "command_id": command_id,
                },
                action_send_sip_info_params.ActionSendSipInfoParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionSendSipInfoResponse,
        )

    async def speak(
        self,
        call_control_id: str,
        *,
        payload: str,
        voice: str,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        language: Literal[
            "arb",
            "cmn-CN",
            "cy-GB",
            "da-DK",
            "de-DE",
            "en-AU",
            "en-GB",
            "en-GB-WLS",
            "en-IN",
            "en-US",
            "es-ES",
            "es-MX",
            "es-US",
            "fr-CA",
            "fr-FR",
            "hi-IN",
            "is-IS",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "nb-NO",
            "nl-NL",
            "pl-PL",
            "pt-BR",
            "pt-PT",
            "ro-RO",
            "ru-RU",
            "sv-SE",
            "tr-TR",
        ]
        | NotGiven = NOT_GIVEN,
        payload_type: Literal["text", "ssml"] | NotGiven = NOT_GIVEN,
        service_level: Literal["basic", "premium"] | NotGiven = NOT_GIVEN,
        stop: str | NotGiven = NOT_GIVEN,
        voice_settings: action_speak_params.VoiceSettings | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionSpeakResponse:
        """Convert text to speech and play it back on the call.

        If multiple speak text
        commands are issued consecutively, the audio files will be placed in a queue
        awaiting playback.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/speak-call#callbacks)
        below):**

        - `call.speak.started`
        - `call.speak.ended`

        Args:
          payload: The text or SSML to be converted into speech. There is a 3,000 character limit.

          voice: Specifies the voice used in speech synthesis.

              - Define voices using the format `<Provider>.<Model>.<VoiceId>`. Specifying only
                the provider will give default values for voice_id and model_id.

                **Supported Providers:**

              - **AWS:** Use `AWS.Polly.<VoiceId>` (e.g., `AWS.Polly.Joanna`). For neural
                voices, which provide more realistic, human-like speech, append `-Neural` to
                the `VoiceId` (e.g., `AWS.Polly.Joanna-Neural`). Check the
                [available voices](https://docs.aws.amazon.com/polly/latest/dg/available-voices.html)
                for compatibility.
              - **Azure:** Use `Azure.<VoiceId>. (e.g. Azure.en-CA-ClaraNeural,
                Azure.en-CA-LiamNeural, Azure.en-US-BrianMultilingualNeural,
                Azure.en-US-Ava:DragonHDLatestNeural. For a complete list of voices, go to
                [Azure Voice Gallery](https://speech.microsoft.com/portal/voicegallery).)
              - **ElevenLabs:** Use `ElevenLabs.<ModelId>.<VoiceId>` (e.g.,
                `ElevenLabs.eleven_multilingual_v2.21m00Tcm4TlvDq8ikWAM`). The `ModelId` part
                is optional. To use ElevenLabs, you must provide your ElevenLabs API key as an
                integration identifier secret in
                `"voice_settings": {"api_key_ref": "<secret_identifier>"}`. See
                [integration secrets documentation](https://developers.telnyx.com/api/secrets-manager/integration-secrets/create-integration-secret)
                for details. Check
                [available voices](https://elevenlabs.io/docs/api-reference/get-voices).
              - **Telnyx:** Use `Telnyx.<model_id>.<voice_id>`

              For service_level basic, you may define the gender of the speaker (male or
              female).

          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          language: The language you want spoken. This parameter is ignored when a `Polly.*` voice
              is specified.

          payload_type: The type of the provided payload. The payload can either be plain text, or
              Speech Synthesis Markup Language (SSML).

          service_level: This parameter impacts speech quality, language options and payload types. When
              using `basic`, only the `en-US` language and payload type `text` are allowed.

          stop: When specified, it stops the current audio being played. Specify `current` to
              stop the current audio being played, and to play the next file in the queue.
              Specify `all` to stop the current audio file being played and to also clear all
              audio files from the queue.

          voice_settings: The settings associated with the voice selected

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return await self._post(
            f"/calls/{call_control_id}/actions/speak",
            body=await async_maybe_transform(
                {
                    "payload": payload,
                    "voice": voice,
                    "client_state": client_state,
                    "command_id": command_id,
                    "language": language,
                    "payload_type": payload_type,
                    "service_level": service_level,
                    "stop": stop,
                    "voice_settings": voice_settings,
                },
                action_speak_params.ActionSpeakParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionSpeakResponse,
        )

    async def start_ai_assistant(
        self,
        call_control_id: str,
        *,
        assistant: action_start_ai_assistant_params.Assistant | NotGiven = NOT_GIVEN,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        greeting: str | NotGiven = NOT_GIVEN,
        interruption_settings: InterruptionSettingsParam | NotGiven = NOT_GIVEN,
        transcription: TranscriptionConfigParam | NotGiven = NOT_GIVEN,
        voice: str | NotGiven = NOT_GIVEN,
        voice_settings: action_start_ai_assistant_params.VoiceSettings | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionStartAIAssistantResponse:
        """
        Start an AI assistant on the call.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/call-start-ai-assistant#callbacks)
        below):**

        - `call.conversation.ended`
        - `call.conversation_insights.generated`

        Args:
          assistant: AI Assistant configuration

          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          greeting: Text that will be played when the assistant starts, if none then nothing will be
              played when the assistant starts. The greeting can be text for any voice or SSML
              for `AWS.Polly.<voice_id>` voices. There is a 3,000 character limit.

          interruption_settings: Settings for handling user interruptions during assistant speech

          transcription: The settings associated with speech to text for the voice assistant. This is
              only relevant if the assistant uses a text-to-text language model. Any assistant
              using a model with native audio support (e.g. `fixie-ai/ultravox-v0_4`) will
              ignore this field.

          voice: The voice to be used by the voice assistant. Currently we support ElevenLabs,
              Telnyx and AWS voices.

              **Supported Providers:**

              - **AWS:** Use `AWS.Polly.<VoiceId>` (e.g., `AWS.Polly.Joanna`). For neural
                voices, which provide more realistic, human-like speech, append `-Neural` to
                the `VoiceId` (e.g., `AWS.Polly.Joanna-Neural`). Check the
                [available voices](https://docs.aws.amazon.com/polly/latest/dg/available-voices.html)
                for compatibility.
              - **Azure:** Use `Azure.<VoiceId>. (e.g. Azure.en-CA-ClaraNeural,
                Azure.en-CA-LiamNeural, Azure.en-US-BrianMultilingualNeural,
                Azure.en-US-Ava:DragonHDLatestNeural. For a complete list of voices, go to
                [Azure Voice Gallery](https://speech.microsoft.com/portal/voicegallery).)
              - **ElevenLabs:** Use `ElevenLabs.<ModelId>.<VoiceId>` (e.g.,
                `ElevenLabs.BaseModel.John`). The `ModelId` part is optional. To use
                ElevenLabs, you must provide your ElevenLabs API key as an integration secret
                under `"voice_settings": {"api_key_ref": "<secret_id>"}`. See
                [integration secrets documentation](https://developers.telnyx.com/api/secrets-manager/integration-secrets/create-integration-secret)
                for details. Check
                [available voices](https://elevenlabs.io/docs/api-reference/get-voices).
              - **Telnyx:** Use `Telnyx.<model_id>.<voice_id>`

          voice_settings: The settings associated with the voice selected

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return await self._post(
            f"/calls/{call_control_id}/actions/ai_assistant_start",
            body=await async_maybe_transform(
                {
                    "assistant": assistant,
                    "client_state": client_state,
                    "command_id": command_id,
                    "greeting": greeting,
                    "interruption_settings": interruption_settings,
                    "transcription": transcription,
                    "voice": voice,
                    "voice_settings": voice_settings,
                },
                action_start_ai_assistant_params.ActionStartAIAssistantParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionStartAIAssistantResponse,
        )

    async def start_forking(
        self,
        call_control_id: str,
        *,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        rx: str | NotGiven = NOT_GIVEN,
        stream_type: Literal["decrypted"] | NotGiven = NOT_GIVEN,
        tx: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionStartForkingResponse:
        """
        Call forking allows you to stream the media from a call to a specific target in
        realtime. This stream can be used to enable realtime audio analysis to support a
        variety of use cases, including fraud detection, or the creation of AI-generated
        audio responses. Requests must specify either the `target` attribute or the `rx`
        and `tx` attributes.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/start-call-fork#callbacks)
        below):**

        - `call.fork.started`
        - `call.fork.stopped`

        Args:
          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          rx: The network target, <udp:ip_address:port>, where the call's incoming RTP media
              packets should be forwarded.

          stream_type: Optionally specify a media type to stream. If `decrypted` selected, Telnyx will
              decrypt incoming SIP media before forking to the target. `rx` and `tx` are
              required fields if `decrypted` selected.

          tx: The network target, <udp:ip_address:port>, where the call's outgoing RTP media
              packets should be forwarded.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return await self._post(
            f"/calls/{call_control_id}/actions/fork_start",
            body=await async_maybe_transform(
                {
                    "client_state": client_state,
                    "command_id": command_id,
                    "rx": rx,
                    "stream_type": stream_type,
                    "tx": tx,
                },
                action_start_forking_params.ActionStartForkingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionStartForkingResponse,
        )

    async def start_noise_suppression(
        self,
        call_control_id: str,
        *,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        direction: Literal["inbound", "outbound", "both"] | NotGiven = NOT_GIVEN,
        noise_suppression_engine: Literal["A", "B"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionStartNoiseSuppressionResponse:
        """
        Noise Suppression Start (BETA)

        Args:
          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          direction: The direction of the audio stream to be noise suppressed.

          noise_suppression_engine: The engine to use for noise suppression. A - rnnoise engine B - deepfilter
              engine.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return await self._post(
            f"/calls/{call_control_id}/actions/suppression_start",
            body=await async_maybe_transform(
                {
                    "client_state": client_state,
                    "command_id": command_id,
                    "direction": direction,
                    "noise_suppression_engine": noise_suppression_engine,
                },
                action_start_noise_suppression_params.ActionStartNoiseSuppressionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionStartNoiseSuppressionResponse,
        )

    async def start_playback(
        self,
        call_control_id: str,
        *,
        audio_type: Literal["mp3", "wav"] | NotGiven = NOT_GIVEN,
        audio_url: str | NotGiven = NOT_GIVEN,
        cache_audio: bool | NotGiven = NOT_GIVEN,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        loop: LoopcountParam | NotGiven = NOT_GIVEN,
        media_name: str | NotGiven = NOT_GIVEN,
        overlay: bool | NotGiven = NOT_GIVEN,
        playback_content: str | NotGiven = NOT_GIVEN,
        stop: str | NotGiven = NOT_GIVEN,
        target_legs: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionStartPlaybackResponse:
        """Play an audio file on the call.

        If multiple play audio commands are issued
        consecutively, the audio files will be placed in a queue awaiting playback.

        _Notes:_

        - When `overlay` is enabled, `target_legs` is limited to `self`.
        - A customer cannot Play Audio with `overlay=true` unless there is a Play Audio
          with `overlay=false` actively playing.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/start-call-playback#callbacks)
        below):**

        - `call.playback.started`
        - `call.playback.ended`

        Args:
          audio_type: Specifies the type of audio provided in `audio_url` or `playback_content`.

          audio_url: The URL of a file to be played back on the call. The URL can point to either a
              WAV or MP3 file. media_name and audio_url cannot be used together in one
              request.

          cache_audio: Caches the audio file. Useful when playing the same audio file multiple times
              during the call.

          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          loop: The number of times the audio file should be played. If supplied, the value must
              be an integer between 1 and 100, or the special string `infinity` for an endless
              loop.

          media_name: The media_name of a file to be played back on the call. The media_name must
              point to a file previously uploaded to api.telnyx.com/v2/media by the same
              user/organization. The file must either be a WAV or MP3 file.

          overlay: When enabled, audio will be mixed on top of any other audio that is actively
              being played back. Note that `overlay: true` will only work if there is another
              audio file already being played on the call.

          playback_content: Allows a user to provide base64 encoded mp3 or wav. Note: when using this
              parameter, `media_url` and `media_name` in the `playback_started` and
              `playback_ended` webhooks will be empty

          stop: When specified, it stops the current audio being played. Specify `current` to
              stop the current audio being played, and to play the next file in the queue.
              Specify `all` to stop the current audio file being played and to also clear all
              audio files from the queue.

          target_legs: Specifies the leg or legs on which audio will be played. If supplied, the value
              must be either `self`, `opposite` or `both`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return await self._post(
            f"/calls/{call_control_id}/actions/playback_start",
            body=await async_maybe_transform(
                {
                    "audio_type": audio_type,
                    "audio_url": audio_url,
                    "cache_audio": cache_audio,
                    "client_state": client_state,
                    "command_id": command_id,
                    "loop": loop,
                    "media_name": media_name,
                    "overlay": overlay,
                    "playback_content": playback_content,
                    "stop": stop,
                    "target_legs": target_legs,
                },
                action_start_playback_params.ActionStartPlaybackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionStartPlaybackResponse,
        )

    async def start_recording(
        self,
        call_control_id: str,
        *,
        channels: Literal["single", "dual"],
        format: Literal["wav", "mp3"],
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        custom_file_name: str | NotGiven = NOT_GIVEN,
        max_length: int | NotGiven = NOT_GIVEN,
        play_beep: bool | NotGiven = NOT_GIVEN,
        recording_track: Literal["both", "inbound", "outbound"] | NotGiven = NOT_GIVEN,
        timeout_secs: int | NotGiven = NOT_GIVEN,
        transcription: bool | NotGiven = NOT_GIVEN,
        transcription_engine: str | NotGiven = NOT_GIVEN,
        transcription_language: Literal[
            "af-ZA",
            "am-ET",
            "ar-AE",
            "ar-BH",
            "ar-DZ",
            "ar-EG",
            "ar-IL",
            "ar-IQ",
            "ar-JO",
            "ar-KW",
            "ar-LB",
            "ar-MA",
            "ar-MR",
            "ar-OM",
            "ar-PS",
            "ar-QA",
            "ar-SA",
            "ar-TN",
            "ar-YE",
            "az-AZ",
            "bg-BG",
            "bn-BD",
            "bn-IN",
            "bs-BA",
            "ca-ES",
            "cs-CZ",
            "da-DK",
            "de-AT",
            "de-CH",
            "de-DE",
            "el-GR",
            "en-AU",
            "en-CA",
            "en-GB",
            "en-GH",
            "en-HK",
            "en-IE",
            "en-IN",
            "en-KE",
            "en-NG",
            "en-NZ",
            "en-PH",
            "en-PK",
            "en-SG",
            "en-TZ",
            "en-US",
            "en-ZA",
            "es-AR",
            "es-BO",
            "es-CL",
            "es-CO",
            "es-CR",
            "es-DO",
            "es-EC",
            "es-ES",
            "es-GT",
            "es-HN",
            "es-MX",
            "es-NI",
            "es-PA",
            "es-PE",
            "es-PR",
            "es-PY",
            "es-SV",
            "es-US",
            "es-UY",
            "es-VE",
            "et-EE",
            "eu-ES",
            "fa-IR",
            "fi-FI",
            "fil-PH",
            "fr-BE",
            "fr-CA",
            "fr-CH",
            "fr-FR",
            "gl-ES",
            "gu-IN",
            "hi-IN",
            "hr-HR",
            "hu-HU",
            "hy-AM",
            "id-ID",
            "is-IS",
            "it-CH",
            "it-IT",
            "iw-IL",
            "ja-JP",
            "jv-ID",
            "ka-GE",
            "kk-KZ",
            "km-KH",
            "kn-IN",
            "ko-KR",
            "lo-LA",
            "lt-LT",
            "lv-LV",
            "mk-MK",
            "ml-IN",
            "mn-MN",
            "mr-IN",
            "ms-MY",
            "my-MM",
            "ne-NP",
            "nl-BE",
            "nl-NL",
            "no-NO",
            "pa-Guru-IN",
            "pl-PL",
            "pt-BR",
            "pt-PT",
            "ro-RO",
            "ru-RU",
            "rw-RW",
            "si-LK",
            "sk-SK",
            "sl-SI",
            "sq-AL",
            "sr-RS",
            "ss-latn-za",
            "st-ZA",
            "su-ID",
            "sv-SE",
            "sw-KE",
            "sw-TZ",
            "ta-IN",
            "ta-LK",
            "ta-MY",
            "ta-SG",
            "te-IN",
            "th-TH",
            "tn-latn-za",
            "tr-TR",
            "ts-ZA",
            "uk-UA",
            "ur-IN",
            "ur-PK",
            "uz-UZ",
            "ve-ZA",
            "vi-VN",
            "xh-ZA",
            "yue-Hant-HK",
            "zh",
            "zh-TW",
            "zu-ZA",
        ]
        | NotGiven = NOT_GIVEN,
        transcription_max_speaker_count: int | NotGiven = NOT_GIVEN,
        transcription_min_speaker_count: int | NotGiven = NOT_GIVEN,
        transcription_profanity_filter: bool | NotGiven = NOT_GIVEN,
        transcription_speaker_diarization: bool | NotGiven = NOT_GIVEN,
        trim: Literal["trim-silence"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionStartRecordingResponse:
        """Start recording the call.

        Recording will stop on call hang-up, or can be
        initiated via the Stop Recording command.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/start-call-record#callbacks)
        below):**

        - `call.recording.saved`
        - `call.recording.transcription.saved`
        - `call.recording.error`

        Args:
          channels: When `dual`, final audio file will be stereo recorded with the first leg on
              channel A, and the rest on channel B.

          format: The audio file format used when storing the call recording. Can be either `mp3`
              or `wav`.

          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          custom_file_name: The custom recording file name to be used instead of the default `call_leg_id`.
              Telnyx will still add a Unix timestamp suffix.

          max_length: Defines the maximum length for the recording in seconds. The minimum value is 0.
              The maximum value is 14400. The default value is 0 (infinite)

          play_beep: If enabled, a beep sound will be played at the start of a recording.

          recording_track: The audio track to be recorded. Can be either `both`, `inbound` or `outbound`.
              If only single track is specified (`inbound`, `outbound`), `channels`
              configuration is ignored and it will be recorded as mono (single channel).

          timeout_secs: The number of seconds that Telnyx will wait for the recording to be stopped if
              silence is detected. The timer only starts when the speech is detected. Please
              note that call transcription is used to detect silence and the related charge
              will be applied. The minimum value is 0. The default value is 0 (infinite)

          transcription: Enable post recording transcription. The default value is false.

          transcription_engine: Engine to use for speech recognition. `A` - `Google`

          transcription_language: Language to use for speech recognition

          transcription_max_speaker_count: Defines maximum number of speakers in the conversation. Applies to `google`
              engine only.

          transcription_min_speaker_count: Defines minimum number of speakers in the conversation. Applies to `google`
              engine only.

          transcription_profanity_filter: Enables profanity_filter. Applies to `google` engine only.

          transcription_speaker_diarization: Enables speaker diarization. Applies to `google` engine only.

          trim: When set to `trim-silence`, silence will be removed from the beginning and end
              of the recording.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return await self._post(
            f"/calls/{call_control_id}/actions/record_start",
            body=await async_maybe_transform(
                {
                    "channels": channels,
                    "format": format,
                    "client_state": client_state,
                    "command_id": command_id,
                    "custom_file_name": custom_file_name,
                    "max_length": max_length,
                    "play_beep": play_beep,
                    "recording_track": recording_track,
                    "timeout_secs": timeout_secs,
                    "transcription": transcription,
                    "transcription_engine": transcription_engine,
                    "transcription_language": transcription_language,
                    "transcription_max_speaker_count": transcription_max_speaker_count,
                    "transcription_min_speaker_count": transcription_min_speaker_count,
                    "transcription_profanity_filter": transcription_profanity_filter,
                    "transcription_speaker_diarization": transcription_speaker_diarization,
                    "trim": trim,
                },
                action_start_recording_params.ActionStartRecordingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionStartRecordingResponse,
        )

    async def start_siprec(
        self,
        call_control_id: str,
        *,
        client_state: str | NotGiven = NOT_GIVEN,
        connector_name: str | NotGiven = NOT_GIVEN,
        include_metadata_custom_headers: Literal[True, False] | NotGiven = NOT_GIVEN,
        secure: Literal[True, False] | NotGiven = NOT_GIVEN,
        session_timeout_secs: int | NotGiven = NOT_GIVEN,
        sip_transport: Literal["udp", "tcp", "tls"] | NotGiven = NOT_GIVEN,
        siprec_track: Literal["inbound_track", "outbound_track", "both_tracks"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionStartSiprecResponse:
        """
        Start siprec session to configured in SIPREC connector SRS.

        **Expected Webhooks:**

        - `siprec.started`
        - `siprec.stopped`
        - `siprec.failed`

        Args:
          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          connector_name: Name of configured SIPREC connector to be used.

          include_metadata_custom_headers: When set, custom parameters will be added as metadata
              (recording.session.ExtensionParameters). Otherwise, they’ll be added to sip
              headers.

          secure: Controls whether to encrypt media sent to your SRS using SRTP and TLS. When set
              you need to configure SRS port in your connector to 5061.

          session_timeout_secs: Sets `Session-Expires` header to the INVITE. A reinvite is sent every half the
              value set. Usefull for session keep alive. Minimum value is 90, set to 0 to
              disable.

          sip_transport: Specifies SIP transport protocol.

          siprec_track: Specifies which track should be sent on siprec session.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return await self._post(
            f"/calls/{call_control_id}/actions/siprec_start",
            body=await async_maybe_transform(
                {
                    "client_state": client_state,
                    "connector_name": connector_name,
                    "include_metadata_custom_headers": include_metadata_custom_headers,
                    "secure": secure,
                    "session_timeout_secs": session_timeout_secs,
                    "sip_transport": sip_transport,
                    "siprec_track": siprec_track,
                },
                action_start_siprec_params.ActionStartSiprecParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionStartSiprecResponse,
        )

    async def start_streaming(
        self,
        call_control_id: str,
        *,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        dialogflow_config: DialogflowConfigParam | NotGiven = NOT_GIVEN,
        enable_dialogflow: bool | NotGiven = NOT_GIVEN,
        stream_bidirectional_codec: StreamBidirectionalCodec | NotGiven = NOT_GIVEN,
        stream_bidirectional_mode: StreamBidirectionalMode | NotGiven = NOT_GIVEN,
        stream_bidirectional_target_legs: StreamBidirectionalTargetLegs | NotGiven = NOT_GIVEN,
        stream_codec: StreamCodec | NotGiven = NOT_GIVEN,
        stream_track: Literal["inbound_track", "outbound_track", "both_tracks"] | NotGiven = NOT_GIVEN,
        stream_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionStartStreamingResponse:
        """
        Start streaming the media from a call to a specific WebSocket address or
        Dialogflow connection in near-realtime. Audio will be delivered as
        base64-encoded RTP payload (raw audio), wrapped in JSON payloads.

        Please find more details about media streaming messages specification under the
        [link](https://developers.telnyx.com/docs/voice/programmable-voice/media-streaming).

        Args:
          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          enable_dialogflow: Enables Dialogflow for the current call. The default value is false.

          stream_bidirectional_codec: Indicates codec for bidirectional streaming RTP payloads. Used only with
              stream_bidirectional_mode=rtp. Case sensitive.

          stream_bidirectional_mode: Configures method of bidirectional streaming (mp3, rtp).

          stream_bidirectional_target_legs: Specifies which call legs should receive the bidirectional stream audio.

          stream_codec: Specifies the codec to be used for the streamed audio. When set to 'default' or
              when transcoding is not possible, the codec from the call will be used.
              Currently, transcoding is only supported between PCMU and PCMA codecs.

          stream_track: Specifies which track should be streamed.

          stream_url: The destination WebSocket address where the stream is going to be delivered.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return await self._post(
            f"/calls/{call_control_id}/actions/streaming_start",
            body=await async_maybe_transform(
                {
                    "client_state": client_state,
                    "command_id": command_id,
                    "dialogflow_config": dialogflow_config,
                    "enable_dialogflow": enable_dialogflow,
                    "stream_bidirectional_codec": stream_bidirectional_codec,
                    "stream_bidirectional_mode": stream_bidirectional_mode,
                    "stream_bidirectional_target_legs": stream_bidirectional_target_legs,
                    "stream_codec": stream_codec,
                    "stream_track": stream_track,
                    "stream_url": stream_url,
                },
                action_start_streaming_params.ActionStartStreamingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionStartStreamingResponse,
        )

    async def start_transcription(
        self,
        call_control_id: str,
        *,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        transcription_engine: Literal["A", "B"] | NotGiven = NOT_GIVEN,
        transcription_engine_config: action_start_transcription_params.TranscriptionEngineConfig | NotGiven = NOT_GIVEN,
        transcription_tracks: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionStartTranscriptionResponse:
        """Start real-time transcription.

        Transcription will stop on call hang-up, or can
        be initiated via the Transcription stop command.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/start-call-transcription#callbacks)
        below):**

        - `call.transcription`

        Args:
          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          transcription_engine: Engine to use for speech recognition. `A` - `Google`, `B` - `Telnyx`.

          transcription_tracks: Indicates which leg of the call will be transcribed. Use `inbound` for the leg
              that requested the transcription, `outbound` for the other leg, and `both` for
              both legs of the call. Will default to `inbound`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return await self._post(
            f"/calls/{call_control_id}/actions/transcription_start",
            body=await async_maybe_transform(
                {
                    "client_state": client_state,
                    "command_id": command_id,
                    "transcription_engine": transcription_engine,
                    "transcription_engine_config": transcription_engine_config,
                    "transcription_tracks": transcription_tracks,
                },
                action_start_transcription_params.ActionStartTranscriptionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionStartTranscriptionResponse,
        )

    async def stop_ai_assistant(
        self,
        call_control_id: str,
        *,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionStopAIAssistantResponse:
        """
        Stop an AI assistant on the call.

        Args:
          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return await self._post(
            f"/calls/{call_control_id}/actions/ai_assistant_stop",
            body=await async_maybe_transform(
                {
                    "client_state": client_state,
                    "command_id": command_id,
                },
                action_stop_ai_assistant_params.ActionStopAIAssistantParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionStopAIAssistantResponse,
        )

    async def stop_forking(
        self,
        call_control_id: str,
        *,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        stream_type: Literal["raw", "decrypted"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionStopForkingResponse:
        """
        Stop forking a call.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/stop-call-fork#callbacks)
        below):**

        - `call.fork.stopped`

        Args:
          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          stream_type: Optionally specify a `stream_type`. This should match the `stream_type` that was
              used in `fork_start` command to properly stop the fork.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return await self._post(
            f"/calls/{call_control_id}/actions/fork_stop",
            body=await async_maybe_transform(
                {
                    "client_state": client_state,
                    "command_id": command_id,
                    "stream_type": stream_type,
                },
                action_stop_forking_params.ActionStopForkingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionStopForkingResponse,
        )

    async def stop_gather(
        self,
        call_control_id: str,
        *,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionStopGatherResponse:
        """
        Stop current gather.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/stop-call-gather#callbacks)
        below):**

        - `call.gather.ended`

        Args:
          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return await self._post(
            f"/calls/{call_control_id}/actions/gather_stop",
            body=await async_maybe_transform(
                {
                    "client_state": client_state,
                    "command_id": command_id,
                },
                action_stop_gather_params.ActionStopGatherParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionStopGatherResponse,
        )

    async def stop_noise_suppression(
        self,
        call_control_id: str,
        *,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionStopNoiseSuppressionResponse:
        """
        Noise Suppression Stop (BETA)

        Args:
          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return await self._post(
            f"/calls/{call_control_id}/actions/suppression_stop",
            body=await async_maybe_transform(
                {
                    "client_state": client_state,
                    "command_id": command_id,
                },
                action_stop_noise_suppression_params.ActionStopNoiseSuppressionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionStopNoiseSuppressionResponse,
        )

    async def stop_playback(
        self,
        call_control_id: str,
        *,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        overlay: bool | NotGiven = NOT_GIVEN,
        stop: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionStopPlaybackResponse:
        """
        Stop audio being played on the call.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/stop-call-playback#callbacks)
        below):**

        - `call.playback.ended` or `call.speak.ended`

        Args:
          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          overlay: When enabled, it stops the audio being played in the overlay queue.

          stop: Use `current` to stop the current audio being played. Use `all` to stop the
              current audio file being played and clear all audio files from the queue.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return await self._post(
            f"/calls/{call_control_id}/actions/playback_stop",
            body=await async_maybe_transform(
                {
                    "client_state": client_state,
                    "command_id": command_id,
                    "overlay": overlay,
                    "stop": stop,
                },
                action_stop_playback_params.ActionStopPlaybackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionStopPlaybackResponse,
        )

    async def stop_recording(
        self,
        call_control_id: str,
        *,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        recording_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionStopRecordingResponse:
        """
        Stop recording the call.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/stop-call-recording#callbacks)
        below):**

        - `call.recording.saved`

        Args:
          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          recording_id: Uniquely identifies the resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return await self._post(
            f"/calls/{call_control_id}/actions/record_stop",
            body=await async_maybe_transform(
                {
                    "client_state": client_state,
                    "command_id": command_id,
                    "recording_id": recording_id,
                },
                action_stop_recording_params.ActionStopRecordingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionStopRecordingResponse,
        )

    async def stop_siprec(
        self,
        call_control_id: str,
        *,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionStopSiprecResponse:
        """
        Stop SIPREC session.

        **Expected Webhooks:**

        - `siprec.stopped`

        Args:
          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return await self._post(
            f"/calls/{call_control_id}/actions/siprec_stop",
            body=await async_maybe_transform(
                {
                    "client_state": client_state,
                    "command_id": command_id,
                },
                action_stop_siprec_params.ActionStopSiprecParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionStopSiprecResponse,
        )

    async def stop_streaming(
        self,
        call_control_id: str,
        *,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        stream_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionStopStreamingResponse:
        """
        Stop streaming a call to a WebSocket.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/stop-call-streaming#callbacks)
        below):**

        - `streaming.stopped`

        Args:
          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          stream_id: Identifies the stream. If the `stream_id` is not provided the command stops all
              streams associated with a given `call_control_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return await self._post(
            f"/calls/{call_control_id}/actions/streaming_stop",
            body=await async_maybe_transform(
                {
                    "client_state": client_state,
                    "command_id": command_id,
                    "stream_id": stream_id,
                },
                action_stop_streaming_params.ActionStopStreamingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionStopStreamingResponse,
        )

    async def stop_transcription(
        self,
        call_control_id: str,
        *,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionStopTranscriptionResponse:
        """
        Stop real-time transcription.

        Args:
          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return await self._post(
            f"/calls/{call_control_id}/actions/transcription_stop",
            body=await async_maybe_transform(
                {
                    "client_state": client_state,
                    "command_id": command_id,
                },
                action_stop_transcription_params.ActionStopTranscriptionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionStopTranscriptionResponse,
        )

    async def switch_supervisor_role(
        self,
        call_control_id: str,
        *,
        role: Literal["barge", "whisper", "monitor"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionSwitchSupervisorRoleResponse:
        """Switch the supervisor role for a bridged call.

        This allows switching between
        different supervisor modes during an active call

        Args:
          role: The supervisor role to switch to. 'barge' allows speaking to both parties,
              'whisper' allows speaking to caller only, 'monitor' allows listening only.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return await self._post(
            f"/calls/{call_control_id}/actions/switch_supervisor_role",
            body=await async_maybe_transform(
                {"role": role}, action_switch_supervisor_role_params.ActionSwitchSupervisorRoleParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionSwitchSupervisorRoleResponse,
        )

    async def transfer(
        self,
        call_control_id: str,
        *,
        to: str,
        answering_machine_detection: Literal[
            "premium", "detect", "detect_beep", "detect_words", "greeting_end", "disabled"
        ]
        | NotGiven = NOT_GIVEN,
        answering_machine_detection_config: action_transfer_params.AnsweringMachineDetectionConfig
        | NotGiven = NOT_GIVEN,
        audio_url: str | NotGiven = NOT_GIVEN,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        custom_headers: Iterable[CustomSipHeaderParam] | NotGiven = NOT_GIVEN,
        early_media: bool | NotGiven = NOT_GIVEN,
        from_: str | NotGiven = NOT_GIVEN,
        from_display_name: str | NotGiven = NOT_GIVEN,
        media_encryption: Literal["disabled", "SRTP", "DTLS"] | NotGiven = NOT_GIVEN,
        media_name: str | NotGiven = NOT_GIVEN,
        mute_dtmf: Literal["none", "both", "self", "opposite"] | NotGiven = NOT_GIVEN,
        park_after_unbridge: str | NotGiven = NOT_GIVEN,
        sip_auth_password: str | NotGiven = NOT_GIVEN,
        sip_auth_username: str | NotGiven = NOT_GIVEN,
        sip_headers: Iterable[SipHeaderParam] | NotGiven = NOT_GIVEN,
        sip_transport_protocol: Literal["UDP", "TCP", "TLS"] | NotGiven = NOT_GIVEN,
        sound_modifications: SoundModificationsParam | NotGiven = NOT_GIVEN,
        target_leg_client_state: str | NotGiven = NOT_GIVEN,
        time_limit_secs: int | NotGiven = NOT_GIVEN,
        timeout_secs: int | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        webhook_url_method: Literal["POST", "GET"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionTransferResponse:
        """Transfer a call to a new destination.

        If the transfer is unsuccessful, a
        `call.hangup` webhook for the other call (Leg B) will be sent indicating that
        the transfer could not be completed. The original call will remain active and
        may be issued additional commands, potentially transfering the call to an
        alternate destination.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/transfer-call#callbacks)
        below):**

        - `call.initiated`
        - `call.bridged` to Leg B
        - `call.answered` or `call.hangup`
        - `call.machine.detection.ended` if `answering_machine_detection` was requested
        - `call.machine.greeting.ended` if `answering_machine_detection` was requested
          to detect the end of machine greeting
        - `call.machine.premium.detection.ended` if
          `answering_machine_detection=premium` was requested
        - `call.machine.premium.greeting.ended` if `answering_machine_detection=premium`
          was requested and a beep was detected

        Args:
          to: The DID or SIP URI to dial out to.

          answering_machine_detection: Enables Answering Machine Detection. When a call is answered, Telnyx runs
              real-time detection to determine if it was picked up by a human or a machine and
              sends an `call.machine.detection.ended` webhook with the analysis result. If
              'greeting_end' or 'detect_words' is used and a 'machine' is detected, you will
              receive another 'call.machine.greeting.ended' webhook when the answering machine
              greeting ends with a beep or silence. If `detect_beep` is used, you will only
              receive 'call.machine.greeting.ended' if a beep is detected.

          answering_machine_detection_config: Optional configuration parameters to modify 'answering_machine_detection'
              performance.

          audio_url: The URL of a file to be played back when the transfer destination answers before
              bridging the call. The URL can point to either a WAV or MP3 file. media_name and
              audio_url cannot be used together in one request.

          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          custom_headers: Custom headers to be added to the SIP INVITE.

          early_media: If set to false, early media will not be passed to the originating leg.

          from_: The `from` number to be used as the caller id presented to the destination (`to`
              number). The number should be in +E164 format. This attribute will default to
              the `to` number of the original call if omitted.

          from_display_name: The `from_display_name` string to be used as the caller id name (SIP From
              Display Name) presented to the destination (`to` number). The string should have
              a maximum of 128 characters, containing only letters, numbers, spaces, and
              -\\__~!.+ special characters. If ommited, the display name will be the same as the
              number in the `from` field.

          media_encryption: Defines whether media should be encrypted on the new call leg.

          media_name: The media_name of a file to be played back when the transfer destination answers
              before bridging the call. The media_name must point to a file previously
              uploaded to api.telnyx.com/v2/media by the same user/organization. The file must
              either be a WAV or MP3 file.

          mute_dtmf: When enabled, DTMF tones are not passed to the call participant. The webhooks
              containing the DTMF information will be sent.

          park_after_unbridge: Specifies behavior after the bridge ends (i.e. the opposite leg either hangs up
              or is transferred). If supplied with the value `self`, the current leg will be
              parked after unbridge. If not set, the default behavior is to hang up the leg.

          sip_auth_password: SIP Authentication password used for SIP challenges.

          sip_auth_username: SIP Authentication username used for SIP challenges.

          sip_headers: SIP headers to be added to the SIP INVITE. Currently only User-to-User header is
              supported.

          sip_transport_protocol: Defines SIP transport protocol to be used on the call.

          sound_modifications: Use this field to modify sound effects, for example adjust the pitch.

          target_leg_client_state: Use this field to add state to every subsequent webhook for the new leg. It must
              be a valid Base-64 encoded string.

          time_limit_secs: Sets the maximum duration of a Call Control Leg in seconds. If the time limit is
              reached, the call will hangup and a `call.hangup` webhook with a `hangup_cause`
              of `time_limit` will be sent. For example, by setting a time limit of 120
              seconds, a Call Leg will be automatically terminated two minutes after being
              answered. The default time limit is 14400 seconds or 4 hours and this is also
              the maximum allowed call length.

          timeout_secs: The number of seconds that Telnyx will wait for the call to be answered by the
              destination to which it is being transferred. If the timeout is reached before
              an answer is received, the call will hangup and a `call.hangup` webhook with a
              `hangup_cause` of `timeout` will be sent. Minimum value is 5 seconds. Maximum
              value is 600 seconds.

          webhook_url: Use this field to override the URL for which Telnyx will send subsequent
              webhooks to for this call.

          webhook_url_method: HTTP request type used for `webhook_url`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return await self._post(
            f"/calls/{call_control_id}/actions/transfer",
            body=await async_maybe_transform(
                {
                    "to": to,
                    "answering_machine_detection": answering_machine_detection,
                    "answering_machine_detection_config": answering_machine_detection_config,
                    "audio_url": audio_url,
                    "client_state": client_state,
                    "command_id": command_id,
                    "custom_headers": custom_headers,
                    "early_media": early_media,
                    "from_": from_,
                    "from_display_name": from_display_name,
                    "media_encryption": media_encryption,
                    "media_name": media_name,
                    "mute_dtmf": mute_dtmf,
                    "park_after_unbridge": park_after_unbridge,
                    "sip_auth_password": sip_auth_password,
                    "sip_auth_username": sip_auth_username,
                    "sip_headers": sip_headers,
                    "sip_transport_protocol": sip_transport_protocol,
                    "sound_modifications": sound_modifications,
                    "target_leg_client_state": target_leg_client_state,
                    "time_limit_secs": time_limit_secs,
                    "timeout_secs": timeout_secs,
                    "webhook_url": webhook_url,
                    "webhook_url_method": webhook_url_method,
                },
                action_transfer_params.ActionTransferParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionTransferResponse,
        )

    async def update_client_state(
        self,
        call_control_id: str,
        *,
        client_state: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionUpdateClientStateResponse:
        """
        Updates client state

        Args:
          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return await self._put(
            f"/calls/{call_control_id}/actions/client_state_update",
            body=await async_maybe_transform(
                {"client_state": client_state}, action_update_client_state_params.ActionUpdateClientStateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionUpdateClientStateResponse,
        )


class ActionsResourceWithRawResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.answer = to_raw_response_wrapper(
            actions.answer,
        )
        self.bridge = to_raw_response_wrapper(
            actions.bridge,
        )
        self.enqueue = to_raw_response_wrapper(
            actions.enqueue,
        )
        self.gather = to_raw_response_wrapper(
            actions.gather,
        )
        self.gather_using_ai = to_raw_response_wrapper(
            actions.gather_using_ai,
        )
        self.gather_using_audio = to_raw_response_wrapper(
            actions.gather_using_audio,
        )
        self.gather_using_speak = to_raw_response_wrapper(
            actions.gather_using_speak,
        )
        self.hangup = to_raw_response_wrapper(
            actions.hangup,
        )
        self.leave_queue = to_raw_response_wrapper(
            actions.leave_queue,
        )
        self.pause_recording = to_raw_response_wrapper(
            actions.pause_recording,
        )
        self.refer = to_raw_response_wrapper(
            actions.refer,
        )
        self.reject = to_raw_response_wrapper(
            actions.reject,
        )
        self.resume_recording = to_raw_response_wrapper(
            actions.resume_recording,
        )
        self.send_dtmf = to_raw_response_wrapper(
            actions.send_dtmf,
        )
        self.send_sip_info = to_raw_response_wrapper(
            actions.send_sip_info,
        )
        self.speak = to_raw_response_wrapper(
            actions.speak,
        )
        self.start_ai_assistant = to_raw_response_wrapper(
            actions.start_ai_assistant,
        )
        self.start_forking = to_raw_response_wrapper(
            actions.start_forking,
        )
        self.start_noise_suppression = to_raw_response_wrapper(
            actions.start_noise_suppression,
        )
        self.start_playback = to_raw_response_wrapper(
            actions.start_playback,
        )
        self.start_recording = to_raw_response_wrapper(
            actions.start_recording,
        )
        self.start_siprec = to_raw_response_wrapper(
            actions.start_siprec,
        )
        self.start_streaming = to_raw_response_wrapper(
            actions.start_streaming,
        )
        self.start_transcription = to_raw_response_wrapper(
            actions.start_transcription,
        )
        self.stop_ai_assistant = to_raw_response_wrapper(
            actions.stop_ai_assistant,
        )
        self.stop_forking = to_raw_response_wrapper(
            actions.stop_forking,
        )
        self.stop_gather = to_raw_response_wrapper(
            actions.stop_gather,
        )
        self.stop_noise_suppression = to_raw_response_wrapper(
            actions.stop_noise_suppression,
        )
        self.stop_playback = to_raw_response_wrapper(
            actions.stop_playback,
        )
        self.stop_recording = to_raw_response_wrapper(
            actions.stop_recording,
        )
        self.stop_siprec = to_raw_response_wrapper(
            actions.stop_siprec,
        )
        self.stop_streaming = to_raw_response_wrapper(
            actions.stop_streaming,
        )
        self.stop_transcription = to_raw_response_wrapper(
            actions.stop_transcription,
        )
        self.switch_supervisor_role = to_raw_response_wrapper(
            actions.switch_supervisor_role,
        )
        self.transfer = to_raw_response_wrapper(
            actions.transfer,
        )
        self.update_client_state = to_raw_response_wrapper(
            actions.update_client_state,
        )


class AsyncActionsResourceWithRawResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.answer = async_to_raw_response_wrapper(
            actions.answer,
        )
        self.bridge = async_to_raw_response_wrapper(
            actions.bridge,
        )
        self.enqueue = async_to_raw_response_wrapper(
            actions.enqueue,
        )
        self.gather = async_to_raw_response_wrapper(
            actions.gather,
        )
        self.gather_using_ai = async_to_raw_response_wrapper(
            actions.gather_using_ai,
        )
        self.gather_using_audio = async_to_raw_response_wrapper(
            actions.gather_using_audio,
        )
        self.gather_using_speak = async_to_raw_response_wrapper(
            actions.gather_using_speak,
        )
        self.hangup = async_to_raw_response_wrapper(
            actions.hangup,
        )
        self.leave_queue = async_to_raw_response_wrapper(
            actions.leave_queue,
        )
        self.pause_recording = async_to_raw_response_wrapper(
            actions.pause_recording,
        )
        self.refer = async_to_raw_response_wrapper(
            actions.refer,
        )
        self.reject = async_to_raw_response_wrapper(
            actions.reject,
        )
        self.resume_recording = async_to_raw_response_wrapper(
            actions.resume_recording,
        )
        self.send_dtmf = async_to_raw_response_wrapper(
            actions.send_dtmf,
        )
        self.send_sip_info = async_to_raw_response_wrapper(
            actions.send_sip_info,
        )
        self.speak = async_to_raw_response_wrapper(
            actions.speak,
        )
        self.start_ai_assistant = async_to_raw_response_wrapper(
            actions.start_ai_assistant,
        )
        self.start_forking = async_to_raw_response_wrapper(
            actions.start_forking,
        )
        self.start_noise_suppression = async_to_raw_response_wrapper(
            actions.start_noise_suppression,
        )
        self.start_playback = async_to_raw_response_wrapper(
            actions.start_playback,
        )
        self.start_recording = async_to_raw_response_wrapper(
            actions.start_recording,
        )
        self.start_siprec = async_to_raw_response_wrapper(
            actions.start_siprec,
        )
        self.start_streaming = async_to_raw_response_wrapper(
            actions.start_streaming,
        )
        self.start_transcription = async_to_raw_response_wrapper(
            actions.start_transcription,
        )
        self.stop_ai_assistant = async_to_raw_response_wrapper(
            actions.stop_ai_assistant,
        )
        self.stop_forking = async_to_raw_response_wrapper(
            actions.stop_forking,
        )
        self.stop_gather = async_to_raw_response_wrapper(
            actions.stop_gather,
        )
        self.stop_noise_suppression = async_to_raw_response_wrapper(
            actions.stop_noise_suppression,
        )
        self.stop_playback = async_to_raw_response_wrapper(
            actions.stop_playback,
        )
        self.stop_recording = async_to_raw_response_wrapper(
            actions.stop_recording,
        )
        self.stop_siprec = async_to_raw_response_wrapper(
            actions.stop_siprec,
        )
        self.stop_streaming = async_to_raw_response_wrapper(
            actions.stop_streaming,
        )
        self.stop_transcription = async_to_raw_response_wrapper(
            actions.stop_transcription,
        )
        self.switch_supervisor_role = async_to_raw_response_wrapper(
            actions.switch_supervisor_role,
        )
        self.transfer = async_to_raw_response_wrapper(
            actions.transfer,
        )
        self.update_client_state = async_to_raw_response_wrapper(
            actions.update_client_state,
        )


class ActionsResourceWithStreamingResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.answer = to_streamed_response_wrapper(
            actions.answer,
        )
        self.bridge = to_streamed_response_wrapper(
            actions.bridge,
        )
        self.enqueue = to_streamed_response_wrapper(
            actions.enqueue,
        )
        self.gather = to_streamed_response_wrapper(
            actions.gather,
        )
        self.gather_using_ai = to_streamed_response_wrapper(
            actions.gather_using_ai,
        )
        self.gather_using_audio = to_streamed_response_wrapper(
            actions.gather_using_audio,
        )
        self.gather_using_speak = to_streamed_response_wrapper(
            actions.gather_using_speak,
        )
        self.hangup = to_streamed_response_wrapper(
            actions.hangup,
        )
        self.leave_queue = to_streamed_response_wrapper(
            actions.leave_queue,
        )
        self.pause_recording = to_streamed_response_wrapper(
            actions.pause_recording,
        )
        self.refer = to_streamed_response_wrapper(
            actions.refer,
        )
        self.reject = to_streamed_response_wrapper(
            actions.reject,
        )
        self.resume_recording = to_streamed_response_wrapper(
            actions.resume_recording,
        )
        self.send_dtmf = to_streamed_response_wrapper(
            actions.send_dtmf,
        )
        self.send_sip_info = to_streamed_response_wrapper(
            actions.send_sip_info,
        )
        self.speak = to_streamed_response_wrapper(
            actions.speak,
        )
        self.start_ai_assistant = to_streamed_response_wrapper(
            actions.start_ai_assistant,
        )
        self.start_forking = to_streamed_response_wrapper(
            actions.start_forking,
        )
        self.start_noise_suppression = to_streamed_response_wrapper(
            actions.start_noise_suppression,
        )
        self.start_playback = to_streamed_response_wrapper(
            actions.start_playback,
        )
        self.start_recording = to_streamed_response_wrapper(
            actions.start_recording,
        )
        self.start_siprec = to_streamed_response_wrapper(
            actions.start_siprec,
        )
        self.start_streaming = to_streamed_response_wrapper(
            actions.start_streaming,
        )
        self.start_transcription = to_streamed_response_wrapper(
            actions.start_transcription,
        )
        self.stop_ai_assistant = to_streamed_response_wrapper(
            actions.stop_ai_assistant,
        )
        self.stop_forking = to_streamed_response_wrapper(
            actions.stop_forking,
        )
        self.stop_gather = to_streamed_response_wrapper(
            actions.stop_gather,
        )
        self.stop_noise_suppression = to_streamed_response_wrapper(
            actions.stop_noise_suppression,
        )
        self.stop_playback = to_streamed_response_wrapper(
            actions.stop_playback,
        )
        self.stop_recording = to_streamed_response_wrapper(
            actions.stop_recording,
        )
        self.stop_siprec = to_streamed_response_wrapper(
            actions.stop_siprec,
        )
        self.stop_streaming = to_streamed_response_wrapper(
            actions.stop_streaming,
        )
        self.stop_transcription = to_streamed_response_wrapper(
            actions.stop_transcription,
        )
        self.switch_supervisor_role = to_streamed_response_wrapper(
            actions.switch_supervisor_role,
        )
        self.transfer = to_streamed_response_wrapper(
            actions.transfer,
        )
        self.update_client_state = to_streamed_response_wrapper(
            actions.update_client_state,
        )


class AsyncActionsResourceWithStreamingResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.answer = async_to_streamed_response_wrapper(
            actions.answer,
        )
        self.bridge = async_to_streamed_response_wrapper(
            actions.bridge,
        )
        self.enqueue = async_to_streamed_response_wrapper(
            actions.enqueue,
        )
        self.gather = async_to_streamed_response_wrapper(
            actions.gather,
        )
        self.gather_using_ai = async_to_streamed_response_wrapper(
            actions.gather_using_ai,
        )
        self.gather_using_audio = async_to_streamed_response_wrapper(
            actions.gather_using_audio,
        )
        self.gather_using_speak = async_to_streamed_response_wrapper(
            actions.gather_using_speak,
        )
        self.hangup = async_to_streamed_response_wrapper(
            actions.hangup,
        )
        self.leave_queue = async_to_streamed_response_wrapper(
            actions.leave_queue,
        )
        self.pause_recording = async_to_streamed_response_wrapper(
            actions.pause_recording,
        )
        self.refer = async_to_streamed_response_wrapper(
            actions.refer,
        )
        self.reject = async_to_streamed_response_wrapper(
            actions.reject,
        )
        self.resume_recording = async_to_streamed_response_wrapper(
            actions.resume_recording,
        )
        self.send_dtmf = async_to_streamed_response_wrapper(
            actions.send_dtmf,
        )
        self.send_sip_info = async_to_streamed_response_wrapper(
            actions.send_sip_info,
        )
        self.speak = async_to_streamed_response_wrapper(
            actions.speak,
        )
        self.start_ai_assistant = async_to_streamed_response_wrapper(
            actions.start_ai_assistant,
        )
        self.start_forking = async_to_streamed_response_wrapper(
            actions.start_forking,
        )
        self.start_noise_suppression = async_to_streamed_response_wrapper(
            actions.start_noise_suppression,
        )
        self.start_playback = async_to_streamed_response_wrapper(
            actions.start_playback,
        )
        self.start_recording = async_to_streamed_response_wrapper(
            actions.start_recording,
        )
        self.start_siprec = async_to_streamed_response_wrapper(
            actions.start_siprec,
        )
        self.start_streaming = async_to_streamed_response_wrapper(
            actions.start_streaming,
        )
        self.start_transcription = async_to_streamed_response_wrapper(
            actions.start_transcription,
        )
        self.stop_ai_assistant = async_to_streamed_response_wrapper(
            actions.stop_ai_assistant,
        )
        self.stop_forking = async_to_streamed_response_wrapper(
            actions.stop_forking,
        )
        self.stop_gather = async_to_streamed_response_wrapper(
            actions.stop_gather,
        )
        self.stop_noise_suppression = async_to_streamed_response_wrapper(
            actions.stop_noise_suppression,
        )
        self.stop_playback = async_to_streamed_response_wrapper(
            actions.stop_playback,
        )
        self.stop_recording = async_to_streamed_response_wrapper(
            actions.stop_recording,
        )
        self.stop_siprec = async_to_streamed_response_wrapper(
            actions.stop_siprec,
        )
        self.stop_streaming = async_to_streamed_response_wrapper(
            actions.stop_streaming,
        )
        self.stop_transcription = async_to_streamed_response_wrapper(
            actions.stop_transcription,
        )
        self.switch_supervisor_role = async_to_streamed_response_wrapper(
            actions.switch_supervisor_role,
        )
        self.transfer = async_to_streamed_response_wrapper(
            actions.transfer,
        )
        self.update_client_state = async_to_streamed_response_wrapper(
            actions.update_client_state,
        )

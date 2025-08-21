# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
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
from ..._base_client import make_request_options
from ...types.conferences import (
    action_hold_params,
    action_join_params,
    action_mute_params,
    action_play_params,
    action_stop_params,
    action_leave_params,
    action_speak_params,
    action_unhold_params,
    action_unmute_params,
    action_update_params,
    action_record_stop_params,
    action_record_pause_params,
    action_record_start_params,
    action_record_resume_params,
)
from ...types.calls.loopcount_param import LoopcountParam
from ...types.conferences.action_hold_response import ActionHoldResponse
from ...types.conferences.action_join_response import ActionJoinResponse
from ...types.conferences.action_mute_response import ActionMuteResponse
from ...types.conferences.action_play_response import ActionPlayResponse
from ...types.conferences.action_stop_response import ActionStopResponse
from ...types.conferences.action_leave_response import ActionLeaveResponse
from ...types.conferences.action_speak_response import ActionSpeakResponse
from ...types.conferences.action_unhold_response import ActionUnholdResponse
from ...types.conferences.action_unmute_response import ActionUnmuteResponse
from ...types.conferences.action_update_response import ActionUpdateResponse
from ...types.conferences.action_record_stop_response import ActionRecordStopResponse
from ...types.conferences.action_record_pause_response import ActionRecordPauseResponse
from ...types.conferences.action_record_start_response import ActionRecordStartResponse
from ...types.conferences.action_record_resume_response import ActionRecordResumeResponse

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

    def update(
        self,
        id: str,
        *,
        call_control_id: str,
        supervisor_role: Literal["barge", "monitor", "none", "whisper"],
        command_id: str | NotGiven = NOT_GIVEN,
        whisper_call_control_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionUpdateResponse:
        """
        Update conference participant supervisor_role

        Args:
          call_control_id: Unique identifier and token for controlling the call

          supervisor_role: Sets the participant as a supervisor for the conference. A conference can have
              multiple supervisors. "barge" means the supervisor enters the conference as a
              normal participant. This is the same as "none". "monitor" means the supervisor
              is muted but can hear all participants. "whisper" means that only the specified
              "whisper_call_control_ids" can hear the supervisor. Defaults to "none".

          command_id: Use this field to avoid execution of duplicate commands. Telnyx will ignore
              subsequent commands with the same `command_id` as one that has already been
              executed.

          whisper_call_control_ids: Array of unique call_control_ids the supervisor can whisper to. If none
              provided, the supervisor will join the conference as a monitoring participant
              only.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/conferences/{id}/actions/update",
            body=maybe_transform(
                {
                    "call_control_id": call_control_id,
                    "supervisor_role": supervisor_role,
                    "command_id": command_id,
                    "whisper_call_control_ids": whisper_call_control_ids,
                },
                action_update_params.ActionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionUpdateResponse,
        )

    def hold(
        self,
        id: str,
        *,
        audio_url: str | NotGiven = NOT_GIVEN,
        call_control_ids: List[str] | NotGiven = NOT_GIVEN,
        media_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionHoldResponse:
        """
        Hold a list of participants in a conference call

        Args:
          audio_url: The URL of a file to be played to the participants when they are put on hold.
              media_name and audio_url cannot be used together in one request.

          call_control_ids: List of unique identifiers and tokens for controlling the call. When empty all
              participants will be placed on hold.

          media_name: The media_name of a file to be played to the participants when they are put on
              hold. The media_name must point to a file previously uploaded to
              api.telnyx.com/v2/media by the same user/organization. The file must either be a
              WAV or MP3 file.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/conferences/{id}/actions/hold",
            body=maybe_transform(
                {
                    "audio_url": audio_url,
                    "call_control_ids": call_control_ids,
                    "media_name": media_name,
                },
                action_hold_params.ActionHoldParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionHoldResponse,
        )

    def join(
        self,
        id: str,
        *,
        call_control_id: str,
        beep_enabled: Literal["always", "never", "on_enter", "on_exit"] | NotGiven = NOT_GIVEN,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        end_conference_on_exit: bool | NotGiven = NOT_GIVEN,
        hold: bool | NotGiven = NOT_GIVEN,
        hold_audio_url: str | NotGiven = NOT_GIVEN,
        hold_media_name: str | NotGiven = NOT_GIVEN,
        mute: bool | NotGiven = NOT_GIVEN,
        soft_end_conference_on_exit: bool | NotGiven = NOT_GIVEN,
        start_conference_on_enter: bool | NotGiven = NOT_GIVEN,
        supervisor_role: Literal["barge", "monitor", "none", "whisper"] | NotGiven = NOT_GIVEN,
        whisper_call_control_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionJoinResponse:
        """Join an existing call leg to a conference.

        Issue the Join Conference command
        with the conference ID in the path and the `call_control_id` of the leg you wish
        to join to the conference as an attribute. The conference can have up to a
        certain amount of active participants, as set by the `max_participants`
        parameter in conference creation request.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/join-conference#callbacks)
        below):**

        - `conference.participant.joined`
        - `conference.participant.left`

        Args:
          call_control_id: Unique identifier and token for controlling the call

          beep_enabled: Whether a beep sound should be played when the participant joins and/or leaves
              the conference. Can be used to override the conference-level setting.

          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string. Please note that the client_state will be updated for
              the participient call leg and the change will not affect conferencing webhooks
              unless the participient is the owner of the conference.

          command_id: Use this field to avoid execution of duplicate commands. Telnyx will ignore
              subsequent commands with the same `command_id` as one that has already been
              executed.

          end_conference_on_exit: Whether the conference should end and all remaining participants be hung up
              after the participant leaves the conference. Defaults to "false".

          hold: Whether the participant should be put on hold immediately after joining the
              conference. Defaults to "false".

          hold_audio_url: The URL of a file to be played to the participant when they are put on hold
              after joining the conference. hold_media_name and hold_audio_url cannot be used
              together in one request. Takes effect only when "start_conference_on_create" is
              set to "false". This property takes effect only if "hold" is set to "true".

          hold_media_name: The media_name of a file to be played to the participant when they are put on
              hold after joining the conference. The media_name must point to a file
              previously uploaded to api.telnyx.com/v2/media by the same user/organization.
              The file must either be a WAV or MP3 file. Takes effect only when
              "start_conference_on_create" is set to "false". This property takes effect only
              if "hold" is set to "true".

          mute: Whether the participant should be muted immediately after joining the
              conference. Defaults to "false".

          soft_end_conference_on_exit: Whether the conference should end after the participant leaves the conference.
              NOTE this doesn't hang up the other participants. Defaults to "false".

          start_conference_on_enter: Whether the conference should be started after the participant joins the
              conference. Defaults to "false".

          supervisor_role: Sets the joining participant as a supervisor for the conference. A conference
              can have multiple supervisors. "barge" means the supervisor enters the
              conference as a normal participant. This is the same as "none". "monitor" means
              the supervisor is muted but can hear all participants. "whisper" means that only
              the specified "whisper_call_control_ids" can hear the supervisor. Defaults to
              "none".

          whisper_call_control_ids: Array of unique call_control_ids the joining supervisor can whisper to. If none
              provided, the supervisor will join the conference as a monitoring participant
              only.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/conferences/{id}/actions/join",
            body=maybe_transform(
                {
                    "call_control_id": call_control_id,
                    "beep_enabled": beep_enabled,
                    "client_state": client_state,
                    "command_id": command_id,
                    "end_conference_on_exit": end_conference_on_exit,
                    "hold": hold,
                    "hold_audio_url": hold_audio_url,
                    "hold_media_name": hold_media_name,
                    "mute": mute,
                    "soft_end_conference_on_exit": soft_end_conference_on_exit,
                    "start_conference_on_enter": start_conference_on_enter,
                    "supervisor_role": supervisor_role,
                    "whisper_call_control_ids": whisper_call_control_ids,
                },
                action_join_params.ActionJoinParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionJoinResponse,
        )

    def leave(
        self,
        id: str,
        *,
        call_control_id: str,
        beep_enabled: Literal["always", "never", "on_enter", "on_exit"] | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionLeaveResponse:
        """
        Removes a call leg from a conference and moves it back to parked state.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/leave-conference#callbacks)
        below):**

        - `conference.participant.left`

        Args:
          call_control_id: Unique identifier and token for controlling the call

          beep_enabled: Whether a beep sound should be played when the participant leaves the
              conference. Can be used to override the conference-level setting.

          command_id: Use this field to avoid execution of duplicate commands. Telnyx will ignore
              subsequent commands with the same `command_id` as one that has already been
              executed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/conferences/{id}/actions/leave",
            body=maybe_transform(
                {
                    "call_control_id": call_control_id,
                    "beep_enabled": beep_enabled,
                    "command_id": command_id,
                },
                action_leave_params.ActionLeaveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionLeaveResponse,
        )

    def mute(
        self,
        id: str,
        *,
        call_control_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionMuteResponse:
        """
        Mute a list of participants in a conference call

        Args:
          call_control_ids: Array of unique identifiers and tokens for controlling the call. When empty all
              participants will be muted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/conferences/{id}/actions/mute",
            body=maybe_transform({"call_control_ids": call_control_ids}, action_mute_params.ActionMuteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionMuteResponse,
        )

    def play(
        self,
        id: str,
        *,
        audio_url: str | NotGiven = NOT_GIVEN,
        call_control_ids: List[str] | NotGiven = NOT_GIVEN,
        loop: LoopcountParam | NotGiven = NOT_GIVEN,
        media_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionPlayResponse:
        """
        Play audio to all or some participants on a conference call.

        Args:
          audio_url: The URL of a file to be played back in the conference. media_name and audio_url
              cannot be used together in one request.

          call_control_ids: List of call control ids identifying participants the audio file should be
              played to. If not given, the audio file will be played to the entire conference.

          loop: The number of times the audio file should be played. If supplied, the value must
              be an integer between 1 and 100, or the special string `infinity` for an endless
              loop.

          media_name: The media_name of a file to be played back in the conference. The media_name
              must point to a file previously uploaded to api.telnyx.com/v2/media by the same
              user/organization. The file must either be a WAV or MP3 file.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/conferences/{id}/actions/play",
            body=maybe_transform(
                {
                    "audio_url": audio_url,
                    "call_control_ids": call_control_ids,
                    "loop": loop,
                    "media_name": media_name,
                },
                action_play_params.ActionPlayParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionPlayResponse,
        )

    def record_pause(
        self,
        id: str,
        *,
        command_id: str | NotGiven = NOT_GIVEN,
        recording_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionRecordPauseResponse:
        """
        Pause conference recording.

        Args:
          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          recording_id: Use this field to pause specific recording.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/conferences/{id}/actions/record_pause",
            body=maybe_transform(
                {
                    "command_id": command_id,
                    "recording_id": recording_id,
                },
                action_record_pause_params.ActionRecordPauseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRecordPauseResponse,
        )

    def record_resume(
        self,
        id: str,
        *,
        command_id: str | NotGiven = NOT_GIVEN,
        recording_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionRecordResumeResponse:
        """
        Resume conference recording.

        Args:
          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          recording_id: Use this field to resume specific recording.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/conferences/{id}/actions/record_resume",
            body=maybe_transform(
                {
                    "command_id": command_id,
                    "recording_id": recording_id,
                },
                action_record_resume_params.ActionRecordResumeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRecordResumeResponse,
        )

    def record_start(
        self,
        id: str,
        *,
        format: Literal["wav", "mp3"],
        command_id: str | NotGiven = NOT_GIVEN,
        custom_file_name: str | NotGiven = NOT_GIVEN,
        play_beep: bool | NotGiven = NOT_GIVEN,
        trim: Literal["trim-silence"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionRecordStartResponse:
        """Start recording the conference.

        Recording will stop on conference end, or via
        the Stop Recording command.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/start-conference-recording#callbacks)
        below):**

        - `conference.recording.saved`

        Args:
          format: The audio file format used when storing the conference recording. Can be either
              `mp3` or `wav`.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `conference_id`.

          custom_file_name: The custom recording file name to be used instead of the default `call_leg_id`.
              Telnyx will still add a Unix timestamp suffix.

          play_beep: If enabled, a beep sound will be played at the start of a recording.

          trim: When set to `trim-silence`, silence will be removed from the beginning and end
              of the recording.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/conferences/{id}/actions/record_start",
            body=maybe_transform(
                {
                    "format": format,
                    "command_id": command_id,
                    "custom_file_name": custom_file_name,
                    "play_beep": play_beep,
                    "trim": trim,
                },
                action_record_start_params.ActionRecordStartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRecordStartResponse,
        )

    def record_stop(
        self,
        id: str,
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
    ) -> ActionRecordStopResponse:
        """
        Stop recording the conference.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/stop-conference-recording#callbacks)
        below):**

        - `conference.recording.saved`

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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/conferences/{id}/actions/record_stop",
            body=maybe_transform(
                {
                    "client_state": client_state,
                    "command_id": command_id,
                    "recording_id": recording_id,
                },
                action_record_stop_params.ActionRecordStopParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRecordStopResponse,
        )

    def speak(
        self,
        id: str,
        *,
        payload: str,
        voice: str,
        call_control_ids: List[str] | NotGiven = NOT_GIVEN,
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
        voice_settings: action_speak_params.VoiceSettings | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionSpeakResponse:
        """
        Convert text to speech and play it to all or some participants.

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

          call_control_ids: Call Control IDs of participants who will hear the spoken text. When empty all
              participants will hear the spoken text.

          command_id: Use this field to avoid execution of duplicate commands. Telnyx will ignore
              subsequent commands with the same `command_id` as one that has already been
              executed.

          language: The language you want spoken. This parameter is ignored when a `Polly.*` voice
              is specified.

          payload_type: The type of the provided payload. The payload can either be plain text, or
              Speech Synthesis Markup Language (SSML).

          voice_settings: The settings associated with the voice selected

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/conferences/{id}/actions/speak",
            body=maybe_transform(
                {
                    "payload": payload,
                    "voice": voice,
                    "call_control_ids": call_control_ids,
                    "command_id": command_id,
                    "language": language,
                    "payload_type": payload_type,
                    "voice_settings": voice_settings,
                },
                action_speak_params.ActionSpeakParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionSpeakResponse,
        )

    def stop(
        self,
        id: str,
        *,
        call_control_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionStopResponse:
        """
        Stop audio being played to all or some participants on a conference call.

        Args:
          call_control_ids: List of call control ids identifying participants the audio file should stop be
              played to. If not given, the audio will be stoped to the entire conference.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/conferences/{id}/actions/stop",
            body=maybe_transform({"call_control_ids": call_control_ids}, action_stop_params.ActionStopParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionStopResponse,
        )

    def unhold(
        self,
        id: str,
        *,
        call_control_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionUnholdResponse:
        """
        Unhold a list of participants in a conference call

        Args:
          call_control_ids: List of unique identifiers and tokens for controlling the call. Enter each call
              control ID to be unheld.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/conferences/{id}/actions/unhold",
            body=maybe_transform({"call_control_ids": call_control_ids}, action_unhold_params.ActionUnholdParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionUnholdResponse,
        )

    def unmute(
        self,
        id: str,
        *,
        call_control_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionUnmuteResponse:
        """
        Unmute a list of participants in a conference call

        Args:
          call_control_ids: List of unique identifiers and tokens for controlling the call. Enter each call
              control ID to be unmuted. When empty all participants will be unmuted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/conferences/{id}/actions/unmute",
            body=maybe_transform({"call_control_ids": call_control_ids}, action_unmute_params.ActionUnmuteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionUnmuteResponse,
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

    async def update(
        self,
        id: str,
        *,
        call_control_id: str,
        supervisor_role: Literal["barge", "monitor", "none", "whisper"],
        command_id: str | NotGiven = NOT_GIVEN,
        whisper_call_control_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionUpdateResponse:
        """
        Update conference participant supervisor_role

        Args:
          call_control_id: Unique identifier and token for controlling the call

          supervisor_role: Sets the participant as a supervisor for the conference. A conference can have
              multiple supervisors. "barge" means the supervisor enters the conference as a
              normal participant. This is the same as "none". "monitor" means the supervisor
              is muted but can hear all participants. "whisper" means that only the specified
              "whisper_call_control_ids" can hear the supervisor. Defaults to "none".

          command_id: Use this field to avoid execution of duplicate commands. Telnyx will ignore
              subsequent commands with the same `command_id` as one that has already been
              executed.

          whisper_call_control_ids: Array of unique call_control_ids the supervisor can whisper to. If none
              provided, the supervisor will join the conference as a monitoring participant
              only.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/conferences/{id}/actions/update",
            body=await async_maybe_transform(
                {
                    "call_control_id": call_control_id,
                    "supervisor_role": supervisor_role,
                    "command_id": command_id,
                    "whisper_call_control_ids": whisper_call_control_ids,
                },
                action_update_params.ActionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionUpdateResponse,
        )

    async def hold(
        self,
        id: str,
        *,
        audio_url: str | NotGiven = NOT_GIVEN,
        call_control_ids: List[str] | NotGiven = NOT_GIVEN,
        media_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionHoldResponse:
        """
        Hold a list of participants in a conference call

        Args:
          audio_url: The URL of a file to be played to the participants when they are put on hold.
              media_name and audio_url cannot be used together in one request.

          call_control_ids: List of unique identifiers and tokens for controlling the call. When empty all
              participants will be placed on hold.

          media_name: The media_name of a file to be played to the participants when they are put on
              hold. The media_name must point to a file previously uploaded to
              api.telnyx.com/v2/media by the same user/organization. The file must either be a
              WAV or MP3 file.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/conferences/{id}/actions/hold",
            body=await async_maybe_transform(
                {
                    "audio_url": audio_url,
                    "call_control_ids": call_control_ids,
                    "media_name": media_name,
                },
                action_hold_params.ActionHoldParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionHoldResponse,
        )

    async def join(
        self,
        id: str,
        *,
        call_control_id: str,
        beep_enabled: Literal["always", "never", "on_enter", "on_exit"] | NotGiven = NOT_GIVEN,
        client_state: str | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        end_conference_on_exit: bool | NotGiven = NOT_GIVEN,
        hold: bool | NotGiven = NOT_GIVEN,
        hold_audio_url: str | NotGiven = NOT_GIVEN,
        hold_media_name: str | NotGiven = NOT_GIVEN,
        mute: bool | NotGiven = NOT_GIVEN,
        soft_end_conference_on_exit: bool | NotGiven = NOT_GIVEN,
        start_conference_on_enter: bool | NotGiven = NOT_GIVEN,
        supervisor_role: Literal["barge", "monitor", "none", "whisper"] | NotGiven = NOT_GIVEN,
        whisper_call_control_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionJoinResponse:
        """Join an existing call leg to a conference.

        Issue the Join Conference command
        with the conference ID in the path and the `call_control_id` of the leg you wish
        to join to the conference as an attribute. The conference can have up to a
        certain amount of active participants, as set by the `max_participants`
        parameter in conference creation request.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/join-conference#callbacks)
        below):**

        - `conference.participant.joined`
        - `conference.participant.left`

        Args:
          call_control_id: Unique identifier and token for controlling the call

          beep_enabled: Whether a beep sound should be played when the participant joins and/or leaves
              the conference. Can be used to override the conference-level setting.

          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string. Please note that the client_state will be updated for
              the participient call leg and the change will not affect conferencing webhooks
              unless the participient is the owner of the conference.

          command_id: Use this field to avoid execution of duplicate commands. Telnyx will ignore
              subsequent commands with the same `command_id` as one that has already been
              executed.

          end_conference_on_exit: Whether the conference should end and all remaining participants be hung up
              after the participant leaves the conference. Defaults to "false".

          hold: Whether the participant should be put on hold immediately after joining the
              conference. Defaults to "false".

          hold_audio_url: The URL of a file to be played to the participant when they are put on hold
              after joining the conference. hold_media_name and hold_audio_url cannot be used
              together in one request. Takes effect only when "start_conference_on_create" is
              set to "false". This property takes effect only if "hold" is set to "true".

          hold_media_name: The media_name of a file to be played to the participant when they are put on
              hold after joining the conference. The media_name must point to a file
              previously uploaded to api.telnyx.com/v2/media by the same user/organization.
              The file must either be a WAV or MP3 file. Takes effect only when
              "start_conference_on_create" is set to "false". This property takes effect only
              if "hold" is set to "true".

          mute: Whether the participant should be muted immediately after joining the
              conference. Defaults to "false".

          soft_end_conference_on_exit: Whether the conference should end after the participant leaves the conference.
              NOTE this doesn't hang up the other participants. Defaults to "false".

          start_conference_on_enter: Whether the conference should be started after the participant joins the
              conference. Defaults to "false".

          supervisor_role: Sets the joining participant as a supervisor for the conference. A conference
              can have multiple supervisors. "barge" means the supervisor enters the
              conference as a normal participant. This is the same as "none". "monitor" means
              the supervisor is muted but can hear all participants. "whisper" means that only
              the specified "whisper_call_control_ids" can hear the supervisor. Defaults to
              "none".

          whisper_call_control_ids: Array of unique call_control_ids the joining supervisor can whisper to. If none
              provided, the supervisor will join the conference as a monitoring participant
              only.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/conferences/{id}/actions/join",
            body=await async_maybe_transform(
                {
                    "call_control_id": call_control_id,
                    "beep_enabled": beep_enabled,
                    "client_state": client_state,
                    "command_id": command_id,
                    "end_conference_on_exit": end_conference_on_exit,
                    "hold": hold,
                    "hold_audio_url": hold_audio_url,
                    "hold_media_name": hold_media_name,
                    "mute": mute,
                    "soft_end_conference_on_exit": soft_end_conference_on_exit,
                    "start_conference_on_enter": start_conference_on_enter,
                    "supervisor_role": supervisor_role,
                    "whisper_call_control_ids": whisper_call_control_ids,
                },
                action_join_params.ActionJoinParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionJoinResponse,
        )

    async def leave(
        self,
        id: str,
        *,
        call_control_id: str,
        beep_enabled: Literal["always", "never", "on_enter", "on_exit"] | NotGiven = NOT_GIVEN,
        command_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionLeaveResponse:
        """
        Removes a call leg from a conference and moves it back to parked state.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/leave-conference#callbacks)
        below):**

        - `conference.participant.left`

        Args:
          call_control_id: Unique identifier and token for controlling the call

          beep_enabled: Whether a beep sound should be played when the participant leaves the
              conference. Can be used to override the conference-level setting.

          command_id: Use this field to avoid execution of duplicate commands. Telnyx will ignore
              subsequent commands with the same `command_id` as one that has already been
              executed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/conferences/{id}/actions/leave",
            body=await async_maybe_transform(
                {
                    "call_control_id": call_control_id,
                    "beep_enabled": beep_enabled,
                    "command_id": command_id,
                },
                action_leave_params.ActionLeaveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionLeaveResponse,
        )

    async def mute(
        self,
        id: str,
        *,
        call_control_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionMuteResponse:
        """
        Mute a list of participants in a conference call

        Args:
          call_control_ids: Array of unique identifiers and tokens for controlling the call. When empty all
              participants will be muted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/conferences/{id}/actions/mute",
            body=await async_maybe_transform(
                {"call_control_ids": call_control_ids}, action_mute_params.ActionMuteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionMuteResponse,
        )

    async def play(
        self,
        id: str,
        *,
        audio_url: str | NotGiven = NOT_GIVEN,
        call_control_ids: List[str] | NotGiven = NOT_GIVEN,
        loop: LoopcountParam | NotGiven = NOT_GIVEN,
        media_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionPlayResponse:
        """
        Play audio to all or some participants on a conference call.

        Args:
          audio_url: The URL of a file to be played back in the conference. media_name and audio_url
              cannot be used together in one request.

          call_control_ids: List of call control ids identifying participants the audio file should be
              played to. If not given, the audio file will be played to the entire conference.

          loop: The number of times the audio file should be played. If supplied, the value must
              be an integer between 1 and 100, or the special string `infinity` for an endless
              loop.

          media_name: The media_name of a file to be played back in the conference. The media_name
              must point to a file previously uploaded to api.telnyx.com/v2/media by the same
              user/organization. The file must either be a WAV or MP3 file.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/conferences/{id}/actions/play",
            body=await async_maybe_transform(
                {
                    "audio_url": audio_url,
                    "call_control_ids": call_control_ids,
                    "loop": loop,
                    "media_name": media_name,
                },
                action_play_params.ActionPlayParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionPlayResponse,
        )

    async def record_pause(
        self,
        id: str,
        *,
        command_id: str | NotGiven = NOT_GIVEN,
        recording_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionRecordPauseResponse:
        """
        Pause conference recording.

        Args:
          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          recording_id: Use this field to pause specific recording.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/conferences/{id}/actions/record_pause",
            body=await async_maybe_transform(
                {
                    "command_id": command_id,
                    "recording_id": recording_id,
                },
                action_record_pause_params.ActionRecordPauseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRecordPauseResponse,
        )

    async def record_resume(
        self,
        id: str,
        *,
        command_id: str | NotGiven = NOT_GIVEN,
        recording_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionRecordResumeResponse:
        """
        Resume conference recording.

        Args:
          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `call_control_id`.

          recording_id: Use this field to resume specific recording.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/conferences/{id}/actions/record_resume",
            body=await async_maybe_transform(
                {
                    "command_id": command_id,
                    "recording_id": recording_id,
                },
                action_record_resume_params.ActionRecordResumeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRecordResumeResponse,
        )

    async def record_start(
        self,
        id: str,
        *,
        format: Literal["wav", "mp3"],
        command_id: str | NotGiven = NOT_GIVEN,
        custom_file_name: str | NotGiven = NOT_GIVEN,
        play_beep: bool | NotGiven = NOT_GIVEN,
        trim: Literal["trim-silence"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionRecordStartResponse:
        """Start recording the conference.

        Recording will stop on conference end, or via
        the Stop Recording command.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/start-conference-recording#callbacks)
        below):**

        - `conference.recording.saved`

        Args:
          format: The audio file format used when storing the conference recording. Can be either
              `mp3` or `wav`.

          command_id: Use this field to avoid duplicate commands. Telnyx will ignore any command with
              the same `command_id` for the same `conference_id`.

          custom_file_name: The custom recording file name to be used instead of the default `call_leg_id`.
              Telnyx will still add a Unix timestamp suffix.

          play_beep: If enabled, a beep sound will be played at the start of a recording.

          trim: When set to `trim-silence`, silence will be removed from the beginning and end
              of the recording.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/conferences/{id}/actions/record_start",
            body=await async_maybe_transform(
                {
                    "format": format,
                    "command_id": command_id,
                    "custom_file_name": custom_file_name,
                    "play_beep": play_beep,
                    "trim": trim,
                },
                action_record_start_params.ActionRecordStartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRecordStartResponse,
        )

    async def record_stop(
        self,
        id: str,
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
    ) -> ActionRecordStopResponse:
        """
        Stop recording the conference.

        **Expected Webhooks (see
        [callback schema](https://developers.telnyx.com/api/call-control/stop-conference-recording#callbacks)
        below):**

        - `conference.recording.saved`

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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/conferences/{id}/actions/record_stop",
            body=await async_maybe_transform(
                {
                    "client_state": client_state,
                    "command_id": command_id,
                    "recording_id": recording_id,
                },
                action_record_stop_params.ActionRecordStopParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionRecordStopResponse,
        )

    async def speak(
        self,
        id: str,
        *,
        payload: str,
        voice: str,
        call_control_ids: List[str] | NotGiven = NOT_GIVEN,
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
        voice_settings: action_speak_params.VoiceSettings | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionSpeakResponse:
        """
        Convert text to speech and play it to all or some participants.

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

          call_control_ids: Call Control IDs of participants who will hear the spoken text. When empty all
              participants will hear the spoken text.

          command_id: Use this field to avoid execution of duplicate commands. Telnyx will ignore
              subsequent commands with the same `command_id` as one that has already been
              executed.

          language: The language you want spoken. This parameter is ignored when a `Polly.*` voice
              is specified.

          payload_type: The type of the provided payload. The payload can either be plain text, or
              Speech Synthesis Markup Language (SSML).

          voice_settings: The settings associated with the voice selected

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/conferences/{id}/actions/speak",
            body=await async_maybe_transform(
                {
                    "payload": payload,
                    "voice": voice,
                    "call_control_ids": call_control_ids,
                    "command_id": command_id,
                    "language": language,
                    "payload_type": payload_type,
                    "voice_settings": voice_settings,
                },
                action_speak_params.ActionSpeakParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionSpeakResponse,
        )

    async def stop(
        self,
        id: str,
        *,
        call_control_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionStopResponse:
        """
        Stop audio being played to all or some participants on a conference call.

        Args:
          call_control_ids: List of call control ids identifying participants the audio file should stop be
              played to. If not given, the audio will be stoped to the entire conference.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/conferences/{id}/actions/stop",
            body=await async_maybe_transform(
                {"call_control_ids": call_control_ids}, action_stop_params.ActionStopParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionStopResponse,
        )

    async def unhold(
        self,
        id: str,
        *,
        call_control_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionUnholdResponse:
        """
        Unhold a list of participants in a conference call

        Args:
          call_control_ids: List of unique identifiers and tokens for controlling the call. Enter each call
              control ID to be unheld.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/conferences/{id}/actions/unhold",
            body=await async_maybe_transform(
                {"call_control_ids": call_control_ids}, action_unhold_params.ActionUnholdParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionUnholdResponse,
        )

    async def unmute(
        self,
        id: str,
        *,
        call_control_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionUnmuteResponse:
        """
        Unmute a list of participants in a conference call

        Args:
          call_control_ids: List of unique identifiers and tokens for controlling the call. Enter each call
              control ID to be unmuted. When empty all participants will be unmuted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/conferences/{id}/actions/unmute",
            body=await async_maybe_transform(
                {"call_control_ids": call_control_ids}, action_unmute_params.ActionUnmuteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionUnmuteResponse,
        )


class ActionsResourceWithRawResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.update = to_raw_response_wrapper(
            actions.update,
        )
        self.hold = to_raw_response_wrapper(
            actions.hold,
        )
        self.join = to_raw_response_wrapper(
            actions.join,
        )
        self.leave = to_raw_response_wrapper(
            actions.leave,
        )
        self.mute = to_raw_response_wrapper(
            actions.mute,
        )
        self.play = to_raw_response_wrapper(
            actions.play,
        )
        self.record_pause = to_raw_response_wrapper(
            actions.record_pause,
        )
        self.record_resume = to_raw_response_wrapper(
            actions.record_resume,
        )
        self.record_start = to_raw_response_wrapper(
            actions.record_start,
        )
        self.record_stop = to_raw_response_wrapper(
            actions.record_stop,
        )
        self.speak = to_raw_response_wrapper(
            actions.speak,
        )
        self.stop = to_raw_response_wrapper(
            actions.stop,
        )
        self.unhold = to_raw_response_wrapper(
            actions.unhold,
        )
        self.unmute = to_raw_response_wrapper(
            actions.unmute,
        )


class AsyncActionsResourceWithRawResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.update = async_to_raw_response_wrapper(
            actions.update,
        )
        self.hold = async_to_raw_response_wrapper(
            actions.hold,
        )
        self.join = async_to_raw_response_wrapper(
            actions.join,
        )
        self.leave = async_to_raw_response_wrapper(
            actions.leave,
        )
        self.mute = async_to_raw_response_wrapper(
            actions.mute,
        )
        self.play = async_to_raw_response_wrapper(
            actions.play,
        )
        self.record_pause = async_to_raw_response_wrapper(
            actions.record_pause,
        )
        self.record_resume = async_to_raw_response_wrapper(
            actions.record_resume,
        )
        self.record_start = async_to_raw_response_wrapper(
            actions.record_start,
        )
        self.record_stop = async_to_raw_response_wrapper(
            actions.record_stop,
        )
        self.speak = async_to_raw_response_wrapper(
            actions.speak,
        )
        self.stop = async_to_raw_response_wrapper(
            actions.stop,
        )
        self.unhold = async_to_raw_response_wrapper(
            actions.unhold,
        )
        self.unmute = async_to_raw_response_wrapper(
            actions.unmute,
        )


class ActionsResourceWithStreamingResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.update = to_streamed_response_wrapper(
            actions.update,
        )
        self.hold = to_streamed_response_wrapper(
            actions.hold,
        )
        self.join = to_streamed_response_wrapper(
            actions.join,
        )
        self.leave = to_streamed_response_wrapper(
            actions.leave,
        )
        self.mute = to_streamed_response_wrapper(
            actions.mute,
        )
        self.play = to_streamed_response_wrapper(
            actions.play,
        )
        self.record_pause = to_streamed_response_wrapper(
            actions.record_pause,
        )
        self.record_resume = to_streamed_response_wrapper(
            actions.record_resume,
        )
        self.record_start = to_streamed_response_wrapper(
            actions.record_start,
        )
        self.record_stop = to_streamed_response_wrapper(
            actions.record_stop,
        )
        self.speak = to_streamed_response_wrapper(
            actions.speak,
        )
        self.stop = to_streamed_response_wrapper(
            actions.stop,
        )
        self.unhold = to_streamed_response_wrapper(
            actions.unhold,
        )
        self.unmute = to_streamed_response_wrapper(
            actions.unmute,
        )


class AsyncActionsResourceWithStreamingResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.update = async_to_streamed_response_wrapper(
            actions.update,
        )
        self.hold = async_to_streamed_response_wrapper(
            actions.hold,
        )
        self.join = async_to_streamed_response_wrapper(
            actions.join,
        )
        self.leave = async_to_streamed_response_wrapper(
            actions.leave,
        )
        self.mute = async_to_streamed_response_wrapper(
            actions.mute,
        )
        self.play = async_to_streamed_response_wrapper(
            actions.play,
        )
        self.record_pause = async_to_streamed_response_wrapper(
            actions.record_pause,
        )
        self.record_resume = async_to_streamed_response_wrapper(
            actions.record_resume,
        )
        self.record_start = async_to_streamed_response_wrapper(
            actions.record_start,
        )
        self.record_stop = async_to_streamed_response_wrapper(
            actions.record_stop,
        )
        self.speak = async_to_streamed_response_wrapper(
            actions.speak,
        )
        self.stop = async_to_streamed_response_wrapper(
            actions.stop,
        )
        self.unhold = async_to_streamed_response_wrapper(
            actions.unhold,
        )
        self.unmute = async_to_streamed_response_wrapper(
            actions.unmute,
        )

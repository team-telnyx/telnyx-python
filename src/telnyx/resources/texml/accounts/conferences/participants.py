# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from .....types.texml.accounts.conferences import participant_update_params, participant_participants_params
from .....types.texml.accounts.conferences.participant_update_response import ParticipantUpdateResponse
from .....types.texml.accounts.conferences.participant_retrieve_response import ParticipantRetrieveResponse
from .....types.texml.accounts.conferences.participant_participants_response import ParticipantParticipantsResponse
from .....types.texml.accounts.conferences.participant_retrieve_participants_response import (
    ParticipantRetrieveParticipantsResponse,
)

__all__ = ["ParticipantsResource", "AsyncParticipantsResource"]


class ParticipantsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ParticipantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ParticipantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ParticipantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ParticipantsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        call_sid_or_participant_label: str,
        *,
        account_sid: str,
        conference_sid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ParticipantRetrieveResponse:
        """
        Gets conference participant resource

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        if not conference_sid:
            raise ValueError(f"Expected a non-empty value for `conference_sid` but received {conference_sid!r}")
        if not call_sid_or_participant_label:
            raise ValueError(
                f"Expected a non-empty value for `call_sid_or_participant_label` but received {call_sid_or_participant_label!r}"
            )
        return self._get(
            f"/texml/Accounts/{account_sid}/Conferences/{conference_sid}/Participants/{call_sid_or_participant_label}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParticipantRetrieveResponse,
        )

    def update(
        self,
        call_sid_or_participant_label: str,
        *,
        account_sid: str,
        conference_sid: str,
        announce_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        announce_url: str | NotGiven = NOT_GIVEN,
        beep_on_exit: bool | NotGiven = NOT_GIVEN,
        call_sid_to_coach: str | NotGiven = NOT_GIVEN,
        coaching: bool | NotGiven = NOT_GIVEN,
        end_conference_on_exit: bool | NotGiven = NOT_GIVEN,
        hold: bool | NotGiven = NOT_GIVEN,
        hold_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        hold_url: str | NotGiven = NOT_GIVEN,
        muted: bool | NotGiven = NOT_GIVEN,
        wait_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ParticipantUpdateResponse:
        """
        Updates a conference participant

        Args:
          announce_method: The HTTP method used to call the `AnnounceUrl`. Defaults to `POST`.

          announce_url: The URL to call to announce something to the participant. The URL may return an
              MP3 fileo a WAV file, or a TwiML document that contains `<Play>`, `<Say>`,
              `<Pause>`, or `<Redirect>` verbs.

          beep_on_exit: Whether to play a notification beep to the conference when the participant
              exits.

          call_sid_to_coach: The SID of the participant who is being coached. The participant being coached
              is the only participant who can hear the participant who is coaching.

          coaching: Whether the participant is coaching another call. When `true`, `CallSidToCoach`
              has to be given.

          end_conference_on_exit: Whether to end the conference when the participant leaves.

          hold: Whether the participant should be on hold.

          hold_method: The HTTP method to use when calling the `HoldUrl`.

          hold_url: The URL to be called using the `HoldMethod` for music that plays when the
              participant is on hold. The URL may return an MP3 file, a WAV file, or a TwiML
              document that contains `<Play>`, `<Say>`, `<Pause>`, or `<Redirect>` verbs.

          muted: Whether the participant should be muted.

          wait_url: The URL to call for an audio file to play while the participant is waiting for
              the conference to start.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        if not conference_sid:
            raise ValueError(f"Expected a non-empty value for `conference_sid` but received {conference_sid!r}")
        if not call_sid_or_participant_label:
            raise ValueError(
                f"Expected a non-empty value for `call_sid_or_participant_label` but received {call_sid_or_participant_label!r}"
            )
        return self._post(
            f"/texml/Accounts/{account_sid}/Conferences/{conference_sid}/Participants/{call_sid_or_participant_label}",
            body=maybe_transform(
                {
                    "announce_method": announce_method,
                    "announce_url": announce_url,
                    "beep_on_exit": beep_on_exit,
                    "call_sid_to_coach": call_sid_to_coach,
                    "coaching": coaching,
                    "end_conference_on_exit": end_conference_on_exit,
                    "hold": hold,
                    "hold_method": hold_method,
                    "hold_url": hold_url,
                    "muted": muted,
                    "wait_url": wait_url,
                },
                participant_update_params.ParticipantUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParticipantUpdateResponse,
        )

    def delete(
        self,
        call_sid_or_participant_label: str,
        *,
        account_sid: str,
        conference_sid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes a conference participant

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        if not conference_sid:
            raise ValueError(f"Expected a non-empty value for `conference_sid` but received {conference_sid!r}")
        if not call_sid_or_participant_label:
            raise ValueError(
                f"Expected a non-empty value for `call_sid_or_participant_label` but received {call_sid_or_participant_label!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/texml/Accounts/{account_sid}/Conferences/{conference_sid}/Participants/{call_sid_or_participant_label}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def participants(
        self,
        conference_sid: str,
        *,
        account_sid: str,
        amd_status_callback: str | NotGiven = NOT_GIVEN,
        amd_status_callback_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        beep: Literal["true", "false", "onEnter", "onExit"] | NotGiven = NOT_GIVEN,
        caller_id: str | NotGiven = NOT_GIVEN,
        call_sid_to_coach: str | NotGiven = NOT_GIVEN,
        cancel_playback_on_detect_message_end: bool | NotGiven = NOT_GIVEN,
        cancel_playback_on_machine_detection: bool | NotGiven = NOT_GIVEN,
        coaching: bool | NotGiven = NOT_GIVEN,
        conference_record: Literal["true", "false", "record-from-start", "do-not-record"] | NotGiven = NOT_GIVEN,
        conference_recording_status_callback: str | NotGiven = NOT_GIVEN,
        conference_recording_status_callback_event: str | NotGiven = NOT_GIVEN,
        conference_recording_status_callback_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        conference_recording_timeout: int | NotGiven = NOT_GIVEN,
        conference_status_callback: str | NotGiven = NOT_GIVEN,
        conference_status_callback_event: str | NotGiven = NOT_GIVEN,
        conference_status_callback_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        conference_trim: Literal["trim-silence", "do-not-trim"] | NotGiven = NOT_GIVEN,
        early_media: bool | NotGiven = NOT_GIVEN,
        end_conference_on_exit: bool | NotGiven = NOT_GIVEN,
        from_: str | NotGiven = NOT_GIVEN,
        machine_detection: Literal["Enable", "DetectMessageEnd"] | NotGiven = NOT_GIVEN,
        machine_detection_silence_timeout: int | NotGiven = NOT_GIVEN,
        machine_detection_speech_end_threshold: int | NotGiven = NOT_GIVEN,
        machine_detection_speech_threshold: int | NotGiven = NOT_GIVEN,
        machine_detection_timeout: int | NotGiven = NOT_GIVEN,
        max_participants: int | NotGiven = NOT_GIVEN,
        muted: bool | NotGiven = NOT_GIVEN,
        preferred_codecs: str | NotGiven = NOT_GIVEN,
        record: bool | NotGiven = NOT_GIVEN,
        recording_channels: Literal["mono", "dual"] | NotGiven = NOT_GIVEN,
        recording_status_callback: str | NotGiven = NOT_GIVEN,
        recording_status_callback_event: str | NotGiven = NOT_GIVEN,
        recording_status_callback_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        recording_track: Literal["inbound", "outbound", "both"] | NotGiven = NOT_GIVEN,
        sip_auth_password: str | NotGiven = NOT_GIVEN,
        sip_auth_username: str | NotGiven = NOT_GIVEN,
        start_conference_on_enter: bool | NotGiven = NOT_GIVEN,
        status_callback: str | NotGiven = NOT_GIVEN,
        status_callback_event: str | NotGiven = NOT_GIVEN,
        status_callback_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        time_limit: int | NotGiven = NOT_GIVEN,
        timeout_seconds: int | NotGiven = NOT_GIVEN,
        to: str | NotGiven = NOT_GIVEN,
        trim: Literal["trim-silence", "do-not-trim"] | NotGiven = NOT_GIVEN,
        wait_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ParticipantParticipantsResponse:
        """
        Dials a new conference participant

        Args:
          amd_status_callback: The URL the result of answering machine detection will be sent to.

          amd_status_callback_method: HTTP request type used for `AmdStatusCallback`. Defaults to `POST`.

          beep: Whether to play a notification beep to the conference when the participant
              enters and exits.

          caller_id: To be used as the caller id name (SIP From Display Name) presented to the
              destination (`To` number). The string should have a maximum of 128 characters,
              containing only letters, numbers, spaces, and `-_~!.+` special characters. If
              ommited, the display name will be the same as the number in the `From` field.

          call_sid_to_coach: The SID of the participant who is being coached. The participant being coached
              is the only participant who can hear the participant who is coaching.

          cancel_playback_on_detect_message_end: Whether to cancel ongoing playback on `greeting ended` detection. Defaults to
              `true`.

          cancel_playback_on_machine_detection: Whether to cancel ongoing playback on `machine` detection. Defaults to `true`.

          coaching: Whether the participant is coaching another call. When `true`, `CallSidToCoach`
              has to be given.

          conference_record: Whether to record the conference the participant is joining. Defualts to
              `do-not-record`. The boolean values `true` and `false` are synonymous with
              `record-from-start` and `do-not-record` respectively.

          conference_recording_status_callback: The URL the conference recording callbacks will be sent to.

          conference_recording_status_callback_event: The changes to the conference recording's state that should generate a call to
              `RecoridngStatusCallback`. Can be: `in-progress`, `completed` and `absent`.
              Separate multiple values with a space. Defaults to `completed`. `failed` and
              `absent` are synonymous.

          conference_recording_status_callback_method: HTTP request type used for `ConferenceRecordingStatusCallback`. Defaults to
              `POST`.

          conference_recording_timeout: The number of seconds that Telnyx will wait for the recording to be stopped if
              silence is detected. The timer only starts when the speech is detected. Please
              note that the transcription is used to detect silence and the related charge
              will be applied. The minimum value is 0. The default value is 0 (infinite)

          conference_status_callback: The URL the conference callbacks will be sent to.

          conference_status_callback_event: The changes to the conference's state that should generate a call to
              `ConferenceStatusCallback`. Can be: `start`, `end`, `join` and `leave`. Separate
              multiple values with a space. By default no callbacks are sent.

          conference_status_callback_method: HTTP request type used for `ConferenceStatusCallback`. Defaults to `POST`.

          conference_trim: Whether to trim any leading and trailing silence from the conference recording.
              Defaults to `trim-silence`.

          early_media: Whether participant shall be bridged to conference before the participant
              answers (from early media if available). Defaults to `false`.

          end_conference_on_exit: Whether to end the conference when the participant leaves. Defaults to `false`.

          from_: The phone number of the party that initiated the call. Phone numbers are
              formatted with a `+` and country code.

          machine_detection: Whether to detect if a human or an answering machine picked up the call. Use
              `Enable` if you would like to ne notified as soon as the called party is
              identified. Use `DetectMessageEnd`, if you would like to leave a message on an
              answering machine.

          machine_detection_silence_timeout: If initial silence duration is greater than this value, consider it a machine.
              Ignored when `premium` detection is used.

          machine_detection_speech_end_threshold: Silence duration threshold after a greeting message or voice for it be
              considered human. Ignored when `premium` detection is used.

          machine_detection_speech_threshold: Maximum threshold of a human greeting. If greeting longer than this value,
              considered machine. Ignored when `premium` detection is used.

          machine_detection_timeout: How long answering machine detection should go on for before sending an
              `Unknown` result. Given in milliseconds.

          max_participants: The maximum number of participants in the conference. Can be a positive integer
              from 2 to 800. The default value is 250.

          muted: Whether the participant should be muted.

          preferred_codecs: The list of comma-separated codecs to be offered on a call.

          record: Whether to record the entire participant's call leg. Defaults to `false`.

          recording_channels: The number of channels in the final recording. Defaults to `mono`.

          recording_status_callback: The URL the recording callbacks will be sent to.

          recording_status_callback_event: The changes to the recording's state that should generate a call to
              `RecoridngStatusCallback`. Can be: `in-progress`, `completed` and `absent`.
              Separate multiple values with a space. Defaults to `completed`.

          recording_status_callback_method: HTTP request type used for `RecordingStatusCallback`. Defaults to `POST`.

          recording_track: The audio track to record for the call. The default is `both`.

          sip_auth_password: The password to use for SIP authentication.

          sip_auth_username: The username to use for SIP authentication.

          start_conference_on_enter: Whether to start the conference when the participant enters. Defaults to `true`.

          status_callback: URL destination for Telnyx to send status callback events to for the call.

          status_callback_event: The changes to the call's state that should generate a call to `StatusCallback`.
              Can be: `initiated`, `ringing`, `answered`, and `completed`. Separate multiple
              values with a space. The default value is `completed`.

          status_callback_method: HTTP request type used for `StatusCallback`.

          time_limit: The maximum duration of the call in seconds.

          timeout_seconds: The number of seconds that we should allow the phone to ring before assuming
              there is no answer. Can be an integer between 5 and 120, inclusive. The default
              value is 30.

          to: The phone number of the called party. Phone numbers are formatted with a `+` and
              country code.

          trim: Whether to trim any leading and trailing silence from the recording. Defaults to
              `trim-silence`.

          wait_url: The URL to call for an audio file to play while the participant is waiting for
              the conference to start.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        if not conference_sid:
            raise ValueError(f"Expected a non-empty value for `conference_sid` but received {conference_sid!r}")
        return self._post(
            f"/texml/Accounts/{account_sid}/Conferences/{conference_sid}/Participants",
            body=maybe_transform(
                {
                    "amd_status_callback": amd_status_callback,
                    "amd_status_callback_method": amd_status_callback_method,
                    "beep": beep,
                    "caller_id": caller_id,
                    "call_sid_to_coach": call_sid_to_coach,
                    "cancel_playback_on_detect_message_end": cancel_playback_on_detect_message_end,
                    "cancel_playback_on_machine_detection": cancel_playback_on_machine_detection,
                    "coaching": coaching,
                    "conference_record": conference_record,
                    "conference_recording_status_callback": conference_recording_status_callback,
                    "conference_recording_status_callback_event": conference_recording_status_callback_event,
                    "conference_recording_status_callback_method": conference_recording_status_callback_method,
                    "conference_recording_timeout": conference_recording_timeout,
                    "conference_status_callback": conference_status_callback,
                    "conference_status_callback_event": conference_status_callback_event,
                    "conference_status_callback_method": conference_status_callback_method,
                    "conference_trim": conference_trim,
                    "early_media": early_media,
                    "end_conference_on_exit": end_conference_on_exit,
                    "from_": from_,
                    "machine_detection": machine_detection,
                    "machine_detection_silence_timeout": machine_detection_silence_timeout,
                    "machine_detection_speech_end_threshold": machine_detection_speech_end_threshold,
                    "machine_detection_speech_threshold": machine_detection_speech_threshold,
                    "machine_detection_timeout": machine_detection_timeout,
                    "max_participants": max_participants,
                    "muted": muted,
                    "preferred_codecs": preferred_codecs,
                    "record": record,
                    "recording_channels": recording_channels,
                    "recording_status_callback": recording_status_callback,
                    "recording_status_callback_event": recording_status_callback_event,
                    "recording_status_callback_method": recording_status_callback_method,
                    "recording_track": recording_track,
                    "sip_auth_password": sip_auth_password,
                    "sip_auth_username": sip_auth_username,
                    "start_conference_on_enter": start_conference_on_enter,
                    "status_callback": status_callback,
                    "status_callback_event": status_callback_event,
                    "status_callback_method": status_callback_method,
                    "time_limit": time_limit,
                    "timeout_seconds": timeout_seconds,
                    "to": to,
                    "trim": trim,
                    "wait_url": wait_url,
                },
                participant_participants_params.ParticipantParticipantsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParticipantParticipantsResponse,
        )

    def retrieve_participants(
        self,
        conference_sid: str,
        *,
        account_sid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ParticipantRetrieveParticipantsResponse:
        """
        Lists conference participants

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        if not conference_sid:
            raise ValueError(f"Expected a non-empty value for `conference_sid` but received {conference_sid!r}")
        return self._get(
            f"/texml/Accounts/{account_sid}/Conferences/{conference_sid}/Participants",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParticipantRetrieveParticipantsResponse,
        )


class AsyncParticipantsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncParticipantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncParticipantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncParticipantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncParticipantsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        call_sid_or_participant_label: str,
        *,
        account_sid: str,
        conference_sid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ParticipantRetrieveResponse:
        """
        Gets conference participant resource

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        if not conference_sid:
            raise ValueError(f"Expected a non-empty value for `conference_sid` but received {conference_sid!r}")
        if not call_sid_or_participant_label:
            raise ValueError(
                f"Expected a non-empty value for `call_sid_or_participant_label` but received {call_sid_or_participant_label!r}"
            )
        return await self._get(
            f"/texml/Accounts/{account_sid}/Conferences/{conference_sid}/Participants/{call_sid_or_participant_label}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParticipantRetrieveResponse,
        )

    async def update(
        self,
        call_sid_or_participant_label: str,
        *,
        account_sid: str,
        conference_sid: str,
        announce_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        announce_url: str | NotGiven = NOT_GIVEN,
        beep_on_exit: bool | NotGiven = NOT_GIVEN,
        call_sid_to_coach: str | NotGiven = NOT_GIVEN,
        coaching: bool | NotGiven = NOT_GIVEN,
        end_conference_on_exit: bool | NotGiven = NOT_GIVEN,
        hold: bool | NotGiven = NOT_GIVEN,
        hold_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        hold_url: str | NotGiven = NOT_GIVEN,
        muted: bool | NotGiven = NOT_GIVEN,
        wait_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ParticipantUpdateResponse:
        """
        Updates a conference participant

        Args:
          announce_method: The HTTP method used to call the `AnnounceUrl`. Defaults to `POST`.

          announce_url: The URL to call to announce something to the participant. The URL may return an
              MP3 fileo a WAV file, or a TwiML document that contains `<Play>`, `<Say>`,
              `<Pause>`, or `<Redirect>` verbs.

          beep_on_exit: Whether to play a notification beep to the conference when the participant
              exits.

          call_sid_to_coach: The SID of the participant who is being coached. The participant being coached
              is the only participant who can hear the participant who is coaching.

          coaching: Whether the participant is coaching another call. When `true`, `CallSidToCoach`
              has to be given.

          end_conference_on_exit: Whether to end the conference when the participant leaves.

          hold: Whether the participant should be on hold.

          hold_method: The HTTP method to use when calling the `HoldUrl`.

          hold_url: The URL to be called using the `HoldMethod` for music that plays when the
              participant is on hold. The URL may return an MP3 file, a WAV file, or a TwiML
              document that contains `<Play>`, `<Say>`, `<Pause>`, or `<Redirect>` verbs.

          muted: Whether the participant should be muted.

          wait_url: The URL to call for an audio file to play while the participant is waiting for
              the conference to start.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        if not conference_sid:
            raise ValueError(f"Expected a non-empty value for `conference_sid` but received {conference_sid!r}")
        if not call_sid_or_participant_label:
            raise ValueError(
                f"Expected a non-empty value for `call_sid_or_participant_label` but received {call_sid_or_participant_label!r}"
            )
        return await self._post(
            f"/texml/Accounts/{account_sid}/Conferences/{conference_sid}/Participants/{call_sid_or_participant_label}",
            body=await async_maybe_transform(
                {
                    "announce_method": announce_method,
                    "announce_url": announce_url,
                    "beep_on_exit": beep_on_exit,
                    "call_sid_to_coach": call_sid_to_coach,
                    "coaching": coaching,
                    "end_conference_on_exit": end_conference_on_exit,
                    "hold": hold,
                    "hold_method": hold_method,
                    "hold_url": hold_url,
                    "muted": muted,
                    "wait_url": wait_url,
                },
                participant_update_params.ParticipantUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParticipantUpdateResponse,
        )

    async def delete(
        self,
        call_sid_or_participant_label: str,
        *,
        account_sid: str,
        conference_sid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes a conference participant

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        if not conference_sid:
            raise ValueError(f"Expected a non-empty value for `conference_sid` but received {conference_sid!r}")
        if not call_sid_or_participant_label:
            raise ValueError(
                f"Expected a non-empty value for `call_sid_or_participant_label` but received {call_sid_or_participant_label!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/texml/Accounts/{account_sid}/Conferences/{conference_sid}/Participants/{call_sid_or_participant_label}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def participants(
        self,
        conference_sid: str,
        *,
        account_sid: str,
        amd_status_callback: str | NotGiven = NOT_GIVEN,
        amd_status_callback_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        beep: Literal["true", "false", "onEnter", "onExit"] | NotGiven = NOT_GIVEN,
        caller_id: str | NotGiven = NOT_GIVEN,
        call_sid_to_coach: str | NotGiven = NOT_GIVEN,
        cancel_playback_on_detect_message_end: bool | NotGiven = NOT_GIVEN,
        cancel_playback_on_machine_detection: bool | NotGiven = NOT_GIVEN,
        coaching: bool | NotGiven = NOT_GIVEN,
        conference_record: Literal["true", "false", "record-from-start", "do-not-record"] | NotGiven = NOT_GIVEN,
        conference_recording_status_callback: str | NotGiven = NOT_GIVEN,
        conference_recording_status_callback_event: str | NotGiven = NOT_GIVEN,
        conference_recording_status_callback_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        conference_recording_timeout: int | NotGiven = NOT_GIVEN,
        conference_status_callback: str | NotGiven = NOT_GIVEN,
        conference_status_callback_event: str | NotGiven = NOT_GIVEN,
        conference_status_callback_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        conference_trim: Literal["trim-silence", "do-not-trim"] | NotGiven = NOT_GIVEN,
        early_media: bool | NotGiven = NOT_GIVEN,
        end_conference_on_exit: bool | NotGiven = NOT_GIVEN,
        from_: str | NotGiven = NOT_GIVEN,
        machine_detection: Literal["Enable", "DetectMessageEnd"] | NotGiven = NOT_GIVEN,
        machine_detection_silence_timeout: int | NotGiven = NOT_GIVEN,
        machine_detection_speech_end_threshold: int | NotGiven = NOT_GIVEN,
        machine_detection_speech_threshold: int | NotGiven = NOT_GIVEN,
        machine_detection_timeout: int | NotGiven = NOT_GIVEN,
        max_participants: int | NotGiven = NOT_GIVEN,
        muted: bool | NotGiven = NOT_GIVEN,
        preferred_codecs: str | NotGiven = NOT_GIVEN,
        record: bool | NotGiven = NOT_GIVEN,
        recording_channels: Literal["mono", "dual"] | NotGiven = NOT_GIVEN,
        recording_status_callback: str | NotGiven = NOT_GIVEN,
        recording_status_callback_event: str | NotGiven = NOT_GIVEN,
        recording_status_callback_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        recording_track: Literal["inbound", "outbound", "both"] | NotGiven = NOT_GIVEN,
        sip_auth_password: str | NotGiven = NOT_GIVEN,
        sip_auth_username: str | NotGiven = NOT_GIVEN,
        start_conference_on_enter: bool | NotGiven = NOT_GIVEN,
        status_callback: str | NotGiven = NOT_GIVEN,
        status_callback_event: str | NotGiven = NOT_GIVEN,
        status_callback_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        time_limit: int | NotGiven = NOT_GIVEN,
        timeout_seconds: int | NotGiven = NOT_GIVEN,
        to: str | NotGiven = NOT_GIVEN,
        trim: Literal["trim-silence", "do-not-trim"] | NotGiven = NOT_GIVEN,
        wait_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ParticipantParticipantsResponse:
        """
        Dials a new conference participant

        Args:
          amd_status_callback: The URL the result of answering machine detection will be sent to.

          amd_status_callback_method: HTTP request type used for `AmdStatusCallback`. Defaults to `POST`.

          beep: Whether to play a notification beep to the conference when the participant
              enters and exits.

          caller_id: To be used as the caller id name (SIP From Display Name) presented to the
              destination (`To` number). The string should have a maximum of 128 characters,
              containing only letters, numbers, spaces, and `-_~!.+` special characters. If
              ommited, the display name will be the same as the number in the `From` field.

          call_sid_to_coach: The SID of the participant who is being coached. The participant being coached
              is the only participant who can hear the participant who is coaching.

          cancel_playback_on_detect_message_end: Whether to cancel ongoing playback on `greeting ended` detection. Defaults to
              `true`.

          cancel_playback_on_machine_detection: Whether to cancel ongoing playback on `machine` detection. Defaults to `true`.

          coaching: Whether the participant is coaching another call. When `true`, `CallSidToCoach`
              has to be given.

          conference_record: Whether to record the conference the participant is joining. Defualts to
              `do-not-record`. The boolean values `true` and `false` are synonymous with
              `record-from-start` and `do-not-record` respectively.

          conference_recording_status_callback: The URL the conference recording callbacks will be sent to.

          conference_recording_status_callback_event: The changes to the conference recording's state that should generate a call to
              `RecoridngStatusCallback`. Can be: `in-progress`, `completed` and `absent`.
              Separate multiple values with a space. Defaults to `completed`. `failed` and
              `absent` are synonymous.

          conference_recording_status_callback_method: HTTP request type used for `ConferenceRecordingStatusCallback`. Defaults to
              `POST`.

          conference_recording_timeout: The number of seconds that Telnyx will wait for the recording to be stopped if
              silence is detected. The timer only starts when the speech is detected. Please
              note that the transcription is used to detect silence and the related charge
              will be applied. The minimum value is 0. The default value is 0 (infinite)

          conference_status_callback: The URL the conference callbacks will be sent to.

          conference_status_callback_event: The changes to the conference's state that should generate a call to
              `ConferenceStatusCallback`. Can be: `start`, `end`, `join` and `leave`. Separate
              multiple values with a space. By default no callbacks are sent.

          conference_status_callback_method: HTTP request type used for `ConferenceStatusCallback`. Defaults to `POST`.

          conference_trim: Whether to trim any leading and trailing silence from the conference recording.
              Defaults to `trim-silence`.

          early_media: Whether participant shall be bridged to conference before the participant
              answers (from early media if available). Defaults to `false`.

          end_conference_on_exit: Whether to end the conference when the participant leaves. Defaults to `false`.

          from_: The phone number of the party that initiated the call. Phone numbers are
              formatted with a `+` and country code.

          machine_detection: Whether to detect if a human or an answering machine picked up the call. Use
              `Enable` if you would like to ne notified as soon as the called party is
              identified. Use `DetectMessageEnd`, if you would like to leave a message on an
              answering machine.

          machine_detection_silence_timeout: If initial silence duration is greater than this value, consider it a machine.
              Ignored when `premium` detection is used.

          machine_detection_speech_end_threshold: Silence duration threshold after a greeting message or voice for it be
              considered human. Ignored when `premium` detection is used.

          machine_detection_speech_threshold: Maximum threshold of a human greeting. If greeting longer than this value,
              considered machine. Ignored when `premium` detection is used.

          machine_detection_timeout: How long answering machine detection should go on for before sending an
              `Unknown` result. Given in milliseconds.

          max_participants: The maximum number of participants in the conference. Can be a positive integer
              from 2 to 800. The default value is 250.

          muted: Whether the participant should be muted.

          preferred_codecs: The list of comma-separated codecs to be offered on a call.

          record: Whether to record the entire participant's call leg. Defaults to `false`.

          recording_channels: The number of channels in the final recording. Defaults to `mono`.

          recording_status_callback: The URL the recording callbacks will be sent to.

          recording_status_callback_event: The changes to the recording's state that should generate a call to
              `RecoridngStatusCallback`. Can be: `in-progress`, `completed` and `absent`.
              Separate multiple values with a space. Defaults to `completed`.

          recording_status_callback_method: HTTP request type used for `RecordingStatusCallback`. Defaults to `POST`.

          recording_track: The audio track to record for the call. The default is `both`.

          sip_auth_password: The password to use for SIP authentication.

          sip_auth_username: The username to use for SIP authentication.

          start_conference_on_enter: Whether to start the conference when the participant enters. Defaults to `true`.

          status_callback: URL destination for Telnyx to send status callback events to for the call.

          status_callback_event: The changes to the call's state that should generate a call to `StatusCallback`.
              Can be: `initiated`, `ringing`, `answered`, and `completed`. Separate multiple
              values with a space. The default value is `completed`.

          status_callback_method: HTTP request type used for `StatusCallback`.

          time_limit: The maximum duration of the call in seconds.

          timeout_seconds: The number of seconds that we should allow the phone to ring before assuming
              there is no answer. Can be an integer between 5 and 120, inclusive. The default
              value is 30.

          to: The phone number of the called party. Phone numbers are formatted with a `+` and
              country code.

          trim: Whether to trim any leading and trailing silence from the recording. Defaults to
              `trim-silence`.

          wait_url: The URL to call for an audio file to play while the participant is waiting for
              the conference to start.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        if not conference_sid:
            raise ValueError(f"Expected a non-empty value for `conference_sid` but received {conference_sid!r}")
        return await self._post(
            f"/texml/Accounts/{account_sid}/Conferences/{conference_sid}/Participants",
            body=await async_maybe_transform(
                {
                    "amd_status_callback": amd_status_callback,
                    "amd_status_callback_method": amd_status_callback_method,
                    "beep": beep,
                    "caller_id": caller_id,
                    "call_sid_to_coach": call_sid_to_coach,
                    "cancel_playback_on_detect_message_end": cancel_playback_on_detect_message_end,
                    "cancel_playback_on_machine_detection": cancel_playback_on_machine_detection,
                    "coaching": coaching,
                    "conference_record": conference_record,
                    "conference_recording_status_callback": conference_recording_status_callback,
                    "conference_recording_status_callback_event": conference_recording_status_callback_event,
                    "conference_recording_status_callback_method": conference_recording_status_callback_method,
                    "conference_recording_timeout": conference_recording_timeout,
                    "conference_status_callback": conference_status_callback,
                    "conference_status_callback_event": conference_status_callback_event,
                    "conference_status_callback_method": conference_status_callback_method,
                    "conference_trim": conference_trim,
                    "early_media": early_media,
                    "end_conference_on_exit": end_conference_on_exit,
                    "from_": from_,
                    "machine_detection": machine_detection,
                    "machine_detection_silence_timeout": machine_detection_silence_timeout,
                    "machine_detection_speech_end_threshold": machine_detection_speech_end_threshold,
                    "machine_detection_speech_threshold": machine_detection_speech_threshold,
                    "machine_detection_timeout": machine_detection_timeout,
                    "max_participants": max_participants,
                    "muted": muted,
                    "preferred_codecs": preferred_codecs,
                    "record": record,
                    "recording_channels": recording_channels,
                    "recording_status_callback": recording_status_callback,
                    "recording_status_callback_event": recording_status_callback_event,
                    "recording_status_callback_method": recording_status_callback_method,
                    "recording_track": recording_track,
                    "sip_auth_password": sip_auth_password,
                    "sip_auth_username": sip_auth_username,
                    "start_conference_on_enter": start_conference_on_enter,
                    "status_callback": status_callback,
                    "status_callback_event": status_callback_event,
                    "status_callback_method": status_callback_method,
                    "time_limit": time_limit,
                    "timeout_seconds": timeout_seconds,
                    "to": to,
                    "trim": trim,
                    "wait_url": wait_url,
                },
                participant_participants_params.ParticipantParticipantsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParticipantParticipantsResponse,
        )

    async def retrieve_participants(
        self,
        conference_sid: str,
        *,
        account_sid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ParticipantRetrieveParticipantsResponse:
        """
        Lists conference participants

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        if not conference_sid:
            raise ValueError(f"Expected a non-empty value for `conference_sid` but received {conference_sid!r}")
        return await self._get(
            f"/texml/Accounts/{account_sid}/Conferences/{conference_sid}/Participants",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParticipantRetrieveParticipantsResponse,
        )


class ParticipantsResourceWithRawResponse:
    def __init__(self, participants: ParticipantsResource) -> None:
        self._participants = participants

        self.retrieve = to_raw_response_wrapper(
            participants.retrieve,
        )
        self.update = to_raw_response_wrapper(
            participants.update,
        )
        self.delete = to_raw_response_wrapper(
            participants.delete,
        )
        self.participants = to_raw_response_wrapper(
            participants.participants,
        )
        self.retrieve_participants = to_raw_response_wrapper(
            participants.retrieve_participants,
        )


class AsyncParticipantsResourceWithRawResponse:
    def __init__(self, participants: AsyncParticipantsResource) -> None:
        self._participants = participants

        self.retrieve = async_to_raw_response_wrapper(
            participants.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            participants.update,
        )
        self.delete = async_to_raw_response_wrapper(
            participants.delete,
        )
        self.participants = async_to_raw_response_wrapper(
            participants.participants,
        )
        self.retrieve_participants = async_to_raw_response_wrapper(
            participants.retrieve_participants,
        )


class ParticipantsResourceWithStreamingResponse:
    def __init__(self, participants: ParticipantsResource) -> None:
        self._participants = participants

        self.retrieve = to_streamed_response_wrapper(
            participants.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            participants.update,
        )
        self.delete = to_streamed_response_wrapper(
            participants.delete,
        )
        self.participants = to_streamed_response_wrapper(
            participants.participants,
        )
        self.retrieve_participants = to_streamed_response_wrapper(
            participants.retrieve_participants,
        )


class AsyncParticipantsResourceWithStreamingResponse:
    def __init__(self, participants: AsyncParticipantsResource) -> None:
        self._participants = participants

        self.retrieve = async_to_streamed_response_wrapper(
            participants.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            participants.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            participants.delete,
        )
        self.participants = async_to_streamed_response_wrapper(
            participants.participants,
        )
        self.retrieve_participants = async_to_streamed_response_wrapper(
            participants.retrieve_participants,
        )

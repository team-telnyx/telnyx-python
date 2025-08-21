# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ParticipantParticipantsParams"]


class ParticipantParticipantsParams(TypedDict, total=False):
    account_sid: Required[str]

    amd_status_callback: Annotated[str, PropertyInfo(alias="AmdStatusCallback")]
    """The URL the result of answering machine detection will be sent to."""

    amd_status_callback_method: Annotated[Literal["GET", "POST"], PropertyInfo(alias="AmdStatusCallbackMethod")]
    """HTTP request type used for `AmdStatusCallback`. Defaults to `POST`."""

    beep: Annotated[Literal["true", "false", "onEnter", "onExit"], PropertyInfo(alias="Beep")]
    """
    Whether to play a notification beep to the conference when the participant
    enters and exits.
    """

    caller_id: Annotated[str, PropertyInfo(alias="CallerId")]
    """
    To be used as the caller id name (SIP From Display Name) presented to the
    destination (`To` number). The string should have a maximum of 128 characters,
    containing only letters, numbers, spaces, and `-_~!.+` special characters. If
    ommited, the display name will be the same as the number in the `From` field.
    """

    call_sid_to_coach: Annotated[str, PropertyInfo(alias="CallSidToCoach")]
    """The SID of the participant who is being coached.

    The participant being coached is the only participant who can hear the
    participant who is coaching.
    """

    cancel_playback_on_detect_message_end: Annotated[bool, PropertyInfo(alias="CancelPlaybackOnDetectMessageEnd")]
    """Whether to cancel ongoing playback on `greeting ended` detection.

    Defaults to `true`.
    """

    cancel_playback_on_machine_detection: Annotated[bool, PropertyInfo(alias="CancelPlaybackOnMachineDetection")]
    """Whether to cancel ongoing playback on `machine` detection. Defaults to `true`."""

    coaching: Annotated[bool, PropertyInfo(alias="Coaching")]
    """Whether the participant is coaching another call.

    When `true`, `CallSidToCoach` has to be given.
    """

    conference_record: Annotated[
        Literal["true", "false", "record-from-start", "do-not-record"], PropertyInfo(alias="ConferenceRecord")
    ]
    """Whether to record the conference the participant is joining.

    Defualts to `do-not-record`. The boolean values `true` and `false` are
    synonymous with `record-from-start` and `do-not-record` respectively.
    """

    conference_recording_status_callback: Annotated[str, PropertyInfo(alias="ConferenceRecordingStatusCallback")]
    """The URL the conference recording callbacks will be sent to."""

    conference_recording_status_callback_event: Annotated[
        str, PropertyInfo(alias="ConferenceRecordingStatusCallbackEvent")
    ]
    """
    The changes to the conference recording's state that should generate a call to
    `RecoridngStatusCallback`. Can be: `in-progress`, `completed` and `absent`.
    Separate multiple values with a space. Defaults to `completed`. `failed` and
    `absent` are synonymous.
    """

    conference_recording_status_callback_method: Annotated[
        Literal["GET", "POST"], PropertyInfo(alias="ConferenceRecordingStatusCallbackMethod")
    ]
    """HTTP request type used for `ConferenceRecordingStatusCallback`.

    Defaults to `POST`.
    """

    conference_recording_timeout: Annotated[int, PropertyInfo(alias="ConferenceRecordingTimeout")]
    """
    The number of seconds that Telnyx will wait for the recording to be stopped if
    silence is detected. The timer only starts when the speech is detected. Please
    note that the transcription is used to detect silence and the related charge
    will be applied. The minimum value is 0. The default value is 0 (infinite)
    """

    conference_status_callback: Annotated[str, PropertyInfo(alias="ConferenceStatusCallback")]
    """The URL the conference callbacks will be sent to."""

    conference_status_callback_event: Annotated[str, PropertyInfo(alias="ConferenceStatusCallbackEvent")]
    """
    The changes to the conference's state that should generate a call to
    `ConferenceStatusCallback`. Can be: `start`, `end`, `join` and `leave`. Separate
    multiple values with a space. By default no callbacks are sent.
    """

    conference_status_callback_method: Annotated[
        Literal["GET", "POST"], PropertyInfo(alias="ConferenceStatusCallbackMethod")
    ]
    """HTTP request type used for `ConferenceStatusCallback`. Defaults to `POST`."""

    conference_trim: Annotated[Literal["trim-silence", "do-not-trim"], PropertyInfo(alias="ConferenceTrim")]
    """Whether to trim any leading and trailing silence from the conference recording.

    Defaults to `trim-silence`.
    """

    early_media: Annotated[bool, PropertyInfo(alias="EarlyMedia")]
    """
    Whether participant shall be bridged to conference before the participant
    answers (from early media if available). Defaults to `false`.
    """

    end_conference_on_exit: Annotated[bool, PropertyInfo(alias="EndConferenceOnExit")]
    """Whether to end the conference when the participant leaves. Defaults to `false`."""

    from_: Annotated[str, PropertyInfo(alias="From")]
    """The phone number of the party that initiated the call.

    Phone numbers are formatted with a `+` and country code.
    """

    machine_detection: Annotated[Literal["Enable", "DetectMessageEnd"], PropertyInfo(alias="MachineDetection")]
    """Whether to detect if a human or an answering machine picked up the call.

    Use `Enable` if you would like to ne notified as soon as the called party is
    identified. Use `DetectMessageEnd`, if you would like to leave a message on an
    answering machine.
    """

    machine_detection_silence_timeout: Annotated[int, PropertyInfo(alias="MachineDetectionSilenceTimeout")]
    """If initial silence duration is greater than this value, consider it a machine.

    Ignored when `premium` detection is used.
    """

    machine_detection_speech_end_threshold: Annotated[int, PropertyInfo(alias="MachineDetectionSpeechEndThreshold")]
    """
    Silence duration threshold after a greeting message or voice for it be
    considered human. Ignored when `premium` detection is used.
    """

    machine_detection_speech_threshold: Annotated[int, PropertyInfo(alias="MachineDetectionSpeechThreshold")]
    """Maximum threshold of a human greeting.

    If greeting longer than this value, considered machine. Ignored when `premium`
    detection is used.
    """

    machine_detection_timeout: Annotated[int, PropertyInfo(alias="MachineDetectionTimeout")]
    """
    How long answering machine detection should go on for before sending an
    `Unknown` result. Given in milliseconds.
    """

    max_participants: Annotated[int, PropertyInfo(alias="MaxParticipants")]
    """The maximum number of participants in the conference.

    Can be a positive integer from 2 to 800. The default value is 250.
    """

    muted: Annotated[bool, PropertyInfo(alias="Muted")]
    """Whether the participant should be muted."""

    preferred_codecs: Annotated[str, PropertyInfo(alias="PreferredCodecs")]
    """The list of comma-separated codecs to be offered on a call."""

    record: Annotated[bool, PropertyInfo(alias="Record")]
    """Whether to record the entire participant's call leg. Defaults to `false`."""

    recording_channels: Annotated[Literal["mono", "dual"], PropertyInfo(alias="RecordingChannels")]
    """The number of channels in the final recording. Defaults to `mono`."""

    recording_status_callback: Annotated[str, PropertyInfo(alias="RecordingStatusCallback")]
    """The URL the recording callbacks will be sent to."""

    recording_status_callback_event: Annotated[str, PropertyInfo(alias="RecordingStatusCallbackEvent")]
    """
    The changes to the recording's state that should generate a call to
    `RecoridngStatusCallback`. Can be: `in-progress`, `completed` and `absent`.
    Separate multiple values with a space. Defaults to `completed`.
    """

    recording_status_callback_method: Annotated[
        Literal["GET", "POST"], PropertyInfo(alias="RecordingStatusCallbackMethod")
    ]
    """HTTP request type used for `RecordingStatusCallback`. Defaults to `POST`."""

    recording_track: Annotated[Literal["inbound", "outbound", "both"], PropertyInfo(alias="RecordingTrack")]
    """The audio track to record for the call. The default is `both`."""

    sip_auth_password: Annotated[str, PropertyInfo(alias="SipAuthPassword")]
    """The password to use for SIP authentication."""

    sip_auth_username: Annotated[str, PropertyInfo(alias="SipAuthUsername")]
    """The username to use for SIP authentication."""

    start_conference_on_enter: Annotated[bool, PropertyInfo(alias="StartConferenceOnEnter")]
    """Whether to start the conference when the participant enters.

    Defaults to `true`.
    """

    status_callback: Annotated[str, PropertyInfo(alias="StatusCallback")]
    """URL destination for Telnyx to send status callback events to for the call."""

    status_callback_event: Annotated[str, PropertyInfo(alias="StatusCallbackEvent")]
    """The changes to the call's state that should generate a call to `StatusCallback`.

    Can be: `initiated`, `ringing`, `answered`, and `completed`. Separate multiple
    values with a space. The default value is `completed`.
    """

    status_callback_method: Annotated[Literal["GET", "POST"], PropertyInfo(alias="StatusCallbackMethod")]
    """HTTP request type used for `StatusCallback`."""

    time_limit: Annotated[int, PropertyInfo(alias="TimeLimit")]
    """The maximum duration of the call in seconds."""

    timeout_seconds: Annotated[int, PropertyInfo(alias="Timeout")]
    """
    The number of seconds that we should allow the phone to ring before assuming
    there is no answer. Can be an integer between 5 and 120, inclusive. The default
    value is 30.
    """

    to: Annotated[str, PropertyInfo(alias="To")]
    """The phone number of the called party.

    Phone numbers are formatted with a `+` and country code.
    """

    trim: Annotated[Literal["trim-silence", "do-not-trim"], PropertyInfo(alias="Trim")]
    """Whether to trim any leading and trailing silence from the recording.

    Defaults to `trim-silence`.
    """

    wait_url: Annotated[str, PropertyInfo(alias="WaitUrl")]
    """
    The URL to call for an audio file to play while the participant is waiting for
    the conference to start.
    """

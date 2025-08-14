# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CallCallsParams"]


class CallCallsParams(TypedDict, total=False):
    application_sid: Required[Annotated[str, PropertyInfo(alias="ApplicationSid")]]
    """The ID of the TeXML Application."""

    from_: Required[Annotated[str, PropertyInfo(alias="From")]]
    """The phone number of the party that initiated the call.

    Phone numbers are formatted with a `+` and country code.
    """

    to: Required[Annotated[str, PropertyInfo(alias="To")]]
    """The phone number of the called party.

    Phone numbers are formatted with a `+` and country code.
    """

    async_amd: Annotated[bool, PropertyInfo(alias="AsyncAmd")]
    """Select whether to perform answering machine detection in the background.

    By default execution is blocked until Answering Machine Detection is completed.
    """

    async_amd_status_callback: Annotated[str, PropertyInfo(alias="AsyncAmdStatusCallback")]
    """URL destination for Telnyx to send AMD callback events to for the call."""

    async_amd_status_callback_method: Annotated[
        Literal["GET", "POST"], PropertyInfo(alias="AsyncAmdStatusCallbackMethod")
    ]
    """HTTP request type used for `AsyncAmdStatusCallback`.

    The default value is inherited from TeXML Application setting.
    """

    caller_id: Annotated[str, PropertyInfo(alias="CallerId")]
    """
    To be used as the caller id name (SIP From Display Name) presented to the
    destination (`To` number). The string should have a maximum of 128 characters,
    containing only letters, numbers, spaces, and `-_~!.+` special characters. If
    ommited, the display name will be the same as the number in the `From` field.
    """

    cancel_playback_on_detect_message_end: Annotated[bool, PropertyInfo(alias="CancelPlaybackOnDetectMessageEnd")]
    """Whether to cancel ongoing playback on `greeting ended` detection.

    Defaults to `true`.
    """

    cancel_playback_on_machine_detection: Annotated[bool, PropertyInfo(alias="CancelPlaybackOnMachineDetection")]
    """Whether to cancel ongoing playback on `machine` detection. Defaults to `true`."""

    detection_mode: Annotated[Literal["Premium", "Regular"], PropertyInfo(alias="DetectionMode")]
    """Allows you to chose between Premium and Standard detections."""

    fallback_url: Annotated[str, PropertyInfo(alias="FallbackUrl")]
    """
    A failover URL for which Telnyx will retrieve the TeXML call instructions if the
    `Url` is not responding.
    """

    machine_detection: Annotated[
        Literal["Enable", "Disable", "DetectMessageEnd"], PropertyInfo(alias="MachineDetection")
    ]
    """Enables Answering Machine Detection."""

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
    """Maximum timeout threshold in milliseconds for overall detection."""

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

    recording_timeout: Annotated[int, PropertyInfo(alias="RecordingTimeout")]
    """
    The number of seconds that Telnyx will wait for the recording to be stopped if
    silence is detected. The timer only starts when the speech is detected. Please
    note that the transcription is used to detect silence and the related charge
    will be applied. The minimum value is 0. The default value is 0 (infinite)
    """

    recording_track: Annotated[Literal["inbound", "outbound", "both"], PropertyInfo(alias="RecordingTrack")]
    """The audio track to record for the call. The default is `both`."""

    send_recording_url: Annotated[bool, PropertyInfo(alias="SendRecordingUrl")]
    """Whether to send RecordingUrl in webhooks."""

    sip_auth_password: Annotated[str, PropertyInfo(alias="SipAuthPassword")]
    """The password to use for SIP authentication."""

    sip_auth_username: Annotated[str, PropertyInfo(alias="SipAuthUsername")]
    """The username to use for SIP authentication."""

    status_callback: Annotated[str, PropertyInfo(alias="StatusCallback")]
    """URL destination for Telnyx to send status callback events to for the call."""

    status_callback_event: Annotated[
        Literal["initiated", "ringing", "answered", "completed"], PropertyInfo(alias="StatusCallbackEvent")
    ]
    """The call events for which Telnyx should send a webhook.

    Multiple events can be defined when separated by a space.
    """

    status_callback_method: Annotated[Literal["GET", "POST"], PropertyInfo(alias="StatusCallbackMethod")]
    """HTTP request type used for `StatusCallback`."""

    trim: Annotated[Literal["trim-silence", "do-not-trim"], PropertyInfo(alias="Trim")]
    """Whether to trim any leading and trailing silence from the recording.

    Defaults to `trim-silence`.
    """

    url: Annotated[str, PropertyInfo(alias="Url")]
    """The URL from which Telnyx will retrieve the TeXML call instructions."""

    url_method: Annotated[Literal["GET", "POST"], PropertyInfo(alias="UrlMethod")]
    """HTTP request type used for `Url`.

    The default value is inherited from TeXML Application setting.
    """

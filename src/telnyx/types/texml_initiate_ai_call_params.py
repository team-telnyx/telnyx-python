# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["TexmlInitiateAICallParams", "CustomHeader"]


class TexmlInitiateAICallParams(TypedDict, total=False):
    ai_assistant_id: Required[Annotated[str, PropertyInfo(alias="AIAssistantId")]]
    """The ID of the AI assistant to use for the call."""

    from_: Required[Annotated[str, PropertyInfo(alias="From")]]
    """The phone number of the party initiating the call.

    Phone numbers are formatted with a `+` and country code.
    """

    to: Required[Annotated[str, PropertyInfo(alias="To")]]
    """The phone number of the called party.

    Phone numbers are formatted with a `+` and country code.
    """

    ai_assistant_dynamic_variables: Annotated[Dict[str, str], PropertyInfo(alias="AIAssistantDynamicVariables")]
    """Key-value map of dynamic variables to pass to the AI assistant."""

    ai_assistant_version: Annotated[str, PropertyInfo(alias="AIAssistantVersion")]
    """The version of the AI assistant to use."""

    async_amd: Annotated[bool, PropertyInfo(alias="AsyncAmd")]
    """Select whether to perform answering machine detection in the background.

    By default execution is blocked until Answering Machine Detection is completed.
    """

    async_amd_status_callback: Annotated[str, PropertyInfo(alias="AsyncAmdStatusCallback")]
    """URL destination for Telnyx to send AMD callback events to for the call."""

    async_amd_status_callback_method: Annotated[
        Literal["GET", "POST"], PropertyInfo(alias="AsyncAmdStatusCallbackMethod")
    ]
    """HTTP request type used for `AsyncAmdStatusCallback`."""

    caller_id: Annotated[str, PropertyInfo(alias="CallerId")]
    """
    To be used as the caller id name (SIP From Display Name) presented to the
    destination (`To` number). The string should have a maximum of 128 characters,
    containing only letters, numbers, spaces, and `-_~!.+` special characters. If
    omitted, the display name will be the same as the number in the `From` field.
    """

    conversation_callback: Annotated[str, PropertyInfo(alias="ConversationCallback")]
    """URL destination for Telnyx to send conversation callback events to."""

    conversation_callback_method: Annotated[Literal["GET", "POST"], PropertyInfo(alias="ConversationCallbackMethod")]
    """HTTP request type used for `ConversationCallback`."""

    conversation_callbacks: Annotated[SequenceNotStr[str], PropertyInfo(alias="ConversationCallbacks")]
    """An array of URL destinations for conversation callback events."""

    custom_headers: Annotated[Iterable[CustomHeader], PropertyInfo(alias="CustomHeaders")]
    """Custom HTTP headers to be sent with the call.

    Each header should be an object with 'name' and 'value' properties.
    """

    detection_mode: Annotated[Literal["Premium", "Regular"], PropertyInfo(alias="DetectionMode")]
    """Allows you to choose between Premium and Standard detections."""

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

    passports: Annotated[str, PropertyInfo(alias="Passports")]
    """A string of passport identifiers to associate with the call."""

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
    `RecordingStatusCallback`. Can be: `in-progress`, `completed` and `absent`.
    Separate multiple values with a space. Defaults to `completed`.
    """

    recording_status_callback_method: Annotated[
        Literal["GET", "POST"], PropertyInfo(alias="RecordingStatusCallbackMethod")
    ]
    """HTTP request type used for `RecordingStatusCallback`. Defaults to `POST`."""

    recording_timeout: Annotated[int, PropertyInfo(alias="RecordingTimeout")]
    """
    The number of seconds that Telnyx will wait for the recording to be stopped if
    silence is detected. The timer only starts when the speech is detected. The
    minimum value is 0. The default value is 0 (infinite).
    """

    recording_track: Annotated[Literal["inbound", "outbound", "both"], PropertyInfo(alias="RecordingTrack")]
    """The audio track to record for the call. The default is `both`."""

    send_recording_url: Annotated[bool, PropertyInfo(alias="SendRecordingUrl")]
    """Whether to send RecordingUrl in webhooks."""

    sip_auth_password: Annotated[str, PropertyInfo(alias="SipAuthPassword")]
    """The password to use for SIP authentication."""

    sip_auth_username: Annotated[str, PropertyInfo(alias="SipAuthUsername")]
    """The username to use for SIP authentication."""

    sip_region: Annotated[
        Literal["US", "Europe", "Canada", "Australia", "Middle East"], PropertyInfo(alias="SipRegion")
    ]
    """Defines the SIP region to be used for the call."""

    status_callback: Annotated[str, PropertyInfo(alias="StatusCallback")]
    """URL destination for Telnyx to send status callback events to for the call."""

    status_callback_event: Annotated[str, PropertyInfo(alias="StatusCallbackEvent")]
    """The call events for which Telnyx should send a webhook.

    Multiple events can be defined when separated by a space. Valid values:
    initiated, ringing, answered, completed.
    """

    status_callback_method: Annotated[Literal["GET", "POST"], PropertyInfo(alias="StatusCallbackMethod")]
    """HTTP request type used for `StatusCallback`."""

    status_callbacks: Annotated[SequenceNotStr[str], PropertyInfo(alias="StatusCallbacks")]
    """
    An array of URL destinations for Telnyx to send status callback events to for
    the call.
    """

    time_limit: Annotated[int, PropertyInfo(alias="TimeLimit")]
    """The maximum duration of the call in seconds.

    The minimum value is 30 and the maximum value is 14400 (4 hours). Default is
    14400 seconds.
    """

    timeout_seconds: Annotated[int, PropertyInfo(alias="Timeout")]
    """
    The number of seconds to wait for the called party to answer the call before the
    call is canceled. The minimum value is 5 and the maximum value is 120. Default
    is 30 seconds.
    """

    trim: Annotated[Literal["trim-silence", "do-not-trim"], PropertyInfo(alias="Trim")]
    """Whether to trim any leading and trailing silence from the recording.

    Defaults to `trim-silence`.
    """


class CustomHeader(TypedDict, total=False):
    name: Required[str]
    """The name of the custom header"""

    value: Required[str]
    """The value of the custom header"""

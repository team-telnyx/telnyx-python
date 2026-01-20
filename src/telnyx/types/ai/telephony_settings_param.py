# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = [
    "TelephonySettingsParam",
    "NoiseSuppressionConfig",
    "VoicemailDetection",
    "VoicemailDetectionOnVoicemailDetected",
    "VoicemailDetectionOnVoicemailDetectedVoicemailMessage",
]


class NoiseSuppressionConfig(TypedDict, total=False):
    """Configuration for noise suppression.

    Only applicable when noise_suppression is 'deepfilternet'.
    """

    attenuation_limit: int
    """Attenuation limit for noise suppression. Range: 0-100."""

    mode: Literal["advanced"]
    """Mode for noise suppression configuration."""


class VoicemailDetectionOnVoicemailDetectedVoicemailMessage(TypedDict, total=False):
    """Configuration for the voicemail message to leave.

    Only applicable when action is 'leave_message_and_stop_assistant'.
    """

    message: str
    """The specific message to leave as voicemail.

    Only applicable when type is 'message'.
    """

    prompt: str
    """The prompt to use for generating the voicemail message.

    Only applicable when type is 'prompt'.
    """

    type: Literal["prompt", "message"]
    """The type of voicemail message.

    Use 'prompt' to have the assistant generate a message based on a prompt, or
    'message' to leave a specific message.
    """


class VoicemailDetectionOnVoicemailDetected(TypedDict, total=False):
    """Action to take when voicemail is detected."""

    action: Literal["stop_assistant", "leave_message_and_stop_assistant", "continue_assistant"]
    """The action to take when voicemail is detected."""

    voicemail_message: VoicemailDetectionOnVoicemailDetectedVoicemailMessage
    """Configuration for the voicemail message to leave.

    Only applicable when action is 'leave_message_and_stop_assistant'.
    """


class VoicemailDetection(TypedDict, total=False):
    """
    Configuration for voicemail detection (AMD - Answering Machine Detection) on outgoing calls. These settings only apply if AMD is enabled on the Dial command. See [TeXML Dial documentation](https://developers.telnyx.com/api-reference/texml-rest-commands/initiate-an-outbound-call) for enabling AMD. Recommended settings: MachineDetection=Enable, AsyncAmd=true, DetectionMode=Premium.
    """

    on_voicemail_detected: VoicemailDetectionOnVoicemailDetected
    """Action to take when voicemail is detected."""


class TelephonySettingsParam(TypedDict, total=False):
    default_texml_app_id: str
    """Default Texml App used for voice calls with your assistant.

    This will be created automatically on assistant creation.
    """

    noise_suppression: Literal["krisp", "deepfilternet", "disabled"]
    """The noise suppression engine to use.

    Use 'disabled' to turn off noise suppression.
    """

    noise_suppression_config: NoiseSuppressionConfig
    """Configuration for noise suppression.

    Only applicable when noise_suppression is 'deepfilternet'.
    """

    supports_unauthenticated_web_calls: bool
    """
    When enabled, allows users to interact with your AI assistant directly from your
    website without requiring authentication. This is required for FE widgets that
    work with assistants that have telephony enabled.
    """

    time_limit_secs: int
    """Maximum duration in seconds for the AI assistant to participate on the call.

    When this limit is reached the assistant will be stopped. This limit does not
    apply to portions of a call without an active assistant (for instance, a call
    transferred to a human representative).
    """

    user_idle_timeout_secs: int
    """Maximum duration in seconds of end user silence on the call.

    When this limit is reached the assistant will be stopped. This limit does not
    apply to portions of a call without an active assistant (for instance, a call
    transferred to a human representative).
    """

    voicemail_detection: VoicemailDetection
    """
    Configuration for voicemail detection (AMD - Answering Machine Detection) on
    outgoing calls. These settings only apply if AMD is enabled on the Dial command.
    See
    [TeXML Dial documentation](https://developers.telnyx.com/api-reference/texml-rest-commands/initiate-an-outbound-call)
    for enabling AMD. Recommended settings: MachineDetection=Enable, AsyncAmd=true,
    DetectionMode=Premium.
    """

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "TelephonySettings",
    "NoiseSuppressionConfig",
    "VoicemailDetection",
    "VoicemailDetectionOnVoicemailDetected",
    "VoicemailDetectionOnVoicemailDetectedVoicemailMessage",
]


class NoiseSuppressionConfig(BaseModel):
    """Configuration for noise suppression.

    Only applicable when noise_suppression is 'deepfilternet'.
    """

    attenuation_limit: Optional[int] = None
    """Attenuation limit for noise suppression. Range: 0-100."""

    mode: Optional[Literal["advanced"]] = None
    """Mode for noise suppression configuration."""


class VoicemailDetectionOnVoicemailDetectedVoicemailMessage(BaseModel):
    """Configuration for the voicemail message to leave.

    Only applicable when action is 'leave_message_and_stop_assistant'.
    """

    message: Optional[str] = None
    """The specific message to leave as voicemail.

    Only applicable when type is 'message'.
    """

    prompt: Optional[str] = None
    """The prompt to use for generating the voicemail message.

    Only applicable when type is 'prompt'.
    """

    type: Optional[Literal["prompt", "message"]] = None
    """The type of voicemail message.

    Use 'prompt' to have the assistant generate a message based on a prompt, or
    'message' to leave a specific message.
    """


class VoicemailDetectionOnVoicemailDetected(BaseModel):
    """Action to take when voicemail is detected."""

    action: Optional[Literal["stop_assistant", "leave_message_and_stop_assistant", "continue_assistant"]] = None
    """The action to take when voicemail is detected."""

    voicemail_message: Optional[VoicemailDetectionOnVoicemailDetectedVoicemailMessage] = None
    """Configuration for the voicemail message to leave.

    Only applicable when action is 'leave_message_and_stop_assistant'.
    """


class VoicemailDetection(BaseModel):
    """
    Configuration for voicemail detection (AMD - Answering Machine Detection) on outgoing calls. These settings only apply if AMD is enabled on the Dial command. See [TeXML Dial documentation](https://developers.telnyx.com/api-reference/texml-rest-commands/initiate-an-outbound-call) for enabling AMD. Recommended settings: MachineDetection=Enable, AsyncAmd=true, DetectionMode=Premium.
    """

    on_voicemail_detected: Optional[VoicemailDetectionOnVoicemailDetected] = None
    """Action to take when voicemail is detected."""


class TelephonySettings(BaseModel):
    default_texml_app_id: Optional[str] = None
    """Default Texml App used for voice calls with your assistant.

    This will be created automatically on assistant creation.
    """

    noise_suppression: Optional[Literal["krisp", "deepfilternet", "disabled"]] = None
    """The noise suppression engine to use.

    Use 'disabled' to turn off noise suppression.
    """

    noise_suppression_config: Optional[NoiseSuppressionConfig] = None
    """Configuration for noise suppression.

    Only applicable when noise_suppression is 'deepfilternet'.
    """

    supports_unauthenticated_web_calls: Optional[bool] = None
    """
    When enabled, allows users to interact with your AI assistant directly from your
    website without requiring authentication. This is required for FE widgets that
    work with assistants that have telephony enabled.
    """

    time_limit_secs: Optional[int] = None
    """Maximum duration in seconds for the AI assistant to participate on the call.

    When this limit is reached the assistant will be stopped. This limit does not
    apply to portions of a call without an active assistant (for instance, a call
    transferred to a human representative).
    """

    user_idle_timeout_secs: Optional[int] = None
    """Maximum duration in seconds of end user silence on the call.

    When this limit is reached the assistant will be stopped. This limit does not
    apply to portions of a call without an active assistant (for instance, a call
    transferred to a human representative).
    """

    voicemail_detection: Optional[VoicemailDetection] = None
    """
    Configuration for voicemail detection (AMD - Answering Machine Detection) on
    outgoing calls. These settings only apply if AMD is enabled on the Dial command.
    See
    [TeXML Dial documentation](https://developers.telnyx.com/api-reference/texml-rest-commands/initiate-an-outbound-call)
    for enabling AMD. Recommended settings: MachineDetection=Enable, AsyncAmd=true,
    DetectionMode=Premium.
    """

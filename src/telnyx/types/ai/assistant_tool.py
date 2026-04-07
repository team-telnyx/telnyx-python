# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .hangup_tool import HangupTool
from .retrieval_tool import RetrievalTool
from .inference_embedding_webhook_tool_params import InferenceEmbeddingWebhookToolParams

__all__ = [
    "AssistantTool",
    "Handoff",
    "HandoffHandoff",
    "HandoffHandoffAIAssistant",
    "Transfer",
    "TransferTransfer",
    "TransferTransferTarget",
    "TransferTransferCustomHeader",
    "TransferTransferVoicemailDetection",
    "TransferTransferVoicemailDetectionDetectionConfig",
    "TransferTransferVoicemailDetectionOnVoicemailDetected",
    "TransferTransferVoicemailDetectionOnVoicemailDetectedVoicemailMessage",
    "Invite",
    "InviteInviteConfig",
    "InviteInviteConfigCustomHeader",
    "InviteInviteConfigVoicemailDetection",
    "InviteInviteConfigVoicemailDetectionOnVoicemailDetected",
    "Refer",
    "ReferRefer",
    "ReferReferTarget",
    "ReferReferCustomHeader",
    "ReferReferSipHeader",
    "SendDtmf",
    "SendMessage",
    "SendMessageSendMessage",
    "SkipTurn",
    "SkipTurnSkipTurn",
]


class HandoffHandoffAIAssistant(BaseModel):
    id: str
    """The ID of the assistant to hand off to."""

    name: str
    """Helpful name for giving context on when to handoff to the assistant."""


class HandoffHandoff(BaseModel):
    ai_assistants: List[HandoffHandoffAIAssistant]
    """List of possible assistants that can receive a handoff."""

    voice_mode: Optional[Literal["unified", "distinct"]] = None
    """
    With the unified voice mode all assistants share the same voice, making the
    handoff transparent to the user. With the distinct voice mode all assistants
    retain their voice configuration, providing the experience of a conference call
    with a team of assistants.
    """


class Handoff(BaseModel):
    """
    The handoff tool allows the assistant to hand off control of the conversation to another AI assistant. By default, this will happen transparently to the end user.
    """

    handoff: HandoffHandoff

    type: Literal["handoff"]


class TransferTransferTarget(BaseModel):
    name: Optional[str] = None
    """The name of the target."""

    to: Optional[str] = None
    """The destination number or SIP URI of the call."""


class TransferTransferCustomHeader(BaseModel):
    name: Optional[str] = None

    value: Optional[str] = None
    """The value of the header.

    Note that we support mustache templating for the value. For example you can use
    `{{#integration_secret}}test-secret{{/integration_secret}}` to pass the value of
    the integration secret.
    """


class TransferTransferVoicemailDetectionDetectionConfig(BaseModel):
    """Advanced AMD detection configuration parameters.

    All values are optional - Telnyx will use defaults if not specified.
    """

    after_greeting_silence_millis: Optional[int] = None
    """Duration of silence after greeting detection before finalizing the result."""

    between_words_silence_millis: Optional[int] = None
    """Maximum silence duration between words during greeting."""

    greeting_duration_millis: Optional[int] = None
    """Expected duration of greeting speech."""

    greeting_silence_duration_millis: Optional[int] = None
    """
    Duration of silence after the greeting to wait before considering the greeting
    complete.
    """

    greeting_total_analysis_time_millis: Optional[int] = None
    """Maximum time to spend analyzing the greeting."""

    initial_silence_millis: Optional[int] = None
    """Maximum silence duration at the start of the call before speech."""

    maximum_number_of_words: Optional[int] = None
    """Maximum number of words expected in a human greeting."""

    maximum_word_length_millis: Optional[int] = None
    """Maximum duration of a single word."""

    min_word_length_millis: Optional[int] = None
    """Minimum duration for audio to be considered a word."""

    silence_threshold: Optional[int] = None
    """Audio level threshold for silence detection."""

    total_analysis_time_millis: Optional[int] = None
    """Total time allowed for AMD analysis."""


class TransferTransferVoicemailDetectionOnVoicemailDetectedVoicemailMessage(BaseModel):
    """Configuration for the voicemail message to leave.

    Only applicable when action is 'leave_message_and_stop_transfer'.
    """

    message: Optional[str] = None
    """The specific message to leave as voicemail (converted to speech).

    Only applicable when type is 'message'.
    """

    type: Optional[Literal["message", "warm_transfer_instructions"]] = None
    """The type of voicemail message.

    Use 'message' to leave a specific TTS message, or 'warm_transfer_instructions'
    to play the warm transfer audio.
    """


class TransferTransferVoicemailDetectionOnVoicemailDetected(BaseModel):
    """Action to take when voicemail is detected on the transferred call."""

    action: Optional[Literal["stop_transfer", "leave_message_and_stop_transfer"]] = None
    """The action to take when voicemail is detected.

    'stop_transfer' hangs up immediately. 'leave_message_and_stop_transfer' leaves a
    message then hangs up.
    """

    voicemail_message: Optional[TransferTransferVoicemailDetectionOnVoicemailDetectedVoicemailMessage] = None
    """Configuration for the voicemail message to leave.

    Only applicable when action is 'leave_message_and_stop_transfer'.
    """


class TransferTransferVoicemailDetection(BaseModel):
    """
    Configuration for voicemail detection (AMD - Answering Machine Detection) on the transferred call. Allows the assistant to detect when a voicemail system answers the transferred call and take appropriate action.
    """

    detection_config: Optional[TransferTransferVoicemailDetectionDetectionConfig] = None
    """Advanced AMD detection configuration parameters.

    All values are optional - Telnyx will use defaults if not specified.
    """

    detection_mode: Optional[Literal["disabled", "premium"]] = None
    """The AMD detection mode to use.

    'premium' enables premium answering machine detection. 'disabled' turns off AMD
    detection.
    """

    on_voicemail_detected: Optional[TransferTransferVoicemailDetectionOnVoicemailDetected] = None
    """Action to take when voicemail is detected on the transferred call."""


class TransferTransfer(BaseModel):
    from_: str = FieldInfo(alias="from")
    """Number or SIP URI placing the call."""

    targets: List[TransferTransferTarget]
    """The different possible targets of the transfer.

    The assistant will be able to choose one of the targets to transfer the call to.
    """

    custom_headers: Optional[List[TransferTransferCustomHeader]] = None
    """Custom headers to be added to the SIP INVITE for the transfer command."""

    voicemail_detection: Optional[TransferTransferVoicemailDetection] = None
    """
    Configuration for voicemail detection (AMD - Answering Machine Detection) on the
    transferred call. Allows the assistant to detect when a voicemail system answers
    the transferred call and take appropriate action.
    """

    warm_message_delay_ms: Optional[int] = None
    """
    Optional delay in milliseconds before playing the warm message audio when the
    transferred call is answered. When set, the audio_url is not included in the
    dial command; instead, playback starts after the specified delay. When not set,
    existing behavior (audio_url in dial) is preserved.
    """

    warm_transfer_instructions: Optional[str] = None
    """
    Natural language instructions for your agent for how to provide context for the
    transfer recipient.
    """


class Transfer(BaseModel):
    transfer: TransferTransfer

    type: Literal["transfer"]


class InviteInviteConfigCustomHeader(BaseModel):
    name: Optional[str] = None

    value: Optional[str] = None
    """The value of the header.

    Note that we support mustache templating for the value. For example you can use
    `{{#integration_secret}}test-secret{{/integration_secret}}` to pass the value of
    the integration secret.
    """


class InviteInviteConfigVoicemailDetectionOnVoicemailDetected(BaseModel):
    """Action to take when voicemail is detected on the invited call."""

    action: Optional[Literal["stop_invite"]] = None
    """The action to take when voicemail is detected."""


class InviteInviteConfigVoicemailDetection(BaseModel):
    """
    Configuration for voicemail detection (AMD - Answering Machine Detection) on the invited call.
    """

    detection_mode: Optional[Literal["disabled", "premium"]] = None
    """The AMD detection mode to use.

    'premium' enables premium answering machine detection. 'disabled' turns off AMD
    detection.
    """

    on_voicemail_detected: Optional[InviteInviteConfigVoicemailDetectionOnVoicemailDetected] = None
    """Action to take when voicemail is detected on the invited call."""


class InviteInviteConfig(BaseModel):
    custom_headers: Optional[List[InviteInviteConfigCustomHeader]] = None
    """Custom headers to be added to the SIP INVITE for the invite command."""

    from_: Optional[str] = FieldInfo(alias="from", default=None)
    """Number or SIP URI placing the call."""

    voicemail_detection: Optional[InviteInviteConfigVoicemailDetection] = None
    """
    Configuration for voicemail detection (AMD - Answering Machine Detection) on the
    invited call.
    """


class Invite(BaseModel):
    invite_config: InviteInviteConfig

    type: Literal["invite"]


class ReferReferTarget(BaseModel):
    name: str
    """The name of the target."""

    sip_address: str
    """The SIP URI to which the call will be referred."""

    sip_auth_password: Optional[str] = None
    """SIP Authentication password used for SIP challenges."""

    sip_auth_username: Optional[str] = None
    """SIP Authentication username used for SIP challenges."""


class ReferReferCustomHeader(BaseModel):
    name: Optional[str] = None

    value: Optional[str] = None
    """The value of the header.

    Note that we support mustache templating for the value. For example you can use
    `{{#integration_secret}}test-secret{{/integration_secret}}` to pass the value of
    the integration secret.
    """


class ReferReferSipHeader(BaseModel):
    name: Optional[Literal["User-to-User", "Diversion"]] = None

    value: Optional[str] = None
    """The value of the header.

    Note that we support mustache templating for the value. For example you can use
    `{{#integration_secret}}test-secret{{/integration_secret}}` to pass the value of
    the integration secret.
    """


class ReferRefer(BaseModel):
    targets: List[ReferReferTarget]
    """The different possible targets of the SIP refer.

    The assistant will be able to choose one of the targets to refer the call to.
    """

    custom_headers: Optional[List[ReferReferCustomHeader]] = None
    """Custom headers to be added to the SIP REFER."""

    sip_headers: Optional[List[ReferReferSipHeader]] = None
    """SIP headers to be added to the SIP REFER.

    Currently only User-to-User and Diversion headers are supported.
    """


class Refer(BaseModel):
    refer: ReferRefer

    type: Literal["refer"]


class SendDtmf(BaseModel):
    send_dtmf: Dict[str, object]

    type: Literal["send_dtmf"]


class SendMessageSendMessage(BaseModel):
    message_template: Optional[str] = None
    """
    Optional message template with dynamic variable support using mustache syntax
    (e.g., {{variable_name}}). When set, the assistant will use this template for
    the SMS body instead of generating one. Dynamic variables like
    {{telnyx_end_user_target}}, {{telnyx_agent_target}}, and custom webhook-provided
    variables will be resolved at runtime.
    """

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class SendMessage(BaseModel):
    """
    The send_message tool allows the assistant to send SMS or MMS messages to the end user. The 'to' and 'from' addresses are automatically determined from the conversation context, and the message text is generated by the assistant unless a message_template is provided for runtime variable substitution.
    """

    send_message: SendMessageSendMessage

    type: Literal["send_message"]


class SkipTurnSkipTurn(BaseModel):
    description: Optional[str] = None
    """The description of the function that will be passed to the assistant."""


class SkipTurn(BaseModel):
    skip_turn: SkipTurnSkipTurn

    type: Literal["skip_turn"]


AssistantTool: TypeAlias = Annotated[
    Union[
        InferenceEmbeddingWebhookToolParams,
        RetrievalTool,
        Handoff,
        HangupTool,
        Transfer,
        Invite,
        Refer,
        SendDtmf,
        SendMessage,
        SkipTurn,
    ],
    PropertyInfo(discriminator="type"),
]

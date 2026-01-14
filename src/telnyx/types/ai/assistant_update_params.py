# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Literal, TypedDict

from .enabled_features import EnabledFeatures
from .assistant_tool_param import AssistantToolParam
from .voice_settings_param import VoiceSettingsParam
from .insight_settings_param import InsightSettingsParam
from .privacy_settings_param import PrivacySettingsParam
from .messaging_settings_param import MessagingSettingsParam
from .telephony_settings_param import TelephonySettingsParam
from .transcription_settings_param import TranscriptionSettingsParam

__all__ = ["AssistantUpdateParams", "WidgetSettings", "WidgetSettingsAudioVisualizerConfig"]


class AssistantUpdateParams(TypedDict, total=False):
    description: str

    dynamic_variables: Dict[str, object]
    """Map of dynamic variables and their default values"""

    dynamic_variables_webhook_url: str
    """
    If the dynamic_variables_webhook_url is set for the assistant, we will send a
    request at the start of the conversation. See our
    [guide](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)
    for more information.
    """

    enabled_features: List[EnabledFeatures]

    greeting: str
    """Text that the assistant will use to start the conversation.

    This may be templated with
    [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)
    """

    insight_settings: InsightSettingsParam

    instructions: str
    """System instructions for the assistant.

    These may be templated with
    [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)
    """

    llm_api_key_ref: str
    """This is only needed when using third-party inference providers.

    The `identifier` for an integration secret
    [/v2/integration_secrets](https://developers.telnyx.com/api/secrets-manager/integration-secrets/create-integration-secret)
    that refers to your LLM provider's API key. Warning: Free plans are unlikely to
    work with this integration.
    """

    messaging_settings: MessagingSettingsParam

    model: str
    """ID of the model to use.

    You can use the
    [Get models API](https://developers.telnyx.com/api/inference/inference-embedding/get-models-public-models-get)
    to see all of your available models,
    """

    name: str

    privacy_settings: PrivacySettingsParam

    promote_to_main: bool
    """Indicates whether the assistant should be promoted to the main version.

    Defaults to true.
    """

    telephony_settings: TelephonySettingsParam

    tools: Iterable[AssistantToolParam]
    """The tools that the assistant can use.

    These may be templated with
    [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)
    """

    transcription: TranscriptionSettingsParam

    voice_settings: VoiceSettingsParam

    widget_settings: WidgetSettings
    """Configuration settings for the assistant's web widget."""


class WidgetSettingsAudioVisualizerConfig(TypedDict, total=False):
    color: Literal["verdant", "twilight", "bloom", "mystic", "flare", "glacier"]
    """The color theme for the audio visualizer."""

    preset: str
    """The preset style for the audio visualizer."""


class WidgetSettings(TypedDict, total=False):
    """Configuration settings for the assistant's web widget."""

    agent_thinking_text: str
    """Text displayed while the agent is processing."""

    audio_visualizer_config: WidgetSettingsAudioVisualizerConfig

    default_state: Literal["expanded", "collapsed"]
    """The default state of the widget."""

    give_feedback_url: Optional[str]
    """URL for users to give feedback."""

    logo_icon_url: Optional[str]
    """URL to a custom logo icon for the widget."""

    position: Literal["fixed", "static"]
    """The positioning style for the widget."""

    report_issue_url: Optional[str]
    """URL for users to report issues."""

    speak_to_interrupt_text: str
    """Text prompting users to speak to interrupt."""

    start_call_text: str
    """Custom text displayed on the start call button."""

    theme: Literal["light", "dark"]
    """The visual theme for the widget."""

    view_history_url: Optional[str]
    """URL to view conversation history."""

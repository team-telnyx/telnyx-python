# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ..._models import BaseModel
from .assistant_tool import AssistantTool
from .voice_settings import VoiceSettings
from .import_metadata import ImportMetadata
from .widget_settings import WidgetSettings
from .enabled_features import EnabledFeatures
from .insight_settings import InsightSettings
from .privacy_settings import PrivacySettings
from .messaging_settings import MessagingSettings
from .telephony_settings import TelephonySettings
from .transcription_settings import TranscriptionSettings

__all__ = ["InferenceEmbedding"]


class InferenceEmbedding(BaseModel):
    id: str

    created_at: datetime

    instructions: str
    """System instructions for the assistant.

    These may be templated with
    [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)
    """

    model: str
    """ID of the model to use.

    You can use the
    [Get models API](https://developers.telnyx.com/api-reference/chat/get-available-models)
    to see all of your available models,
    """

    name: str

    description: Optional[str] = None

    dynamic_variables: Optional[Dict[str, object]] = None
    """Map of dynamic variables and their values"""

    dynamic_variables_webhook_url: Optional[str] = None
    """
    If the dynamic_variables_webhook_url is set for the assistant, we will send a
    request at the start of the conversation. See our
    [guide](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)
    for more information.
    """

    enabled_features: Optional[List[EnabledFeatures]] = None

    greeting: Optional[str] = None
    """Text that the assistant will use to start the conversation.

    This may be templated with
    [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables).
    Use an empty string to have the assistant wait for the user to speak first. Use
    the special value `<assistant-speaks-first-with-model-generated-message>` to
    have the assistant generate the greeting based on the system instructions.
    """

    import_metadata: Optional[ImportMetadata] = None

    insight_settings: Optional[InsightSettings] = None

    llm_api_key_ref: Optional[str] = None
    """This is only needed when using third-party inference providers.

    The `identifier` for an integration secret
    [/v2/integration_secrets](https://developers.telnyx.com/api-reference/integration-secrets/create-a-secret)
    that refers to your LLM provider's API key. Warning: Free plans are unlikely to
    work with this integration.
    """

    messaging_settings: Optional[MessagingSettings] = None

    privacy_settings: Optional[PrivacySettings] = None

    telephony_settings: Optional[TelephonySettings] = None

    tools: Optional[List[AssistantTool]] = None
    """The tools that the assistant can use.

    These may be templated with
    [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)
    """

    transcription: Optional[TranscriptionSettings] = None

    voice_settings: Optional[VoiceSettings] = None

    widget_settings: Optional[WidgetSettings] = None
    """Configuration settings for the assistant's web widget."""

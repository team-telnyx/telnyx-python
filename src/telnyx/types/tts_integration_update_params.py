# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

__all__ = ["TtsIntegrationUpdateParams"]


class TtsIntegrationUpdateParams(TypedDict, total=False):
    capabilities: "CommunityTtsEngineCapabilitiesParam"
    """What the engine supports. An unknown key is rejected."""

    connect_timeout_ms: int

    contact_email: Optional[str]

    data_retention_policy_url: Optional[str]

    documentation_url: Optional[str]

    supported_audio_formats: List["CommunityTtsAudioFormat"]

    visibility: "CommunityTtsEngineVisibility"
    """`private`: only your organization can use the engine.

    `public`: any organization can, once it is `active`.
    """

    voices_api_key_ref: Optional[str]

    voices_url: str
    """See the create request."""

    websocket_url: str
    """See the create request."""


from .community_tts_audio_format import CommunityTtsAudioFormat
from .community_tts_engine_visibility import CommunityTtsEngineVisibility
from .community_tts_engine_capabilities_param import CommunityTtsEngineCapabilitiesParam

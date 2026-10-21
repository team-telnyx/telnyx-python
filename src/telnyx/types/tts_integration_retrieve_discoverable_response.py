# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .community_tts_audio_format import CommunityTtsAudioFormat
from .community_tts_engine_status import CommunityTtsEngineStatus
from .community_tts_engine_list_meta import CommunityTtsEngineListMeta
from .community_tts_engine_visibility import CommunityTtsEngineVisibility
from .community_tts_engine_capabilities import CommunityTtsEngineCapabilities

__all__ = ["TtsIntegrationRetrieveDiscoverableResponse", "Data"]


class Data(BaseModel):
    """What a caller needs to choose an engine.

    It carries no publisher contact details, review notes or credential references.
    """

    id: str

    name: str

    status: CommunityTtsEngineStatus
    """
    Whether the engine can serve traffic right now, independent of `visibility` and
    `review_status`. `draft`: not yet approved (new and awaiting its first review,
    rejected and awaiting a fix, or approved earlier and awaiting re-review after a
    review-sensitive change). `active`: serving traffic. `disabled`: owner-paused,
    reversible via `enable`. `suspended`: paused by Telnyx (repeated failures of a
    public engine, or an abuse action); the owner cannot clear this by calling
    `enable`, and Telnyx can reinstate it.
    """

    visibility: CommunityTtsEngineVisibility
    """`private`: only your organization can use the engine.

    `public`: any organization can, once it is `active`.
    """

    capabilities: Optional[CommunityTtsEngineCapabilities] = None
    """What the engine supports. An unknown key is rejected."""

    connect_timeout_ms: Optional[int] = None

    created_at: Optional[datetime] = None

    data_retention_policy_url: Optional[str] = None

    documentation_url: Optional[str] = None

    supported_audio_formats: Optional[List[CommunityTtsAudioFormat]] = None

    voices_count: Optional[int] = None

    websocket_url: Optional[str] = None


class TtsIntegrationRetrieveDiscoverableResponse(BaseModel):
    data: List[Data]

    meta: CommunityTtsEngineListMeta

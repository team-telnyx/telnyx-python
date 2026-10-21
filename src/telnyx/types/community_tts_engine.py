# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .community_tts_audio_format import CommunityTtsAudioFormat
from .community_tts_engine_status import CommunityTtsEngineStatus
from .community_tts_engine_visibility import CommunityTtsEngineVisibility
from .community_tts_engine_capabilities import CommunityTtsEngineCapabilities

__all__ = ["CommunityTtsEngine"]


class CommunityTtsEngine(BaseModel):
    """The full record of a community TTS engine you own.

    Select its voices by the engine's `name`, as `<name>.<voice_id>`, with your own key for it (`api_key_ref`).
    """

    id: str

    capabilities: CommunityTtsEngineCapabilities
    """What the engine supports. An unknown key is rejected."""

    name: str
    """The engine's unique name: the first part of its voices."""

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

    supported_audio_formats: List[CommunityTtsAudioFormat]

    visibility: CommunityTtsEngineVisibility
    """`private`: only your organization can use the engine.

    `public`: any organization can, once it is `active`.
    """

    voices_url: str

    websocket_url: str

    connect_timeout_ms: Optional[int] = None

    contact_email: Optional[str] = None

    created_at: Optional[datetime] = None

    data_retention_policy_url: Optional[str] = None

    documentation_url: Optional[str] = None

    review_notes: Optional[str] = None
    """The reviewer's notes on a rejection."""

    review_status: Optional[Literal["pending", "approved", "rejected"]] = None
    """
    `null`: never submitted, or an approved engine whose review-sensitive field
    changed and awaits re-review. `pending`: submitted. `approved`: approved.
    `rejected`: rejected, with `review_notes`.
    """

    reviewed_at: Optional[datetime] = None

    updated_at: Optional[datetime] = None

    voices_api_key_ref: Optional[str] = None

    voices_count: Optional[int] = None
    """The number of voices in the stored list."""

    voices_degraded: Optional[bool] = None
    """`true` after three failed reads in a row, until a read succeeds.

    A degraded engine keeps serving from its last list.
    """

    voices_fetched_at: Optional[datetime] = None
    """When the stored list was last read successfully."""

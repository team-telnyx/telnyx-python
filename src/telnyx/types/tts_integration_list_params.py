# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TtsIntegrationListParams", "Page"]


class TtsIntegrationListParams(TypedDict, total=False):
    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[size], page[number]
    """

    status: "CommunityTtsEngineStatus"
    """Filter by status."""

    visibility: "CommunityTtsEngineVisibility"
    """Filter by visibility."""


class Page(TypedDict, total=False):
    """Consolidated page parameter (deepObject style).

    Originally: page[size], page[number]
    """

    number: int

    size: int
    """Clamped to 1-100."""


from .community_tts_engine_status import CommunityTtsEngineStatus
from .community_tts_engine_visibility import CommunityTtsEngineVisibility

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from .._models import BaseModel
from .community_tts_engine import CommunityTtsEngine
from .community_tts_engine_list_meta import CommunityTtsEngineListMeta

__all__ = ["TtsIntegrationListResponse"]


class TtsIntegrationListResponse(BaseModel):
    data: List[CommunityTtsEngine]

    meta: CommunityTtsEngineListMeta

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from .._models import BaseModel
from .community_tts_engine_list_meta import CommunityTtsEngineListMeta
from .tts_integrations.community_tts_conformance_run import CommunityTtsConformanceRun

__all__ = ["TtsIntegrationRetrieveConformanceRunsResponse"]


class TtsIntegrationRetrieveConformanceRunsResponse(BaseModel):
    data: List[CommunityTtsConformanceRun]

    meta: CommunityTtsEngineListMeta

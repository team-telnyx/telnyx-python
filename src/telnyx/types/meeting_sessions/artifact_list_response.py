# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from ..._models import BaseModel
from .meeting_session_artifact import MeetingSessionArtifact

__all__ = ["ArtifactListResponse"]


class ArtifactListResponse(BaseModel):
    data: List[MeetingSessionArtifact]

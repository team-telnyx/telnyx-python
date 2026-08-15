# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._models import BaseModel
from .meeting_session_artifact import MeetingSessionArtifact

__all__ = ["MeetingSessionArtifactResponse"]


class MeetingSessionArtifactResponse(BaseModel):
    data: MeetingSessionArtifact

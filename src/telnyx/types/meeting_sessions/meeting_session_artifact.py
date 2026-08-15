# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MeetingSessionArtifact", "Content", "ModelProvenance"]


class Content(BaseModel):
    text: str


class ModelProvenance(BaseModel):
    model: str

    provider: str


class MeetingSessionArtifact(BaseModel):
    id: str

    content: Optional[Content] = None

    created_at: datetime

    failure_reason: Optional[str] = None

    api_model_provenance: Optional[ModelProvenance] = FieldInfo(alias="model_provenance", default=None)

    session_id: str

    status: Literal["pending", "completed", "failed"]

    type: Literal["summary", "action_items"]

    updated_at: datetime

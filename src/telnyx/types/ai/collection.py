# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .collections.source import Source
from .collections.retrieval_settings_wrapper import RetrievalSettingsWrapper

__all__ = ["Collection"]


class Collection(BaseModel):
    created_at: Optional[datetime] = None

    description: Optional[str] = None

    name: Optional[str] = None

    record_type: Optional[str] = None
    """Identifies the record type. Always `ai_collection`."""

    settings: Optional[RetrievalSettingsWrapper] = None

    slug: Optional[str] = None

    sources: Optional[List[Source]] = None

    status: Optional[str] = None

    updated_at: Optional[datetime] = None

    uuid: Optional[str] = None

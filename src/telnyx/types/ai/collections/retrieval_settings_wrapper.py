# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ...._models import BaseModel
from .retrieval_settings import RetrievalSettings

__all__ = ["RetrievalSettingsWrapper"]


class RetrievalSettingsWrapper(BaseModel):
    record_type: Optional[str] = None
    """Identifies the record type. Always `ai_collection_settings`."""

    retrieval: Optional[RetrievalSettings] = None
    """How documents are retrieved when searching the collection."""

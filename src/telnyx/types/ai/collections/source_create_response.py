# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ...._models import BaseModel
from .collections_source import CollectionsSource

__all__ = ["SourceCreateResponse"]


class SourceCreateResponse(BaseModel):
    """Envelope containing a single collection source."""

    data: Optional[CollectionsSource] = None

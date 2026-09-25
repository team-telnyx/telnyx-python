# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ...._models import BaseModel
from .collections_source import CollectionsSource

__all__ = ["SourceListResponse"]


class SourceListResponse(BaseModel):
    data: Optional[List[CollectionsSource]] = None

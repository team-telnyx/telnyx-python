# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from .source import Source
from ...._models import BaseModel

__all__ = ["SourceListResponse"]


class SourceListResponse(BaseModel):
    data: Optional[List[Source]] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from .source import Source
from ...._models import BaseModel

__all__ = ["SourceReplaceResponse", "Meta"]


class Meta(BaseModel):
    """
    Reports which source IDs were added, retained, and removed by a replace operation.
    """

    added: Optional[List[str]] = None

    removed: Optional[List[str]] = None

    retained: Optional[List[str]] = None


class SourceReplaceResponse(BaseModel):
    data: Optional[List[Source]] = None

    meta: Optional[Meta] = None
    """
    Reports which source IDs were added, retained, and removed by a replace
    operation.
    """

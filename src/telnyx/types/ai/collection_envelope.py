# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ..._models import BaseModel
from .collection import Collection

__all__ = ["CollectionEnvelope"]


class CollectionEnvelope(BaseModel):
    data: Optional[Collection] = None

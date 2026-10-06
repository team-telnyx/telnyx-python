# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from .namespace import Namespace
from ...._models import BaseModel

__all__ = ["NamespaceListResponse"]


class NamespaceListResponse(BaseModel):
    data: List[Namespace]

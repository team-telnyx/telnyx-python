# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ..._models import BaseModel
from .kv_namespace import KvNamespace

__all__ = ["KvNamespaceResponseWrapper"]


class KvNamespaceResponseWrapper(BaseModel):
    data: Optional[KvNamespace] = None

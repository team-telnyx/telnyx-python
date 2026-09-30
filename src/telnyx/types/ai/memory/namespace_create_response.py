# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .namespace import Namespace
from ...._models import BaseModel

__all__ = ["NamespaceCreateResponse"]


class NamespaceCreateResponse(BaseModel):
    data: Namespace
    """An isolated memory store within your organization."""

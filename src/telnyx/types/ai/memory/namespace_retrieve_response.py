# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["NamespaceRetrieveResponse", "Data"]


class Data(BaseModel):
    operation_id: str

    status: Literal["pending", "processing", "completed", "failed", "cancelled"]
    """Where the write is.

    `completed`, `failed` and `cancelled` are terminal: stop polling at any of them,
    and treat `failed` and `cancelled` as writes that did not happen.
    """

    completed_at: Optional[str] = None

    created_at: Optional[str] = None


class NamespaceRetrieveResponse(BaseModel):
    data: Data

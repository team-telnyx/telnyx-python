# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel

__all__ = ["CallReasonListResponse"]


class CallReasonListResponse(BaseModel):
    """Pre-vetted call-reason library entry."""

    id: Optional[str] = None

    description: Optional[str] = None

    reason: Optional[str] = None

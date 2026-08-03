# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ..._models import BaseModel

__all__ = ["InboundEmailAddress"]


class InboundEmailAddress(BaseModel):
    email: str

    name: Optional[str] = None

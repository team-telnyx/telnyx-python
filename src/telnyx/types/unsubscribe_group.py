# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["UnsubscribeGroup"]


class UnsubscribeGroup(BaseModel):
    id: str

    created_at: datetime

    description: Optional[str] = None
    """Always present (not omit-nullable); `null` when unset."""

    name: str

    record_type: Literal["email_unsubscribe_group"]
    """View-only."""

    updated_at: datetime

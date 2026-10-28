# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Session", "Limits", "Policy"]


class Limits(BaseModel):
    idle_timeout_s: int

    lifetime_s: int


class Policy(BaseModel):
    allowed_domains: List[str]


class Session(BaseModel):
    id: str

    closed_at: Optional[datetime] = None

    created_at: datetime

    expires_at: Optional[datetime] = None

    failure_reason: Optional[str] = None

    last_activity_at: Optional[datetime] = None

    limits: Limits

    metadata: object

    policy: Policy

    ready_at: Optional[datetime] = None

    status: Literal["provisioning", "ready", "closing", "closed", "failed", "expired"]

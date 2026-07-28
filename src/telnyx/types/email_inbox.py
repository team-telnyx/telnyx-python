# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EmailInbox"]


class EmailInbox(BaseModel):
    id: str

    address: str

    created_at: datetime

    domain: str
    """Domain name used by the inbox address."""

    domain_id: str

    record_type: Literal["email_inbox"]

    settings: Dict[str, object]

    status: Literal["active", "paused"]

    updated_at: datetime

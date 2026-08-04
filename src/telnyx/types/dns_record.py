# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DNSRecord"]


class DNSRecord(BaseModel):
    id: str

    host: str

    purpose: Literal["ownership", "spf", "dkim", "dmarc", "mx"]

    record_type: Literal["TXT", "MX"]

    required: bool

    status: Literal["pending", "verified", "failed", "not_required"]

    value: str

    actual_value: Optional[str] = None

    priority: Optional[int] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .cloudflare_sync_status import CloudflareSyncStatus

__all__ = ["AccessIPAddressResponse"]


class AccessIPAddressResponse(BaseModel):
    id: str

    ip_address: str

    source: str

    status: CloudflareSyncStatus
    """An enumeration."""

    user_id: str

    created_at: Optional[datetime] = None

    description: Optional[str] = None

    updated_at: Optional[datetime] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SqlDatabase"]


class SqlDatabase(BaseModel):
    id: Optional[str] = None

    created_at: Optional[datetime] = None

    name: Optional[str] = None

    record_type: Optional[str] = None

    status: Optional[Literal["pending", "provision_ok", "provision_failed", "deleting", "delete_failed"]] = None
    """Provisioning status.

    A database is usable once `status` is `provision_ok`. Once deletion completes,
    the database no longer appears in the API.
    """

    updated_at: Optional[datetime] = None

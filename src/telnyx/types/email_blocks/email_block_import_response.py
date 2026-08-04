# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["EmailBlockImportResponse", "Data"]


class Data(BaseModel):
    """Import job.

    Schema fields hidden: `account_id`, `csv_content`,
    `block_ttl_days`. Nullable fields use the omit-nullable pattern.
    """

    id: str

    created_at: datetime

    record_type: Literal["email_block_import"]
    """View-only."""

    status: Literal["pending", "processing", "completed", "failed"]

    total: int
    """Data-row count at upload."""

    updated_at: datetime

    completed_at: Optional[datetime] = None
    """Omitted until terminal success."""

    created_count: Optional[int] = None
    """Only when `status == completed`."""

    error_count: Optional[int] = None
    """Only when `status == completed`."""

    errors: Optional[Dict[str, str]] = None
    """`{row_number: reason}`; only rendered when non-empty."""

    existing_count: Optional[int] = None
    """Only when `status == completed`."""

    failure_reason: Optional[str] = None
    """Only on terminal failure."""

    processed_rows: Optional[int] = None
    """Only when `status == completed`."""

    provider: Optional[Literal["sendgrid", "mailgun", "ses", "generic"]] = None
    """Omitted when nil."""

    skipped_count: Optional[int] = None
    """Only when `status == completed`."""


class EmailBlockImportResponse(BaseModel):
    data: Data
    """Import job.

    Schema fields hidden: `account_id`, `csv_content`, `block_ttl_days`. Nullable
    fields use the omit-nullable pattern.
    """

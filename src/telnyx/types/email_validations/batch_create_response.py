# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .email_validation_batch_status import EmailValidationBatchStatus

__all__ = ["BatchCreateResponse", "Data"]


class Data(BaseModel):
    """Shape returned by the create endpoint. Includes duplicates_removed."""

    id: str

    duplicates_removed: int

    record_type: Literal["email_validation_batch"]

    status: EmailValidationBatchStatus

    total: int

    webhook_url: Optional[str] = None


class BatchCreateResponse(BaseModel):
    data: Data
    """Shape returned by the create endpoint. Includes duplicates_removed."""

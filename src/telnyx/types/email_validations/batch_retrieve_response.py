# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..email_validation_checks import EmailValidationChecks
from .email_validation_batch_status import EmailValidationBatchStatus

__all__ = ["BatchRetrieveResponse", "Data", "DataResults"]


class DataResults(BaseModel):
    checks: EmailValidationChecks

    email: str

    risk_score: float

    valid: bool

    did_you_mean: Optional[str] = None
    """Suggested correction for typo. Omitted when nil."""


class Data(BaseModel):
    """Shape returned by the GET endpoint. Does not include duplicates_removed."""

    id: str

    record_type: Literal["email_validation_batch"]

    status: EmailValidationBatchStatus

    total: int

    completed_at: Optional[datetime] = None

    results: Optional[Dict[str, DataResults]] = None
    """Map keyed by original email address. Present only when the batch is completed."""

    webhook_url: Optional[str] = None


class BatchRetrieveResponse(BaseModel):
    data: Data
    """Shape returned by the GET endpoint. Does not include duplicates_removed."""

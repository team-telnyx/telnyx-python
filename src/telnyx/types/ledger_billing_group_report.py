# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LedgerBillingGroupReport"]


class LedgerBillingGroupReport(BaseModel):
    id: Optional[str] = None
    """Identifies the type of resource."""

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    organization_id: Optional[str] = None
    """Uniquely identifies the organization that owns the resource."""

    record_type: Optional[Literal["ledger_billing_group_report"]] = None
    """Identifies the type of the resource."""

    report_url: Optional[str] = None
    """External url of the ledger billing group report, if the status is complete"""

    status: Optional[Literal["pending", "complete", "failed", "deleted"]] = None
    """Status of the ledger billing group report"""

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was updated."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .export_portouts_csv_report import ExportPortoutsCsvReport

__all__ = ["PortoutReport"]


class PortoutReport(BaseModel):
    id: Optional[str] = None
    """Uniquely identifies the report."""

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    document_id: Optional[str] = None
    """Identifies the document that was uploaded when report was generated.

    This field is only populated when the report is under completed status.
    """

    params: Optional[ExportPortoutsCsvReport] = None
    """The parameters for generating a port-outs CSV report."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    report_type: Optional[Literal["export_portouts_csv"]] = None
    """Identifies the type of report"""

    status: Optional[Literal["pending", "completed"]] = None
    """The current status of the report generation."""

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was updated."""

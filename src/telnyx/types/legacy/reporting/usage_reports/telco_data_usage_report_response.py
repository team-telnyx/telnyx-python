# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime

from ....._models import BaseModel
from .telco_data_usage_record import TelcoDataUsageRecord

__all__ = ["TelcoDataUsageReportResponse"]


class TelcoDataUsageReportResponse(BaseModel):
    """Telco data usage report response"""

    id: Optional[str] = None
    """Unique identifier for the report"""

    aggregation_type: Optional[str] = None
    """Type of aggregation used in the report"""

    created_at: Optional[datetime] = None
    """Timestamp when the report was created"""

    end_date: Optional[date] = None
    """End date of the report period"""

    managed_accounts: Optional[List[str]] = None
    """List of managed account IDs included in the report"""

    record_type: Optional[str] = None
    """Record type identifier"""

    report_url: Optional[str] = None
    """URL to download the complete report"""

    result: Optional[List[TelcoDataUsageRecord]] = None
    """Array of usage records"""

    start_date: Optional[date] = None
    """Start date of the report period"""

    status: Optional[str] = None
    """Current status of the report"""

    updated_at: Optional[datetime] = None
    """Timestamp when the report was last updated"""

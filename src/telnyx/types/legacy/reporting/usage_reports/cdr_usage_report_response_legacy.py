# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ....._models import BaseModel

__all__ = ["CdrUsageReportResponseLegacy"]


class CdrUsageReportResponseLegacy(BaseModel):
    """Legacy V2 CDR usage report response"""

    id: Optional[str] = None
    """Identifies the resource"""

    aggregation_type: Optional[int] = None
    """
    Aggregation type: All = 0, By Connections = 1, By Tags = 2, By Billing Group = 3
    """

    connections: Optional[List[str]] = None

    created_at: Optional[datetime] = None

    end_time: Optional[datetime] = None

    product_breakdown: Optional[int] = None
    """
    Product breakdown type: No breakdown = 0, DID vs Toll-free = 1, Country = 2, DID
    vs Toll-free per Country = 3
    """

    record_type: Optional[str] = None

    report_url: Optional[str] = None

    result: Optional[Dict[str, object]] = None

    start_time: Optional[datetime] = None

    status: Optional[int] = None
    """Status of the report: Pending = 1, Complete = 2, Failed = 3, Expired = 4"""

    updated_at: Optional[datetime] = None

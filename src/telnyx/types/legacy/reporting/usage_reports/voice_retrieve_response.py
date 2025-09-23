# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ....._models import BaseModel

__all__ = ["VoiceRetrieveResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """Identifies the resource"""

    aggregation_type: Optional[int] = None
    """
    Aggregation type: All = 0, By Connections = 1, By Tags = 2, By Billing Group = 3
    """

    connections: Optional[List[int]] = None

    created_at: Optional[datetime] = None

    end_time: Optional[datetime] = None

    product_breakdown: Optional[int] = None
    """
    Product breakdown type: No breakdown = 0, DID vs Toll-free = 1, Country = 2, DID
    vs Toll-free per Country = 3
    """

    record_type: Optional[str] = None

    report_url: Optional[str] = None

    result: Optional[object] = None

    start_time: Optional[datetime] = None

    status: Optional[int] = None
    """Status of the report: Pending = 1, Complete = 2, Failed = 3, Expired = 4"""

    updated_at: Optional[datetime] = None


class VoiceRetrieveResponse(BaseModel):
    data: Optional[Data] = None
    """Legacy V2 CDR usage report response"""

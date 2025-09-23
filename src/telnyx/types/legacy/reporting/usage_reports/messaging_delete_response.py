# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ....._models import BaseModel

__all__ = ["MessagingDeleteResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """Identifies the resource"""

    aggregation_type: Optional[int] = None
    """Aggregation type: No aggregation = 0, By Messaging Profile = 1, By Tags = 2"""

    connections: Optional[List[int]] = None

    created_at: Optional[datetime] = None

    end_time: Optional[datetime] = None

    profiles: Optional[List[str]] = None
    """List of messaging profile IDs"""

    record_type: Optional[str] = None

    report_url: Optional[str] = None

    result: Optional[object] = None

    start_time: Optional[datetime] = None

    status: Optional[int] = None
    """Status of the report (Pending = 1, Complete = 2, Failed = 3, Expired = 4)"""

    updated_at: Optional[datetime] = None


class MessagingDeleteResponse(BaseModel):
    data: Optional[Data] = None
    """Legacy V2 MDR usage report response"""

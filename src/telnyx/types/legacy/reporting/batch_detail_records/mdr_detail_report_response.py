# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..filter import Filter
from ....._models import BaseModel

__all__ = ["MdrDetailReportResponse"]


class MdrDetailReportResponse(BaseModel):
    id: Optional[str] = None
    """Identifies the resource"""

    connections: Optional[List[int]] = None

    created_at: Optional[datetime] = None

    directions: Optional[List[Literal["INBOUND", "OUTBOUND"]]] = None

    end_date: Optional[datetime] = None

    filters: Optional[List[Filter]] = None

    profiles: Optional[List[str]] = None
    """List of messaging profile IDs"""

    record_type: Optional[str] = None

    record_types: Optional[List[Literal["INCOMPLETE", "COMPLETED", "ERRORS"]]] = None

    report_name: Optional[str] = None

    report_url: Optional[str] = None

    start_date: Optional[datetime] = None

    status: Optional[Literal["PENDING", "COMPLETE", "FAILED", "EXPIRED"]] = None

    updated_at: Optional[datetime] = None

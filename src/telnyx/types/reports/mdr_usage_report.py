# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MdrUsageReport", "Result"]


class Result(BaseModel):
    carrier_passthrough_fee: Optional[str] = None

    connection: Optional[str] = None

    cost: Optional[str] = None

    currency: Optional[str] = None

    delivered: Optional[str] = None

    direction: Optional[str] = None

    message_type: Optional[str] = None

    parts: Optional[str] = None

    product: Optional[str] = None

    profile_id: Optional[str] = None

    received: Optional[str] = None

    sent: Optional[str] = None

    tags: Optional[str] = None

    tn_type: Optional[str] = None


class MdrUsageReport(BaseModel):
    id: Optional[str] = None
    """Identifies the resource"""

    aggregation_type: Optional[Literal["NO_AGGREGATION", "PROFILE", "TAGS"]] = None

    connections: Optional[List[int]] = None

    created_at: Optional[datetime] = None

    end_date: Optional[datetime] = None

    profiles: Optional[str] = None

    record_type: Optional[str] = None

    report_url: Optional[str] = None

    result: Optional[List[Result]] = None

    start_date: Optional[datetime] = None

    status: Optional[Literal["PENDING", "COMPLETE", "FAILED", "EXPIRED"]] = None

    updated_at: Optional[datetime] = None

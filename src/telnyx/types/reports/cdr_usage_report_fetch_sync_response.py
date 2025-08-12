# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CdrUsageReportFetchSyncResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """Identifies the resource"""

    aggregation_type: Optional[Literal["NO_AGGREGATION", "CONNECTION", "TAG", "BILLING_GROUP"]] = None

    connections: Optional[List[int]] = None

    created_at: Optional[datetime] = None

    end_time: Optional[datetime] = None

    product_breakdown: Optional[
        Literal["NO_BREAKDOWN", "DID_VS_TOLL_FREE", "COUNTRY", "DID_VS_TOLL_FREE_PER_COUNTRY"]
    ] = None

    record_type: Optional[str] = None

    report_url: Optional[str] = None

    result: Optional[Dict[str, object]] = None

    start_time: Optional[datetime] = None

    status: Optional[Literal["PENDING", "COMPLETE", "FAILED", "EXPIRED"]] = None

    updated_at: Optional[datetime] = None


class CdrUsageReportFetchSyncResponse(BaseModel):
    data: Optional[Data] = None

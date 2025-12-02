# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime

from ....._models import BaseModel
from .standard_pagination_meta import StandardPaginationMeta

__all__ = ["NumberLookupListResponse", "Data", "DataResult", "DataResultAggregation"]


class DataResultAggregation(BaseModel):
    currency: Optional[str] = None
    """Currency code"""

    total_cost: Optional[float] = None
    """Total cost for this aggregation"""

    total_dips: Optional[int] = None
    """Total number of lookups performed"""

    type: Optional[str] = None
    """Type of telco data lookup"""


class DataResult(BaseModel):
    aggregations: Optional[List[DataResultAggregation]] = None
    """List of aggregations by lookup type"""

    record_type: Optional[str] = None
    """Record type identifier"""

    user_id: Optional[str] = None
    """User ID"""


class Data(BaseModel):
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

    result: Optional[List[DataResult]] = None
    """Array of usage records"""

    start_date: Optional[date] = None
    """Start date of the report period"""

    status: Optional[str] = None
    """Current status of the report"""

    updated_at: Optional[datetime] = None
    """Timestamp when the report was last updated"""


class NumberLookupListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[StandardPaginationMeta] = None

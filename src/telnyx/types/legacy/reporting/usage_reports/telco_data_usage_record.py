# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel
from .telco_data_aggregation import TelcoDataAggregation

__all__ = ["TelcoDataUsageRecord"]


class TelcoDataUsageRecord(BaseModel):
    aggregations: Optional[List[TelcoDataAggregation]] = None
    """List of aggregations by lookup type"""

    record_type: Optional[str] = None
    """Record type identifier"""

    user_id: Optional[str] = None
    """User ID"""

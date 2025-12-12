# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel

__all__ = ["TelcoDataAggregation"]


class TelcoDataAggregation(BaseModel):
    currency: Optional[str] = None
    """Currency code"""

    total_cost: Optional[float] = None
    """Total cost for this aggregation"""

    total_dips: Optional[int] = None
    """Total number of lookups performed"""

    type: Optional[str] = None
    """Type of telco data lookup"""

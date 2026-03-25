# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel

__all__ = ["NumberListResponse", "ReputationData", "ReputationDataReputationData"]


class ReputationDataReputationData(BaseModel):
    """Reputation metrics"""

    connection_score: Optional[int] = None
    """Connection quality metric (0–100)"""

    engagement_score: Optional[int] = None
    """Engagement metric (0–100). Higher = more positive engagement"""

    last_refreshed_at: Optional[datetime] = None
    """Timestamp of the last reputation data refresh"""

    maturity_score: Optional[int] = None
    """Maturity metric (0–100). Higher = more established number"""

    sentiment_score: Optional[int] = None
    """Sentiment metric (0–100). Higher = more positive sentiment"""

    spam_category: Optional[str] = None
    """Spam category classification (e.g., Telemarketing, Debt Collector)"""

    spam_risk: Optional[Literal["low", "medium", "high"]] = None
    """Overall spam risk level"""


ReputationData: TypeAlias = Union[ReputationDataReputationData, Optional[object]]


class NumberListResponse(BaseModel):
    id: Optional[str] = None
    """Unique identifier"""

    created_at: Optional[datetime] = None
    """When the number was associated"""

    enterprise_id: Optional[str] = None
    """ID of the associated enterprise"""

    phone_number: Optional[str] = None
    """Phone number in E.164 format"""

    reputation_data: Optional[ReputationData] = None
    """Reputation metrics (null if not yet fetched)"""

    updated_at: Optional[datetime] = None
    """When the record was last updated"""

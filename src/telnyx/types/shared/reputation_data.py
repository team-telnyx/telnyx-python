# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ReputationData"]


class ReputationData(BaseModel):
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

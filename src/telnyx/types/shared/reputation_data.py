# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ReputationData"]


class ReputationData(BaseModel):
    """Reputation snapshot for a phone number.

    Each metric is a 0–100 score; `spam_risk` is a coarse bucket. Field set may grow over time — read by key.
    """

    connection_score: Optional[int] = None

    engagement_score: Optional[int] = None

    last_refreshed_at: Optional[datetime] = None

    maturity_score: Optional[int] = None

    sentiment_score: Optional[int] = None

    spam_category: Optional[str] = None
    """Category label from the reputation feed when the number is flagged."""

    spam_risk: Optional[Literal["low", "medium", "high"]] = None
    """Overall spam-risk classification."""

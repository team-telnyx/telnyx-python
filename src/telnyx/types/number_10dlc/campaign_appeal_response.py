# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["CampaignAppealResponse"]


class CampaignAppealResponse(BaseModel):
    appealed_at: Optional[datetime] = None
    """Timestamp when the appeal was submitted"""

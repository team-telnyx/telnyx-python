# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["CampaignSubmitAppealResponse"]


class CampaignSubmitAppealResponse(BaseModel):
    appealed_at: Optional[datetime] = None
    """Timestamp when the appeal was submitted"""

    previous_status: Optional[str] = None
    """Previous campaign status (currently always null)"""

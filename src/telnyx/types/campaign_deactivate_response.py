# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["CampaignDeactivateResponse"]


class CampaignDeactivateResponse(BaseModel):
    time: float

    message: Optional[str] = None

    record_type: Optional[str] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from .whatsapp_profile_data import WhatsappProfileData

__all__ = ["ProfileRetrieveResponse"]


class ProfileRetrieveResponse(BaseModel):
    data: Optional[WhatsappProfileData] = None

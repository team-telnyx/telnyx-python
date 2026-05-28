# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .whatsapp_user_data import WhatsappUserData

__all__ = ["UserDataUpdateResponse"]


class UserDataUpdateResponse(BaseModel):
    data: Optional[WhatsappUserData] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ..._models import BaseModel
from .whatsapp_user_data import WhatsappUserData

__all__ = ["UserDataRetrieveResponse"]


class UserDataRetrieveResponse(BaseModel):
    data: Optional[WhatsappUserData] = None

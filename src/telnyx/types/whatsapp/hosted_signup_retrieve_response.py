# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ..._models import BaseModel
from .whatsapp_hosted_signup import WhatsappHostedSignup

__all__ = ["HostedSignupRetrieveResponse"]


class HostedSignupRetrieveResponse(BaseModel):
    data: Optional[WhatsappHostedSignup] = None

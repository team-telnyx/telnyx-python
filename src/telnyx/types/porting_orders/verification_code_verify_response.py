# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ..._models import BaseModel
from .porting_verification_code import PortingVerificationCode

__all__ = ["VerificationCodeVerifyResponse"]


class VerificationCodeVerifyResponse(BaseModel):
    data: Optional[List[PortingVerificationCode]] = None

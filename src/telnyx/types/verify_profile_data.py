# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .verify_profile import VerifyProfile

__all__ = ["VerifyProfileData"]


class VerifyProfileData(BaseModel):
    data: Optional[VerifyProfile] = None

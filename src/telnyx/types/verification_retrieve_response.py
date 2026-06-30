# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .._models import BaseModel
from .verification import Verification

__all__ = ["VerificationRetrieveResponse"]


class VerificationRetrieveResponse(BaseModel):
    data: Verification

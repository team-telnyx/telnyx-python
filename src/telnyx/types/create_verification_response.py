# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .verification import Verification

__all__ = ["CreateVerificationResponse"]


class CreateVerificationResponse(BaseModel):
    data: Verification

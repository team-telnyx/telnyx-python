# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .verify_profile import VerifyProfile
from .verifications.verify_meta import VerifyMeta

__all__ = ["VerifyProfileListResponse"]


class VerifyProfileListResponse(BaseModel):
    data: List[VerifyProfile]

    meta: VerifyMeta

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .verify_meta import VerifyMeta
from ..verification import Verification

__all__ = ["ByPhoneNumberListResponse"]


class ByPhoneNumberListResponse(BaseModel):
    data: List[Verification]

    meta: VerifyMeta

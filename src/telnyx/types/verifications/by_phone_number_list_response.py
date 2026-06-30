# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, List

from ..._models import BaseModel
from .verify_meta import VerifyMeta

if TYPE_CHECKING:
    from ..verification import Verification

__all__ = ["ByPhoneNumberListResponse"]


class ByPhoneNumberListResponse(BaseModel):
    data: List[Verification]

    meta: VerifyMeta

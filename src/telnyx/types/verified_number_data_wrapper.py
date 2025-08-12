# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .verified_number import VerifiedNumber

__all__ = ["VerifiedNumberDataWrapper"]


class VerifiedNumberDataWrapper(BaseModel):
    data: Optional[VerifiedNumber] = None

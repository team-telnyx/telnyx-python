# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ..._models import BaseModel
from .numbers_phone_numbers_job import NumbersPhoneNumbersJob

__all__ = ["JobDeleteBatchResponse"]


class JobDeleteBatchResponse(BaseModel):
    data: Optional[NumbersPhoneNumbersJob] = None

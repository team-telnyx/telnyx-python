# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .phone_numbers_job import PhoneNumbersJob

__all__ = ["JobUpdateBatchResponse"]


class JobUpdateBatchResponse(BaseModel):
    data: Optional[PhoneNumbersJob] = None

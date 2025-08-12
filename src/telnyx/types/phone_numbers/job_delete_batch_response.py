# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .phone_numbers_job import PhoneNumbersJob

__all__ = ["JobDeleteBatchResponse"]


class JobDeleteBatchResponse(BaseModel):
    data: Optional[PhoneNumbersJob] = None

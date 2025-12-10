# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..pagination_meta import PaginationMeta
from .phone_numbers_job import PhoneNumbersJob

__all__ = ["JobListResponse"]


class JobListResponse(BaseModel):
    data: Optional[List[PhoneNumbersJob]] = None

    meta: Optional[PaginationMeta] = None

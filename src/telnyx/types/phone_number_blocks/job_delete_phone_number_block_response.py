# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .job import Job
from ..._models import BaseModel

__all__ = ["JobDeletePhoneNumberBlockResponse"]


class JobDeletePhoneNumberBlockResponse(BaseModel):
    data: Optional[Job] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .fax import Fax
from .._models import BaseModel

__all__ = ["FaxListResponse"]


class FaxListResponse(BaseModel):
    data: Optional[List[Fax]] = None

    meta: Optional[object] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .fax import Fax
from .._models import BaseModel

__all__ = ["FaxRetrieveResponse"]


class FaxRetrieveResponse(BaseModel):
    data: Optional[Fax] = None

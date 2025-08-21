# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .fax_application import FaxApplication

__all__ = ["FaxApplicationUpdateResponse"]


class FaxApplicationUpdateResponse(BaseModel):
    data: Optional[FaxApplication] = None

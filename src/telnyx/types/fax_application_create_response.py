# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .fax_application import FaxApplication

__all__ = ["FaxApplicationCreateResponse"]


class FaxApplicationCreateResponse(BaseModel):
    data: Optional[FaxApplication] = None

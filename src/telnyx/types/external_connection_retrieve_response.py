# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .external_connection import ExternalConnection

__all__ = ["ExternalConnectionRetrieveResponse"]


class ExternalConnectionRetrieveResponse(BaseModel):
    data: Optional[ExternalConnection] = None

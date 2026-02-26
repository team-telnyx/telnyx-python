# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .integration_connection import IntegrationConnection

__all__ = ["ConnectionListResponse"]


class ConnectionListResponse(BaseModel):
    data: List[IntegrationConnection]

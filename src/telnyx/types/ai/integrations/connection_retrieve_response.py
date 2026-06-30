# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._models import BaseModel
from .integration_connection import IntegrationConnection

__all__ = ["ConnectionRetrieveResponse"]


class ConnectionRetrieveResponse(BaseModel):
    data: IntegrationConnection

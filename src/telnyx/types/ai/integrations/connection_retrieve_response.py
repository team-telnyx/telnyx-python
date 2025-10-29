# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel

__all__ = ["ConnectionRetrieveResponse", "Data"]


class Data(BaseModel):
    id: str

    allowed_tools: List[str]

    integration_id: str


class ConnectionRetrieveResponse(BaseModel):
    data: Data

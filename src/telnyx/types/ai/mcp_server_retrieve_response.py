# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["McpServerRetrieveResponse"]


class McpServerRetrieveResponse(BaseModel):
    id: str

    created_at: datetime

    name: str

    type: str

    url: str

    allowed_tools: Optional[List[str]] = None

    api_key_ref: Optional[str] = None

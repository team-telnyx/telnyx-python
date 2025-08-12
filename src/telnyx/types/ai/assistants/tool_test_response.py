# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from ...._models import BaseModel

__all__ = ["ToolTestResponse", "Data"]


class Data(BaseModel):
    content_type: str

    request: Dict[str, object]

    response: str

    status_code: int

    success: bool


class ToolTestResponse(BaseModel):
    data: Data
    """Response model for webhook tool test results"""

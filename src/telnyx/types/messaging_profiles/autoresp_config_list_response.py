# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .auto_resp_config import AutoRespConfig

__all__ = ["AutorespConfigListResponse", "Meta"]


class Meta(BaseModel):
    page_number: int

    page_size: int

    total_pages: int

    total_results: int


class AutorespConfigListResponse(BaseModel):
    """List of Auto-Response Settings"""

    data: List[AutoRespConfig]

    meta: Meta

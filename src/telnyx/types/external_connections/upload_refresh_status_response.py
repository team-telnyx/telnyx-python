# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["UploadRefreshStatusResponse"]


class UploadRefreshStatusResponse(BaseModel):
    success: Optional[bool] = None
    """Describes wether or not the operation was successful"""

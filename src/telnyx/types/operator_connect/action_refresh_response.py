# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ActionRefreshResponse"]


class ActionRefreshResponse(BaseModel):
    message: Optional[str] = None
    """A message describing the result of the operation"""

    success: Optional[bool] = None
    """Describes wether or not the operation was successful"""

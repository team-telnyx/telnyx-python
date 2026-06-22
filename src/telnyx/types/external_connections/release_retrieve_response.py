# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .release import Release
from ..._models import BaseModel

__all__ = ["ReleaseRetrieveResponse"]


class ReleaseRetrieveResponse(BaseModel):
    data: Optional[Release] = None

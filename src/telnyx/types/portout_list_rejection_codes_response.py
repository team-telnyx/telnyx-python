# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["PortoutListRejectionCodesResponse", "Data"]


class Data(BaseModel):
    code: Optional[int] = None

    description: Optional[str] = None

    reason_required: Optional[bool] = None


class PortoutListRejectionCodesResponse(BaseModel):
    data: Optional[List[Data]] = None
